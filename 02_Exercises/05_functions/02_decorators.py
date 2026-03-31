# 模組 4-2：語法糖與裝飾器 (Decorators)
# 目標：理解 @ 語法糖的本質，學會撰寫與使用裝飾器

# === 範例 1：裝飾器的本質 — 函式包函式 ===
def make_louder(func):
    def wrapper():
        print("===== 開始 =====")
        func()
        print("===== 結束 =====")
    return wrapper

@make_louder
def say_hello():
    print("Hello!")

say_hello()
# 思考：上面的 @make_louder 等同於哪一行程式碼？


# === 範例 2：帶參數的被裝飾函式 ===
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

print(add(3, 5))
print(f"函式名稱: {add.__name__}")  # 驗證 functools.wraps 有沒有生效


# === 範例 3：計時器裝飾器 ===
import time

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
    time.sleep(0.5)
    return "done"

print(slow_task())


# === 範例 4：帶參數的裝飾器（三層巢狀） ===
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()


# === 範例 5：內建裝飾器 @property ===
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半徑不能為負數")
        self._radius = value

c = Circle(5)
print(f"面積: {c.area}")      # 不用加 ()
c.radius = 10
print(f"新面積: {c.area}")
# c.radius = -1              # 取消註解試試看會怎樣


# ========================================
# 🎯 練習題
# ========================================

# --- 練習 1：寫一個 @debug 裝飾器 ---
# 需求：印出函式名稱、傳入參數、回傳值
# 提示：參考範例 2 的 @log

# def debug(func):
#     # 你的程式碼
#     pass

# @debug
# def multiply(a, b):
#     return a * b

# print(multiply(4, 7))
# 預期輸出：
# 🔍 呼叫 multiply(4, 7)
# 🔍 回傳 28
# 28


# --- 練習 2：寫一個 @require_positive 裝飾器 ---
# 需求：檢查所有傳入的數字參數是否為正數，不是就 raise ValueError
# 提示：用 *args 遍歷所有參數

# @require_positive
# def calculate_area(width, height):
#     return width * height

# print(calculate_area(3, 5))    # ✅ 15
# print(calculate_area(-1, 5))   # 💥 ValueError


# --- 練習 3：寫一個帶參數的 @retry(times=3) 裝飾器 ---
# 需求：如果被裝飾的函式拋出例外，自動重試指定次數
# 提示：需要三層巢狀，參考範例 4

# @retry(times=3)
# def unstable_task():
#     import random
#     if random.random() < 0.7:
#         raise ConnectionError("連線失敗")
#     return "成功！"

# print(unstable_task())


# --- 練習 4：寫一個 @cache 裝飾器（手動實作快取） ---
# 需求：記住函式的回傳值，相同參數不重複計算
# 提示：用 dict 儲存 {參數: 結果}，不要用 functools.lru_cache
# 進階思考：為什麼 key 要用 (args, tuple(sorted(kwargs.items()))) ?

# @cache
# def expensive(n):
#     print(f"  計算 {n}...")
#     return n ** 2

# print(expensive(5))    # 印出 "計算 5..." → 25
# print(expensive(5))    # 不印 "計算 5..."，直接回傳 25（命中快取）
# print(expensive(3))    # 印出 "計算 3..." → 9


# --- 練習 5：寫一個 @singleton 裝飾器（裝飾 class） ---
# 需求：確保一個 class 只有一個 instance，重複呼叫回傳同一個物件
# 提示：裝飾器不只能裝飾函式，也能裝飾 class！

# @singleton
# class Database:
#     def __init__(self):
#         print("建立 Database 連線...")

# db1 = Database()    # 印出 "建立 Database 連線..."
# db2 = Database()    # 不再印出（回傳同一個 instance）
# print(db1 is db2)   # True


# --- 練習 6：寫一個 @validate_types 帶參數裝飾器 ---
# 需求：檢查函式的參數型別是否符合預期
# 提示：裝飾器參數是型別，要與 *args 逐一比對

# @validate_types(int, int)
# def add(a, b):
#     return a + b

# print(add(3, 5))        # ✅ 8
# print(add("3", 5))      # 💥 TypeError: 參數 0 應為 <class 'int'>，但收到 <class 'str'>


# --- 練習 7：裝飾器堆疊 — 預測輸出順序 ---
# 需求：不執行程式的情況下，預測下面的輸出順序，然後再執行驗證

# def bold(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return f"<b>{func(*args, **kwargs)}</b>"
#     return wrapper

# def italic(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return f"<i>{func(*args, **kwargs)}</i>"
#     return wrapper

# @bold
# @italic
# def greet(name):
#     return f"Hello, {name}"

# # 問題：print(greet("Pan")) 會印出什麼？
# # A: <b><i>Hello, Pan</i></b>
# # B: <i><b>Hello, Pan</b></i>
# # 答案：（先想再取消註解執行）
# # print(greet("Pan"))


# --- 練習 8：用 @contextmanager 寫一個上下文管理器 ---
# 需求：寫一個 @contextmanager 包裝的 timer，印出程式碼區塊的執行時間
# 提示：from contextlib import contextmanager

# from contextlib import contextmanager

# @contextmanager
# def timer(label="區塊"):
#     # 你的程式碼（yield 前後分別做什麼？）
#     pass

# with timer("排序"):
#     sorted(range(100000, 0, -1))
# 預期輸出：⏱ 排序 花了 0.xxxx 秒
