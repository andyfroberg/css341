import numpy
import matplotlib.pyplot as plt

def convert_date_to_float(date_str):
    """Converts a date string into a float.
    
    This function converts a string representing a specific date into a floating
    point number. The date string should follow the format yyyy-mm-dd, for
    example, 1950-04-26 would indicate the date of April 26, 1950.
    
    Positional Input Parameters:
        date_str | string:
            A string which represents a specific date. Should be in the format
            yyyy-mm-dd (e.g. 1950-04-26 should represent April 26, 1950).
            
    Returns:
        date | float:
            The floating point representation of the input date string. Should
            follow the same general format as the string, but with no hyphens,
            and with a .0 after the date (floating point representation). An
            example return for April 26, 1950 would be 19500426.0. 
    """
    return float(date_str.split("-")[0] + date_str.split("-")[1] + 
        date_str.split("-")[2])
       
def correlation(x, y):
    """Calculates and prints the correlation between stock index lists.
    
    This function calculates and prints the correlation between two input lists
    (of stock indices). Calculation for lag correlation is as follows (square
    brackets are for mathematical clarity and do not denote array syntax or
    any other programming data structures):
        
        r_xy = [cov(x,y)] / [stddev(x) * stdev(y)]
             = [sum i=1 to n ((x_i - x_bar) (y_i - y_bar))]
               / [sqrt(sum i=1 to n (x_i - x_bar)^2 
               * sum i=1 to n (y_i - y_bar)^2)] 
    
    Postitional Input Parameters:
        x | list (float):
            A list of stock index prices. Assumed to be floats.
        y | list (float):
            A list of stock index prices. Assumed to be floats.
        
    Returns:
        correlation | float:
            The correlation coefficient of two input stock indices.
    """
    if len(x) == len(y):
        x_tot = 0.0
        y_tot = 0.0
        for i in range(len(x)):
            x_tot += x[i]
            y_tot += y[i]
        x_bar = x_tot / len(x)
        y_bar = y_tot / len(y)
        covariance = 0.0
        for i in range(len(x)):
            covariance += (x[i] - x_bar) * (y[i] - y_bar)
        x_var = 0.0
        y_var = 0.0
        for i in range(len(x)):
            x_var += (x[i] - x_bar)**2
            y_var += (y[i] - y_bar)**2
        x_sig = x_var**(0.5)
        y_sig = y_var**(0.5)
        return covariance / (x_sig * y_sig)
    else:
        raise ValueError, 'Lists must be the same length'
        
def autocorrelation(x, lag):
    """Calculates lag autocorrelation of a given stock index (given some lag).
    
    This function calculates the lag autocorrelation of a given stock index, 
    given some lag (in days). 
    
    Positional Input Parameters:
        x | list (float):
            A list of stock index prices. Assumed to be floats.
        lag | int:
            the lag (in days) used to measure the lag autocorrelation of a given
            stock index. Only positive lags are considered (e.g. f(t) vs 
            f(t+lag)).
    
    Returns:
        correlation | float:
            The lag autocorrelation of a given stock index, given some lag.   
    """
    if lag > len(x):
        raise ValueError, 'Lag must be less than the length of the input array'    
    x_array = numpy.array(x, dtype='f')
    if lag == 0:
        return correlation(x_array, x_array)
    else:
        return correlation(x_array[:-1*lag], x_array[lag:])

# Read in the contents of stock index data file
fileobj = open('table.csv', 'r')
stock_data = []

# Iterate through the csv file, and add each value between the commas to a list
for iline in fileobj:
    stock_data.append(iline.split(","))

# Convert all of the strings in stock_data to floats         
for i in range(1, len(stock_data)): #  Exclude the header line
    stock_data[i][0] = convert_date_to_float(stock_data[i][0])
    for j in range(1, len(stock_data[i])):
        stock_data[i][j] = float(stock_data[i][j])

# Build the array
stock_data = numpy.array(stock_data[1:], dtype='f')
data2 = numpy.flipud(stock_data)

# ~~~~~~~~~~~~~~~~~~~~~ Graphical Analysis ~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Plot 1
plt.figure("Adjusted Close vs. Trading Day")
plt.plot(range(len(data2)), data2[:,6], 'b-o', markersize='1', linewidth='1', 
    markeredgecolor='b', label='Adj. Close') # use range so we don't get 
                                             # sci-notation on x-axis
plt.axis([0, 4023, 0, 2500])
plt.xlabel('days since Dec. 7, 2000')
plt.ylabel('Adjusted Closing Price ($ USD)')
plt.title("Adjusted Closing Price of S&P500")
plt.legend(loc='upper left')
plt.savefig('adj_close.png', dpi=300)

# Plot 2
plt.figure("Net Daily Gain/Loss")
plt.plot(range(len(data2)), data2[:,6] - data2[:,1], 'g-o', # Use of array syntax 
    markersize='1', linewidth='1', markeredgecolor='b', 
    label='Net Gain/Loss') # use range so we don't get sci-notation on x-axis
plt.axis([0, 4023, -120, 120])
plt.xlabel('days since Dec. 7, 2000')
plt.ylabel('Adjusted Closing Price - Open Price ($ USD)')
plt.title("Net Daily Gain/Loss of S&P500")
plt.legend(loc='upper left')
plt.savefig('gain_loss.png', dpi=300)

# Plot 3
lag_autocorr_days = range(14)
sp500_autocorr = []
for i in range(len(lag_autocorr_days)):
    sp500_autocorr.append(autocorrelation(data2[4000:,6], i))
# Plot the lag autocorrelation of S&P500
plt.figure("Lag Autocorrelation of S&P500")
plt.plot(lag_autocorr_days, sp500_autocorr, 'g-o',
    markersize='4', linewidth='3', markeredgecolor='g',
    label='S&P500')
plt.axis([0, 13, 0.25, 1.05])
plt.xlabel('Lag (Days)')
plt.ylabel('Correlation Coefficient')
plt.title("Lag Autocorrelation of S&P500")
plt.legend(loc='lower left')
plt.savefig('lag_autocorr.png', dpi=300)
plt.show()

# ~~~~~~~~~~~~~~~~~~~~~ Non-Graphical Analysis ~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# Calculate the mean of the data set (Adj. Close)
total = 0.0
for i in range(numpy.shape(data2)[0]):
    total += data2[i,6]
mean = total / float(numpy.shape(data2)[0])    
print("The mean (adj. close) of the data set is: " + str(mean))

# Calculate number of days S&P 500 has been over $2,000 (Adj. Close) since
# Dec. 7, 2000.
tot_days = 0
for i in range(numpy.shape(data2)[0]):
    if data2[i,6] >= 2000.0:
        tot_days += 1    
print("\nThe number of days S&P 500 has been over \n$2,000 (Adj. Close)" \
    + "since Dec. 7, 2000 is: " + str(tot_days))

# Calculate the highest and lowest values the S&P500 has had since Dec. 7, 2000
high = data2[0,2]
low = data2[0,3]
for i in range(numpy.shape(data2)[0]):
    if data2[i,2] > high:
        high = data2[i,2]
    if data2[i,3] < low:
        low = data2[i,3]
print("\nThe highest price the S&P500 has been \nsince Dec. 7, 2000 is: " + \
    str(high))
print("\nThe lowest price the S&P500 has been \nsince Dec. 7, 2000 is: " + \
    str(low))
    
# ~~~~~~~~~~~~~~~~~~~~~ Further Analysis ~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# For my dataset analysis project, I used the the last seventeen years of S&P500 
# stock index, from December 7, 2000 to December 6, 2016. My graphical analysis
# has shown (Plot 1) that despite some major world changing events (e.g. 9/11
# which is shown about 300 trading days into the graph) that the economy is 
# resilient and has bounced back to an adjusted close price of over $2,200 (as
# of today). After the 2008 financial crisis, the S&P500 saw a significant
# decrease in value, and reached a low of just $666.79 on March 6, 2009. Given
# a lag of 7 days, the S&P500 stock index (toward the end of the time series)
# is still somewhat correlated (about 0.7) and then drops significantly as the
# lag increases past 7 days. Overall the S&P500 data set is quite diverse, and
# that is why I believe it was a good choice.   
  