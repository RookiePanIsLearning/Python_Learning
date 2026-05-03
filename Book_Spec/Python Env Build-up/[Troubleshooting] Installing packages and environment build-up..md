#troubleshooting 
### 1. 指令找不到（環境變數未設定）

- **錯誤訊息**：`'pip' is not recognized as an internal or external command` 或 `command not found: pip`
    
- **根本原因**：你在安裝 Python 時，沒有勾選「Add Python to PATH」，導致作業系統不知道 `pip` 程式放在哪裡。
    
- **解決辦法**：重新安裝並勾選 Add to PATH，或者在終端機改用 **`python -m pip install ...`**（因為 `python` 指令通常是有效的）。
    

### 2. 裝在房間外，人在房間內（虛擬環境未啟動）

- **錯誤訊息**：`ModuleNotFoundError: No module named 'requests'`
    
- **根本原因**：你在「全域環境」安裝了套件，但你卻啟動了「虛擬環境」來執行程式，虛擬環境內部是真空的，看不到外面的套件。
    
- **解決辦法**：先啟動虛擬環境（出現 `(venv)` 標誌），再重新執行一次安裝指令。
    

### 3. 編輯器與終端機的「平行時空」

- **錯誤訊息**：終端機顯示安裝成功，但 VS Code 程式碼下面出現紅線，且按下執行鈕報錯。
    
- **根本原因**：你的 VS Code 選擇的 **Python Interpreter（直譯器）** 是系統預設路徑，而你的終端機是在虛擬環境裡。
    
- **解決辦法**：在 VS Code 按 `Ctrl+Shift+P` -> `Select Interpreter` -> 選擇對應虛擬環境的 Python 檔案。
    

### 4. 權限不足（嘗試染指系統資料夾）

- **錯誤訊息**：`OSError: [Errno 13] Permission denied` 或 `Consider using the --user option`
    
- **根本原因**：你在沒開管理員權限的情況下，嘗試把套件裝在系統的核心資料夾（通常發生在 Mac/Linux 的全域環境）。
    
- **解決辦法**：強烈建議使用**虛擬環境**（不需權限），或暫時在指令後加上 `--user`（如：`pip install requests --user`）。
    

### 5. 檔案命名自殺事件（影子效應）

- **錯誤訊息**：`AttributeError: module 'requests' has no attribute 'get'`
    
- **根本原因**：你把你自己的程式檔命名為 `requests.py`。當你 `import requests` 時，Python 會優先抓到你這一份，而不是真正的套件。
    
- **解決辦法**：**絕對不要**把你的 `.py` 檔案命名成跟知名套件一樣的名字，請改名並刪除自動生成的 `__pycache__` 資料夾。
    

### 6. 相依性地獄（版本衝突）

- **錯誤訊息**：`ERROR: Cannot install ... because these package versions have conflicting dependencies.`
    
- **根本原因**：你想裝套件 A（需要套件 C 的 1.0 版），但你已經裝了套件 B（需要套件 C 的 2.0 版）。
    
- **解決辦法**：使用 `pipenv` 或 `poetry` 等現代化工具自動解決，或者手動調整 `requirements.txt` 中的版本號。
    

### 7. 編譯失敗（缺少 C++ 建置工具）

- **錯誤訊息**：`error: Microsoft Visual C++ 14.0 or greater is required.`
    
- **根本原因**：某些套件（如 `pandas` 或某些 AI 庫）的部分底層是 C++，安裝時需要編譯器，但你的 Windows 沒裝。
    
- **解決辦法**：照著錯誤提示去微軟官網下載安裝 "Build Tools for Visual Studio"，或是改用 `conda` 安裝（它會直接下載編譯好的二進位檔）。
    

### 8. 網路長城或公司防火牆（SSL 錯誤）

- **錯誤訊息**：`SSLError(SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED])`
    
- **根本原因**：你的公司網路或防毒軟體攔截了 pip 連往 PyPI 伺服器的加密連線。
    
- **解決辦法**：使用指令暫時跳過驗證：`pip install <套件> --trusted-host pypi.org --trusted-host files.pythonhosted.org`。
    

### 9. Python 2 與 3 的混亂（舊版 Mac/Linux 常見）

- **錯誤訊息**：套件裝好了，但執行時說版本不對（例如某些套件只支援 3.7+）。
    
- **根本原因**：你用的 `pip` 指令其實是連到 Python 2.7，而你的 `python` 指令也是 2.7。
    
- **解決辦法**：養成習慣，永遠使用 **`python3 -m pip install`** 和 **`python3 app.py`** 來明確指定版本。
    

### 10. 採購清單路徑錯誤

- **錯誤訊息**：`Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'`
    
- **根本原因**：你執行 `pip install -r requirements.txt` 時，終端機所在的位置（路徑）根本沒有這個檔案。
    
- **解決辦法**：先用 `cd` 指令切換到該檔案所在的資料夾，或是輸入完整路徑（例如 `pip install -r C:\projects\requirements.txt`）。

### 11. 如果我有建置「虛擬環境」，還會發生套件找不到的錯誤嗎？

答案是：**只要你「正確使用」，就絕對不會發生！但是，新手依然很容易在兩個常見的坑裡「翻車」。**

虛擬環境最偉大的發明，就是當你**啟動 (activate)** 它之後，它會強制把你終端機裡的 `python` 和 `pip` 綁定在同一個房間裡。所以在虛擬環境中，你直接打 `pip install pandas` 和 `python -m pip install pandas` 其實是一模一樣的安全。

但如果你有建置虛擬環境，卻還是出現 `ModuleNotFoundError`，通常只會是以下兩種情況：

#### 💣 翻車情況一：你建了房間，但忘記「走進去」（忘記啟動）

很多新手建好虛擬環境後，就直接開始打 `pip install`。 **結果：** 因為你沒有執行 `activate`（啟動指令），你其實還是站在「房間外」（系統全域環境）。套件裝到了系統裡，但你的程式可能是在房間內跑的，當然就找不到套件。

- **檢查方法：** 看看你的終端機指令列最前面，有沒有出現括號包住的環境名稱，例如 `(myenv) C:\Users\...`。有括號，才代表你真的在房間裡。
    

#### 💣 翻車情況二：終端機在房間裡，但你的「編輯器 (VS Code / PyCharm)」在房間外

這是最常見的大魔王！ **結果：** 你在終端機裡看著 `(myenv)`，開心地用 `pip install requests` 裝好了套件。結果你點擊 VS Code 右上角的「執行按鈕」▶️，程式卻還是報錯說找不到！

- **為什麼會這樣？** 因為你在終端機裡安裝套件，確實是裝進虛擬環境了。**但是你的 VS Code 卻還在用系統預設的 Python 執行程式**。編輯器跟終端機兩邊使用的 Python 不是同一個！
    
- **解決方法（以 VS Code 為例）：**
    
    1. 按下 `Ctrl + Shift + P` (Mac 是 `Cmd + Shift + P`) 開啟命令面板。
        
    2. 輸入並選擇 `Python: Select Interpreter` (選擇直譯器)。
        
    3. 在列表裡，選擇帶有你虛擬環境名稱（例如 `myenv`）的那一個 Python 路徑。這樣 VS Code 才會知道要去你的房間裡執行程式。
        

**總結來說：** 虛擬環境確實能完美解決版本打架的問題，但前提是你必須確認 **「你安裝套件的終端機」** 和 **「你執行程式的編輯器」**，這兩者都確實切換到了同一個虛擬環境中

---

### 💡 給你的最後建議

如果你想要避開以上 90% 的問題，最專業且省心的方法就是： **「每開一個新資料夾，就立刻建立一個全新的虛擬環境 (venv)，並只在裡面工作。」**

當你養成「先開房間（venv）、再進房間（activate）、最後買東西（pip install）」的習慣後，你會發現 Python 開發其實非常優雅且乾淨！