#troubleshooting 

### Python Import 故障排除總表

| **序號** | **錯誤訊息 (Error Msg)**                                                  | **根本原因 (Root Cause)**                                      | **解決辦法 (Solution)**                                                                                                  |
| ------ | --------------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **1**  | `ModuleNotFoundError: No module named 'xxx'`                          | **套件根本沒安裝**。你的環境中找不到這個套件。                                  | 執行 `pip install xxx`。                                                                                                |
| **2**  | `ModuleNotFoundError: No module named 'xxx'` (明明裝了)                   | **環境錯亂**。你裝在「系統環境」，但程式執行在「虛擬環境」（或反之）。                      | 確認 `pip` 和 `python` 是同一組。使用 `python -m pip install xxx` 最保險。                                                         |
| **3**  | `ImportError: cannot import name 'yyy' from 'xxx'`                    | **版本過舊或名稱寫錯**。套件裡沒有這個功能，或該功能在舊版不存在。                        | 1. 檢查拼字大小寫。 2. 升級套件：`pip install --upgrade xxx`。                                                                     |
| **4**  | `AttributeError: module 'xxx' has no attribute 'yyy'`                 | **影子效應 (Shadowing)**。你當前目錄有個跟套件**同名**的檔案（如 `requests.py`）。 | **修改你的檔案名稱**，不要跟知名套件撞名，並刪除 `__pycache__` 資料夾。                                                                        |
| **5**  | `ImportError: circular import groups`                                 | **循環引用**。A 檔案 import B，B 檔案又同時 import A，導致死結。              | 1. 重新設計架構。 2. 將 `import` 移到函數或方法內部。                                                                                  |
| **6**  | `ImportError: DLL load failed` (Windows 常見)                           | **缺少底層 C++ 執行庫**。某些套件需要 Windows 的 C++ Redistributable。     | 安裝 [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)。 |
| **7**  | `ModuleNotFoundError` (在子資料夾中)                                        | **路徑遺失**。Python 找不到自定義資料夾，因為它不在 `sys.path` 裡。              | 在資料夾內建立空的 `__init__.py`，或在執行前設定 `PYTHONPATH`。                                                                        |
| **8**  | `ImportError: attempted relative import with no known parent package` | **相對路徑錯誤**。你直接執行了使用 `from . import xxx` 的腳本。               | 不要直接執行子模組，應從專案根目錄用 `python -m my_package.sub_module` 執行。                                                             |
| **9**  | `PermissionError: [Errno 13]`                                         | **權限不足**。套件裝在系統路徑，但你沒有管理員權限。                               | 使用虛擬環境（強烈建議），或在指令後加上 `--user`。                                                                                       |
| **10** | `SyntaxError: invalid syntax`                                         | **Python 版本不相容**。你用 Python 2 的語法在 Python 3 環境中跑（或反之）。      | 檢查當前 Python 版本：`python --version`，確保與套件需求相符。                                                                         |

---

### 💡 專業診斷小工具

當你遇到 `import` 失敗且毫無頭緒時，請在你的程式碼最頂端加入這兩行：

Python

```
import sys
print(sys.path)
```

這會印出 Python 尋找套件的 **「所有清單」**。如果你的套件安裝路徑不在這份清單裡，Python 就永遠找不到它。

### 診斷 SOP：

1. **檢查有沒有裝**：`pip list` 看看清單裡有沒有它。
2. **檢查在哪裡跑**：在終端機輸入 `which python` (Mac/Linux) 或 `where python` (Windows)，確認你用的是不是你以為的那個環境。
3. **檢查有沒有撞名**：看看你的資料夾裡有沒有跟套件一樣名字的 `.py` 檔案。