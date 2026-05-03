### 1. 蛇形命名法 (Snake Case) —— Python 的最愛

所有字母均小寫，單字之間用**底線 (`_`)** 連接。

- **樣式**：`user_name`, `retry_count`, `is_logged_in`
- **用途**：Python 官方推薦的**一般變數**、**函數名稱**與**檔案名稱**命名標準。
- **由來**：看起來像一條長長的蛇。
    

### 2. 駝峰命名法 (Camel Case / lowerCamelCase)

第一個單字首字母小寫，之後的每個單字首字母大寫，不使用底線。

- **樣式**：`userName`, `retryCount`, `isLoggedIn`
    
- **用途**：在 JavaScript、Java、C# 中是主流，但在 Python 中較少用於變數，通常只在特定框架要求時使用。
    
- **由來**：單字中間的大寫字母像駱駝的駝峰。
    

### 3. 帕斯卡命名法 (Pascal Case / UpperCamelCase)

每一個單字的首字母均大寫，不使用底線。

- **樣式**：`UserName`, `DatabaseManager`, `OrderSystem`
    
- **用途**：Python 官方規範中，專門用於 **類別 (Class)** 的命名。
    
- **原則**：看到這種命名，開發者會立刻意識到「這是一個藍圖 (Class)」，而不是一個普通的變數。
    

### 4. 尖叫蛇形命名法 (Screaming Snake Case)

所有字母均大寫，單字之間用**底線 (`_`)** 連接。

- **樣式**：`MAX_STRENGTH`, `API_KEY`, `DATABASE_URL`
    
- **用途**：專門用於 **常量 (Constants)**。也就是程式執行過程中不應該被修改的變數。
    
- **由來**：全大寫看起來就像在對讀者大喊「我很重要，不要動我！」。
    

### 5. 串燒命名法 (Kebab Case) —— 變數命名禁區

所有字母小寫，單字之間用**連字號 (`-`)** 連接。

- **樣式**：`user-name`, `page-title`
    
- **注意**：在大多數程式語言（包含 Python）中，**不能**用來命名變數。
    
- **原因**：因為 Python 會把 `-` 誤解為「減號」（例如 `a-b` 會變成變數 `a` 減去變數 `b`）。
    
- **用途**：常見於 CSS 樣式名稱或網頁的 URL 路徑。
    

---

### 總結對照表

| **命名樣式**            | **範例**        | **Python 建議用途**          |
| ------------------- | ------------- | ------------------------ |
| **Snake Case**      | `my_variable` | **一般變數、函數、檔案名**          |
| **Pascal Case**     | `MyClass`     | **類別 (Class)**           |
| **Screaming Snake** | `MY_CONSTANT` | **常量 (不可變的值)**           |
| **Camel Case**      | `myVariable`  | Python 較少使用 (JS/Java 主流) |
| **Kebab Case**      | `my-variable` | **禁止用於變數** (用於 CSS/URL)  |

---

