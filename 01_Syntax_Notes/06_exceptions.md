# 例外處理語法總結 (try / except)

---

## 📐 基本結構

```python
try:
    # 可能出錯的程式碼
except 例外型態 as e:
    # 出錯時執行
else:
    # 沒有出錯時才執行
finally:
    # 無論如何都會執行（常用於關閉資源）
```

> **白話文**：`try` = 嘗試；`except` = 出事了就跑這裡；`else` = 沒事才跑這裡；`finally` = 不管有沒有事都跑這裡。

---

## 🌳 18 種例外情境（樹狀結構）

```
📦 Python 內建例外
│
├── 📂 值與型態 (Value & Type)
│   ├── 01. ValueError          ← int("abc")              值正確但內容不合法
│   ├── 02. TypeError           ← "字串" + 100             型態不符的運算
│   ├── 03. AssertionError      ← assert x != 0           assert 條件為 False
│   └── 04. OverflowError       ← math.exp(100000)        數值超出 float 範圍
│
├── 📂 容器與名稱 (Container & Name)
│   ├── 05. IndexError          ← list[99]                索引超出範圍
│   ├── 06. KeyError            ← dict["missing"]         字典找不到鍵
│   ├── 07. AttributeError      ← (42).append(1)          物件沒有該方法
│   └── 08. NameError           ← print(x) # x未宣告      變數未定義
│
├── 📂 運算與執行 (Computation)
│   ├── 09. ZeroDivisionError   ← 100 / 0                 除以零
│   ├── 10. RecursionError      ← 無終止條件的遞迴          超過最大遞迴深度
│   └── 11. StopIteration       ← next(iter([]))          迭代器耗盡
│
├── 📂 檔案與系統 (File & OS)
│   ├── 12. FileNotFoundError   ← open("ghost.txt")       找不到檔案
│   ├── 13. PermissionError     ← 存取被鎖定的檔案          沒有存取權限
│   └── 14. OSError             ← 磁碟已滿                 作業系統層級錯誤
│
├── 📂 模組與編碼 (Module & Encoding)
│   ├── 15. ModuleNotFoundError ← import fake_lib         模組不存在
│   ├── 16. UnicodeDecodeError  ← b"\xff".decode("utf-8") bytes 解碼失敗
│   └── 17. UnicodeEncodeError  ← "你好".encode("ascii")   字串編碼失敗
│
└── 📂 設計與架構 (Design)
    ├── 18. NotImplementedError ← 子類別未覆寫抽象方法       方法尚未實作
    ├──  +. RuntimeError        ← 不屬於其他類別的執行錯誤   通用執行錯誤
    └──  +. Exception           ← except Exception as e    捕捉所有例外（除錯用）
```

---

## 💻 18 種例外逐一範例

### 01. ValueError — 值的內容不合法
```python
try:
    value = int("abc")          # "abc" 無法轉為整數
except ValueError as e:
    print(f"[ValueError] {e}")
```

### 02. TypeError — 型態不符的運算
```python
try:
    result = "數字" + 100       # str 不能加 int
except TypeError as e:
    print(f"[TypeError] {e}")
```

### 03. AssertionError — assert 條件為 False
```python
def divide(a, b):
    assert b != 0, "除數不能為 0"
    return a / b

try:
    divide(10, 0)
except AssertionError as e:
    print(f"[AssertionError] {e}")
```

### 04. OverflowError — 數值超出範圍
```python
import math

try:
    result = math.exp(100000)   # e^100000 超出 float 上限
except OverflowError as e:
    print(f"[OverflowError] {e}")
```

### 05. IndexError — 索引超出範圍
```python
fruits = ["apple", "banana", "cherry"]  # index 0~2

try:
    print(fruits[10])
except IndexError as e:
    print(f"[IndexError] {e}")
```

### 06. KeyError — 字典找不到鍵
```python
person = {"name": "Alice", "age": 30}

try:
    print(person["email"])      # "email" 鍵不存在
except KeyError as e:
    print(f"[KeyError] {e}")
```

### 07. AttributeError — 物件沒有該屬性或方法
```python
try:
    number = 42
    number.append(1)            # int 沒有 append()
except AttributeError as e:
    print(f"[AttributeError] {e}")
```

### 08. NameError — 變數未定義
```python
try:
    print(undefined_variable)   # 從未宣告此變數
except NameError as e:
    print(f"[NameError] {e}")
```

### 09. ZeroDivisionError — 除以零
```python
try:
    result = 100 / 0
except ZeroDivisionError as e:
    print(f"[ZeroDivisionError] {e}")
```

### 10. RecursionError — 超過最大遞迴深度
```python
def infinite_recursion():
    return infinite_recursion() # 沒有終止條件

try:
    infinite_recursion()
except RecursionError as e:
    print(f"[RecursionError] {e}")
```

### 11. StopIteration — 迭代器耗盡
```python
my_iter = iter([1, 2])          # 只有 2 個元素

try:
    print(next(my_iter))        # → 1
    print(next(my_iter))        # → 2
    print(next(my_iter))        # → StopIteration
except StopIteration:
    print("[StopIteration] 迭代器已無更多元素")
```

### 12. FileNotFoundError — 找不到檔案
```python
try:
    with open("ghost_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"[FileNotFoundError] {e}")
```

### 13. PermissionError — 沒有存取權限
```python
try:
    with open("C:/Windows/System32/config/SAM", "r") as f:
        content = f.read()
except PermissionError as e:
    print(f"[PermissionError] {e}")
```

### 14. OSError — 作業系統層級錯誤
```python
import os

try:
    os.remove("non_existent_file.txt") # 刪除不存在的檔案
except OSError as e:
    print(f"[OSError] {e}")
```

### 15. ModuleNotFoundError — 找不到模組
```python
try:
    import non_existent_module
except ModuleNotFoundError as e:
    print(f"[ModuleNotFoundError] {e}")
```

### 16. UnicodeDecodeError — bytes 解碼失敗
```python
try:
    b = b"\xff\xfe"             # 無效的 UTF-8 byte 序列
    text = b.decode("utf-8")
except UnicodeDecodeError as e:
    print(f"[UnicodeDecodeError] {e}")
```

### 17. UnicodeEncodeError — 字串編碼失敗
```python
try:
    text = "你好"               # 中文字
    encoded = text.encode("ascii")  # ASCII 無法處理中文
except UnicodeEncodeError as e:
    print(f"[UnicodeEncodeError] {e}")
```

### 18. NotImplementedError — 方法尚未實作
```python
class Animal:
    def speak(self):
        raise NotImplementedError("子類別必須實作 speak()")

class Dog(Animal):
    pass                        # 忘記覆寫 speak()

try:
    Dog().speak()
except NotImplementedError as e:
    print(f"[NotImplementedError] {e}")
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

# ⚠️ 捕捉所有例外（除錯用，生產環境避免）
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

---

## ⚠️ 易錯點 (Gotchas)

1. **`except` 順序很重要**：子類別要放在父類別前面，否則永遠不會被捕捉到。
   ```python
   # ❌ 錯誤：FileNotFoundError 是 OSError 的子類別，永遠到不了
   except OSError: ...
   except FileNotFoundError: ...

   # ✅ 正確：子類別優先
   except FileNotFoundError: ...
   except OSError: ...
   ```

2. **`finally` 一定會執行**，即使 `except` 裡面也有 `return`，`finally` 仍會先跑。

3. **不要裸捕捉 `except:`（沒有型態）**：這連 `KeyboardInterrupt`（Ctrl+C）都會吃掉。
   ```python
   # ❌ 危險
   except:
       pass

   # ✅ 安全
   except Exception:
       pass
   ```

4. **`else` 常被遺忘**：它只在 `try` 區塊完全沒有例外時執行，比把程式碼全塞進 `try` 更精確。
