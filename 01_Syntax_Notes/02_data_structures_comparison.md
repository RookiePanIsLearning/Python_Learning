# Python 資料結構觀念比較 (List, Tuple, Set, Dict)

在 Python 中，要把一堆資料裝在一起，我們有四種最常用的「容器」。
初學者最常混淆的就是到底什麼時候要用哪一個？

## 快速比較表

| 資料結構 | 符號 | 有無順序？ | 可否修改？ | 元素可否重複？ | 查詢速度 | 適合情境 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **List (串列)** | `[ ]` | ✅ 有 | ✅ 可 | ✅ 可 | 慢 | 一般最常用的容器，需要依序處理資料時 |
| **Tuple (元組)** | `( )` | ✅ 有 | ❌ **不可** | ✅ 可 | 中 | 當資料**絕對不能被改動**時（例如：經緯度座標、常數設定） |
| **Set (集合)** | `{ }` | ❌ 無 | ✅ 可 | ❌ **不可** | **極快** | 需要**去除重複資料**，或是判斷 A 裡面有沒有 B 時（交集、聯集） |
| **Dict (字典)** | `{k: v}`| ✅ (3.7+) | ✅ 可 | Key 不可, Value 可| **極快** | 像查字典一樣，有一個「標籤(Key)」對應一個「值(Value)」，例如：學號對應姓名 |

---

## 寫法與重點比較

### 1. List (串列) vs Tuple (元組)
最大的差別在於**「可不可改變 (Mutable vs Immutable)」**。

```python
# List 可以隨意新增、修改、刪除
my_list = [10, 20, 30]
my_list[0] = 99         # 變成 [99, 20, 30]
my_list.append(40)      # 變成 [99, 20, 30, 40]

# Tuple 生出來之後就不能動了！(這是一種保護機制)
my_tuple = (10, 20, 30)
# my_tuple[0] = 99      # ❌ 會報錯: TypeError: 'tuple' object does not support item assignment
```

### 2. List (串列) vs Set (集合)
最大的差別在於**「能不能重複」**以及**「尋找速度」**。

```python
# List 可以有重複元素
my_list = [1, 2, 2, 3, 3, 3]
print(my_list)  # [1, 2, 2, 3, 3, 3]

# Set 絕對不會有重複元素 (自動去重)
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)   # {1, 2, 3}

# 【效能比較】
# 如果要判斷一個數字有沒有在裡面 (in 操作)：
# x in my_list -> 電腦會從頭找到尾，資料越多找越慢。
# x in my_set  -> 電腦用 Hash Table，瞬間就能找到！
```

### 3. Dict (字典) 的常見寫法與取值
字典最適合拿來存「結構化」的資料。

```python
# 傳統取值法 vs 安全取值法(get)
user = {"name": "Peter", "age": 25}

# 1. 傳統取值法: 如果 key 不存在會大當機 (KeyError)
print(user["name"])  # Peter
# print(user["gender"])  # ❌ KeyError

# 2. 安全取值法 (強烈推薦!): 如果 key 不存在，可以設定預設值，不會當機
print(user.get("name"))           # Peter
print(user.get("gender", "未知")) # 未知
```
