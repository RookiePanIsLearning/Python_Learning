# 例外處理語法總結 (try / except)

---

## 📐 基本結構

```python
try:
    # 可能出錯的程式碼
except 例外型態 as e:
    # 出錯時執行
else:
    # 沒有出錯時才執行（try 完全沒例外才跑）
finally:
    # 無論如何都會執行（常用於關閉資源）
```

> **白話文**：`try` = 嘗試；`except` = 出事了就跑這裡；`else` = 沒事才跑這裡；`finally` = 不管有沒有事都跑這裡。

---

## 🌳 完整繼承樹（真實 Python 結構）

所有錯誤都是「類別（Class）」，具有繼承關係，越下層代表是上層的**子類別（Subclass）**。

```
BaseException                       ← 所有例外的根節點（系統層級）
│
├── SystemExit                      ← sys.exit() 正常終止程式
├── KeyboardInterrupt               ← 使用者按下 Ctrl+C 中斷程式
│
└── Exception                       ← 🌟 所有「程式邏輯錯誤」的基礎類別
    │
    ├── 📂 語法錯誤 (Syntax)         ⚠️ 執行前就發生，try/except 在同一段程式碼裡救不了
    │   ├── SyntaxError             ← 程式碼語法寫錯（漏冒號、括號不對等）
    │   └── IndentationError        ← 縮排錯誤（SyntaxError 的子類別）
    │
    ├── 📂 數學運算 (ArithmeticError)
    │   ├── ZeroDivisionError       ← 除以零
    │   └── OverflowError           ← 運算結果超出 float 數值限制
    │
    ├── 📂 容器查找 (LookupError)
    │   ├── IndexError              ← List 索引超出範圍
    │   └── KeyError                ← Dict 找不到指定的 Key
    │
    ├── 📂 作業系統 (OSError)
    │   ├── FileNotFoundError       ← 找不到檔案
    │   ├── PermissionError         ← 沒有存取權限
    │   └── TimeoutError            ← 作業逾時
    │
    ├── 📂 模組匯入 (ImportError)
    │   └── ModuleNotFoundError     ← 找不到指定模組
    │
    ├── 📂 名稱與屬性 (Name & Attribute)
    │   ├── NameError               ← 使用了未定義的變數
    │   │   └── UnboundLocalError   ← 區域變數在賦值前就被使用
    │   └── AttributeError          ← 呼叫物件不存在的屬性或方法
    │
    ├── 📂 型態與值 (Type & Value)
    │   ├── TypeError               ← 使用了不適合的資料型態
    │   └── ValueError              ← 型態正確但內容不合理
    │
    ├── 📂 執行與迭代 (Runtime & Iteration)
    │   ├── RecursionError          ← 超過最大遞迴深度
    │   ├── StopIteration           ← 迭代器已無更多元素
    │   ├── RuntimeError            ← 不屬於其他類別的執行時期錯誤
    │   └── NotImplementedError     ← 抽象方法尚未被子類別實作（RuntimeError 子類別）
    │
    ├── 📂 斷言 (Assertion)
    │   └── AssertionError          ← assert 條件為 False
    │
    └── 📂 編碼 (Unicode)
        ├── UnicodeDecodeError      ← bytes 解碼為字串失敗
        └── UnicodeEncodeError      ← 字串編碼為 bytes 失敗
```

> 💡 **重要**：`SystemExit` 和 `KeyboardInterrupt` 不是 `Exception` 的子類別！
> 所以 `except Exception` **捕捉不到**它們，這是有意為之的設計。

---

## 💻 逐一範例（附錯誤訊息）

### ⚠️ SyntaxError — 語法寫錯（執行前就發生）

```python
# ❌ 這樣寫會讓整個 cell/檔案直接掛掉，try/except 救不了：
# if True
#     print("Hello")
# 💥 SyntaxError: expected ':'

# ✅ 唯一能捕捉的方式：透過 eval() 或 compile() 動態執行字串
try:
    eval("def (")
except SyntaxError as e:
    print(f"[SyntaxError] {e}")
    print(f"  發生在第 {e.lineno} 行，偏移 {e.offset} 字元")
```

### ⚠️ IndentationError — 縮排錯誤（SyntaxError 子類別）

```python
bad_code = """
def my_func():
print("沒有縮排")
"""
# 💥 IndentationError: expected an indented block after function definition

try:
    compile(bad_code, "<string>", "exec")
except IndentationError as e:
    print(f"[IndentationError] {e}")
```

---

### 01. TypeError — 型態不符的運算

```python
try:
    result = "我有 " + 10 + " 顆蘋果"
except TypeError as e:
    print(f"[TypeError] {e}")
# 💥 TypeError: can only concatenate str (not "int") to str
```

### 02. ValueError — 值的內容不合法

```python
try:
    number = int("這不是數字")
except ValueError as e:
    print(f"[ValueError] {e}")
# 💥 ValueError: invalid literal for int() with base 10: '這不是數字'
```

### 03. ZeroDivisionError — 除以零

```python
try:
    result = 100 / 0
except ZeroDivisionError as e:
    print(f"[ZeroDivisionError] {e}")
# 💥 ZeroDivisionError: division by zero
```

### 04. OverflowError — 數值超出範圍

```python
import math

try:
    result = math.exp(100000)
except OverflowError as e:
    print(f"[OverflowError] {e}")
# 💥 OverflowError: math range error
```

### 05. IndexError — 索引超出範圍

```python
my_list = ['A', 'B', 'C']  # 只有 index 0, 1, 2

try:
    print(my_list[5])
except IndexError as e:
    print(f"[IndexError] {e}")
# 💥 IndexError: list index out of range
```

### 06. KeyError — 字典找不到鍵

```python
my_dict = {'name': 'Alice', 'age': 25}

try:
    print(my_dict['gender'])
except KeyError as e:
    print(f"[KeyError] {e}")
# 💥 KeyError: 'gender'
```

### 07. FileNotFoundError — 找不到檔案

```python
try:
    with open("不存在的檔案.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"[FileNotFoundError] {e}")
# 💥 FileNotFoundError: [Errno 2] No such file or directory: '不存在的檔案.txt'
```

### 08. PermissionError — 沒有存取權限

```python
try:
    with open("C:/Windows/System32/config/SAM", "r") as f:
        content = f.read()
except PermissionError as e:
    print(f"[PermissionError] {e}")
# 💥 PermissionError: [Errno 13] Permission denied
```

### 09. ModuleNotFoundError — 找不到模組

```python
try:
    import non_existent_module
except ModuleNotFoundError as e:
    print(f"[ModuleNotFoundError] {e}")
# 💥 ModuleNotFoundError: No module named 'non_existent_module'
```

### 10. NameError — 變數未定義

```python
try:
    print(mesage)  # 拼字錯誤，少了一個 s
except NameError as e:
    print(f"[NameError] {e}")
# 💥 NameError: name 'mesage' is not defined. Did you mean: 'message'?
```

### 11. UnboundLocalError — 區域變數賦值前就被使用

```python
count = 10

def increment():
    count += 1   # count 在函式內被賦值，Python 視為區域變數，但賦值前就被讀取了
    return count

try:
    increment()
except UnboundLocalError as e:
    print(f"[UnboundLocalError] {e}")
# 💥 UnboundLocalError: local variable 'count' referenced before assignment
```

### 12. AttributeError — 物件沒有該屬性或方法

```python
try:
    number = 10
    number.append(5)   # int 沒有 append()，那是 List 才有的
except AttributeError as e:
    print(f"[AttributeError] {e}")
# 💥 AttributeError: 'int' object has no attribute 'append'
```

### 13. AssertionError — 斷言失敗

```python
def divide(a, b):
    assert b != 0, "除數不能為 0"
    return a / b

try:
    divide(10, 0)
except AssertionError as e:
    print(f"[AssertionError] {e}")
# 💥 AssertionError: 除數不能為 0
```

### 14. RecursionError — 超過最大遞迴深度

```python
def infinite_recursion():
    return infinite_recursion()  # 沒有終止條件

try:
    infinite_recursion()
except RecursionError as e:
    print(f"[RecursionError] {e}")
# 💥 RecursionError: maximum recursion depth exceeded
```

### 15. StopIteration — 迭代器耗盡

```python
my_iter = iter([1, 2])  # 只有 2 個元素

try:
    print(next(my_iter))   # → 1
    print(next(my_iter))   # → 2
    print(next(my_iter))   # 已無元素
except StopIteration:
    print("[StopIteration] 迭代器已無更多元素")
# 💥 StopIteration
```

### 16. NotImplementedError — 抽象方法未實作

```python
class Animal:
    def speak(self):
        raise NotImplementedError("子類別必須實作 speak()")

class Dog(Animal):
    pass   # 忘記覆寫 speak()

try:
    Dog().speak()
except NotImplementedError as e:
    print(f"[NotImplementedError] {e}")
# 💥 NotImplementedError: 子類別必須實作 speak()
```

### 17. UnicodeDecodeError — bytes 解碼失敗

```python
try:
    b = b"\xff\xfe"
    text = b.decode("utf-8")   # 無效的 UTF-8 序列
except UnicodeDecodeError as e:
    print(f"[UnicodeDecodeError] {e}")
# 💥 UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0
```

### 18. UnicodeEncodeError — 字串編碼失敗

```python
try:
    text = "你好"
    encoded = text.encode("ascii")   # ASCII 無法處理中文
except UnicodeEncodeError as e:
    print(f"[UnicodeEncodeError] {e}")
# 💥 UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1
```

### 19. KeyboardInterrupt — 使用者按 Ctrl+C

```python
# ⚠️ 注意：KeyboardInterrupt 不是 Exception 的子類別
# 用 except Exception 捕捉不到它！要用 except KeyboardInterrupt 或 except BaseException

try:
    while True:
        pass   # 模擬長時間執行，按 Ctrl+C 觸發
except KeyboardInterrupt:
    print("[KeyboardInterrupt] 程式被使用者中斷")
```

### 20. SystemExit — sys.exit() 終止程式

```python
import sys

# ⚠️ 同樣不是 Exception 的子類別，except Exception 捕捉不到
try:
    sys.exit(0)
except SystemExit as e:
    print(f"[SystemExit] 程式結束，exit code: {e.code}")
```

---

## 🔀 多重例外寫法比較

```python
# ✅ 分開捕捉（推薦）：針對不同錯誤給不同訊息
try:
    ...
except ValueError:
    print("值不合法")
except ZeroDivisionError:
    print("不可除以 0")

# ✅ 合併捕捉：同一個處理邏輯時使用
try:
    ...
except (ValueError, TypeError) as e:
    print(f"輸入錯誤：{e}")

# ⚠️ 捕捉所有一般例外（除錯用，捕捉不到 SystemExit / KeyboardInterrupt）
try:
    ...
except Exception as e:
    print(f"發生了：{type(e).__name__} → {e}")
```

---

## 🏗️ 情境舉例 (Use Cases)

| 情境 | 適合捕捉的例外 |
|---|---|
| 讀取使用者輸入並轉型 | `ValueError` |
| 存取 dict / list 元素 | `KeyError`, `IndexError` |
| 讀寫檔案 | `FileNotFoundError`, `PermissionError` |
| 匯入外部套件前先確認 | `ModuleNotFoundError` |
| 設計類別繼承架構 | `NotImplementedError` |
| 處理任何數學運算錯誤 | `ArithmeticError`（同時捕捉 `ZeroDivisionError` 和 `OverflowError`） |
| 處理任何容器查找錯誤 | `LookupError`（同時捕捉 `IndexError` 和 `KeyError`） |

---

## ⚠️ 易錯點 (Gotchas)

1. **`SyntaxError` 無法在同一段程式碼裡被捕捉**：Python 執行前就先解析語法，語法錯誤時整個 cell/檔案直接掛掉，`try/except` 根本來不及執行。唯一辦法是透過 `eval()` / `compile()` 捕捉動態字串。

2. **`except Exception` 捕捉不到 `SystemExit` 和 `KeyboardInterrupt`**：它們是 `BaseException` 的子類別，不是 `Exception`。要捕捉要用 `except BaseException` 或明確指定型態。

3. **`except` 順序很重要**：子類別要放在父類別前面，否則永遠不會被捕捉到。
   ```python
   # ❌ 錯誤：FileNotFoundError 是 OSError 的子類別，永遠到不了
   except OSError: ...
   except FileNotFoundError: ...

   # ✅ 正確：子類別優先
   except FileNotFoundError: ...
   except OSError: ...
   ```

4. **不要裸捕捉 `except:`（沒有型態）**：這連 `KeyboardInterrupt`（Ctrl+C）都會吃掉，非常危險。
   ```python
   # ❌ 危險
   except:
       pass

   # ✅ 安全
   except Exception:
       pass
   ```

5. **`finally` 一定會執行**，即使 `except` 裡面有 `return`，`finally` 仍會先跑才回傳。

6. **`else` 常被遺忘**：只在 `try` 完全沒有例外時執行，比把所有程式碼塞進 `try` 更精確。
