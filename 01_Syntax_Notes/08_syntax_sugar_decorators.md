# 語法糖完全指南 (Syntax Sugar & Decorators)

---

## 🍬 Part 1：什麼是語法糖？

### 定義與起源

「語法糖 (Syntactic Sugar)」這個詞是 Peter J. Landin 在 1964 年提出的。
白話說就是：**用更短、更直覺的寫法，做到跟「囉嗦版」完全一樣的事情。**
它不會帶來新功能，只是讓你的程式碼更好讀、更好寫。

> Python 核心開發者 Brett Cannon 的研究指出：Python 3.8 所有複雜語法，
> 實際上可以被拆解（脫糖, Desugaring）成僅僅 **11 個基礎語法片段** 加上特殊方法的組合。

### 語法糖 vs 語法鹽 vs 語法糖精

| 名詞 | 意思 | Python 的態度 |
|---|---|---|
| **語法糖 (Syntactic Sugar)** | 更甜的寫法，讓程式碼更好讀 | ✅ 大量採用 |
| **語法鹽 (Syntactic Salt)** | 故意設計的繁瑣語法，防止你犯錯 | 少量（例如強制縮排） |
| **語法糖精 (Syntactic Saccharin)** | 過度堆砌的語法，甜但沒營養 | ❌ Python 設計哲學避免 |

### Python 常見語法糖一覽（完整版）

| 語法糖 | 等價的「囉嗦版」 | 說明 |
|---|---|---|
| `a += 1` | `a = a + 1` | 增強型賦值 |
| `a, b = 1, 2` | 分開兩行賦值 | 解構賦值 / 解包 |
| `a, b = b, a` | 需要第三個臨時變數 | 變數交換 |
| `[x for x in lst]` | `for` 迴圈 + `append` | List Comprehension |
| `f"Hello {name}"` | `"Hello " + name` | f-string |
| `@decorator` | `func = decorator(func)` | 裝飾器語法 |
| `with open(...) as f:` | `try/finally` + `f.close()` | Context Manager |
| `x if cond else y` | `if/else` 多行 | 三元運算式 |
| `a + b` | `a.__add__(b)` | 運算子 → 特殊方法 |
| `a[i]` | `a.__getitem__(i)` | 索引存取 → 特殊方法 |
| `1 < x < 10` | `(1 < x) and (x < 10)` | 鏈式比較 |
| `n := expr` | 先賦值再用（需多行）| 海象運算子 (Python 3.8+) |
| `match x:` | 長串 `if-elif-else` | 模式匹配 (Python 3.10+) |

---

## 🔗 Part 2：運算子的真面目 — 特殊方法映射

Python 的靈魂是「萬物皆物件」。你寫的每一個運算子，底層都在呼叫物件的特殊方法 (Dunder Methods)。

| 你寫的（語法糖） | Python 實際執行的 | 說明 |
|---|---|---|
| `a + b` | `a.__add__(b)` | 加法 / 物件合併 |
| `a == b` | `a.__eq__(b)` | 相等比較 |
| `a < b` | `a.__lt__(b)` | 小於比較 |
| `a[index]` | `a.__getitem__(index)` | 索引取值 |
| `a[index] = val` | `a.__setitem__(index, val)` | 索引設值 |
| `len(a)` | `a.__len__()` | 取長度 |
| `item in container` | `container.__contains__(item)` | 成員測試 |
| `str(a)` | `a.__str__()` | 轉字串 |
| `for x in a:` | `a.__iter__()` → `__next__()` | 迭代協定 |

> **重點：** 當你在自定義 class 中實作了 `__getitem__`，該物件就能用 `obj[0]` 這種語法存取。
> 這就是 Python 的「鴨子型別 (Duck Typing)」——只要你長得像鴨子，你就是鴨子。

```python
class MyList:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

m = MyList([10, 20, 30])
print(m[1])       # 20  ← 語法糖，實際呼叫 m.__getitem__(1)
print(len(m))     # 3   ← 語法糖，實際呼叫 m.__len__()
```

### 鏈式比較 (Chained Comparisons)

```python
x = 5
# 語法糖版
print(1 < x < 10)          # True

# 等價的囉嗦版
print((1 < x) and (x < 10))  # True

# 重點：Python 保證中間的 x 只會被「評估一次」，避免副作用
```

---

## 📦 Part 3：解包 (Unpacking) — 賦值的語法糖

### 基本解包

```python
# 囉嗦版
point = (10, 20)
x = point[0]
y = point[1]

# 語法糖版
x, y = (10, 20)
print(x, y)   # 10 20
```

### 星號解包 — 處理不定長度序列

```python
first, *middle, last = [1, 2, 3, 4, 5]
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

# 實用場景：取 CSV 的表頭與資料
header, *rows = [
    ["name", "age", "city"],
    ["Pan", 25, "Taipei"],
    ["Alice", 30, "Tokyo"],
]
print(header)   # ['name', 'age', 'city']
print(rows)     # [['Pan', 25, 'Taipei'], ['Alice', 30, 'Tokyo']]
```

### 變數交換 — 最經典的 Pythonic 寫法

```python
a, b = 1, 2

# 其他語言的寫法（需要臨時變數）
# temp = a; a = b; b = temp

# Python 語法糖：利用元組打包/解包的原子性
a, b = b, a
print(a, b)   # 2 1
```

### 增強型賦值 (Augmented Assignment)

```python
a = 10
a += 5    # 等同 a = a + 5   → 15
a -= 3    # 等同 a = a - 3   → 12
a *= 2    # 等同 a = a * 2   → 24
a //= 5   # 等同 a = a // 5  → 4

# ⚠️ 對可變物件（list）有特殊行為：
lst = [1, 2]
lst += [3, 4]   # 觸發 lst.__iadd__([3, 4])，原地修改，不建立新物件
```

---

## 🔄 Part 4：推導式 (Comprehensions) — 性能分析

> 推導式的基礎語法已在 [進階迴圈與推導式](./04_loops_advanced.md) 詳細介紹，本節聚焦「為什麼推導式比 for 迴圈快」。

### 性能秘密：字節碼差異

| 指標 | 傳統 `for` + `append()` | List Comprehension |
|---|---|---|
| 執行效率 | 較慢：每輪迭代都要查找 `append` 屬性 | 較快：使用 `LIST_APPEND` 字節碼，直接在 C 層級壓入 |
| 程式碼長度 | 多行，需初始化空列表 | 單行，聲明式語法 |
| 記憶體管理 | 逐步分配 | 建構過程中最佳化分配 |
| 適合情境 | 複雜邏輯、有副作用的操作 | 單純的數據轉換與過濾 |

```python
import timeit

# 傳統版
def traditional():
    result = []
    for i in range(10000):
        result.append(i ** 2)
    return result

# 推導式版
def comprehension():
    return [i ** 2 for i in range(10000)]

print(timeit.timeit(traditional, number=1000))    # 較慢
print(timeit.timeit(comprehension, number=1000))   # 較快 (通常快 20-40%)
```

### 集合 & 字典推導式

```python
words = ["hello", "world", "hi", "hey"]

# 集合推導式 — 自動去重
lengths = {len(w) for w in words}
print(lengths)    # {2, 3, 5}

# 字典推導式 — 建立映射
word_len = {w: len(w) for w in words}
print(word_len)   # {'hello': 5, 'world': 5, 'hi': 2, 'hey': 3}
```

### ⚠️ 推導式的使用原則

> **超過兩層嵌套就應該回歸 `for` 迴圈。** 酷炫但看不懂的一行程式碼 ≠ Pythonic。

```python
# ✅ 好：單層過濾 + 轉換
evens = [x ** 2 for x in range(20) if x % 2 == 0]

# ⚠️ 尚可：兩層嵌套
flat = [x for row in matrix for x in row]

# ❌ 壞：三層嵌套，沒人看得懂
# result = [f(x) for lst in data for row in lst for x in row if x > 0]
# → 這種請改用 for 迴圈
```

---

## 🦭 Part 5：海象運算子 `:=` (Python 3.8+)

海象運算子（Walrus Operator）正式名稱叫「賦值表達式 (Assignment Expressions)」，來自 PEP 572。
它讓你**在表達式中同時賦值並使用值**，解決「重複計算」的痛點。

### 基本用法

```python
# 囉嗦版：input() 被呼叫了兩次，或需要提前賦值
line = input("輸入: ")
while line != "quit":
    print(f"你輸入了: {line}")
    line = input("輸入: ")

# 海象版：一行搞定
while (line := input("輸入: ")) != "quit":
    print(f"你輸入了: {line}")
```

### 在推導式中避免重複計算

```python
data = [1, 5, 12, 3, 18, 7]

# 囉嗦版：heavy_calc 被呼叫兩次
# results = [heavy_calc(x) for x in data if heavy_calc(x) > 10]

# 海象版：只算一次
results = [y for x in data if (y := x * 3) > 10]
print(results)   # [36, 54, 21]
```

### ⚠️ 不要濫用

```python
# ❌ 為了省一行而犧牲可讀性
if (n := len(a)) > 10 and (m := n * 2) > 25:
    print(m)

# ✅ 清楚就好
n = len(a)
m = n * 2
if n > 10 and m > 25:
    print(m)
```

---

## 🎯 Part 6：結構化模式匹配 `match-case` (Python 3.10+)

這不只是其他語言的 `switch-case`，而是能**根據物件的型別、屬性、結構**做精確匹配的強大工具。

### 基本用法

```python
def handle_command(command):
    match command.split():
        case ["quit"]:
            print("掰掰！")
        case ["hello", name]:
            print(f"你好，{name}！")
        case ["move", direction, steps]:
            print(f"往 {direction} 移動 {steps} 步")
        case _:
            print(f"不認識的指令: {command}")

handle_command("hello Pan")       # 你好，Pan！
handle_command("move north 5")    # 往 north 移動 5 步
handle_command("quit")            # 掰掰！
```

### 與 `if-elif` 的比較

| 特性 | `if-elif-else` 鏈 | `match-case` |
|---|---|---|
| 邏輯表達 | 過程式，判斷布林值 | 聲明式，描述資料形狀 |
| 數據解構 | 需手動取屬性比對 | 自動解構物件並綁定變數 |
| 適合場景 | 簡單布林條件 | 嵌套字典、類別屬性、協議解析 |
| Python 版本 | 所有版本 | 3.10+ |

### 進階：型別匹配 + Guard

```python
def process(value):
    match value:
        case int(n) if n > 0:
            print(f"正整數: {n}")
        case int(n):
            print(f"非正整數: {n}")
        case str(s) if len(s) > 5:
            print(f"長字串: {s}")
        case str(s):
            print(f"短字串: {s}")
        case [x, y]:
            print(f"兩元素列表: {x}, {y}")
        case _:
            print("其他類型")

process(42)         # 正整數: 42
process(-5)         # 非正整數: -5
process("Hello!")   # 長字串: Hello!
process([1, 2])     # 兩元素列表: 1, 2
```

---

## 📝 Part 7：F-string 的進化史

### 三代字串格式化比較

```python
name = "Pan"
age = 25

# 第一代：% 運算子（古老）
print("我是 %s，%d 歲" % (name, age))

# 第二代：.format()（過渡期）
print("我是 {}，{} 歲".format(name, age))

# 第三代：f-string（現在的主流，Python 3.6+）
print(f"我是 {name}，{age} 歲")
```

### F-string 實用技巧

```python
import math

# 格式化微語言
pi = math.pi
print(f"圓周率: {pi:.4f}")          # 圓周率: 3.1416
print(f"進度: {0.856:.1%}")          # 進度: 85.6%
print(f"{'Python':>15}")             # 右對齊，寬度 15
print(f"{'Python':-^20}")            # 居中，用 - 填充

# Debug 用法：f"{var=}"（Python 3.8+）
x = 42
y = [1, 2, 3]
print(f"{x = }")         # x = 42
print(f"{len(y) = }")    # len(y) = 3
```

### Python 3.12 的 F-string 大革新 (PEP 701)

Python 3.12 之前，f-string 有很多奇怪的限制。3.12 把 f-string 整合進了 PEG 解析器，限制全部解除：

| 過去的限制 | 3.12 之前 | 3.12 之後 |
|---|---|---|
| 引號嵌套 | 必須切換單雙引號，層數有限 | ✅ 支持無限層嵌套 |
| `{}` 內用反斜槓 | ❌ 禁止 | ✅ 允許 `\n`、`\t`、Unicode |
| `{}` 內寫注解 | ❌ 禁止 | ✅ 允許 `#` 註解 |
| 多行表達式 | 需要三引號字串 | ✅ 單引號也能換行 |

```python
# Python 3.12+ 才能用的寫法
songs = ["Yesterday", "Imagine", "Bohemian Rhapsody"]

# 嵌套引號不再報錯
print(f"{''.join(songs)}")

# {} 內可以用反斜槓
print(f"換行符的 repr: {'\n'!r}")
```

---

## 🎩 Part 8：裝飾器 (Decorator) — 中間件語法糖

一句話：**裝飾器就是「用一個函式去包裝另一個函式」，在不改動原本函式程式碼的前提下，幫它加上額外功能。**

### 沒有裝飾器的寫法（囉嗦版）

```python
def say_hello():
    print("Hello!")

def make_louder(func):
    def wrapper():
        print("===== 開始 =====")
        func()
        print("===== 結束 =====")
    return wrapper

# 手動包裝
say_hello = make_louder(say_hello)
say_hello()
```

### 有裝飾器的寫法（語法糖版）

```python
def make_louder(func):
    def wrapper():
        print("===== 開始 =====")
        func()
        print("===== 結束 =====")
    return wrapper

@make_louder          # 等同 say_hello = make_louder(say_hello)
def say_hello():
    print("Hello!")

say_hello()
```

> `@make_louder` 就是語法糖！Python 看到 `@` 就會自動幫你做 `say_hello = make_louder(say_hello)` 這件事。

### 裝飾器的背後：閉包 (Closure)

裝飾器的物理模型是閉包——內部函式「記住」了外部函式的變數：

```python
def outer(msg):
    def inner():
        print(msg)    # inner 記住了 outer 的 msg
    return inner

hello = outer("Hello!")
hello()   # Hello! ← msg 已經在 outer 執行完後「活在」inner 裡
```

### 裝飾器的基本模板

```python
import functools

def my_decorator(func):
    @functools.wraps(func)       # 保留原函式的名字與文件字串
    def wrapper(*args, **kwargs):
        # --- 前處理 ---
        result = func(*args, **kwargs)
        # --- 後處理 ---
        return result
    return wrapper
```

### 為什麼需要 `functools.wraps`？

如果不加 `@functools.wraps(func)`，被裝飾的函式會「失去身份」：

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """打招呼用的函式"""
    print("Hi!")

print(greet.__name__)    # ❌ 印出 'wrapper'，不是 'greet'
print(greet.__doc__)     # ❌ 印出 None，不是 '打招呼用的函式'
```

加了 `@functools.wraps(func)` 之後：

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """打招呼用的函式"""
    print("Hi!")

print(greet.__name__)    # ✅ 'greet'
print(greet.__doc__)     # ✅ '打招呼用的函式'
```

### 實用裝飾器範例

#### 1. 計時器 — 測量函式執行時間

```python
import functools, time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"⏱ {func.__name__} 執行了 {elapsed:.4f} 秒")
        return result
    return wrapper

@timer
def slow_task():
    time.sleep(1)

slow_task()   # ⏱ slow_task 執行了 1.00xx 秒
```

#### 2. 日誌記錄 — 自動印出呼叫資訊

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📝 呼叫 {func.__name__}(args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)
        print(f"📝 回傳 {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(3, 5)
```

#### 3. 帶參數的裝飾器（三層巢狀）

```python
import functools

def require_role(role):               # 外層：接收裝飾器參數
    def decorator(func):              # 中層：接收被裝飾的函式
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):   # 內層：接收函式參數
            if user.get("role") != role:
                raise PermissionError(f"需要 {role} 權限")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")                # require_role("admin") 回傳 decorator
def delete_user(user, target_id):
    print(f"已刪除使用者 {target_id}")

admin = {"name": "Pan", "role": "admin"}
guest = {"name": "Guest", "role": "viewer"}

delete_user(admin, 42)    # ✅ 已刪除使用者 42
# delete_user(guest, 42)  # 💥 PermissionError: 需要 admin 權限
```

#### 4. 快取裝飾器 — `@functools.lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))   # 瞬間完成，沒有快取的話會跑到天荒地老
print(fibonacci.cache_info())   # 可以查看快取命中率
```

### Python 內建常用裝飾器

| 裝飾器 | 用在哪裡 | 作用 |
|---|---|---|
| `@staticmethod` | Class 內 | 不需要 `self`，純工具方法 |
| `@classmethod` | Class 內 | 第一個參數是 `cls`（類別本身），常用於工廠模式 |
| `@property` | Class 內 | 把方法偽裝成屬性，讀取時不用加 `()` |
| `@functools.wraps` | 裝飾器內 | 保留被裝飾函式的 `__name__` 與 `__doc__` |
| `@functools.lru_cache` | 任何函式 | 自動快取函式結果，避免重複計算 |

#### `@property` 範例

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.area)      # ✅ 直接讀取，不用 c.area()
```

#### `@classmethod` 範例

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])

u = User.from_dict({"name": "Pan", "age": 25})
print(u.name)   # Pan
```

---

## 🗂️ Part 9：上下文管理器 (Context Manager)

`with` 語法是 `try...finally` 的語法糖，確保資源（檔案、鎖、連線）一定會被正確釋放。

### 基本用法

```python
# 囉嗦版
f = open("test.txt", "w")
try:
    f.write("hello")
finally:
    f.close()    # 無論如何都要 close

# 語法糖版
with open("test.txt", "w") as f:
    f.write("hello")
# ← 離開 with 區塊時自動 close，即使發生例外
```

### 自定義上下文管理器（用 class）

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"⏱ 花了 {elapsed:.4f} 秒")
        return False    # False = 不攔截例外

with Timer():
    total = sum(range(1_000_000))
```

### 用 `contextlib` 簡化（裝飾器 + 生成器）

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield                     # yield 之前 = __enter__，之後 = __exit__
    elapsed = time.time() - start
    print(f"⏱ 花了 {elapsed:.4f} 秒")

with timer():
    total = sum(range(1_000_000))
```

> `@contextmanager` 是「裝飾器」與「上下文管理器」的完美結合，展示了語法糖可以互相堆疊。

---

## ⚠️ Part 10：易錯點與工程取捨 (Gotchas & Trade-offs)

### 裝飾器易錯點

1. **忘記 `@functools.wraps`**：被裝飾的函式會失去 `__name__` 和 `__doc__`，debug 時會很痛苦。
2. **忘記 `return result`**：`wrapper` 裡面如果沒 return，被裝飾的函式永遠回傳 `None`。
3. **帶參數裝飾器少包一層**：帶參數的裝飾器需要三層巢狀（外層接參數 → 中層接函式 → 內層接函式參數）。
4. **裝飾器順序**：多個 `@` 堆疊時，**由下往上**執行：
   ```python
   @A
   @B
   def func(): ...
   # 等同於 func = A(B(func))
   ```

### 語法糖的負面效應

| 問題 | 說明 |
|---|---|
| **可讀性 vs 簡潔性** | 一行的嵌套推導式雖然酷炫，但如果同事要花幾分鐘才能看懂，那就失去價值了 |
| **調試難度** | 過度使用裝飾器 + 動態屬性 (`__getattr__`) 會讓 Traceback 變得難以追蹤 |
| **版本兼容性** | 海象運算子需要 3.8+，match-case 需要 3.10+，F-string 新特性需要 3.12+；企業環境可能還在用舊版 |
| **團隊協作** | 不是每個團隊成員都熟悉所有語法糖，過度使用反而增加溝通成本 |

> **PEP 20（Python 之禪）的兩句話永遠管用：**
> - *Explicit is better than implicit.* （明確優於隱含）
> - *Readability counts.* （可讀性至上）

---

## 🧠 Part 11：什麼時候該用什麼？

### 裝飾器使用時機

| 情境 | 適合用裝飾器嗎？ |
|---|---|
| 加 log / 計時 / 快取 | ✅ 非常適合 |
| 權限檢查 / 驗證 | ✅ 適合 |
| 路由註冊（Web 框架）| ✅ Flask/FastAPI 的標配 |
| 只有一個函式需要的邏輯 | ❌ 不需要，直接寫在函式裡就好 |
| 邏輯跟函式本身緊密相關 | ❌ 不適合抽出來當裝飾器 |

> **原則：裝飾器適合處理「橫切關注點 (Cross-cutting Concerns)」——那些跟業務邏輯無關，但很多函式都需要的功能。**

### 語法糖選擇速查

| 你想做的事 | 推薦語法糖 |
|---|---|
| 快速建立清單 | List Comprehension |
| 多變數同時賦值 | 解包 `a, b = ...` |
| 資源管理（檔案、鎖） | `with` 上下文管理器 |
| 字串插值 | f-string |
| 迴圈中同時取索引 | `enumerate()` |
| 迴圈中同時遍歷兩個列表 | `zip()` |
| 避免重複計算 + 條件判斷 | 海象運算子 `:=` |
| 複雜的資料形狀分派 | `match-case` |
| 函式增強（log、cache）| 裝飾器 `@` |

---

## 📚 Part 12：推薦學習路徑

| 階段 | 重點 | 推薦資源 |
|---|---|---|
| **初學者** | 養成 Pythonic 習慣：解包、推導式、f-string、`enumerate`/`zip` | Exercism Python Track（有導師 Code Review） |
| **中階** | 裝飾器、上下文管理器、生成器、海象運算子 | 《Effective Python》(Brett Slatkin)、《Fluent Python》(Luciano Ramalho) |
| **進階** | 脫糖分析、特殊方法、元編程 | Brett Cannon "Unravelling Python" 系列、PyCon 演講 |
