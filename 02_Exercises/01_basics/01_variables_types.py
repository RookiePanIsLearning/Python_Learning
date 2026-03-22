# 模組 1：開發環境建置與變數型態 
# 目標：練習宣告 int, float, str, bool 以及基本的 f-string 操作

## int 宣告

# 使用 int() 函式宣告一個整數變數，預設值為 0
# 直接賦值宣告整數變數，分別為正整數和負整數
# 使用型態檢查確認變數的型態是否為 int

int_x1 = int()
int_x2 = 123
int_x3 = -456
int_x4 : int = 0  # 使用型態註解宣告整數變數，但不會限制變數型態
int_x5 : int = 3.14  # 使用型態註解宣告整數變數，但賦值為浮點數，Python 不會報錯，但變數型態仍為 float
int_x6 : int = "Hello"  # 使用型態註解宣告整數變數，但賦值為字串，Python 不會報錯，但變數型態仍為 str


# float 宣告

flt_x1 = float()
flt_x2 = 3.1415927
flt_x3 : float = 0.0  # 使用型態註解宣告浮點數變數，但不會限制變數型態
flt_x4 : float = 123  # 使用型態註解宣告浮點數變數，但賦值為整數，Python 不會報錯，但變數型態仍為 int
flt_x5 : float = "Hello"  # 使用型態註解宣告浮點數變數，但賦值為字串，Python 不會報錯，但變數型態仍為 str


# Check the result of type
check_int = "<class 'int'>"
check_flt = "<class 'float'>"



# Result Output


print("----------------------------------")
print(" int")
print(f"x1:{int_x1}, type: {type(int_x1)} :{str(type(int_x1)) == check_int}")
print(f"x2:{int_x2}, type: {type(int_x2)} :{str(type(int_x2)) == check_int}")
print(f"x3:{int_x3}, type: {type(int_x3)} :{str(type(int_x3)) == check_int}")
print(f"x4:{int_x4}, type: {type(int_x4)} :{str(type(int_x4)) == check_int}")
print(f"x5:{int_x5}, type: {type(int_x5)} :{str(type(int_x5)) == check_int}")
print(f"x6:{int_x6}, type: {type(int_x6)} :{str(type(int_x6)) == check_int}")
print("----------------------------------")
print(" float")
print(f"x1:{flt_x1}, type: {type(flt_x1)} :{str(type(flt_x1)) == check_flt}")
print(f"x2:{flt_x2}, type: {type(flt_x2)} :{str(type(flt_x2)) == check_flt}")
print(f"x3:{flt_x3}, type: {type(flt_x3)} :{str(type(flt_x3)) == check_flt}")
print(f"x4:{flt_x4}, type: {type(flt_x4)} :{str(type(flt_x4)) == check_flt}")
print(f"x5:{flt_x5}, type: {type(flt_x5)} :{str(type(flt_x5)) == check_flt}")
print("----------------------------------")