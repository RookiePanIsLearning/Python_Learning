# Python 函式寫法比較 (def vs lambda)

## 1. 傳統函式 (`def`)
最正規、最常用的寫法。適合邏輯複雜、超過一行的程式碼。

### 語法結構：
```python
def 函式名稱(參數1, 參數2=預設值):
    # 執行邏輯
    return 結果
```

**【範例】**：計算兩數相加，如果沒給第二個數字，預設加 10。
```python
def add_numbers(a, b=10):
    result = a + b
    return result

print(add_numbers(5, 3))  # 8
print(add_numbers(5))     # 15
```

---

## 2. 匿名函式 (`lambda`)
如果一個函式的邏輯「超級簡單，只要一行就能寫完」，我們就可以用 `lambda` 來簡寫，連名字都不用取！

### 語法結構：
`lambda 參數1, 參數2: 回傳結果`

### 寫法對照比較：

**【比較 1：簡單計算】**
```python
# 傳統寫法
def square_def(x):
    return x ** 2

# lambda 寫法
square_lambda = lambda x: x ** 2

print(square_def(5))     # 25
print(square_lambda(5))  # 25
```

**【比較 2：搭配 `map` 或 `filter` (最常見的霸氣寫法)】**
這才是 `lambda` 真正發威的地方！我們不用為了只用一次的小邏輯去大費周章寫一個 `def`。

```python
numbers = [1, 2, 3, 4, 5]

# 目標：把清單裡每個數字都乘以 2

# 傳統寫法：
def double(x):
    return x * 2

result_old = list(map(double, numbers))  # 必須先在外面定義 def double

# lambda 寫法：乾淨、俐落，不留痕跡
result_new = list(map(lambda x: x * 2, numbers)) 

print(result_new)  # [2, 4, 6, 8, 10]
```
> **提示**：現在有了 `List Comprehension`（請參考 04_loops_advanced.md），`map` + `lambda` 的組合比較少用了，但面試或看別人的扣時還是很常遇到喔！
