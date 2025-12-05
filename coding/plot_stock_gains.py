# filename: plot_stock_gains.py
import yfinance as yf
import matplotlib.pyplot as plt

# Define the tickers
tickers = ['NVDA', 'TSLA']

# Set the start and end dates for YTD
start_date = '2025-01-01'
end_date = '2025-12-05'

# Download stock data focusing only on the "Close" prices
data = yf.download(tickers, start=start_date, end=end_date)['Close']

# Calculate YTD gains in percentage
ytd_gain = ((data / data.iloc[0]) - 1) * 100

# Plot the YTD gains
plt.figure(figsize=(10, 6))
ytd_gain.plot()
plt.title('YTD Stock Gains for NVDA and TSLA')
plt.ylabel('Percentage Gain (%)')
plt.xlabel('Date')
plt.grid(True)
plt.legend(title='Ticker')

# Save the plot to a PNG file and do not show it in a window
plt.savefig('ytd_stock_gains.png')
plt.close()  # Explicitly close the plot to avoid showing it and confusion