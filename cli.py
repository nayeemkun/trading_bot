import time
from client import get_binance_client
from orders import place_market_order
from validators import validate_quantity, validate_pair

def run_bot_loop(client, symbol, quantity):
    print(f"\n[INFO] STARTED AUTO-TRADING ON {symbol}")
    print("Press Ctrl + C to stop the bot.\n")

    try:
        while True:
            print(f"[INFO] Checking market for {symbol}...")
            
            # Place a small BUY order
            place_market_order(client, symbol, "BUY", quantity)
            
            # Wait 10 seconds before next trade
            print("[INFO] Waiting 10 seconds...")
            time.sleep(10)

    except KeyboardInterrupt:
        print("\n[INFO] Bot stopped by user.")

def main():
    client = get_binance_client(testnet=True)
    if not client: return

    print("\n--- Binance Futures Trading Bot ---")
    print("1. Manual Trade (One-time)")
    print("2. Auto-Bot (Loop every 10s)")
    
    choice = input("Choose mode (1 or 2): ")
    
    symbol = "BTCUSDT"
    
    if choice == "1":
        # Manual Mode
        side = input("BUY or SELL? ").upper()
        if side not in ["BUY", "SELL"]:
            print("Error: Invalid side.")
            return

        raw_qty = input("Quantity: ")
        qty = validate_quantity(raw_qty)
        
        if qty:
            place_market_order(client, symbol, side, qty)
        
    elif choice == "2":
        # Auto Mode
        qty = 0.01  # Fixed small amount for safety
        run_bot_loop(client, symbol, qty)
        
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()