# Python 學習計畫規格書 (Learning Specification)

這份文件定義了我們後續學習 Python 的核心策略、檔案架構以及互動流程。
在雙方確認無誤後，未來的所有練習與筆記都會依照此規格進行。

## 1. 核心學習策略 (Core Strategies)
1. **輸出大於輸入 (Active Learning)**：看完觀念後，立刻動手打程式碼，並故意修改看看錯誤訊息。
2. **費曼學習法 (Feynman Technique)**：語法總結與日記，必須用「自己的話」寫下，而非複製貼上官方文件。
3. **專案導向 (Project-Based)**：學完基礎語法後，盡快進入小專案實作（如爬蟲、小遊戲），從實戰中找解答。
4. **刻意練習 (Deliberate Practice)**：針對迴圈、推導式等重要觀念，建立專屬資料夾反覆演練不同變化。

## 2. 檔案目錄架構 (Directory Structure)
```text
Python_Learning/
│
├── index.html                         # ✨ 前端學習追蹤儀表板 (部署至 GitHub Pages)
├── spec.md                            # 學習計畫規格書 (本文件)
├── Learning_Diary.md                  # 學習日記本 (記錄每日學習、Bug 卡關紀錄、解決心得)
│
├── scripts/                           # 自動化腳本區
│   └── build_tracker.py               # (未來專案) 自動讀取 Markdown 並更新前端進度的 Python 程式
│
├── 01_Syntax_Notes/                   # 語法總結與筆記區
│   ├── 00_Index.md                    # 語法筆記總目錄
│   └── [主題]_notes.md                 # 各主題的語法對照與觀念比較 (例如：def_vs_lambda.md)
│
├── 02_Exercises/                      # 實戰演練區 (實際寫 code 的地方)
│   ├── 01_basics/                     # 基礎變數與型態練習
│   ├── 03_loops/                      # 迴圈專屬練習區
│   │   ├── 01_for_and_while.py
│   │   └── 03_list_comprehension.py   # 將題目與解答寫在一起，方便單獨執行
│   └── leetcode_practice/             # 演算法或刷題區
│
└── 03_Projects/                       # 實作小專案 (未來擴充)
```

## 3. 語法總結的撰寫原則 (Notes Guideline)
在 `01_Syntax_Notes` 內的筆記，必須遵循以下四大原則：
1. **白話文優先**：用教導朋友的口吻撰寫，拒絕文言文。
2. **對照比較 (Comparison)**：必須列出「傳統寫法」vs「進階寫法」，或類似觀念的比較表格 (如 List vs Tuple)。
3. **情境舉例 (Use Case)**：明確列出「什麼時候」該用這個語法。
4. **易錯點 (Gotchas)**：標記曾經踩雷或常見的新手錯誤。

## 4. 學習進度與課表規劃 (Learning Roadmap - QA Automation Focus)
這是一份為期約 12 到 16 週的系統性課綱，重心放在**自動化腳本**、**API 串接**以及**軟體測試 (QA)** 等實務應用上，能直接對接系統管理與進階測試工程的需求。

### 🟩 階段一：Python 核心基礎 (週次 1-3)
*目標：建立紮實的程式邏輯與 Python 語法基礎。*
* [ ] 模組 1：開發環境建置與變數型態 (VS Code, 型態, 運算子操作)
* [ ] 模組 2：條件判斷 (if/elif/else)
* [x] 模組 2：迴圈控制與跳脫 (for, while, break, continue)
* [x] 模組 3：核心資料結構 (List, Tuple, Set, Dict)
* [x] 模組 3：進階操作與推導式 (List/Dict Comprehensions)

### 🟨 階段二：進階程式設計與物件導向 (週次 4-6)
*目標：掌握可重複使用的程式碼架構與模組化開發。*
* [x] 模組 4：函式定義與匿名函式 (def, args/kwargs, lambda, scope)
* [ ] 模組 5：檔案與例外處理 (txt/csv 讀寫, log 記錄, try/except)
* [ ] 模組 6：物件導向程式設計 (Class, Object, 繼承, 多型)

### 🟧 階段三：系統管理與 API 自動化 (週次 7-9)
*目標：能夠撰寫腳本來自動化日常任務、管理資源並與外部服務溝通。*
* [ ] 模組 7：系統與作業系統互動 (os, sys, subprocess, shutil)
* [ ] 模組 8：API 串接與資料解析 (HTTP GET/POST, requests, JSON)
* [ ] 模組 9：自動化排程與批次處理 (datetime, schedule)

### 🟥 階段四：軟體測試與進階 QA 框架 (週次 10-13)
*目標：導入專業的自動化測試框架（涵蓋 API 與 UI），提升軟體品質驗證的效率。*
* [ ] 模組 10：單元測試基礎 (unittest, assert)
* [ ] 模組 11：Pytest 測試框架 (Pytest 語法, Fixture, 參數化測試)
* [ ] 模組 12：API 自動化測試實戰 (requests + pytest, Mocking 驗證)
* [ ] 模組 13：Playwright UI 自動化測試實戰 (Web UI 元素定位, E2E 端到端測試)

### 🏆 階段五：期末實戰專案 (週次 14-17)
*目標：整合所學，完成一個具備商業價值的自動化解決方案。*
* [ ] **專案 1 (自動化測試框架)**：對特定 Web API 建立自動化測試，產出測試報告 (Allure)。
* [ ] **專案 2 (系統巡檢自動化)**：定期檢查伺服器狀態，透過 API 發送 Slack 告警。
* [ ] **專案 3 (我們預定的儀表板)**：完成 `scripts/build_tracker.py` 自動生成前端儀表板 (index.html)。

---

## 5. 學習與互動工作流 (Workflow)
未來我們互動的標準流程如下：
1. **提出主題**：由 PeterPan 從上面的 Roadmap 挑選一個想學的目標（例如：檔案讀寫）。
2. **實作演練**：我在 `02_Exercises` 建立包含範例與練習題的 `.py` 檔，你實際動手寫 code 並執行。
3. **請求總結**：練習完成後，你發出指令：「幫我總結一下剛剛的內容」。
4. **產出筆記**：我依照上述「撰寫原則」，在 `01_Syntax_Notes` 產出 `.md` 筆記，並且更新 `00_Index.md` 目錄與 `spec.md` 的進度。
