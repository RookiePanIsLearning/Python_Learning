自己建置的class或是py filses 要怎麼引用

在 Python 程式碼內部，**永遠使用「點號 `.`」作為路徑分隔符**。

- **為什麼不用 `/`？**：因為 `/` 是作業系統的路徑符號（File Path），而 `.` 是 Python 的**命名空間符號（Namespace）**。
    
- **子資料夾適用嗎？**：完全適用。在 Python 眼中，一個資料夾只要裡面有 `.py` 檔案，它就是一個「套件 (Package)」。

#### 範例結構：

Plaintext

```
my_project/
├── main.py            <-- 執行起點
└── my_library/        <-- 子資料夾
    ├── __init__.py    <-- 告訴 Python 這是一個套件
    ├── database.py    <-- 裡面有 class MySQLHandler
    └── tools/         <-- 孫子資料夾
        ├── __init__.py
        └── validator.py <-- 裡面有 def check_email()
```

#### 引用語法：

1. **引用子資料夾的 Class**： `from my_library.database import MySQLHandler`
2. **引用孫子資料夾的函數**： `from my_library.tools.validator import check_email`