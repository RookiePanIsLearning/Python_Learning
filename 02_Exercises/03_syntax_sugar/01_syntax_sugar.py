# 模組 1-2：Python 語法糖綜合練習
# 目標：熟悉解包、推導式、海象運算子、match-case、f-string 等語法糖

# =============================================
# 🎯 範例區
# =============================================

# === 範例 1：解包 (Unpacking) ===
# 基本解包
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")

# 星號解包
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# 變數交換
a, b = 1, 2
a, b = b, a
print(f"交換後: a={a}, b={b}")


# === 範例 2：運算子 ↔ 特殊方法 ===
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2           # 語法糖，實際呼叫 v1.__add__(v2)
print(v3)               # Vector(4, 6)
print(v1 == v2)         # False（呼叫 v1.__eq__(v2)）


# === 範例 3：鏈式比較 ===
score = 75
if 60 <= score < 80:
    print("及格")       # 等同 (60 <= score) and (score < 80)


# === 範例 4：海象運算子 := ===
# 在 while 迴圈中一行搞定讀取 + 判斷
data = [5, 12, 3, 18, 7, 2]
filtered = [y for x in data if (y := x * 3) > 10]
print(f"海象過濾: {filtered}")   # [36, 54, 21]


# === 範例 5：f-string 進階技巧 ===
import math
pi = math.pi
print(f"圓周率: {pi:.4f}")           # 3.1416
print(f"{'Python':>15}")              # 右對齊
print(f"{'Python':-^20}")             # 居中填充
print(f"{pi = }")                     # debug 用法: pi = 3.14...


# === 範例 6：match-case 模式匹配 (Python 3.10+) ===
def classify(value):
    match value:
        case int(n) if n > 0:
            return f"正整數: {n}"
        case int(n):
            return f"非正整數: {n}"
        case str(s):
            return f"字串: {s}"
        case [x, y]:
            return f"二元素列表: [{x}, {y}]"
        case _:
            return "其他"

print(classify(42))
print(classify(-3))
print(classify("hello"))
print(classify([1, 2]))


# =============================================
# 🎯 練習區
# =============================================

# --- 練習 1：用解包取出嵌套資料 ---
# 需求：用一行解包取出 name, age, city
# 提示：支援嵌套解包 (a, (b, c)) = ...
person = ("Pan", (25, "Taipei"))

# 你的程式碼（一行）


# 預期：print(name, age, city)
# → Pan 25 Taipei


# --- 練習 2：用星號解包分離表頭 ---
# 需求：從 csv_data 中分離出 header 和所有 rows
csv_data = [
    "name,age,city",
    "Pan,25,Taipei",
    "Alice,30,Tokyo",
    "Bob,28,Seoul",
]

# 你的程式碼（一行）


# 預期：
# header = "name,age,city"
# rows = ["Pan,25,Taipei", "Alice,30,Tokyo", "Bob,28,Seoul"]


# --- 練習 3：實作自定義 class 的特殊方法 ---
# 需求：讓 Money class 支援 +, ==, <, str() 四種運算子語法糖
# 提示：實作 __add__, __eq__, __lt__, __str__

# class Money:
#     def __init__(self, amount, currency="TWD"):
#         self.amount = amount
#         self.currency = currency
#
#     # 你的程式碼
#     pass

# m1 = Money(100)
# m2 = Money(200)
# m3 = m1 + m2
# print(m3)          # 300 TWD
# print(m1 < m2)     # True
# print(m1 == Money(100))  # True


# --- 練習 4：推導式三連發 ---
# 需求 A：用 list comprehension 找出 1~50 中所有能被 3 整除但不能被 5 整除的數
# 需求 B：用 dict comprehension 建立 {字母: ASCII碼} 的字典，範圍 a-z
# 需求 C：用 set comprehension 找出兩個列表中共同出現的元素

list_a = [1, 2, 3, 4, 5, 6, 7, 8]
list_b = [5, 6, 7, 8, 9, 10, 11]

# A: divisible_by_3 = ???
# B: ascii_map = ???
# C: common = ???


# --- 練習 5：海象運算子實戰 ---
# 需求：重構下面的程式碼，用海象運算子消除重複計算
# 原始版本：
import re

texts = ["hello world", "foo 123 bar", "no numbers", "test 456 ok"]

# 囉嗦版（match 被算了兩次）
results_verbose = []
for text in texts:
    if re.search(r"\d+", text):
        results_verbose.append(re.search(r"\d+", text).group())

# 用海象運算子重寫成一行（list comprehension + :=）
# results_walrus = ???

# print(results_walrus)  # ['123', '456']


# --- 練習 6：match-case 指令解析器 ---
# 需求：寫一個 parse_command 函式，用 match-case 解析以下指令
# "move north 5"  → 回傳 ("move", "north", 5)
# "attack goblin"  → 回傳 ("attack", "goblin")
# "heal"           → 回傳 ("heal",)
# "quit"           → 回傳 None
# 其他              → raise ValueError

# def parse_command(cmd):
#     match cmd.split():
#         # 你的 case 分支
#         pass

# print(parse_command("move north 5"))    # ('move', 'north', 5)
# print(parse_command("attack goblin"))   # ('attack', 'goblin')
# print(parse_command("heal"))            # ('heal',)
# print(parse_command("quit"))            # None


# --- 練習 7：f-string 格式化報表 ---
# 需求：用 f-string 格式化微語言，印出對齊的報表
products = [
    ("蘋果", 35, 120),
    ("香蕉", 18, 300),
    ("藍莓禮盒", 450, 15),
]

# 預期輸出（右對齊數字、左對齊品名、千分位分隔）：
# 品名           單價      數量        小計
# ──────────────────────────────────────────
# 蘋果             35       120      4,200
# 香蕉             18       300      5,400
# 藍莓禮盒        450        15      6,750

# 提示：
# f"{'文字':<10}"  → 左對齊，寬度10
# f"{數字:>8}"     → 右對齊，寬度8
# f"{數字:>8,}"    → 右對齊 + 千分位


# --- 練習 8：綜合挑戰 — 用語法糖重構囉嗦程式碼 ---
# 需求：把下面的「囉嗦版」重構成 Pythonic 版（盡量用語法糖）

# 囉嗦版：
data = {"users": [
    {"name": "Pan", "scores": [85, 92, 78]},
    {"name": "Alice", "scores": [90, 88, 95]},
    {"name": "Bob", "scores": [70, 65, 80]},
]}

# 找出平均分數 > 80 的使用者名稱
result_verbose = []
for user in data["users"]:
    total = 0
    for s in user["scores"]:
        total += s
    avg = total / len(user["scores"])
    if avg > 80:
        result_verbose.append(user["name"])

print(result_verbose)   # ['Pan', 'Alice']

# Pythonic 版（用一行 list comprehension + 海象運算子 或 sum() 重寫）
# result_pythonic = ???
