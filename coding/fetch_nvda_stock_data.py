# filename: fetch_nvda_stock_data.py
import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    # Fetch the historical data for the stock
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Define the ticker symbol and the date range
ticker_symbol = "NVDA"
start_date = "2024-03-23"
end_date = "2024-04-24"  # Include one day after to ensure we capture April 23 data

# Fetch the stock data
nvda_data = fetch_stock_data(ticker_symbol, start_date, end_date)

# Print the closing prices
print("Closing Prices for NVIDIA (NVDA) from March 23, 2024 to April 23, 2024:")
print(nvda_data['Close'])
