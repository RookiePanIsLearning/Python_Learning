# 🐍 PeterPan's Python Learning Journey (QA & Automation Focus)

這是我專屬的 Python 學習紀錄區。這個專案的目標是透過**「做中學 (Active Learning)」**與**「產出導向 (Project-Based)」**，在 16 週內從零開始掌握 Python 自動化腳本開發與軟體測試框架 (QA)。

---

## 🎯 核心學習專案：Dashboard 自動化生成
我的終極目標之一，是在學完基礎語法後撰寫一個 Python 標記語言解析器 (`scripts/build_tracker.py`)。
這個腳本會讀取我的 Markdown 筆記，並且自動編譯產生一個超有科技感的 [學習進度儀表板 (Dashboard) - `index.html`](./index.html)。

未來這個 Dashboard 將透過 GitHub Pages 直接公開展示！

---

## 📂 專案目錄結構

```text
Python_Learning/
│
├── index.html                         # ✨ 前端學習追蹤儀表板
├── spec.md                            # 📝 核心學習計畫規格書 (內含 16 週 QA 自動化課綱)
├── Learning_Diary.md                  # 📓 學習日記本 (Bug 紀錄與心得)
├── README.md                          # 📖 專案說明 (本文件)
│
├── 01_Syntax_Notes/                   # 🧠 語法總結與筆記區 (費曼學習法的產出)
│   ├── 00_Index.md                    # 語法筆記總目錄
│   └── (各主題語法對照與觀念比較)
│
├── 02_Exercises/                      # 💻 實戰演練區 (從 Phase 1 到 Phase 4)
│   ├── 01_basics ~ 13_playwright_e2e  # 各模組練習程式碼存放處
│   └── leetcode_practice/             # 演算法或刷題區
│
├── 03_Projects/                       # 🚀 實作小專案 (Phase 5)
│   ├── 01_test_framework              # 自動化測試框架搭建
│   ├── 02_system_monitor              # 系統巡檢自動化
│   └── 03_tracker_dashboard           # 負責產出 index.html 的網站生成器
│
└── scripts/                           # 🤖 開發工具腳本區
    └── create_skeleton.py             # 用來自動生成學習目錄與範本檔的腳本
```

---

## 🗺️ 學習進度規劃 (16-Week QA & Automation Roadmap)

我們依據實戰需求，將學習路徑分為五大階段。詳細的課綱與打勾進度，請參考專案根目錄下的 [`spec.md`](./spec.md)。

- 🟩 **階段一：Python 核心基礎 (週次 1-3)**
  - 奠定程式基礎、迴圈、與四大資料結構 (List, Tuple, Set, Dict)。
- 🟨 **階段二：進階程式設計與物件導向 (週次 4-6)**
  - 掌握 `def`、`lambda`、例外處理與基礎 OOP。
- 🟧 **階段三：系統管理與 API 自動化 (週次 7-9)**
  - 利用 Python 操作作業系統資源 (`os`, `sys`) 並撰寫 HTTP 請求打 API (`requests`)。
- 🟥 **階段四：軟體測試與進階 QA 框架 (週次 10-13)**
  - 導入單元測試 (`unittest`)、與強大的 API/UI 自動化框架 (`Pytest`, `Playwright`)。
- 🏆 **階段五：期末實戰專案 (週次 14-17)**
  - 實作「測試報告生成器」與「自動化學習儀表板」。

---
## 📓 Notebook 學習模式（已啟用）

為了提升互動式學習效率，`02_Exercises` 的前段基礎主題已新增 `.ipynb` 版本，方便你用「分段執行 + 即時觀察輸出」的方式練習：

- `01_basics/01_variables_types.ipynb`
- `02_flow_control/01_if_else.ipynb`
- `04_loops/03_list_comprehension.ipynb`
- `05_functions/01_def_and_scope.ipynb`
- `06_file_and_exceptions/01_file_io.ipynb`
- `06_file_and_exceptions/02_try_except.ipynb`
- `07_oop/01_classes.ipynb`
- `08_os_sys_automation/01_os_module.ipynb`
- `09_api_requests/01_get_post.ipynb`
- `10_scheduling/01_schedule.ipynb`

原本的 `.py` 檔案仍保留，方便你後續做版本比較、命令列執行與測試整合。

建議做法：

- 學習與探索：優先使用 `.ipynb`
- 測試與自動化（`11_unittest` 之後）：維持 `.py`

每次完成 Notebook 練習後，建議執行一次「Restart Kernel + Run All」，避免隱性狀態造成誤判。

---

## 🔧 Git 常用命令流程

以下是一些常用的 Git 命令流程，方便快速提醒自己：

### 初始化倉庫
```bash
git init                    # 初始化本地倉庫
git remote add origin <url> # 添加遠端倉庫
```

### 日常工作流程
```bash
git status                  # 查看當前狀態
git add .                   # 添加所有更改到暫存區
git add <file>              # 添加特定文件
git commit -m "message"     # 提交更改
git push origin main        # 推送到遠端主分支
git pull origin main        # 從遠端拉取最新更改
```

### 分支管理
```bash
git branch                  # 查看所有分支
git branch <name>           # 創建新分支
git checkout <name>         # 切換到分支
git checkout -b <name>      # 創建並切換到新分支
git merge <branch>          # 合併分支到當前分支
```

### 其他實用命令
```bash
git log                     # 查看提交歷史
git diff                    # 查看更改差異
git reset --hard HEAD~1     # 回退到上一個提交
git stash                   # 暫存當前更改
git stash pop               # 恢復暫存的更改
```

> *Generated efficiently with love and Python. Ready to code!* 🚀
