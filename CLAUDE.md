# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

An Azure CLI extension (`deploy-to-azure`) that automates setting up GitHub Actions CI/CD pipelines targeting Azure services. The three supported targets are:

- **AKS** (`az aks app up`) — builds container image, pushes to ACR, deploys via Helm to AKS
- **ACI** (`az container app up`) — builds container image, pushes to ACR, deploys to Azure Container Instances
- **Function App** (`az functionapp app up`) — deploys to Azure Functions

All three commands follow the same flow: detect/prompt for GitHub repo → authenticate with GitHub PAT → detect language → select/create Azure resources → generate and commit workflow YAML (and optionally Dockerfiles/Helm charts) → optionally poll for workflow completion.

## Development Commands

All commands run from the repo root unless noted.

### Install for local development
```bash
cd deploy-to-azure && pip install --upgrade -e .
```

### Build wheel
```bash
cd deploy-to-azure && python setup.py sdist bdist_wheel
```

### Run tests
```bash
# From repo root (runs all tests discovered by pytest)
pytest

# Run a single test file
pytest deploy-to-azure/azext_deploy_to_azure/tests/common/test_git.py

# Run a single test by name
pytest deploy-to-azure/azext_deploy_to_azure/tests/common/test_git.py::TestGitMethods::test_github_url_candidate
```

### Linting (both must pass)
```bash
python -m pylint --rcfile pylintrc ./deploy-to-azure/azext_deploy_to_azure -f colorized
python -m flake8 --config .flake8
```

Install linters first if needed: `pip install pylint flake8`

## Code Architecture

### Extension entry point
`deploy-to-azure/azext_deploy_to_azure/__init__.py` registers `DevCommandsLoader` with `COMMAND_LOADER_CLS`. This class delegates to `load_command_table` and `load_arguments` which fan out to the three feature modules (aks, aci, functionapp).

### Feature modules pattern
Each of `dev/aks/`, `dev/aci/`, `dev/functionapp/` contains the same four files:
- `commands.py` — registers the CLI command and maps it to the `up.py` function
- `arguments.py` — declares CLI argument overrides (e.g., `--repository/-r`)
- `_help.py` / `help.py` — help text
- `up.py` — the actual implementation (the `aks_deploy`, `aci_up`, `functionapp_deploy` functions)

### Shared common module (`dev/common/`)
| File | Purpose |
|---|---|
| `git.py` | Detects GitHub remote URL from local git context |
| `github_credential_manager.py` | Singleton that prompts for/caches GitHub PAT; checks `GITHUB_PAT` env var first |
| `github_api_helper.py` | All GitHub REST API calls (branches, file commits, PRs, secrets, check runs). Defines `Files(path, content)` dataclass |
| `github_azure_secrets.py` | Creates `AZURE_CREDENTIALS`, `REGISTRY_USERNAME`, `REGISTRY_PASSWORD` secrets in the GitHub repo via `az ad sp create-for-rbac` |
| `github_workflow_helper.py` | Polls workflow status using `colorama`/`humanfriendly` spinners |
| `azure_cli_resources.py` | Queries Azure resources (AKS, ACR, Function Apps) by shelling out to `az` CLI |
| `prompting.py` | Interactive prompting helpers wrapping knack |
| `const.py` | Placeholder strings used in template substitution |

### Templates and resource files
`dev/resources/resourcefiles.py` contains all GitHub Actions workflow YAML templates as Python string constants (e.g. `DEPLOY_TO_AKS_TEMPLATE`). Placeholders like `container_registry_name_place_holder` are replaced at runtime using `.replace()` with constants from `const.py`.

`dev/resources/packs/{java,javascript,python}/` contains language-specific Dockerfile, `.dockerignore`, and Helm chart templates. The `docker_helm_template.py` reads these from disk and substitutes port/ACR name placeholders before committing to GitHub.

### GitHub API authentication
`GithubCredentialManager` (singleton via `@singleton` decorator in `utils.py`) handles PAT acquisition. It checks the `GITHUB_PAT` environment variable first, then prompts interactively. The PAT is used as HTTP Basic Auth password in all `requests` calls.

### Azure resource queries
`azure_cli_resources.py` shells out to `az` CLI via `subprocess.check_output(..., shell=True)` and parses JSON output. It uses `azure.cli.core._profile.Profile` to get the current subscription context.

## Linting Rules

- Max line length: 120 characters (flake8 and pylint)
- Pylint disabled globally: `missing-docstring`, `too-many-arguments`, `invalid-name`, `duplicate-code`, `import-outside-toplevel`
- Tests are excluded from pylint (`ignore-patterns=test_*`) and flake8 linting

## Versioning and Release

Version is defined in `deploy-to-azure/azext_deploy_to_azure/version.py`. To release:
1. Trigger the Azure Pipelines "Create Release" build (creates wheel + draft GitHub release)
2. Update `src/index.json` in the `azure/azure-cli-extensions` repo with the new wheel URL and SHA256
3. Create a `release-0.x.0` branch from master
4. Bump `version.py` for the next development cycle

See `doc/release_new_version.md` for details.

---

# Plugin MEGA — 全技能合體版

> 共 30 個技能，根據用戶請求自動判斷啟動
> 所有涉及真實世界操作的技能，**必須在執行前獲得明確確認**

---

# 🎨 創意設計技能

## 演算法生成藝術
**觸發**：生成藝術、演算法藝術、粒子系統、流場、互動視覺
**動作**：建立演算法哲學（4-6段）→ 用 p5.js 實作 → 輸出含種子控制器的 HTML Artifact

## 視覺海報設計
**觸發**：海報、視覺藝術、設計作品、PNG/PDF 輸出
**動作**：建立設計哲學 → 用 Python+PIL 建立 → 輸出 PDF 或 PNG

## Slack GIF 製作
**觸發**：Slack GIF、動態表情、動畫 GIF
**動作**：用 PIL 逐幀繪製 → 儲存為 128×128 or 480×480 優化 GIF

## 主題樣式工廠
**觸發**：套用主題、投影片風格、設計主題
**動作**：展示 10 種預設主題 → 用戶選擇 → 套用顏色和字體
**10 種主題**：Ocean Depths / Sunset Boulevard / Forest Canopy / Modern Minimalist / Golden Hour / Arctic Frost / Desert Rose / Tech Innovation / Botanical Garden / Midnight Galaxy

## Anthropic 品牌規範
**觸發**：Anthropic 品牌、品牌風格、公司設計規範
**顏色**：深色 #141413 / 淺色 #faf9f5 / 橙 #d97757 / 藍 #6a9bcc / 綠 #788c5d
**字體**：標題 Poppins / 內文 Lora

---

# 💼 工作效率技能

## 文件共同撰寫
**觸發**：寫文件、提案、技術規格、PRD、RFC、決策文件
**三階段**：情境收集 → 逐段精煉（每段 5-20 選項篩選）→ 讀者測試

## 內部溝通文件
**觸發**：3P 更新、週報、公告、FAQ、事故報告
**格式**：3P更新/電子報/FAQ/狀態報告/領導層更新/事故報告

## 財務試算機
**觸發**：稅務估算、貸款計算、退休規劃、投資試算、薪資比較
**輸出**：醒目結論 + 詳細計算 + 3個比較情境 + 一句重點結論

## MCP 伺服器建構
**觸發**：建立 MCP 伺服器、整合 API、Claude 連接外部服務
**四階段**：研究規劃 → TypeScript 實作 → 測試 → 建立評估

## Web Artifact 建構
**觸發**：複雜前端 Artifact、需要 React/shadcn 元件
**技術棧**：React 18 + TypeScript + Tailwind + shadcn/ui + Parcel 打包

## Skill 建立器
**觸發**：建立/改善 Claude Skill、技能評估、觸發優化
**流程**：了解意圖 → 撰寫 SKILL.md → 建立測試 → 執行評估 → 反覆改善

---

# 🛒 生活助理技能

## 電話預約
**觸發**：幫我預約 [任何地方]
**流程**：查日曆 → 收集資訊 → 確認計畫 → 撥打電話（立即自報是 Claude AI）→ 加入行事曆

## 取消訂閱 ⚠️
**觸發**：取消訂閱、退訂服務、不要再扣款
**注意**：破壞性操作，展示計畫並獲得明確確認才執行
**流程**：識別服務 → 可掃描帳單批次取消 → 確認時機和退款 → 執行 → 確認卡

## 活動規劃
**觸發**：規劃活動、生日/婚禮/聚會
**規模**：小型（輕觸）/ 中型（+預算追蹤）/ 大型（+供應商協調）

## 費用申報
**觸發**：報帳、申報費用、填費用報告
**支援平台**：Benepass / Brex / Concur / Expensify / Ramp
**流程**：選平台 → 搜尋收據 → 重複申報檢查 → 填表上傳 → 確認卡 → 提交

## 政府/行政表單
**觸發**：陪審義務/停車罰單/護照/監理/許可證/保險申請
**流程**：識別任務（可看照片）→ 研究流程 → 填入記憶中的個人資訊 → 執行 → 確認

## 生鮮採購
**觸發**：訂生鮮、採購食材、超市購物外送
**流程**：選 App → 確定目的 → 生成建議清單 → 確認 → 加入購物車 → 確認後結帳

## 找人幫忙
**觸發**：找人清潔/修繕/搬家/組裝
**平台**：TaskRabbit / Handy / Thumbtack / Care.com
**流程**：了解需求 → 搜尋 2-3 人選 → 確認摘要卡 → 執行預訂

## 訂餐外送
**觸發**：幫我訂餐，X 點要到
**流程**：確認到達時間 → 從目標時間往回推算下單時機 → 只展示可準時到的餐廳 → 推薦套餐 → 確認後下單

## 處方補充
**觸發**：藥快用完了、幫我補藥
**注意**：先確認是補充同一處方（非換劑量）
**流程**：確認處方 → 收集藥局資訊 → 找最快方式 → 確認計畫 → 執行

## 退貨退款
**觸發**：退貨、申請退款
**流程**：確認商品 → 查退貨政策 → 找最快路徑 → 執行（線上/電話/親自到店）→ 確認卡

## Benepass 報銷
**觸發**：Benepass 報銷
**前提**：需要瀏覽器 + Gmail MCP
**流程**：提取收據資訊 → 登入（Email Code 驗證）→ 選福利類別 → 填表上傳 → 確認後提交

---

# 📄 文件工具技能

## Word 文件（.docx）
**觸發**：Word 文件、.docx、正式報告/信件/合約
**工具**：docx-js 套件，輸出可下載的 .docx

## PDF 工具
**觸發**：建立/合併/分割/填寫/加浮水印 PDF
**功能**：建立/合併/分割/旋轉/浮水印/填表/加密/提取圖片/OCR

## PDF 閱讀
**觸發**：讀取/分析 PDF 內容
**策略**：文字豐富→直接提取 / 掃描版→OCR / 投影片→截圖分析

## PowerPoint（.pptx）
**觸發**：投影片、簡報、.pptx
**工具**：python-pptx，支援版面/主題/動畫/備註

## Excel（.xlsx）
**觸發**：Excel、試算表、.xlsx/.csv
**工具**：openpyxl / pandas，保留格式或重組均可

## 前端 UI 設計
**觸發**：設計網頁/介面/元件/儀表板
**原則**：避免 AI 制式感（無紫色漸層/統一圓角），生產級品質

## 檔案閱讀路由器
**觸發**：用戶上傳了任何檔案需要讀取
**路由**：PDF→提取/OCR / docx→extract / xlsx/csv→pandas / 圖片→視覺分析

---

# 🌐 全語系翻譯技能

**觸發**：翻譯、translation、任何要求語言轉換的情況
**支援**：全球主要語言，自動判斷語言和內容類型
**快速指令**：`全語言` / `正式版` / `口語版` / `對照版` / `回譯檢查`
**台灣繁中優先**：軟體/網路/資訊/應用程式（非軟件/網絡/信息）

### 翻譯輸出格式

**標準翻譯**
```
【翻譯結果】
（翻譯內容）

【語言】來源語言 → 目標語言
【類型】偵測到的內容類型
```

**多語言同步輸出**（指令：全語言）
```
🇹🇼 繁中：...
🇺🇸 英文：...
🇯🇵 日文：...
🇰🇷 韓文：...
🇪🇸 西班牙文：...
```

### 自動判斷邏輯
1. 未指定目標語言 → 繁中輸入譯英文；英文輸入譯繁中（台灣）
2. 未指定風格 → 依內容類型自動選擇
3. 混合語言輸入 → 整體翻成主要目標語言，保留必要專有名詞
4. 單一詞彙 → 給出詞義、多種翻法、例句

---

## 自動判斷規則

遇到請求時，按以下優先順序判斷：

1. **有明確技能名稱** → 直接啟動對應技能
2. **描述符合觸發條件** → 啟動最匹配的技能
3. **涉及實際操作（預約/購買/提交）** → 啟動前必須確認
4. **無法判斷** → 詢問用戶需要哪種類型的幫助
