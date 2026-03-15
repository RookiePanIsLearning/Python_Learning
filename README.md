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
> *Generated efficiently with love and Python. Ready to code!* 🚀
