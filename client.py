from binance.client import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_binance_client(testnet=True):
    """
    Creates a connection to Binance.
    """
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not api_secret:
        print("Error: API Keys not found!")
        return None

    # Connect to the Client
    client = Client(api_key, api_secret, testnet=testnet)
    print(f"Connected to Binance {'Testnet' if testnet else 'Mainnet'}!")
    
    return client

if __name__ == "__main__":
    # Test the connection immediately when running this file
    client = get_binance_client(testnet=True)
    
    # Try to fetch server time to prove it works
    if client:
        print("Server Time:", client.get_server_time())