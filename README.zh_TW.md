# deploy-to-azure — Azure CLI 擴充套件（繁體中文）

此 Azure CLI 擴充套件提供自動化指令，可透過 GitHub Actions 建立 CI/CD 流程並部署至 Azure 服務。

## 支援的部署目標

| 指令 | 目標服務 |
|---|---|
| `az aks app up` | Azure Kubernetes Service (AKS) |
| `az container app up` | Azure Container Instances (ACI) |
| `az functionapp app up` | Azure Functions |

---

## 安裝說明

### 前置需求

- Python 3.8 或更新版本
- [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli) 已安裝並登入

### Linux / macOS

```bash
# 下載並執行繁體中文安裝腳本
chmod +x install_zh_TW.sh
./install_zh_TW.sh
```

或手動安裝：

```bash
export LANG=zh_TW.UTF-8
az extension add --source deploy-to-azure/dist/deploy_to_azure-0.2.0-py2.py3-none-any.whl --yes
```

### Windows

```bat
install_zh_TW.bat
```

或手動安裝：

```bat
set LANG=zh_TW
az extension add --source deploy-to-azure\dist\deploy_to_azure-0.2.0-py2.py3-none-any.whl --yes
```

---

## 使用範例

### az aks app up — 部署至 AKS

```bash
# 互動模式（自動偵測設定）
LANG=zh_TW.UTF-8 az aks app up

# 指定叢集與儲存庫
LANG=zh_TW.UTF-8 az aks app up \
  --acr myregistry \
  --aks-cluster myakscluster \
  --repository https://github.com/myorg/myapp
```

### az container app up — 部署至 ACI

```bash
# 互動模式
LANG=zh_TW.UTF-8 az container app up

# 指定儲存庫
LANG=zh_TW.UTF-8 az container app up \
  --repository https://github.com/myorg/myapp \
  --acr myregistry
```

### az functionapp app up — 部署至 Azure Functions

```bash
# 互動模式
LANG=zh_TW.UTF-8 az functionapp app up

# 指定函式應用程式名稱
LANG=zh_TW.UTF-8 az functionapp app up \
  --app-name MyFunctionApp

# 指定函式應用程式與儲存庫
LANG=zh_TW.UTF-8 az functionapp app up \
  --app-name MyFunctionApp \
  --repository https://github.com/myorg/my-functions
```

---

## 繁體中文支援說明

當系統環境變數 `LANG` 或 `LC_ALL` 設定為 `zh_TW` 或 `zh_Hant` 開頭的值時，
CLI 介面將自動顯示繁體中文訊息。

```bash
# 僅對單次指令使用繁體中文
LANG=zh_TW.UTF-8 az aks app up

# 永久設定（加入 ~/.bashrc 或 ~/.zshrc）
export LANG=zh_TW.UTF-8
export LC_ALL=zh_TW.UTF-8
```

---

## 常見問題排解

### 問：執行時出現「找不到 az 指令」

**解決方法：** 請確認 Azure CLI 已正確安裝並加入系統 PATH。
- Linux/macOS：`curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`
- Windows：從 [Microsoft 官網](https://docs.microsoft.com/cli/azure/install-azure-cli-windows) 下載安裝程式

---

### 問：GitHub PAT 權杖建立失敗

**解決方法：**
1. 前往 [GitHub 設定 → 開發人員設定 → 個人存取權杖](https://github.com/settings/tokens)
2. 建立具有 `repo` 與 `user` 範圍的新 PAT
3. 將 PAT 設定為環境變數：
   ```bash
   export GITHUB_PAT=your_pat_token
   ```

---

### 問：部署後 GitHub Actions 工作流程失敗

**解決方法：**
1. 前往 GitHub 儲存庫的 **Actions** 頁面查看詳細日誌
2. 確認 Azure 資源（AKS、ACR、Function App）的名稱拼寫正確
3. 確認服務主體具有足夠的 Azure 資源存取權限

---

### 問：如何解除安裝此擴充套件？

```bash
az extension remove --name deploy-to-azure
```

---

## 版本資訊

目前版本：**0.2.0**

如需回報問題或貢獻代碼，請前往 [GitHub 儲存庫](https://github.com/Azure/deploy-to-azure-cli-extension)。
