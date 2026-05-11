# 建立繁體中文安裝包 (Build Traditional Chinese Installation Package)

你的任務是為 `deploy-to-azure` Azure CLI 擴充套件建立支援繁體中文的萬用安裝包。

## 步驟一：新增繁體中文本地化字串

1. 在 `deploy-to-azure/azext_deploy_to_azure/dev/common/` 目錄下建立 `locale/zh_TW/` 資料夾。
2. 建立 `messages.py`，包含所有 CLI 提示訊息的繁體中文翻譯。翻譯範圍涵蓋：
   - `prompting.py` 中的所有使用者提示
   - `github_credential_manager.py` 中的認證訊息
   - `github_workflow_helper.py` 中的狀態訊息
   - `azure_cli_resources.py` 中的資源選擇提示
   - 各功能模組 (`aks/`, `aci/`, `functionapp/`) 的 `_help.py` / `help.py` 說明文字

3. 修改 `dev/common/prompting.py`，在訊息輸出前先偵測系統語言（`LANG` / `LC_ALL` 環境變數），若為 `zh_TW` 或 `zh_Hant`，則使用繁體中文字串。

## 步驟二：更新說明文字

在 `dev/aks/_help.py`、`dev/aci/_help.py`、`dev/functionapp/help.py` 中，為每個指令加入繁體中文 `short-summary` 和 `long-summary`。

## 步驟三：建立安裝腳本

在專案根目錄建立 `install_zh_TW.sh`（Linux/macOS）和 `install_zh_TW.bat`（Windows），內容包含：
1. 環境前置檢查（Python 3.8+、Azure CLI 已安裝）
2. 設定 `LANG=zh_TW.UTF-8`（Linux/macOS）或 `set LANG=zh_TW`（Windows）
3. 用 `az extension add --source` 安裝本地 wheel
4. 安裝成功後顯示繁體中文確認訊息

## 步驟四：建立 Wheel 安裝包

執行以下指令建立 wheel 並驗證：

```bash
cd deploy-to-azure
python setup.py sdist bdist_wheel
# 驗證 wheel 內容
python -m zipfile -l dist/*.whl | grep -E "(py|txt|cfg)"
```

## 步驟五：產生繁體中文 README

建立 `README.zh_TW.md`，包含：
- 繁體中文安裝說明（支援 Linux、macOS、Windows）
- `az aks app up`、`az container app up`、`az functionapp app up` 的使用範例
- 常見問題排解（繁體中文）

## 驗證清單

- [ ] `pytest` 全部通過
- [ ] `pylint` 無新增警告
- [ ] `flake8` 無新增錯誤
- [ ] 在 `LANG=zh_TW.UTF-8` 環境下測試 CLI 輸出為繁體中文
- [ ] wheel 可透過 `az extension add --source dist/*.whl` 安裝

完成後，提交所有變更並推送到 `claude/add-chinese-support-Oljse` 分支。
