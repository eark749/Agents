# filename: stock_price_plot.py

from functions import get_stock_prices, plot_stock_prices

# Define the stock symbols and the date range
stock_symbols = ['NVDA', 'TSLA']
start_date = '2025-01-01'
end_date = '2025-12-05'

# Get the stock prices
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Plot the stock prices and save the result to a file
filename = 'stock_prices_YTD_plot.png'
plot_stock_prices(stock_prices, filename)

print(f"Stock prices from {start_date} to {end_date} for {stock_symbols} have been plotted and saved to {filename}")