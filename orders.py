from binance.exceptions import BinanceAPIException

def place_market_order(client, symbol, side, quantity):
    """
    Places a Market Order (buys/sells immediately).
    """
    try:
        print(f"Submitting {side} order for {quantity} {symbol}...")
        
        # Send the order to Binance Futures
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        
        print(f"Order Successful! Order ID: {order['orderId']}")
        return order

    except BinanceAPIException as e:
        print(f"Error placing order: {e}")
        return None