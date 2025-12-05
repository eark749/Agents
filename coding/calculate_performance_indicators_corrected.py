# filename: calculate_performance_indicators_corrected.py
import yfinance as yf
import pandas as pd

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

# Closing prices
closing_prices = nvda_data['Close']

# Performance Indicators:
# Percentage Change
first_day = pd.Timestamp("2024-03-25")
last_day = pd.Timestamp("2024-04-23")
percentage_change = ((closing_prices.loc[last_day] - closing_prices.loc[first_day]) / closing_prices.loc[first_day]) * 100
# Highest Price
highest_price = closing_prices.max()
# Lowest Price
lowest_price = closing_prices.min()
# Average Price
average_price = closing_prices.mean()

# Print the calculated performance metrics
print(f"Performance of NVIDIA (NVDA) from March 25, 2024 to April 23, 2024:")
print(f"Percentage Change: {percentage_change:.2f}%")
print(f"Highest Closing Price: ${highest_price:.2f}")
print(f"Lowest Closing Price: ${lowest_price:.2f}")
print(f"Average Closing Price: ${average_price:.2f}")