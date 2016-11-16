import stocks
import numpy
import matplotlib.pyplot as plt 
# 1
# Calculates and prints out the correlation between each combination of the 
# three indices, e.g., between nasdaq and sp500, nasdaq and djia, and sp500 and 
# djia. This calculation cannot make use of any pre-written calculation 
# functions from SciPy, NumPy, matplotlib, pandas, etc. (You can, however, use 
# functions like shape, ravel, etc.) That is to say, you have to write your own 
# mean, standard deviation, covariance, etc. functions (if you choose to use 
# them) in the .py file.  (If you don't import scipy, etc., you'll be fine.)  
# Note that if you do this task by writing a correlation calculating function, 
# it will help you do #2 below.
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

# Print the three correlation between combinations of indices
# Correlation between Nasdaq and S&P500
print("Correlation beween stock indices: \n" + "r(x,y) = r(nasdaq, sp500) = "
    + str(correlation(stocks.nasdaq, stocks.sp500)))
# Correlation between Nasdaq and DJIA
print("r(x,y) = r(nasdaq, djia) = " + str(correlation(stocks.nasdaq, stocks.djia)))
# Correlation between S&P500 and DJIA
print("r(x,y) = r(sp500, djia) = " + str(correlation(stocks.sp500, stocks.djia))) 

# test with numpy correlate function
print("\nTest accuracy using Numpy corrcoeff function: \n" + "r(x,y) = " + 
    "r(nasdaq, sp500) = " + str(numpy.corrcoef(stocks.nasdaq, stocks.sp500)[0,1]))   
print("r(x,y) = r(nasdaq, djia) = " + 
    str(numpy.corrcoef(stocks.nasdaq, stocks.djia)[0,1]))
print("r(x,y) = r(sp500, djia) = " 
    + str(numpy.corrcoef(stocks.sp500, stocks.djia)[0,1])) 
# 2
# Calculates the lag autocorrelation for each of the three indices. You can 
# consider only positive lags if you're correlating f(t) vs. f(t+lag), where f 
# is the NASDAQ, S&P500, or DJIA index.  Again, you cannot use calculation 
# functions you have not written yourself. (You can, however, use functions 
# like shape, ravel, etc.)
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

# 3
# Plots each lag autocorrelation out on a single figure. The y-axis of the graph 
# should be the correlation coefficient and the x-axis should be lag in number 
# of days. You may use matplotlib functions for this section. 
# Build the autocorrelation measurement lists
# Note: Autocorrelation plot takes measurements in 1 day increments.
lag_autocorr_days = range(14)
nasdaq_autocorr = []
sp500_autocorr = []
djia_autocorr = []
for i in range(len(lag_autocorr_days)):
    nasdaq_autocorr.append(autocorrelation(stocks.nasdaq, i))
    sp500_autocorr.append(autocorrelation(stocks.sp500, i))
    djia_autocorr.append(autocorrelation(stocks.djia, i))

# Plot the lag autocorrelations
plt.figure("Lag Autocorrelation of Stock Indices")
plt.plot(lag_autocorr_days, nasdaq_autocorr, 'r-o', 
    markersize='4', linewidth='3', markeredgecolor='r',
    label='NASDAQ')
plt.plot(lag_autocorr_days, sp500_autocorr, 'g-o',
    markersize='4', linewidth='3', markeredgecolor='g',
    label='S&P500')
plt.plot(lag_autocorr_days, djia_autocorr, 'b-o',
    markersize='4', linewidth='3', markeredgecolor='b',
    label='DJIA')
plt.axis([0, 13, 0.25, 1.05])
plt.xlabel('Lag (Days)')
plt.ylabel('Correlation Coefficient')
plt.title("Lag Autocorrelation of Stock Indices")
plt.legend(loc='lower left')
plt.savefig('lag_autocorr.png', dpi=300)
plt.show()

# 4
# Describe what the plot tells you. (You do not have to be "right" about what 
# the plot says, just not "wrong." That is, if you claim the plot says something 
# and it says the opposite of that, that's "wrong." If you say the plot says 
# something and it might say that or might not, that's okay.) I mainly want you 
# to try and interpret the plot.

# Given a lag of 0, all three stock indices have a lag autocorrelation 
# coefficient of 1.0. This is to be expected, because the correlation function 
# is comparing two identical timeseries, so they should be perfectly correlated. 
# As the lag increases, each respective autocorrelation becomes less correlated. 
# This also makes sense, because we would expect that closing prices far into 
# the future would have less of a relationship with closing prices today 
# (unless there were an unforseen event that suddenly made the stock market 
# closing prices remain flat for a long period of time, which is unlikely). In 
# just two weeks, the lag autocorrelation between each respective stock index 
# drops to around 0.5 or below, indicating that (given our current data set) the 
# closing prices of a given stock index today become a relatively poor indicator 
# of stock index prices just two weeks in the future.
    
    
    
    
    
    
    
