# Binance Futures Trading Bot

A Python-based trading bot that interacts with the Binance Futures Testnet. This project was built as part of a technical assessment to demonstrate API connectivity, order execution, and automated trading logic.

## Features
* **Connectivity:** Securely connects to Binance Futures Testnet using API keys.
* **Manual Mode:** User can place Buy/Sell market orders via a command-line interface.
* **Auto-Trading Mode:** An automated loop that executes trades every 10 seconds (for demonstration).
* **Safety & Validation:** Includes robust input validation to prevent invalid orders and safeguards against crashes.

## Tech Stack
* Python 3.x
* `python-binance` library
* `python-dotenv` for security

## Project Structure
* `cli.py`: The main entry point (Manager). Handles user input and the trading loop.
* `client.py`: Manages the connection to Binance.
* `orders.py`: executing the specific trade logic (Market Orders).
* `validators.py`: Ensures all user inputs (quantities, symbols) are valid.

## Note on Security
The `.env` file containing API keys is strictly excluded from this repository for security reasons. To run this locally, you must create a `.env` file with `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`.
