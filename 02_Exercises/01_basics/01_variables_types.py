# 模組 1：開發環境建置與變數型態 
# 目標：練習宣告 int, float, str, bool 以及基本的 f-string 操作

## int 宣告

int_x1 = int()
int_x2 = 123


# float 宣告

flt_x1 = float()
flt_x2 = 3.1415927




# Check the result of type
check_int = "<class 'int'>"
check_flt = "<class 'float'>"



# Result Output


print("----------------------------------")
print(" int")
print(f"x1:{int_x1}, type: {type(int_x1)} :{str(type(int_x1)) == check_int}")
print(f"x2:{int_x2}, type: {type(int_x2)} :{str(type(int_x2)) == check_int}")
print("----------------------------------")
print(" float")
print(f"x1:{flt_x1}, type: {type(flt_x1)} :{str(type(flt_x1)) == check_flt}")
print(f"x2:{flt_x2}, type: {type(flt_x2)} :{str(type(flt_x2)) == check_flt}")
print("----------------------------------")