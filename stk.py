import yfinance as yf
from datetime import datetime

def get_stock_price(symbol):
    # Fetch stock data
    stock = yf.Ticker(symbol + ".NS")
    stock_info = stock.info

    # Extract the market status and appropriate price
    market_open = stock_info.get('regularMarketOpen')
    regular_market_price = stock_info.get('regularMarketPrice')
    previous_close = stock_info.get('previousClose')

    # Check if the market is open (NSE trading hours are typically 9:15 AM to 3:30 PM IST)
    current_time = datetime.now().time()
    market_open_time = datetime.strptime("09:15", "%H:%M").time()
    market_close_time = datetime.strptime("15:30", "%H:%M").time()

    if market_open_time <= current_time <= market_close_time and market_open is not None:
        return f"Market is open. Real-time price of {symbol.upper()}: {regular_market_price}"
    else:
        return f"Market is closed. Last closing price of {symbol.upper()}: {previous_close}"

def main():
    # Prompt the user to enter stock symbols separated by commas
    stock_symbols = input("Enter the stock symbols separated by commas: ").strip().upper().split(',')

    # Get and print the stock prices for the entered symbols
    for symbol in stock_symbols:
        symbol = symbol.strip()
        if symbol:
            print(get_stock_price(symbol))

if __name__ == "__main__":
    main()
