# 進階例外處理：raise 與自定義例外

---

## ⚾ 投手 vs 捕手思維

| 角色 | 語法 | 職責 |
|---|---|---|
| **投手（進攻方）** | `raise` | 程式狀態不對時，**主動拋出**錯誤 |
| **捕手（防守方）** | `try/except` | **捕捉並處理**飛過來的錯誤 |

> 搭配 `06_exceptions.md` 的繼承樹：`raise` 就是從「例外目錄」中挑一個適合的錯誤丟出去。

---

## 🎯 raise 的四大用法

### 1. 基礎拋出 — 丟出內建例外

```python
def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("身高必須大於 0")   # 從例外目錄挑 ValueError 丟出去
    return weight / ((height / 100) ** 2)

calculate_bmi(70, -5)
# 💥 ValueError: 身高必須大於 0
```

### 2. 無參數拋出 — 攔截後原封不動往上丟

攔截錯誤只是為了記錄 Log，處理完後還是要讓上層知道出事了。

```python
def read_config():
    try:
        with open("config.json", "r") as f:
            return f.read()
    except FileNotFoundError:
        print("【系統日誌】警告！找不到設定檔。")
        raise   # 不帶參數 = 把剛才抓到的 FileNotFoundError 原封不動再丟出去

# 💥 FileNotFoundError 會繼續往上層傳遞
```

### 3. 例外鏈接 — 把底層錯誤包裝成商業邏輯錯誤

用 `raise ... from ...` 轉換錯誤，**同時保留原始錯誤軌跡**，Debug 時看得到兩層原因。

```python
class UserNotFoundError(Exception):
    pass

def get_user_data(user_id):
    database = {"001": "Alice"}
    try:
        return database[user_id]
    except KeyError as raw_error:
        # 技術錯誤 (KeyError) → 包裝成商業邏輯錯誤 (UserNotFoundError)
        raise UserNotFoundError(f"找不到 ID 為 {user_id} 的使用者") from raw_error

get_user_data("999")
# 💥 KeyError: '999'
# The above exception was the direct cause of the following exception:
# 💥 UserNotFoundError: 找不到 ID 為 999 的使用者
```

### 4. 自定義例外類別 — 擴充「例外目錄」

繼承 `Exception` 建立自己的例外，讓錯誤更有語義。

```python
# 建立專屬的例外階層（對應繼承樹概念）
class BankError(Exception):
    """銀行系統所有錯誤的基礎類別"""
    pass

class InsufficientFundsError(BankError):
    """餘額不足"""
    pass

class InvalidAccountError(BankError):
    """帳號格式錯誤"""
    pass
```

---

## 🌳 自定義例外如何接枝到繼承樹上

當我們建立自定義例外，就是在 Python 原有的樹上「接枝」，長出新分支。

### 為什麼要先建一個「根節點」？

| 理由 | 說明 |
|---|---|
| **隔離業務錯誤** | `except ShopSystemError` 只抓自己系統的錯，不會誤抓 Python 內建的 `TypeError`、`NameError` |
| **多層精準捕捉** | 上層可以用 `except PaymentError` 抓所有付款錯誤，下層可以針對 `CreditCardExpiredError` 做特定處理 |

### 範例 A：銀行系統（2 層）

```
Exception
└── BankError                    ← 專案根節點
    ├── InsufficientFundsError   ← 餘額不足
    └── InvalidAccountError      ← 帳號格式錯誤
```

```python
class BankError(Exception): pass
class InsufficientFundsError(BankError): pass
class InvalidAccountError(BankError): pass
```

### 範例 B：電商系統（3 層）

```
Exception
└── ShopSystemError                    ← 專案根節點
    ├── OutOfStockError                ← 商品缺貨
    ├── UserAuthError                  ← 使用者驗證錯誤
    └── PaymentError                   ← 付款相關（中間分類層）
        ├── CreditCardExpiredError     ← 信用卡過期
        └── InsufficientBalanceError   ← 餘額不足
```

```python
class ShopSystemError(Exception): pass       # 根節點

class OutOfStockError(ShopSystemError): pass
class UserAuthError(ShopSystemError): pass

class PaymentError(ShopSystemError): pass    # 中間分類層
class CreditCardExpiredError(PaymentError): pass
class InsufficientBalanceError(PaymentError): pass
```

**捕捉彈性示範 — `except` 就是例外處理的 `elif`：**

多個 `except` 的運作邏輯與 `if...elif...` **幾乎一模一樣**：
- **由上往下找，先搶先贏**：一旦遇到第一個符合的 `except`，就執行它，後面全部跳過
- **黃金法則**：「**由小到大，由精準到寬鬆**」— 子類別排在父類別前面

```python
try:
    process_payment()

# 🐟 小漁網 A：只抓「餘額不足」
except InsufficientBalanceError:
    show_topup_page()

# 🐟 小漁網 B：只抓「信用卡過期」
except CreditCardExpiredError:
    show_card_update_page()

# 🦈 中漁網：抓「所有付款問題」（前兩個沒抓到的付款錯誤）
except PaymentError:
    show_payment_retry_page()

# 🐳 大漁網：抓「整個電商系統的專屬錯誤」（如缺貨）
except ShopSystemError:
    log_error_and_notify_admin()

# 🌊 海綿：抓「所有 Python 內建常規錯誤」（完全沒預料到的錯）
except Exception:
    raise   # 未知錯誤往上丟，讓程式崩潰以警示開發者
```

> ❌ **新手常犯：父類別放前面，子類別永遠不會被執行到**
>
> ```python
> # ⛔ 錯誤示範：父類別放前面
> except PaymentError:
>     print("付款發生問題了！")
> except InsufficientBalanceError:
>     print("餘額不足！")  # 💀 永遠不會執行到！
>                          # InsufficientBalanceError 是 PaymentError 子類別
>                          # 早就被上面攔截了
> ```

> 💡 **多個錯誤做同樣處理？用 Tuple 合併：**
>
> ```python
> except (InsufficientBalanceError, CreditCardExpiredError) as e:
>     print(f"付款失敗：{e}")
>     return_to_home_page()
> ```

### 🤔 同級例外之間的順序有差嗎？

`InsufficientBalanceError` 和 `CreditCardExpiredError` 同屬 `PaymentError` 的子類別，是「兄弟」關係，**彼此之間沒有繼承關係，先後順序不影響結果**。

```
PaymentError
├── InsufficientBalanceError   ← 同級，不會互搶
└── CreditCardExpiredError     ← 同級，不會互搶
```

重點在於**要不要區分它們**，依此選擇設計方式：

**① 需要不同處理 → 分開 `except`（順序無所謂）**
```python
except InsufficientBalanceError:     # 和下面交換也沒差
    show_topup_page()
except CreditCardExpiredError:
    show_card_update_page()
```

**② 相同處理但想知道是哪種 → Tuple**
```python
except (InsufficientBalanceError, CreditCardExpiredError) as e:
    print(f"是哪種錯：{type(e).__name__}")
    show_payment_retry_page()
```

**③ 完全不在乎細節 → 直接用父類別**
```python
except PaymentError:                 # 最簡潔，任何付款錯誤都一視同仁
    show_payment_retry_page()
```

| 問題 | 選擇 |
|---|---|
| 兩種錯誤要跳到不同頁面？ | ① 分開 `except` |
| 兩種錯誤行為一樣，但想知道是哪種？ | ② Tuple |
| 完全不需要區分？ | ③ 父類別 |



---

## 📁 實務專案結構：`exceptions.py`

當專案變大，把所有自定義例外集中在一個獨立檔案：

```
shop_system/
├── main.py          ← 主程式，import exceptions
├── cart.py          ← 購物車邏輯
├── payment.py       ← 付款邏輯
└── exceptions.py    ← 所有自定義例外集中在這裡
```

**`exceptions.py`:**
```python
class ShopSystemError(Exception): pass
class OutOfStockError(ShopSystemError): pass
class PaymentError(ShopSystemError): pass
class CreditCardExpiredError(PaymentError): pass
class InsufficientBalanceError(PaymentError): pass
```

**`payment.py`:**
```python
from exceptions import PaymentError, InsufficientBalanceError

def process_payment(amount, balance):
    if amount > balance:
        raise InsufficientBalanceError(f"餘額不足：需要 {amount}，只有 {balance}")
```

**`main.py`:**
```python
from exceptions import ShopSystemError
from payment import process_payment

try:
    process_payment(5000, 1000)
except ShopSystemError as e:
    print(f"購物失敗：{e}")
```

---

## 🏦 終極整合範例：銀行轉帳系統

將「自定義例外 + raise + try/except 繼承捕捉」全部串在一起：

```python
# ==========================================
# 第一步：擴充例外目錄（自定義例外階層）
# ==========================================
class BankError(Exception):
    pass

class InsufficientFundsError(BankError):
    pass

class InvalidAccountError(BankError):
    pass


# ==========================================
# 第二步：進攻方 — 用 raise 主動防禦
# ==========================================
def transfer_money(from_account, to_account, amount, balance):
    if not isinstance(amount, (int, float)):
        raise TypeError("轉帳金額必須是數字！")

    if len(to_account) != 5:
        raise InvalidAccountError(f"帳號 {to_account} 格式錯誤，長度需為 5 碼。")

    if amount > balance:
        raise InsufficientFundsError(f"轉帳 {amount} 元失敗，餘額僅 {balance} 元。")

    new_balance = balance - amount
    return f"成功轉帳 {amount} 元至 {to_account}，剩餘 {new_balance} 元。"


# ==========================================
# 第三步：防守方 — 用 except 捕捉與處理
# ==========================================
def run_atm_system():
    my_balance = 1000

    try:
        # ↓ 改這裡來觀察不同錯誤路徑
        # amount="五十"  → TypeError
        # to_account="123" → InvalidAccountError（被 BankError 接住）
        # amount=5000    → InsufficientFundsError
        result = transfer_money("A0001", "B0002", 5000, my_balance)
        print("🟢", result)

    except TypeError as e:
        print("🔴 【輸入格式錯誤】", e)

    except InsufficientFundsError as e:
        print("🟡 【交易拒絕】", e)
        print("   👉 請先存入足夠金額。")

    except BankError as e:
        # InvalidAccountError 是 BankError 的子類別，會在這裡被捕捉
        print("🟠 【銀行業務異常】", e)

    except Exception as e:
        # 最後的防線：捕捉所有未知常規錯誤，記錄後往上丟
        print("💥 【未知嚴重錯誤】", e)
        raise   # 讓程式崩潰以喚醒開發者

run_atm_system()
```

**執行路徑圖：**
```
amount=5000
    → raise InsufficientFundsError
        → except InsufficientFundsError ✅ 被精準捕捉

to_account="123"
    → raise InvalidAccountError
        → except InsufficientFundsError ❌ 不符合
        → except BankError ✅ 被父類別捕捉（繼承樹的威力）
```

---

## 💡 為什麼這樣寫是「好」的程式碼？

| 原則 | 說明 |
|---|---|
| **Fail-Fast（快死原則）** | 透過 `raise`，一發現不對勁立刻停止，不帶著錯誤的資料繼續跑 |
| **職責分離** | `transfer_money` 只定義規則並拋錯；`run_atm_system` 只負責顯示給使用者看 |
| **精準打擊** | 自定義例外讓你可以針對 `InsufficientFundsError` 寫特定處理邏輯 |
| **可追蹤性** | `raise ... from ...` 保留原始錯誤軌跡，Debug 時看得到完整脈絡 |

---

## ⚠️ 易錯點 (Gotchas)

1. **`raise` 不帶參數只能在 `except` 區塊裡用**：它重新拋出「當前正在處理的例外」，在 `except` 外面用會報 `RuntimeError`。

2. **自定義例外要繼承 `Exception`，不要繼承 `BaseException`**：繼承 `BaseException` 會讓你的例外和 `SystemExit`、`KeyboardInterrupt` 同層，難以被一般的 `except Exception` 捕捉。

3. **`raise ... from None`**：如果你不想顯示原始錯誤鏈，可以用 `from None` 切斷。
   ```python
   raise UserNotFoundError("找不到使用者") from None
   # 只顯示 UserNotFoundError，隱藏底層 KeyError
   ```
