# 進階迴圈 (Advanced Loops) 與 推導式 (Comprehension)

## 1. List Comprehension (串列推導式)
重點觀念：用一行程式碼產生一個新的 List，語法不僅簡潔，執行速度通常也比傳統迴圈(append)快。

### 語法結構：
`[ 運算結果 or 變數操作 for 變數 in 可迭代物件 if 條件判斷 ]`

### 寫法對照比較：

**【傳統做法】**
```python
squares = []
for x in range(5):
    if x % 2 == 0:
        squares.append(x**2)
```

**【推導式寫法】**
```python
squares = [x**2 for x in range(5) if x % 2 == 0]
```

## 2. Dict Comprehension (字典推導式)
### 語法結構：
`{ key: value for 變數 in 可迭代物件 }`

### 常見應用場景：
把兩個清單合併成一個字典！
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
```
