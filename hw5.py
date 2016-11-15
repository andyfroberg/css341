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
        x = numpy.array(x, dtype='f') # make sure input is array
        y = numpy.array(y, dtype='f')
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

# test with numpy correlate function
print(numpy.corrcoef(stocks.nasdaq, stocks.sp500)[0,1])

# Print the three correlation between combinations of indices
# Correlation between Nasdaq and S&P500
print(correlation(stocks.nasdaq, stocks.sp500))
# Correlation between Nasdaq and DJIA
print(correlation(stocks.nasdaq, stocks.djia))
# Correlation between S&P500 and DJIA
print(correlation(stocks.sp500, stocks.djia))    

# 2
# Calculates the lag autocorrelation for each of the three indices. You can 
# consider only positive lags if you're correlating f(t) vs. f(t+lag), where f 
# is the NASDAQ, S&P500, or DJIA index.  Again, you cannot use calculation 
# functions you have not written yourself. (You can, however, use functions 
# like shape, ravel, etc.)
def autocorrelation(x, lag):
    """Calculates the lag autocorrelation of a given stock index (given some lag).
    
    This function calculates the lag autocorrelation 
    
    """
    if lag > len(x):
        raise ValueError, 'Lag must be less than the length of the input array'    
    x_array = numpy.array(x, dtype='f')
    y_array = numpy.array(x, dtype='f')
    if lag == 0:
        return correlation(x_array, y_array)
    else:
        return correlation(x_array[:-1*lag], x_array[lag:])

# Test
print(autocorrelation(stocks.nasdaq, 3))
print(autocorrelation(stocks.sp500, 5))  

# 3
# Plots each lag autocorrelation out on a single figure. The y-axis of the graph 
# should be the correlation coefficient and the x-axis should be lag in number 
# of days. You may use matplotlib functions for this section. 
plt.figure("Lag Autocorrelation of Stock Indices")
plt.plot(lag_corr_days, autocorrelation(stocks.nasdaq), 'r-o', 
    markersize='4', linewidth='3', markeredgecolor='r',
    label='NASDAQ')
plt.plot(lag_corr_days, autocorrelation(stocks.sp500), 'g-o',
    markersize='4', linewidth='3', markeredgecolor='g',
    label='S&P500')
plt.plot(lag_corr_days, autocorrelation(stocks.djia), 'b-o',
    markersize='4', linewidth='3', markeredgecolor='b',
    label='DJIA')
plt.xlabel('Lag (Days)')
plt.ylabel('Correlation Coefficient')
plt.title("Lag Autocorrelation of Stock Indices")
plt.legend(loc='lower right')
plt.savefig('lag_autocorr.png', dpi=300)

# 4
# Describe what the plot tells you. (You do not have to be "right" about what 
# the plot says, just not "wrong." That is, if you claim the plot says something 
# and it says the opposite of that, that's "wrong." If you say the plot says 
# something and it might say that or might not, that's okay.) I mainly want you 
# to try and interpret the plot.
