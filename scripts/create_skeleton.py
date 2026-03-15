import os

base_dir = r"C:\Users\PeterPan\Python_Learning\Python_Learning"

# 根據 spec.md 的課綱規劃建立資料夾
directories = [
    "02_Exercises/01_basics",
    "02_Exercises/02_flow_control",
    "02_Exercises/03_data_structures",
    "02_Exercises/04_functions",
    "02_Exercises/05_file_and_exceptions",
    "02_Exercises/06_oop",
    "02_Exercises/07_os_sys_automation",
    "02_Exercises/08_api_requests",
    "02_Exercises/09_scheduling",
    "02_Exercises/10_unittest",
    "02_Exercises/11_pytest",
    "02_Exercises/12_api_automation",
    "02_Exercises/13_playwright_e2e",
    "03_Projects/01_test_framework",
    "03_Projects/02_system_monitor",
    "03_Projects/03_tracker_dashboard",
    "scripts"
]

# 針對每個模組建立一個起手式 (練習檔範本)
files = {
    "02_Exercises/01_basics/01_variables_types.py": "# 模組 1：開發環境建置與變數型態 \n# 目標：練習宣告 int, float, str, bool 以及基本的 f-string 操作",
    "02_Exercises/02_flow_control/01_if_else.py": "# 模組 2：條件判斷 (if/elif/else)\n# 目標：實作基礎邏輯判斷",
    "02_Exercises/04_functions/01_def_and_scope.py": "# 模組 4：函式定義與變數作用域\n# 目標：練習撰寫帶有預設參數與 return 的傳統函式",
    "02_Exercises/05_file_and_exceptions/01_file_io.py": "# 模組 5：檔案讀寫 (File I/O)\n# 目標：練習使用 with open 讀寫 txt/csv 檔案",
    "02_Exercises/05_file_and_exceptions/02_try_except.py": "# 模組 5：例外處理\n# 目標：練習 try/except 來捕捉常見錯誤",
    "02_Exercises/06_oop/01_classes.py": "# 模組 6：物件導向程式設計 (OOP)\n# 目標：定義基本 Class 與 __init__",
    "02_Exercises/07_os_sys_automation/01_os_module.py": "# 模組 7：系統與作業系統互動 (os, sys)\n# 目標：寫一個小腳本自動列出資料夾內的所有檔案名稱",
    "02_Exercises/08_api_requests/01_get_post.py": "# 模組 8：API 串接與資料解析\n# 目標：使用 requests 發送 GET 請求並解析 JSON",
    "02_Exercises/09_scheduling/01_schedule.py": "# 模組 9：自動化排程與批次處理\n# 目標：用 time 模組或定時任務定期印出時間",
    "02_Exercises/10_unittest/test_basic.py": "# 模組 10：單元測試基礎 (unittest)\nimport unittest\n\nclass TestMyFunction(unittest.TestCase):\n    pass",
    "02_Exercises/11_pytest/test_fixtures.py": "# 模組 11：Pytest 測試框架\nimport pytest\n\ndef test_example():\n    assert 1 + 1 == 2",
    "02_Exercises/12_api_automation/test_api.py": "# 模組 12：API 自動化測試實戰\nimport requests\nimport pytest\n\n# 對某個公開 API 進行單元測試",
    "02_Exercises/13_playwright_e2e/test_ui.py": "# 模組 13：Playwright UI 自動化測試實戰\n# 將使用 playwright 測試網頁互動",
    "scripts/build_tracker.py": "# 期末專案：Dashboard 自動化生成腳本\n# 負責讀取 Markdown 並自動更新 index.html 給 GitHub Pages"
}

for d in directories:
    dir_path = os.path.join(base_dir, d)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Created directory: {d}")

for f, content in files.items():
    path = os.path.join(base_dir, f)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as file:
            file.write(content + "\n")
        print(f"Created file: {f}")

print("========================================")
print("所有課綱的練習資料夾與範本檔案已成功建立！")
print("========================================")
