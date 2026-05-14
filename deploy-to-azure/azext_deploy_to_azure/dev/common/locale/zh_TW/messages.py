# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# prompting.py
PROMPT_ENTER_CHOICE = '請輸入選項 [預設選項({})]: '
PROMPT_VALID_VALUES = '有效值為 %s'
PROMPT_FIELD_NOT_BLANK = '此欄位不可留空。'
PROMPT_ERROR_NO_OPTIONS = '{} 錯誤：無可用選項。'

# github_credential_manager.py
MSG_PAT_CREATE_INFO = (
    '我們需要建立個人存取權杖（PAT）以與 GitHub 溝通。'
    '將建立具有以下範圍的新 PAT：repo、user。'
)
MSG_PAT_ENV_HINT = '您可以將 PAT 設定於環境變數 (%s) 中以避免輸入帳號密碼。'
MSG_ENTER_GITHUB_USERNAME = '請輸入您的 GitHub 使用者名稱（留空則使用已產生的 PAT）：'
MSG_ENTER_GITHUB_PASSWORD = '請輸入您的 GitHub 密碼：'
MSG_ENTER_GITHUB_PAT = '請輸入您的 GitHub PAT：'
MSG_ENTER_2FA_CODE = '請輸入雙因素驗證碼：'
MSG_PAT_CREATED = '已成功建立個人存取權杖，範圍為：repo、user。'
MSG_PAT_NAME = '名稱：%s'
MSG_PAT_REVOKE_HINT = '若不再需要此 CI/CD 流程，您可至 GitHub 設定撤銷此權杖。'
MSG_PAT_MANAGE_URL = '請至 GitHub 設定管理您的 PAT 權杖：https://github.com/settings/tokens'
MSG_PAT_CREATE_FAILED = '無法為 GitHub 建立個人存取權杖。請確認您的憑證後再試一次。'
MSG_PAT_ENV_FOUND = '已使用環境變數 (%s) 中的 GitHub PAT 權杖。'

# github_workflow_helper.py
MSG_WORKFLOW_QUEUED = '工作流程排隊中'
MSG_WORKFLOW_IN_PROGRESS = '工作流程執行中'
MSG_WORKFLOW_COMPLETED = 'GitHub 工作流程已完成。'
MSG_WORKFLOW_SUCCEEDED = '工作流程執行成功'
MSG_WORKFLOW_STATUS = '工作流程狀態：{}'
MSG_WORKFLOW_YAML_EXISTS = 'main.yml 已存在於 .github/workflows 資料夾中。'
MSG_ENTER_NEW_YAML_NAME = '請輸入工作流程 yml 檔案的新名稱：'
MSG_YAML_NAME_HELP = '例如：/new_main.yml 以加入 .github/workflows 資料夾。'

# azure_cli_resources.py
MSG_CREATING_AKS = '正在使用您的預設 Azure 訂用帳戶 %s 建立新的 AKS 叢集，這可能需要數分鐘'
MSG_CREATING_ACR = '正在使用您的預設 Azure 訂用帳戶 %s 建立新的 Azure 容器登錄。'
MSG_NO_DEFAULT_SUBSCRIPTION = '您的帳戶沒有預設的 Azure 訂用帳戶。請執行 \'az login\' 以設定帳戶。'
MSG_FETCHING_RESOURCE_GROUPS = '正在使用您的預設 Azure 訂用帳戶 %s 擷取資源群組。'
MSG_SELECT_RESOURCE_GROUP = '您想在哪個資源群組中建立資源？'
MSG_FETCHING_AKS = '正在使用您的預設 Azure 訂用帳戶 %s 擷取 AKS 叢集。'
MSG_SELECT_AKS = '您想要目標哪個 Kubernetes 叢集？'
MSG_CREATE_NEW_AKS = '建立新的 AKS 叢集'
MSG_ENTER_AKS_NAME = '請輸入要建立的叢集名稱：'
MSG_AKS_EXISTS = 'AKS 叢集已存在相同名稱。將使用現有叢集。'
MSG_AKS_NOT_FOUND = '找不到名稱為 {} 的叢集。請使用命令 az aks list 確認。'
MSG_FETCHING_ACR = '正在使用您的預設 Azure 訂用帳戶 %s 擷取 Azure 容器登錄。'
MSG_SELECT_ACR = '您想使用哪個 Azure 容器登錄？'
MSG_CREATE_NEW_ACR = '建立新的 Azure 容器登錄'
MSG_ENTER_ACR_NAME = '請輸入要建立的 Azure 容器登錄名稱：'
MSG_ACR_EXISTS = 'Azure 容器登錄已存在相同名稱。將使用現有登錄。'
MSG_ACR_NOT_FOUND = '找不到名稱為 {} 的容器登錄。請使用命令 az acr list 確認。'
MSG_FETCHING_FUNCTIONAPPS = '正在使用您的預設 Azure 訂用帳戶 %s 擷取函式應用程式。'
MSG_NO_FUNCTIONAPPS = '在您的 Azure 訂用帳戶中找不到任何函式應用程式部署。'
MSG_SELECT_FUNCTIONAPP = '您想要目標哪個函式應用程式？'
MSG_FUNCTIONAPP_NOT_FOUND = '找不到名稱為 {} 的函式應用程式。請使用命令 az functionapp list 確認。'
MSG_SELECT_SKU = '請選擇容器登錄的 SKU？'
MSG_FETCHING_AKS_CREDENTIALS = '正在使用您的預設 Azure 訂用帳戶 %s 取得 AKS 叢集認證。'

# help text
HELP_AKS_GROUP_SHORT = '管理 AKS 應用程式的命令。'
HELP_AKS_UP_SHORT = '透過 GitHub Actions 部署至 AKS。'
HELP_ACI_GROUP_SHORT = '管理 Azure 容器執行個體應用程式的命令。'
HELP_ACI_UP_SHORT = '使用 GitHub Actions 部署至 Azure 容器執行個體。詳見 https://aka.ms/aci-deploy-action'
HELP_FUNCTIONAPP_GROUP_SHORT = '管理 Azure Functions 應用程式的命令。'
HELP_FUNCTIONAPP_UP_SHORT = '透過 GitHub Actions 部署至 Azure Functions。'
HELP_FUNCTIONAPP_EX1_NAME = '部署/設定 GitHub Action 至 Azure 函式 - 互動模式'
HELP_FUNCTIONAPP_EX2_NAME = '部署/設定本機 GitHub 儲存庫至 Azure 函式的 GitHub Action'
HELP_FUNCTIONAPP_EX2_TEXT = '--repository 將從本機 git 儲存庫自動偵測'
HELP_FUNCTIONAPP_EX3_NAME = '部署/設定 GitHub 儲存庫至 Azure 函式的 GitHub Action'
