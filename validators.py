def validate_quantity(quantity_str):
    """
    Checks if the entered quantity is a valid positive number.
    """
    try:
        qty = float(quantity_str)
        if qty <= 0:
            print("Error: Quantity must be greater than 0.")
            return None
        return qty
    except ValueError:
        print("Error: Input is not a valid number.")
        return None

def validate_pair(symbol):
    """
    Checks if the symbol looks correct (e.g., BTCUSDT).
    """
    if not symbol.endswith("USDT"):
        print("Warning: This bot is optimized for USDT pairs (like BTCUSDT).")
        return False
    return True