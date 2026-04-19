# Assertion（斷言）與 AssertionError — 完整教學

目標：讓你了解 `assert` 的語法、用途、常見錯誤情境、最佳實務，以及在測試與生產環境中應採取的替代作法。

---

## 概述

`assert`（斷言）是一個用來在程式執行期間檢查假設（invariants）的簡潔語法。當斷言的條件為 False 時，Python 會拋出 `AssertionError`，並可帶上自訂訊息以利除錯。

斷言常用於開發與測試期間，檢查程式內部的不變式；但不應被用來做使用者輸入或外部資料的正式驗證，因為在優化模式下（例如以 `python -O` 執行）所有 `assert` 會被移除。

---

## 語法

基本語法：

```python
assert <condition>
assert <condition>, "錯誤訊息"
```

範例：

```python
x = 5
assert x > 0, "x 必須為正數"
```

如果 `x > 0` 為 False，程式會拋出 `AssertionError: x 必須為正數`。

你也可以直接以程式方式拋出相同例外：

```python
if not x > 0:
    raise AssertionError("x 必須為正數")
```

但通常不建議用 `raise AssertionError(...)` 取代更適切的具名例外（例如 `ValueError`、`TypeError` 等）。

---

## 何時會觸發 AssertionError

- 使用 `assert` 時條件評估為 False
- 程式中以 `raise AssertionError(...)` 明確拋出

例如：

```python
def divide(a, b):
    assert b != 0, "除數不能為 0"
    return a / b

divide(1, 0)  # -> AssertionError: 除數不能為 0
```

注意：上例雖然可工作，但在處理外部輸入（例如函式參數來自使用者）時，應改用具名例外：

```python
def divide(a, b):
    if b == 0:
        raise ValueError("除數不能為 0")
    return a / b
```

原因在於 `assert` 可能在某些執行模式被移除（下節詳細說明）。

---

## assert 與優化模式（python -O / __debug__）

當 Python 以優化模式執行（例如 `python -O script.py` 或設定環境變數 `PYTHONOPTIMIZE`）時，所有 `assert` 陳述式會在編譯階段被忽略，也就是它們不會執行或產生任何副作用。

因此：

- 不要把 `assert` 當作生產環境中必要的檢查或控制流程。
- `__debug__` 是一個內建變數，當執行在非優化模式時為 True，在 `-O` 或 `-OO` 下為 False。你可以用它檢查是否啟用了優化模式，但在實務上，最穩妥的做法是不要依賴 `assert` 做必要的檢查。

範例：

```python
print(__debug__)  # 正常執行時 True，-O 時為 False

def f():
    assert False, "這個斷言會在非優化模式下觸發"

f()
```

在 `python -O` 下，`f()` 裡的 `assert` 會被移除，所以不會拋出例外。

---

## 捕捉 AssertionError

你可以像捕捉其他例外一樣捕捉 `AssertionError`：

```python
try:
    assert False, "測試失敗"
except AssertionError as e:
    print("捕捉到斷言失敗：", e)
```

在某些工具或測試程式中，捕捉 `AssertionError` 是合理的；但在程式業務邏輯中不建議以此控制正常邏輯流程。

---

## 在單元測試中的使用

在測試中使用 `assert` 非常常見，特別是搭配 pytest。pytest 會重寫 `assert` 陳述式，使失敗輸出顯示更多表達式的中間值，提升診斷能力：

```python
def test_add():
    assert add(2, 3) == 5
```

此外，要測某個操作會拋出特定例外，請用 pytest 提供的上下文管理器：

```python
import pytest

def test_div_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
```

（在測試中使用 `assert` 是推薦做法；與此不同的是，不要把 `assert` 當作函式的輸入驗證手段）

---

## 最佳實務與建議

- 用途：把 `assert` 保留給開發期及內部不變式檢查（例如在演算法中確認狀態前提、或在測試內部檢查）。
- 不該用途：外部輸入驗證、業務邏輯的必要檢查、或任何在生產環境必須確保的防護（因為 `assert` 可能被移除）。
- 若需在生產環境檢查參數或輸入，請使用明確的條件並拋出具名例外（`ValueError`、`TypeError`、`RuntimeError` 等）。
- 在庫 / API 設計上，請以清楚的例外型別作為錯誤語意的契約，不要依賴 `AssertionError`。

範例替代（不要用 assert 做輸入驗證）：

```python
def process(items):
    if not isinstance(items, list):
        raise TypeError("items 必須為 list")
    # 正式處理流程...
```

---

## 常見用法範例

1) 內部不變式（開發/測試期間）

```python
def normalize(scores):
    assert len(scores) > 0, "scores 不能為空"
    total = sum(scores)
    return [s / total for s in scores]
```

2) 不推薦但常見的 `raise AssertionError`（較少見，且通常可用更明確的例外代替）：

```python
if unexpected_condition:
    raise AssertionError("不應該發生的狀態")
```

3) 在類別初始化檢查（建議用具名例外）：

```python
from dataclasses import dataclass

@dataclass
class Account:
    balance: float

    def __post_init__(self):
        if self.balance < 0:
            raise ValueError("balance 必須 >= 0")
```

若改用 `assert`：

```python
    def __post_init__(self):
        # 不推薦：如果使用 -O，這個檢查會被移除
        assert self.balance >= 0, "balance 必須 >= 0"
```

---

## 進階：把 AssertionError 轉換為更清楚的例外

如果你接收到第三方程式或測試程式拋出的 AssertionError，想把它轉換成對使用者更有意義的錯誤，可以這樣做：

```python
try:
    assert config_is_valid(config), "config 不合法"
except AssertionError as e:
    raise ValueError("設定錯誤：請檢查 config") from e
```

這樣可以保留原始的例外鏈結，並對外提供一致的例外型別。

---

## 練習題（建議練習）

1. 製作一個函式 `safe_divide(a, b)`，當 `b == 0` 時用 `ValueError` 回報，並寫兩個測試：一個測正常輸入、一個測 `b == 0`。
2. 找出你專案中不應該用 `assert` 做輸入驗證的地方，改寫成具名例外並撰寫測試。
3. 用 pytest 實作一個測試，示範 pytest 在 `assert` 失敗時的詳細差異輸出。

---

---

## 附錄：穩健替代寫法（實作範例）

以下為幾種在生產或教學中常用的替代寫法，能避免依賴 `assert` 帶來的中斷或在優化模式下被忽略的問題。

1) 具名例外（生產用）

```python
def safe_divide(a, b):
    if b == 0:
        raise ValueError("除數不能為 0")
    return a / b
```

2) 回傳 (result, error) 風格（API 友善）

```python
def try_int(s):
    try:
        return int(s), None
    except ValueError as e:
        return None, str(e)
```

3) 使用 `warnings` 發出警示（非致命）

```python
import warnings

def process_scores(scores):
    if not scores:
        warnings.warn("scores 為空，回傳空列表", RuntimeWarning)
        return []
    total = sum(scores)
    return [s / total for s in scores]
```

4) 記錄錯誤並使用回退值（可恢復情況）

```python
import logging
logger = logging.getLogger(__name__)
DEFAULT_CFG = {"mode": "safe"}

def load_config(cfg):
    if not isinstance(cfg, dict) or "mode" not in cfg:
        logger.error("config 無效，使用預設值")
        return DEFAULT_CFG.copy()
    return cfg
```

5) 使用驗證框架（較複雜輸入）

```python
try:
    from pydantic import BaseModel, ValidationError

    class Item(BaseModel):
        name: str
        qty: int

    # Item(name='pen', qty=-1)  # 將拋出 ValidationError
except Exception:
    # 若環境沒安裝 pydantic，示範可跳過
    pass
```

6) 捕捉並轉換 `AssertionError`（過渡方案）

```python
try:
    assert config_is_valid(config), "config 不合法"
except AssertionError as e:
    raise ValueError("設定錯誤：請檢查 config") from e
```

---

## 參考與延伸閱讀

- 深入閱讀例外處理： [01_Syntax_Notes/06_exceptions.md](01_Syntax_Notes/06_exceptions.md)
- raise 與手動拋例外說明： [01_Syntax_Notes/07_raise.md](01_Syntax_Notes/07_raise.md)

---

如果你希望，我可以：

- 將這個檔案加入 00_Index.md 的目錄中（更新索引）；
- 為檔案補上更多練習答案或互動範例（例如可直接執行的範例檔）；
- 或把重點整理成簡短的投影片式筆記方便教學使用。

請告訴我你想要的下一步。
