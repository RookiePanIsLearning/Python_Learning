# ==========================================
# 主題：List Comprehension (串列推導式) 練習
# ==========================================

print("--- 題目 1：將原本的迴圈改寫成 Comprehension ---")
# [傳統寫法]
numbers = [1, 2, 3, 4, 5]
squares_old = []
for n in numbers:
    squares_old.append(n**2)
print(f"傳統寫法: {squares_old}")

# [我的練習 - Comprehension 寫法]
squares_new = [n**2 for n in numbers]
print(f"推導寫法: {squares_new}")


print("\n--- 題目 2：加入 if 條件篩選 ---")
# 目標：找出 1~10 之間的偶數
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"1~10的偶數: {even_numbers}")


print("\n--- 題目 3：動手玩玩看 (字串處理) ---")
# 目標：把一段文字中的母音 (a, e, i, o, u) 挑出來放進一個 list
text = "hello world, python is awesome"
vowels = "aeiou"

# 提示：用一個 for 迴圈走訪 text 的每一個字，判斷它有沒有 in vowels
# TODO: 你的程式碼寫在下面
# my_vowels = [...]
# print("抓到的母音:", my_vowels)

