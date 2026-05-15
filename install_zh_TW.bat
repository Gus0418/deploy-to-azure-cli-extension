@echo off
REM --------------------------------------------------------------------------------------------
REM 繁體中文版 deploy-to-azure CLI 擴充套件安裝腳本 (Windows)
REM --------------------------------------------------------------------------------------------
chcp 65001 >nul
set LANG=zh_TW

echo ==============================
echo  deploy-to-azure 擴充套件安裝程式
echo ==============================
echo.

REM 1. 檢查 Python 3.8+
echo ^>^>^> 檢查 Python 版本...
python --version >nul 2>&1
if errorlevel 1 (
    echo 錯誤：找不到 Python。請先安裝 Python 3.8 或更新版本。
    echo 下載：https://www.python.org/downloads/
    exit /b 1
)
for /f "tokens=2" %%v in ('python --version 2^>^&1') do set PY_VER=%%v
for /f "tokens=1,2 delims=." %%a in ("%PY_VER%") do (
    set PY_MAJOR=%%a
    set PY_MINOR=%%b
)
if %PY_MAJOR% LSS 3 (
    echo 錯誤：需要 Python 3.8 或更新版本，目前版本為 %PY_VER%。
    exit /b 1
)
if %PY_MAJOR% EQU 3 if %PY_MINOR% LSS 8 (
    echo 錯誤：需要 Python 3.8 或更新版本，目前版本為 %PY_VER%。
    exit /b 1
)
echo     Python %PY_VER% - 符合要求

REM 2. 檢查 Azure CLI
echo ^>^>^> 檢查 Azure CLI...
az version >nul 2>&1
if errorlevel 1 (
    echo 錯誤：找不到 Azure CLI。請先安裝 Azure CLI。
    echo 安裝說明：https://docs.microsoft.com/cli/azure/install-azure-cli-windows
    exit /b 1
)
echo     Azure CLI - 符合要求

REM 3. 找到 wheel 檔案
echo ^>^>^> 尋找 wheel 安裝包...
set SCRIPT_DIR=%~dp0
set WHEEL_FILE=
for /f "delims=" %%f in ('dir /b /s "%SCRIPT_DIR%deploy-to-azure\dist\*.whl" 2^>nul') do set WHEEL_FILE=%%f

if "%WHEEL_FILE%"=="" (
    echo     找不到 wheel 檔案，正在建立...
    pushd "%SCRIPT_DIR%deploy-to-azure"
    python setup.py sdist bdist_wheel
    if errorlevel 1 (
        echo 錯誤：wheel 建立失敗。
        popd
        exit /b 1
    )
    popd
    for /f "delims=" %%f in ('dir /b /s "%SCRIPT_DIR%deploy-to-azure\dist\*.whl" 2^>nul') do set WHEEL_FILE=%%f
)
if "%WHEEL_FILE%"=="" (
    echo 錯誤：無法找到或建立 wheel 安裝包。
    exit /b 1
)
echo     使用安裝包：%WHEEL_FILE%

REM 4. 安裝擴充套件
echo ^>^>^> 安裝 deploy-to-azure 擴充套件...
az extension add --source "%WHEEL_FILE%" --yes
if errorlevel 1 (
    echo 錯誤：擴充套件安裝失敗。請確認 wheel 檔案有效且 Azure CLI 正常運作。
    exit /b 1
)

echo.
echo ==============================
echo  安裝成功！
echo ==============================
echo.
echo 可用命令：
echo   az aks app up          - 透過 GitHub Actions 部署至 AKS
echo   az container app up    - 透過 GitHub Actions 部署至 ACI
echo   az functionapp app up  - 透過 GitHub Actions 部署至 Azure Functions
echo.
echo 執行 az aks app up --help 以查看詳細說明。
