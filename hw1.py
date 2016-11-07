import stocks
import matplotlib.pyplot as plt
from scipy import mean, std

# Calculate the mean, std dev, and
# std dev / mean for Nasdaq, S&P 500,
# and Dow Jones Industrial Average
nasdaq_mean = mean(stocks.nasdaq)
nasdaq_std = std(stocks.nasdaq)
nasdaq_ratio = nasdaq_std / nasdaq_mean
sp500_mean = mean(stocks.sp500)
sp500_std = std(stocks.sp500)
sp500_ratio = sp500_std / sp500_mean
djia_mean = mean(stocks.djia)
djia_std = std(stocks.djia)
djia_ratio = djia_std / djia_mean

# Print the data with appropriate labels
output_str = "Stock data from June 1 to Aug 31 2016" + \
  "\n\nMean Closing Price\nNasdaq: " + str(nasdaq_mean) + \
  "\nS&P 500: " + str(sp500_mean) + "\nDJIA: " + \
  str(djia_mean) + "\n\nClosing Price Standard Deviation" + \
  "\nNasdaq: " + str(nasdaq_std) + "\nS&P 500: " + \
  str(sp500_std) + "\nDJIA: " + str(djia_std) + \
  "\n\nStandard Deviation as a Fraction of the Mean" + \
  "\nNasdaq: " + str(nasdaq_ratio) + "\nS&P 500: " + \
  str(sp500_ratio) + "\nDJIA: " + str(djia_ratio) + \
  "\n\nPlease see graphs for further analysis"
print(output_str)

# Plot the timeseries of each index on a  separate figure
# Nasdaq plot
plt.figure(0)
plt.plot(stocks.trading_days, stocks.nasdaq, 'r-o',
  markersize='4', linewidth='3', markeredgecolor='r')
plt.xlabel('Trading Days since June 1, 2016 (Day 0)')
plt.ylabel('Closing price ($ USD)')
plt.title('Nasdaq Closing Price from 6/1/16 to 8/31/16')
plt.show(0)

# Standard & Poor's 500 plot
plt.figure(1)
plt.plot(stocks.trading_days, stocks.sp500, 'g-o',
  markersize='4', linewidth='3', markeredgecolor='g')
plt.xlabel('Trading Days since June 1, 2016 (Day 0)')
plt.ylabel('Closing price ($ USD)')
plt.title('S&P 500 Closing Price from 6/1/16 to 8/31/16')
plt.show(1)

# Dow Jones Industrial Average plot
plt.figure(2)
plt.plot(stocks.trading_days, stocks.djia, 'b-o',
  markersize='4', linewidth='3', markeredgecolor='b')
plt.xlabel('Trading Days since June 1, 2016 (Day 0)')
plt.ylabel('Closing price ($ USD)')
plt.title('Dow Jones Closing Price from 6/1/16 to' +
  ' 8/31/16')
plt.show(2)

# Plot all three indices together
plt.figure(3)
plt.plot(stocks.trading_days, stocks.nasdaq, 'r-o',
  markersize='4', linewidth='3', markeredgecolor='r',
  label="Nasdaq")
plt.plot(stocks.trading_days, stocks.sp500, 'g-o',
  markersize='4', linewidth='3', markeredgecolor='g',
  label="S&P500")
plt.plot(stocks.trading_days, stocks.djia, 'b-o',
  markersize='4', linewidth='3', markeredgecolor='b',
  label="Dow Jones")
plt.xlabel('Trading Days since June 1, 2016 (Day 0)')
plt.ylabel('Closing price ($ USD)')
plt.legend(loc='center right')
plt.title("Closing Prices of stock indices from 6/1/16" +
  " to 8/31/16")
plt.show(3)
