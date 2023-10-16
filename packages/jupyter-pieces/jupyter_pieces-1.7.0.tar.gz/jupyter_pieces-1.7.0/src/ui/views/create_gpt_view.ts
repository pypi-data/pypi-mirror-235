import {
  QGPTQuestionOutput,
  RelevantQGPTSeed,
  RelevantQGPTSeeds,
} from '../../PiecesSDK/core';
import QGPT from '../../actions/qgpt';
import { QGPTConversationMessage } from '../../PiecesSDK/common/models/QGPTConversationMessage';
import { QGPTConversationMessageRoleEnum } from '../../PiecesSDK/common/models/QGPTConversationMessageRoleEnum';
import Notifications from '../../connection/notification_handler';
import { marked } from 'marked';
import {
  LabIcon,
  copyIcon,
  saveIcon,
  shareIcon,
} from '@jupyterlab/ui-components';
import Constants from '../../const';
import { highlightSnippet } from '../utils/loadPrism';
import langReadableToExt from '../utils/langReadableToExt';
import { defaultApp } from '../..';
import copyToClipboard from '../utils/copyToClipboard';
import { findSimilarity } from '../../actions/create_commands';
import createAsset from '../../actions/create_asset';
import ShareableLinksService from '../../connection/shareable_link';
import { SegmentAnalytics } from '../../analytics/SegmentAnalytics';
import { AnalyticsEnum } from '../../analytics/AnalyticsEnum';
import DisplayController from './DisplayController';
import { versionValid } from '../../connection/version_check';
import getProfile from '../utils/getUserIcon';
import { sendSVG, openFile, userIcon } from '../LabIcons';
import { CodeCell } from '@jupyterlab/cells';
import CopilotStreamController from '../../connection/CopilotStreamController';
import ActivitySingleton from '../../actions/activities';
import CopilotLLMConfigModal from '../modals/CopilotLLMConfigModal';
import { getIcon } from '../utils/langExtToIcon';
import { PageConfig } from '@jupyterlab/coreutils';

export default class QGPTView {
  public static currentConversation: QGPTConversationMessage[] = [];
  private static notification: Notifications = Notifications.getInstance();
  private static shareableLinks: ShareableLinksService =
    ShareableLinksService.getInstance();
  private static tempCollapseTimer: NodeJS.Timeout | undefined = undefined; // Timer for the collapse button
  private static userSVG: LabIcon | HTMLImageElement;
  private static cancelled = true;
  private static parentContainer: HTMLDivElement;

  private static conversationArray: Array<{
    query: string;
    answer: string;
  }> = [];

  private static generatingResults = false;

  private static aiSVG = Constants.AI_SVG;

  private static relevant: string | undefined = undefined;

  /*
    Creates the top level elements for the copilot view
    @param containervar: the container element
  */
  static async createGPTView({
    containerVar,
    newInstance = false,
    query,
  }: {
    containerVar: HTMLDivElement;
    newInstance?: boolean;
    query?: { query: string; code: string };
  }): Promise<void> {
    this.userSVG = userIcon;
    getProfile().then((el) => (this.userSVG = el));
    this.parentContainer = containerVar;
    this.parentContainer.innerHTML = '';

    this.parentContainer.classList.add('gpt-container');

    // gpt container
    const containerDiv = document.createElement('div');
    this.parentContainer.appendChild(containerDiv);
    containerDiv.classList.add('gpt-col', 'px-2', 'overflow-x-hidden');

    // div for all messages
    const textDiv = document.createElement('div');
    containerDiv.appendChild(textDiv);
    textDiv.classList.add('gpt-row', 'gpt-text-div');

    const textContent = document.createElement('div');
    textDiv.appendChild(textContent);
    textContent.classList.add('gpt-col', 'gpt-text-content');

    let introText: HTMLDivElement | undefined = undefined;
    // if there is not a conversation loaded, show the preview
    if (this.currentConversation.length == 0 || newInstance) {
      this.currentConversation = [];
      this.conversationArray = [];
      textContent.style.display = 'none';
      introText = document.createElement('div');
      textDiv.appendChild(introText);
      introText.classList.add(
        'h-full',
        'flex',
        'flex-col',
        'text-center',
        'items-center',
        'justify-center',
        'gap-3'
      );

      const titleDiv = document.createElement('div');
      titleDiv.classList.add();

      const imageHolder = document.createElement('div');
      imageHolder.classList.add('h-12', 'flex');

      imageHolder.innerHTML = Constants.COPILOT_BLACK;

      introText.appendChild(imageHolder);
      introText.appendChild(titleDiv);

      const introTextTitle = document.createElement('p');
      titleDiv.appendChild(introTextTitle);
      introTextTitle.classList.add('m-0', 'text-2xl', 'font-bold');
      introTextTitle.innerText = 'Pieces Copilot';

      const introTextSub = document.createElement('p');
      introText.appendChild(introTextSub);
      introTextSub.classList.add('m-0');
      introTextSub.innerText = !versionValid
        ? 'POS is not up-to-date, please update to use Copilot.'
        : DisplayController.isFetchFailed
        ? 'Error connecting to POS! To use Copilot, please make sure Pieces OS is installed updated, and running.'
        : 'Your own personalized assistant, contextualized by your notebook(s)';

      const runtimeBtn = introText.createDiv();
      runtimeBtn.classList.add(
        'cursor-pointer',
        'text-[var(--text-accent)]',
        'pt-1'
      );
      runtimeBtn.innerText = 'Select Runtime';
      runtimeBtn.onclick = () => {
        new CopilotLLMConfigModal().open();
      };
    }

    // div for relevant files
    const fileRow = document.createElement('div');
    textDiv.appendChild(fileRow);
    fileRow.classList.add('gpt-row');
    fileRow.id = 'gpt-files-container';

    // hint div
    const hintRow = document.createElement('div');
    textDiv.appendChild(hintRow);
    hintRow.classList.add('gpt-row');
    hintRow.id = 'gpt-hints-container';

    const btnRow = textDiv.createDiv();
    btnRow.classList.add('flex', 'flex-row', 'justify-between', 'py-2');

    // model selection button
    const llmButton = btnRow.createDiv();
    llmButton.classList.add(
      'cursor-pointer',
      'text-xs',
      'text-[gray]',
      'hover:text-[var(--text-accent)]'
    );
    llmButton.innerText = 'Copilot Runtime';
    llmButton.onclick = () => {
      new CopilotLLMConfigModal().open();
    };

    // clear chat button
    const cancelSpan = document.createElement('span');
    btnRow.appendChild(cancelSpan);
    cancelSpan.classList.add('gpt-cancel', 'hover:text-red-600', 'text-xs');
    cancelSpan.innerText = 'Clear Chat';

    // user input
    const textAreaDiv = document.createElement('div');
    textContent.appendChild(textAreaDiv);
    textAreaDiv.classList.add('gpt-col', 'gpt-text-area', 'gap-2');

    cancelSpan.addEventListener('mouseup', async () => {
      this.relevant = undefined;
      this.cancelled = true;
      this.currentConversation = [];
      this.conversationArray = [];
      this.generatingResults = false;
      this.createGPTView({
        containerVar: this.parentContainer,
        newInstance: true,
      });

      SegmentAnalytics.track({
        event: AnalyticsEnum.JUPYTER_AI_ASSISTANT_RESET,
      });
    });

    // user input
    const inputDiv = document.createElement('div');
    containerDiv.appendChild(inputDiv);
    inputDiv.classList.add('gpt-row', 'gpt-input');

    const inputText = document.createElement('span');
    inputDiv.appendChild(inputText);
    inputText.title = !versionValid
      ? 'POS is not up-to-date, please update to use Copilot.'
      : DisplayController.isFetchFailed
      ? 'POS not detected, please launch POS to use Copilot.'
      : 'Ask a question about your notebook(s)';
    inputText.classList.add('gpt-input-textarea');
    inputText.contentEditable =
      !versionValid || DisplayController.isFetchFailed ? 'false' : 'true';
    inputText.spellcheck = true;

    // send button
    const sendDiv = document.createElement('div');
    inputDiv.appendChild(sendDiv);
    sendDiv.classList.add('pr-2', 'text-[var(--text-accent)]', 'hidden');
    sendDiv.innerHTML = Constants.SEND_SVG;

    sendDiv.addEventListener('mouseup', async () => {
      sendDiv.classList.add('hidden');
      if (inputText.innerText === '') {
        return;
      }
      QGPTView.cancelled = false;
      await QGPTView.handleChat({
        inputText,
        textAreaDiv,
        currentConversation: QGPTView.currentConversation,
        introText,
      });
    });

    inputText.addEventListener('keyup', async (evt) => {
      sendDiv.classList.remove('hidden');
      if (inputText.innerText === '') {
        sendDiv.classList.add('hidden');
        return;
      }
      if (evt.key !== 'Enter' || evt.shiftKey) {
        return;
      }

      sendDiv.classList.add('hidden');
      hintRow.innerHTML = '';
      this.cancelled = false;
      await QGPTView.handleChat({
        inputText,
        textAreaDiv,
        currentConversation: this.currentConversation,
        introText,
      });
    });

    if (this.conversationArray.length != 0 && !newInstance) {
      QGPTView.buildCurrentConversation(textAreaDiv);
    }

    if (query) {
      //@ts-ignore
      const activeCell = defaultApp.shell.currentWidget?.content.activeCell;
      if (!(activeCell instanceof CodeCell)) {
        inputText.textContent = `${query.query}\n\n\`${query.code}\``;
      } else {
        inputText.textContent = `${query.query}\n\n\`\`\`python\n${query.code}\n\`\`\``;
      }
      this.relevant = query.code;
      await this.handleChat({
        inputText,
        textAreaDiv,
        currentConversation: this.currentConversation,
        introText,
        query,
      });
    }
  }

  static redrawGpt = () => {
    const parent = document.getElementById('gpt-tab') as HTMLDivElement;
    if (!parent) {
      return;
    }
    QGPTView.cancelled = true;
    QGPTView.currentConversation = [];
    QGPTView.conversationArray = [];
    QGPTView.generatingResults = false;
    QGPTView.createGPTView({ containerVar: parent, newInstance: true });
  };
  private static handleChat = async ({
    inputText,
    textAreaDiv,
    currentConversation,
    introText,
    query,
  }: {
    inputText: HTMLSpanElement;
    textAreaDiv: HTMLDivElement;
    currentConversation: QGPTConversationMessage[];
    introText: HTMLDivElement | undefined;
    query?: { query: string; code: string };
  }): Promise<void> => {
    // make sure they can't send a message while one is processing
    if (QGPTView.generatingResults) {
      Notifications.getInstance().error({
        message: 'Already generating a message! Please wait a bit.',
      });
      return;
    }

    // Remove / clear dom elements where necessary
    document.getElementById('gpt-files-container')!.innerHTML = '';
    QGPTView.generatingResults = true;
    if (currentConversation.length == 0) {
      textAreaDiv.innerHTML = '';
    }
    const curQuery = inputText.textContent?.trim() ?? '';
    inputText.innerText = '';
    if (curQuery == '') {
      QGPTView.generatingResults = false;
      return;
    }
    if (introText) {
      textAreaDiv.parentElement!.style.display = 'flex';
      introText.remove();
    }
    const queryDiv = document.createElement('div');
    queryDiv.classList.add('gpt-row', 'gpt-right-align');

    // build chat message dom elements
    const answerQuery = document.createElement('div');
    answerQuery.classList.add(
      'gpt-text-response',
      'gpt-query',
      'mr-1',
      'flex',
      'flex-col',
      'overflow-x-hidden'
    );
    answerQuery.innerHTML = marked.parse(curQuery);
    this.doSyntaxHighlighting(answerQuery);

    const userDiv = document.createElement('div');
    userDiv.id = 'user-img';
    if (QGPTView.userSVG instanceof HTMLImageElement) {
      QGPTView.userSVG.classList.add('gpt-user-image');
      userDiv.innerHTML = Constants.USER_SVG;
    } else {
      QGPTView.userSVG.element({ container: userDiv });
    }
    userDiv.classList.add('gpt-img', 'self-end');

    queryDiv.appendChild(answerQuery);
    queryDiv.appendChild(userDiv);

    textAreaDiv.appendChild(queryDiv);

    const answerDiv = document.createElement('div');
    answerDiv.classList.add('gpt-row', 'gpt-left-align');

    const aiDiv = document.createElement('div');
    aiDiv.id = 'ai-img';
    aiDiv.innerHTML = QGPTView.aiSVG;
    aiDiv.classList.add('gpt-img', 'self-end');
    answerDiv.appendChild(aiDiv);

    const answerEl = document.createElement('div');
    answerEl.classList.add(
      'gpt-text-response',
      'gpt-response',
      'gpt-col',
      'overflow-hidden',
      'flex'
    );
    answerEl.innerText = "Let's see what I got here...";

    answerDiv.appendChild(answerEl);

    textAreaDiv.append(answerDiv);

    setTimeout(() => {
      if (answerEl.innerText == `Let's see what I got here...`) {
        answerEl.innerText = `Choosing the best answer for your question...`;
      }
    }, 2000);

    setTimeout(() => {
      if (
        answerEl.innerText == `Choosing the best answer for your question...`
      ) {
        answerEl.innerText = `Almost there...`;
      }
    }, 10000);
    // call reprompt if it's the 2nd or later message
    let result: { answer: string; relevant: RelevantQGPTSeeds };
    try {
      let usedQuery = query ? query.query : curQuery;
      if (currentConversation.length >= 2) {
        const repromptRes = await QGPT.reprompt({
          conversation: currentConversation,
          query: usedQuery,
        });
        if (repromptRes) {
          usedQuery = repromptRes.query;
        }
      }
      result = await CopilotStreamController.getInstance().askQGPT({
        query: usedQuery,
        relevant: this.relevant,
        answerEl: answerEl,
      });
    } catch (e) {
      console.error(e);
      answerEl.innerText = 'Sorry, something went wrong with that request.';
      this.generatingResults = false;
      return;
    }

    // if we did get an answer
    if (result) {
      // update conversation array
      currentConversation.push({
        text: curQuery,
        role: QGPTConversationMessageRoleEnum.User,
        // subtract 10 as arbitrary number to ensure sort validity
        timestamp: { value: new Date(new Date().getTime() - 10) },
      });

      currentConversation.push({
        text: result.answer,
        role: QGPTConversationMessageRoleEnum.Assistant,
        timestamp: { value: new Date() },
      });

      // show the relevant notes
      const controller = CopilotStreamController.getInstance();
      if (result.relevant?.iterable.length) {
        let isAtBottom = controller.isAtBottom(answerEl);
        this.renderSuggestedFiles(result.relevant.iterable, answerEl);
        if (isAtBottom) controller.forceScroll(answerEl);
        // generate followup questions
        QGPT.hints({
          query: curQuery,
          relevant: result.relevant,
          answer: { text: result.answer, score: 1 },
        })
          .then((hintsRes) => {
            if (this.cancelled || !hintsRes.answers.iterable.length) {
              return;
            } else {
              isAtBottom = controller.isAtBottom(answerEl);
              this.renderHints({
                hints: hintsRes,
                inputText,
                introText,
                textAreaDiv,
              });
              if (isAtBottom) controller.forceScroll(answerEl);
            }
          })
          .catch(() => {
            // do nothing
          });
      }
    } else {
      answerEl.innerHTML = marked.parse(
        `I'm sorry, it seems I don't have any relevant context to that question. Please try again 😃`,
        { headerIds: false, mangle: false }
      );
    }

    QGPTView.conversationArray.push({
      query: curQuery,
      answer: answerEl.innerText,
    });
    QGPTView.generatingResults = false;
  };
  /*
    Builds the conversation while switching back to copilot
     - textareadiv: the container for the chat messages
  */
  private static buildCurrentConversation = (textAreaDiv: HTMLDivElement) => {
    QGPTView.conversationArray.forEach((element) => {
      const queryDiv = document.createElement('div');
      queryDiv.classList.add('gpt-row', 'gpt-right-align');

      const answerQuery = document.createElement('p');
      queryDiv.appendChild(answerQuery);
      answerQuery.classList.add('gpt-text-response', 'gpt-query');
      answerQuery.innerText = element.query;

      const userDiv = document.createElement('div');
      queryDiv.appendChild(userDiv);
      userDiv.classList.add('gpt-img');

      textAreaDiv.append(queryDiv);

      const answerDiv = document.createElement('div');
      answerDiv.classList.add('gpt-row', 'gpt-left-align');

      const aiDiv = document.createElement('div');
      answerDiv.appendChild(aiDiv);
      aiDiv.classList.add('gpt-img');

      const answerEl = document.createElement('p');
      answerDiv.appendChild(answerEl);
      answerEl.classList.add('gpt-text-response', 'gpt-response', 'gpt-col');
      answerEl.innerText = element.answer;
      textAreaDiv.append(answerDiv);
    });
  };

  /*
    Renders the suggested query buttones
     - hints: response from /hints
     - inputtext: the user input div
     - textareadiv: the chat messages container
     - introText: the container for the introduction text (if there is not a conversation)
*/
  private static renderHints = ({
    hints,
    inputText,
    textAreaDiv,
    introText,
  }: {
    hints: QGPTQuestionOutput;
    inputText: HTMLSpanElement;
    textAreaDiv: HTMLDivElement;
    introText: HTMLDivElement | undefined;
  }) => {
    // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
    const hintRow = document.getElementById('gpt-hints-container')!;
    hintRow.innerHTML = '';
    const hintCol = document.createElement('div');
    hintRow.appendChild(hintCol);
    hintCol.classList.add('gpt-col', 'hpt-hint-col');

    // setup container(s)
    const hintTitleRow = document.createElement('div');
    hintCol.appendChild(hintTitleRow);
    hintTitleRow.classList.add('gpt-row', 'gpt-hint-row');
    const hintTitle = document.createElement('p');
    hintTitle.innerText = 'Suggested Queries: ';
    hintTitleRow.appendChild(hintTitle);
    hintTitle.classList.add('hint-title', 'hint-title-file', 'm-0', 'pb-1');

    const hintListRow = document.createElement('div');
    hintCol.appendChild(hintListRow);
    hintListRow.classList.add('gpt-row', 'hint-list');

    const hintList = document.createElement('div');
    hintListRow.appendChild(hintList);
    hintList.classList.add('gpt-col', 'gap-2');

    // render the buttons for every hint
    for (let i = 0; i < hints.answers.iterable.length; i++) {
      if (QGPTView.cancelled) {
        QGPTView.createGPTView({
          containerVar: QGPTView.parentContainer,
          newInstance: true,
        });
      }
      const hintButton = document.createElement('button');
      hintList.appendChild(hintButton);
      hintButton.classList.add('hint-btn', 'gpt-row', 'w-full');
      hintButton.onclick = () => {
        hintRow.innerHTML = '';
        inputText.innerText = hints.answers.iterable[i].text;
        QGPTView.handleChat({
          inputText,
          textAreaDiv,
          currentConversation: QGPTView.currentConversation,
          introText,
        });

        SegmentAnalytics.track({
          event: AnalyticsEnum.JUPYTER_AI_ASSISTANT_CLICKED_SUGGESTED_QUERY,
        });
      };

      const hintButtonText = document.createElement('p');
      hintButton.appendChild(hintButtonText);
      hintButtonText.classList.add('hint-btn-text', 'gpt-col', 'line-clamp-2');
      hintButtonText.textContent = hints.answers.iterable[i].text;

      // add icon to the button
      const sendIconDiv = document.createElement('div');
      sendIconDiv.classList.add(
        'gpt-btn-icon',
        'hover:text-[var(--text-accent)]'
      );
      hintButton.appendChild(sendIconDiv);
      sendSVG.element({ container: sendIconDiv });
    }
  };
  // in the case that we get multiple relevant snippets from the same file,
  // we need to remove the duplicate files from the rendered list
  private static deleteIdenticalElements = (
    files: RelevantQGPTSeed[]
  ): RelevantQGPTSeed[] => {
    const result: RelevantQGPTSeed[] = [];
    const paths: { [key: string]: boolean } = {};
    files.forEach((file: RelevantQGPTSeed) => {
      // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
      if (!paths[file.path!]) {
        // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
        paths[file.path!] = true;
        result.push(file);
      }
    });
    return result;
  };

  private static renderSuggestedFiles = (
    files: RelevantQGPTSeed[],
    answerEl: HTMLDivElement
  ) => {
    // make sure there is no duplicates using a set also get all the paths from the map in qgpt.ts
    files = this.deleteIdenticalElements(files);
    files = files.filter((el) => el.seed);

    if (files.length == 0) {
      return;
    }

    const filePaths: Set<string> = new Set<string>();
    for (let i = 0; i < files.length; i++) {
      const path = QGPT.getSeedPath(files[i].seed!);
      if (path) filePaths.add(path);
    }
    if (!filePaths.size) {
      return;
    }
    const fileRow = answerEl;

    // button(s) container(s)
    const fileCol = document.createElement('div');
    fileRow.appendChild(fileCol);
    fileCol.classList.add('gpt-col');

    const fileTitleRow = document.createElement('div');
    fileCol.appendChild(fileTitleRow);
    fileTitleRow.classList.add('gpt-row');
    const fileTitle = document.createElement('p');
    fileTitle.textContent = 'Relevant Files: ';
    fileTitleRow.appendChild(fileTitle);
    fileTitle.classList.add('hint-title-file');

    const fileListRowDiv = document.createElement('div');
    fileCol.appendChild(fileListRowDiv);
    fileListRowDiv.classList.add('gpt-row', 'hint-list-file');

    const fileListCol = document.createElement('div');
    fileListRowDiv.appendChild(fileListCol);
    fileListCol.classList.add('gpt-col');

    const fileListRow = document.createElement('div');
    fileListCol.appendChild(fileListRow);
    fileListRow.classList.add('gpt-row', 'gpt-rel-wrap');

    // Create the file pills
    // 2 per row
    filePaths.forEach((path) => {
      if (!path) return;
      QGPTView.createFilePill(path, fileListRow);
    });
  };

  // Renders suggested files to the dom

  // // DOM element for a file pill
  // // file: the file to be rendered
  // // fileListRow: the parent element
  private static createFilePill = (
    path: string,
    fileListRow: HTMLDivElement
  ) => {
    const fileList = document.createElement('div');
    fileListRow.appendChild(fileList);
    fileList.classList.add('gpt-col-small');

    const fileName = (path?.substring(path.lastIndexOf('/') + 1) ?? '').split(
      '.'
    )[0];

    const fileButton = document.createElement('button');
    fileList.appendChild(fileButton);
    fileButton.title = `Open '${fileName}' in a new tab`;
    fileButton.classList.add('hint-btn-file');
    fileButton.onclick = () => {
      SegmentAnalytics.track({
        event: AnalyticsEnum.JUPYTER_AI_ASSISTANT_OPEN_RELEVANT_FILE,
      });

      defaultApp.commands.execute('docmanager:open', {
        path: path,
        options: {
          mode: 'tab-after',
        },
      });
    };

    const fileButtonText = document.createElement('p');
    fileButton.appendChild(fileButtonText);
    fileButtonText.classList.add('hint-btn-text', 'gpt-col');
    fileButtonText.textContent = path ?? '';

    const fileButtonIcon = document.createElement('div');
    fileButton.appendChild(fileButtonIcon);
    fileButtonIcon.classList.add(
      'gpt-btn-icon',
      'gpt-icon-file',
      'hover:text-[var(--text-accent)]'
    );

    openFile.element({ container: fileButtonIcon });
  };

  /*
    This is for our button holder
    in obsidian this is a widget class that also gets injected into the editor 
    but we declare it here because we don't inject anything

    snippetData is the <code> element that comes from gpt

*/
  private static buildButtonHolder = (
    snippetData: HTMLElement,
    relevant?: RelevantQGPTSeed[]
  ): HTMLDivElement => {
    const buttonDiv = document.createElement('div');
    buttonDiv.classList.add('gpt-response-button-div');

    const holderDiv = document.createElement('div');
    holderDiv.classList.add('save-to-pieces-holder');

    const collapsedHolder = document.createElement('div');
    collapsedHolder.classList.add('collapsed-pieces-holder', 'collapsed');

    const collapseControlButton = document.createElement('button');
    holderDiv.appendChild(collapseControlButton);
    collapseControlButton.title = 'See Pieces actions';
    collapseControlButton.classList.add('jp-btn');
    const piecesIcon = LabIcon.resolve({ icon: 'jupyter-pieces:logo' });
    piecesIcon.element({ container: collapseControlButton });
    collapseControlButton.addEventListener('click', async () => {
      clearTimeout(QGPTView.tempCollapseTimer);

      // detect if this exact code has been saved or not
      const { similarity, comparisonID } = await findSimilarity(
        snippetData.textContent ?? ''
      );

      // if it's collapsed, render the buttons
      if (collapsedHolder.classList.contains('collapsed')) {
        const copyBtn = document.createElement('button');
        collapsedHolder.appendChild(copyBtn);
        copyBtn.classList.add('jp-btn', 'gpt-button-div');
        copyBtn.title = 'Copy snippet to clipboard';
        copyIcon.element({ container: copyBtn });
        copyBtn.addEventListener('click', async () => {
          await copyToClipboard(snippetData.textContent ?? '');
          QGPTView.notification.information({
            message: Constants.COPY_SUCCESS,
          });
          if (similarity < 2)
            ActivitySingleton.getInstance().referenced(
              comparisonID,
              undefined,
              true
            );
        });
        // if we don't have a similar snippet make it a save button
        if (similarity > 2) {
          const saveBtn = document.createElement('button');
          collapsedHolder.appendChild(saveBtn);
          saveBtn.classList.add('jp-btn', 'gpt-button-div');
          saveBtn.title = 'Save snippet to pieces';
          saveIcon.element({ container: saveBtn });
          saveBtn.addEventListener('click', async () => {
            const paths = [];
            for (let snippet of relevant ?? []) {
              if (!snippet.seed) continue;
              paths.push(QGPT.getSeedPath(snippet.seed));
            }
            const loading = document.createElement('div');
            loading.classList.add('share-code-bouncing-loader');
            const bounceDiv = document.createElement('div');
            loading.appendChild(bounceDiv);
            loading.appendChild(bounceDiv.cloneNode(true));
            loading.appendChild(bounceDiv.cloneNode(true));

            collapsedHolder.replaceChild(loading, saveBtn);
            if (snippetData.textContent) {
              const root = PageConfig.getOption('serverRoot');
              await createAsset({
                selection: snippetData.textContent ?? '',
                anchors: paths.map((el) => root + '/' + el),
              });
            } else {
              this.notification.error({
                message: 'Cannot save to pieces, the snippet is empty.',
              });
            }
            collapsedHolder.removeChild(loading);
            const computedWidth = (5 + 42) * collapsedHolder.childElementCount;
            collapsedHolder.style.width = computedWidth + 'px';
          });
        }

        // create share button
        const shareBtn = document.createElement('button');
        collapsedHolder.appendChild(shareBtn);
        shareBtn.classList.add('jp-btn', 'gpt-button-div');
        shareBtn.title = 'Copy snippet to clipboard';
        shareIcon.element({ container: shareBtn });
        shareBtn.addEventListener('click', async () => {
          const loading = document.createElement('div');
          loading.classList.add('share-code-bouncing-loader');
          const bounceDiv = document.createElement('div');
          loading.appendChild(bounceDiv);
          loading.appendChild(bounceDiv.cloneNode(true));
          loading.appendChild(bounceDiv.cloneNode(true));

          collapsedHolder.replaceChild(loading, shareBtn);

          // if it's already saved, use the existing snippet, otherwise save it as a new snippet
          if (similarity < 2 && comparisonID) {
            const link = await QGPTView.shareableLinks.generate({
              id: comparisonID,
            });
            copyToClipboard(link ?? '');
          } else {
            if (!snippetData.textContent) {
              this.notification.error({
                message: 'Cannot generate link, the snippet is empty.',
              });
              return;
            }
            const id = await createAsset({
              selection: snippetData.textContent ?? '',
            });
            if (typeof id === 'string') {
              const link = await QGPTView.shareableLinks.generate({
                id: id,
              });
              copyToClipboard(link ?? '');
            }
          }

          collapsedHolder.replaceChild(shareBtn, loading);
        });

        collapsedHolder.classList.remove('collapsed');
        const computedWidth = (3 + 42) * collapsedHolder.childElementCount;
        collapsedHolder.style.width = computedWidth + 'px';

        QGPTView.tempCollapseTimer = setTimeout(() => {
          QGPTView.tempCollapseTimer = undefined;
          collapsedHolder.classList.add('expanded');
        }, 500);

        collapseControlButton.title = 'Hide Pieces actions';
      } else {
        // the button is open, so collapse it
        collapsedHolder.classList.remove('expanded');
        collapsedHolder.classList.add('collapsed');
        collapsedHolder.style.width = '0px';
        collapseControlButton.disabled = true;
        QGPTView.tempCollapseTimer = setTimeout(() => {
          QGPTView.tempCollapseTimer = undefined;
          collapsedHolder.innerHTML = '';
          collapseControlButton.disabled = false;
        }, 500);

        collapseControlButton.title = 'See Pieces actions';
      }
    });

    holderDiv.appendChild(collapsedHolder);
    buttonDiv.appendChild(holderDiv);

    const children = Array.from(holderDiv.children);
    children.reverse();
    holderDiv.innerHTML = '';
    children.forEach((child) => holderDiv.appendChild(child));

    return buttonDiv;
  };

  public static doSyntaxHighlighting(element: HTMLElement, button = true) {
    const pChildren = Array.from((element as HTMLParagraphElement).children);

    const codeChildren: HTMLElement[] = [];

    // find the <code> elements
    pChildren.forEach((child) => {
      child.classList.add('gpt-response-margin-delete');
      if (child.tagName.toUpperCase() === 'PRE') {
        child.classList.add('gpt-col');
        codeChildren.push(child.children[0] as HTMLElement);
        child.children[0].classList.add('code-element');
      }
    });

    // add syntax highlighting to the <code> elements
    // also add embedded buttons
    if (codeChildren.length) {
      this.highlightCodeBlocks(codeChildren);
      if (!button) return;
      this.buildCodeButtons(codeChildren);
    }
  }

  static createLoader() {
    const loading = document.createElement('div');
    loading.classList.add('share-code-bouncing-loader');
    const bounceDiv = document.createElement('div');
    loading.appendChild(bounceDiv);
    loading.appendChild(bounceDiv.cloneNode(true));
    loading.appendChild(bounceDiv.cloneNode(true));
    return loading;
  }

  public static buildCodeButtons(
    codeElements: HTMLElement[],
    relevant?: RelevantQGPTSeed[]
  ) {
    for (const el of codeElements) {
      const buttonDiv = QGPTView.buildButtonHolder(el, relevant);

      el.appendChild(buttonDiv);
    }
  }

  static highlightCodeBlocks(codeElements: HTMLElement[]) {
    for (const codeBlock of codeElements) {
      const langClass = codeBlock.classList[0] as string | undefined;
      const lang =
        langClass && langClass.startsWith('language-')
          ? langClass.slice('language-'.length)
          : 'ts';

      codeBlock.parentElement!.classList.add('gpt-col');
      codeBlock.classList.add('code-element', 'w-full');

      codeBlock.innerHTML = highlightSnippet({
        snippetContent: codeBlock.textContent!,
        snippetLanguage: langReadableToExt(lang),
      });
      codeBlock.classList.add('!shadow-none');

      const codeParent = codeBlock.parentElement!;
      codeParent.classList.add('flex', '!flex-row');

      if (langClass && langClass.startsWith('language-')) {
        const codeHeader = document.createElement('div');
        codeHeader.classList.add('flex', 'flex-row');
        codeHeader.classList.add(
          'rounded-t',
          'bg-[var(--jp-cell-editor-background)]',
          'pt-2',
          'text-[var(--text-muted)]',
          'text-xs',
          'pl-2',
          'gap-2',
          'h-4',
          'items-center'
        );
        codeParent.insertAdjacentElement('beforebegin', codeHeader);

        // idk for real man the image just won't align correctly
        // thanks to us needing to do images via css class names?!
        const imgContainer = codeHeader.createDiv();
        imgContainer.classList.add('-ml-3', '-mr-4', 'flex', 'items-center');

        const langImg = imgContainer.createEl('div');
        const langIcon = getIcon(langReadableToExt(lang));
        langImg.classList.add(langIcon);
        langImg.classList.add('h-12', 'w-12', 'scale-[.4]');

        codeHeader.append(lang);
      }

      const lineNums = document.createElement('div');
      lineNums.classList.add(
        'text-right',
        'pl-2',
        'pr-1',
        'text-[var(--text-muted)]',
        'rounded-bl',
        'pt-2',
        'leading-[1.5]',
        'bg-[var(--jp-cell-editor-background)]'
      );
      const lineCount = (codeBlock.textContent?.match(/\n/g) || []).length;

      for (let i = 0; i < lineCount; i++) {
        lineNums.append(`${i + 1}\n`);
      }
      codeParent.insertBefore(lineNums, codeBlock);
    }
  }
}
