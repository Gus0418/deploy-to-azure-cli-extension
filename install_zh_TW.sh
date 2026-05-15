#!/usr/bin/env bash
# --------------------------------------------------------------------------------------------
# 繁體中文版 deploy-to-azure CLI 擴充套件安裝腳本 (Linux / macOS)
# --------------------------------------------------------------------------------------------
set -euo pipefail

# 設定繁體中文環境
export LANG=zh_TW.UTF-8
export LC_ALL=zh_TW.UTF-8

echo "=============================="
echo " deploy-to-azure 擴充套件安裝程式"
echo "=============================="
echo ""

# 1. 檢查 Python 3.8+
echo ">>> 檢查 Python 版本..."
if ! command -v python3 &>/dev/null; then
    echo "錯誤：找不到 python3。請先安裝 Python 3.8 或更新版本。"
    exit 1
fi
PY_VER=$(python3 -c "import sys; print('{}.{}'.format(sys.version_info.major, sys.version_info.minor))")
PY_MAJOR=$(echo "$PY_VER" | cut -d. -f1)
PY_MINOR=$(echo "$PY_VER" | cut -d. -f2)
if [ "$PY_MAJOR" -lt 3 ] || { [ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 8 ]; }; then
    echo "錯誤：需要 Python 3.8 或更新版本，目前版本為 ${PY_VER}。"
    exit 1
fi
echo "    Python ${PY_VER} - 符合要求 ✓"

# 2. 檢查 Azure CLI
echo ">>> 檢查 Azure CLI..."
if ! command -v az &>/dev/null; then
    echo "錯誤：找不到 Azure CLI (az)。請先安裝 Azure CLI。"
    echo "安裝說明：https://docs.microsoft.com/cli/azure/install-azure-cli"
    exit 1
fi
AZ_VER=$(az version --query '"azure-cli"' -o tsv 2>/dev/null || echo "未知")
echo "    Azure CLI ${AZ_VER} - 符合要求 ✓"

# 3. 找到 wheel 檔案
echo ">>> 尋找 wheel 安裝包..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WHEEL_FILE=$(find "${SCRIPT_DIR}/deploy-to-azure/dist" -name "*.whl" 2>/dev/null | sort -V | tail -1)
if [ -z "$WHEEL_FILE" ]; then
    echo "    找不到 wheel 檔案，正在建立..."
    cd "${SCRIPT_DIR}/deploy-to-azure"
    python3 setup.py sdist bdist_wheel --quiet
    WHEEL_FILE=$(find "${SCRIPT_DIR}/deploy-to-azure/dist" -name "*.whl" | sort -V | tail -1)
    cd "${SCRIPT_DIR}"
fi
echo "    使用安裝包：${WHEEL_FILE}"

# 4. 安裝擴充套件
echo ">>> 安裝 deploy-to-azure 擴充套件..."
az extension add --source "${WHEEL_FILE}" --yes

echo ""
echo "=============================="
echo " 安裝成功！"
echo "=============================="
echo ""
echo "可用命令："
echo "  az aks app up          - 透過 GitHub Actions 部署至 AKS"
echo "  az container app up    - 透過 GitHub Actions 部署至 ACI"
echo "  az functionapp app up  - 透過 GitHub Actions 部署至 Azure Functions"
echo ""
echo "執行 'az aks app up --help' 以查看詳細說明。"
