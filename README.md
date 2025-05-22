## 💻 Author: Davi Galdino de Souza

---

## 🧠 Algorithm Logic  
Uses a **greedy approach** with `Decimal` for precision to:  
1. Calculate required change (`payment - price`).  
2. Find the closest higher denomination (if exact change isn’t available).  
3. Output the optimal payment + minimal change.  

### 🔧 Key Features  
✔ **Precision Handling**: Uses `Decimal` to avoid floating-point errors.  
✔ **Dynamic Denominations**: Works with any currency list (default: USD coins/bills).  
✔ **Input Validation**: Ensures numeric inputs format.  

## 🛠️ Code Structure  
```python
from decimal import Decimal

# Default USD denominations (sorted as Decimals)
currency = sorted([Decimal(str(c)) for c in [0.01, 0.05, 0.10, 0.25, 1, 5, 10, 20, 50, 100]])

def find_closest(change):
    """Returns nearest denomination to `change`."""
    return min(currency, key=lambda x: abs(x - change))

def change_optimized(product_price: str, payment: str):
    """Core logic: Computes optimal payment + change."""
    # ... (see full code for details)
```

## 🚀 Run Locally

  git clone https://github.com/Floorsk/python-technical-challenge  
  cd [repo-directory]  
  python3 script.py

## 📝 Notes
  1. Why Not float? Floating-point math fails for financial calculations (e.g., $0.1 + $0.2 ≠ $0.3).
  2. Extendable: Replace currency list with Euros, Crypto, etc.
