import stocks
import numpy
import matplotlib.pyplot as plt

# 1
# Write a function called percent_of_mean that accepts one 1-D array of the
# values of an index as input. The function calculates the value of the index 
# for each day as a percent of the mean value over the period covered by the 
# list (you may use the SciPy mean function if you wish).  Do not use loops.
def percent_of_mean(the_array):
    """Calculates the daily value as a percentage of the mean over the index.
    
    This function calculates the value of the index for each day as a percent
    of the mean value over the period covered by the list.
    
    Positional Input Parameters:
        the_array | 1-Dimensional NumPy array:
            An array of daily prices of a specific stock index. Values in the 
            array are assumed to be floats or doubles.
        
    Returns:
        percentages | 1-Dimensional NumPy array:
            An array of daily stock index values as a percentage of the mean
            over the period covered by the input array.
    """
    the_mean = numpy.mean(the_array)
    percentages = numpy.array(the_array, dtype='f')
    return (percentages * 100) / the_mean

# 2
# Make a plot of all three stock indices on one figure showing the value of 
# each index as a percentage of the mean of that index vs. trading day since 
# Jun 1, 2016.  Title the plot and axes and add a legend as appropriate. You 
# may reuse your previous assignment's code to do this task.  I'm asking you 
# to do this again to confirm your function in Task #1 worked correctly.
plt.figure("Percent of Mean")
plt.plot(stocks.trading_days, percent_of_mean(stocks.nasdaq), 'r-o', 
    markersize='4', linewidth='3', markeredgecolor='r',
    label='NASDAQ')
plt.plot(stocks.trading_days, percent_of_mean(stocks.sp500), 'g-o',
    markersize='4', linewidth='3', markeredgecolor='g',
    label='S&P500')
plt.plot(stocks.trading_days, percent_of_mean(stocks.djia), 'b-o',
    markersize='4', linewidth='3', markeredgecolor='b',
    label='DJIA')
plt.xlabel('Trading Days since June 1, 2016 (Day 0)')
plt.ylabel('Closing price as a percentage of the mean (%)')
plt.title("Index prices (as a percentage of the mean from " +
    "June 1 to Aug 31)")
plt.legend(loc='lower right')
plt.savefig('percent_of_mean.png', dpi=300)

# 3
# Write a function called num_days_big_percent_chg that has two inputs: a 
# 1-D array that contains the values of an index and a number that is a percent.
# The function calculates and returns the total number of trading days where 
# the magnitude of the percent change (up or down) in the index since the 
# previous day is greater than the value of the percent input into the function.
# Do not use loops.
def num_days_big_percent_chg(index_list, pct):
    """ Calculates the number of days above a given percentage change.
     
    This function calculates and returns the total number of trading
    days where the magnitude of the percent change (+/-) in the index
    is greater than the given percent change.
     
    Positional Input Parameters:  
        index_list | 1-Dimensional NumPy array:
            An array of daily prices of a specific stock index. Values in the 
            array are assumed to be floats or doubles. 
        pct | float:
            The percentage threshold to check the magnatude against
         
    Returns:
        days | int:
            The number of days a given stock index percentage change is greater
            than the input percentage.
    """
    index_array = numpy.array(index_list) # make sure index_list is array 
    pct_changes = abs(1 - (index_array[1:] / index_array[0:-1])) * 100
    days_indices = numpy.where(pct_changes > pct)
    return numpy.size(days_indices)

# 4
# For each index, calculate the number of days the magnitude of the percent 
# change (up or down) in the index since the previous day is greater than 
# 0.2%, 0.4%, 0.6%, 0.8%, and 1.0%. (It's easier if you put the number of days 
# values you calculated in a list for each of the above percent threshold 
# values.) Make a plot of all three stock indices on one figure showing, for 
# each index, the number of days vs. the percent threshold value.  You may 
# reuse your previous assignment's code to do this task.  I'm asking you to do 
# this again to confirm your function in Task #3 worked correctly.
def find_occurrences(index_list, magnitudes):
    """Finds the number of occurrences greater than a given pct change.
     
    Finds the number of days that the magnitude of the percent change
    (+/-) in the indices is greater than 0.2%, 0.4%, 0.6%, 0.8%, and
    1.0%, respectively. Then make a plot of all three stock indices 
    showing the number of days vs. the percentage threshold.
         
    Positional Input Parameters:  
        index_list | should be 1-Dimensional NumPy array:
            The list of a given stock index (from stocks.py). Is converted into
            the NumPy array index_array.
        magnitude | 1-Dimensional NumPy array:
            The array of the threshold magnitudes.
     
    Returns:
        occurences | 1-Dimensional NumPy array:
            An array of the number of times each percentage change is more 
            than a given set of percentages for a given index.
    """
    # Build an array (occurrences) that has an equal number of
    # elements as the magnitude array. This expands the capability
    # of the funtion to allow more than the given 5 magnitudes.
    index_array = numpy.array(index_list) # make sure it is an array
    mags_array = numpy.array(magnitudes) # make sure it is an array
    occurrences = numpy.zeros(numpy.shape(mags_array), dtype='i')
    pct_changes = abs(1 - (index_array[1:] / index_array[0:-1])) * 100
    for i in range(numpy.size(pct_changes)):
        for j in range(numpy.size(mags_array)):
            if (pct_changes[i] > mags_array[j]):
                occurrences[j] += 1
    return occurrences
  
# Plot the output
plt.figure("Days Above Threshold")
plt.plot([0.2, 0.4, 0.6, 0.8, 1.0], find_occurrences(stocks.nasdaq, 
    [0.2, 0.4, 0.6, 0.8, 1.0]), 'r-o', markersize='4', linewidth='3', 
    markeredgecolor='r', label='NASDAQ')
plt.plot([0.2, 0.4, 0.6, 0.8, 1.0], find_occurrences(stocks.sp500, 
    [0.2, 0.4, 0.6, 0.8, 1.0]), 'g-o', markersize='4', linewidth='3', 
    markeredgecolor='g', label='S&P500')
plt.plot([0.2, 0.4, 0.6, 0.8, 1.0], find_occurrences(stocks.djia, 
    [0.2, 0.4, 0.6, 0.8, 1.0]), 'b-o', markersize='4', linewidth='3', 
    markeredgecolor='b', label='DJIA')
plt.xlabel('Percent threshold value')
plt.ylabel('Number of days exceeding threshold')
plt.title('Days exceeding percent threshold')
plt.legend(loc='upper right')
plt.savefig('days_above_threshold.png', dpi=300)

# 5
# Write a function moving_average that accepts a 1-D array as input and returns
# the three-day simple moving average. For each day of the stock index, you 
# calculate the three-day simple moving average for a day in question by 
# averaging the values of the stock index for the last three days (including 
# the day in question). The function's return value will thus be an array two 
# elements less than the input array. You cannot use a pre-written moving 
# average function, though you may use the NumPy mean function if you wish 
# (though you do not have to). You may use no more than one loop for this task 
# and must make use of array syntax in your solution.
def moving_average(the_array):
    """Calculates the three-day simple moving average of an input array.
    
    Calculates the three-day simple moving average of a given 1-Dimensional
    input array.
    
    Positional Input Parameters:
        the_array | 1-Dimensional NumPy array:
            An array of daily prices of a specific stock index. Values in the 
            array are assumed to be floats or doubles.
    
    Returns:
        occurences | 1-Dimensional NumPy array:
            An array of the three-day simple moving averages. Size of array
            will be two elements less than the input array.
    """
    index_array = numpy.array(the_array) # Make sure the_array is an array
    mov_avg = numpy.zeros(numpy.size(index_array), dtype='f')
    mov_avg = (index_array[2:] + index_array[1:-1] + index_array[0:-2]) / 3.0 
    return mov_avg 
      
# 6
# Make plots of the three-day simple moving average for all three stock indices,
# with each index's curve on separate figures, vs. trading day since Jun 1, 
# 2016.  On each plot, also superimpose the non-moving averaged stock index. 
# Title the plots, axes, and add legends as appropriate. Thus, for this task, 
# you should have three separate plots and each plot should have two curves.
# NASDAQ Moving Avg. Plot
plt.figure("Nasdaq With Moving Average")
plt.plot(stocks.trading_days, stocks.nasdaq, 'r-o', markersize='4', 
    linewidth='3', markeredgecolor='r', label='NASDAQ')
plt.plot(stocks.trading_days[2:], moving_average(stocks.nasdaq),'g-o', 
    markersize='4', linewidth='3', markeredgecolor='g' , label='NASDAQ Mov Avg')
plt.xlabel('Trading Days since June 1, 2016 (Day 0)')
plt.ylabel('Closing price ($ USD)')
plt.title("NASDAQ index and Moving Avg. (3-day SMA)")
plt.legend(loc='lower right')
plt.savefig('NasdaqMA.png', dpi=300)

# S&P500 Moving Avg. Plot
plt.figure("S&P500 With Moving Average")
plt.plot(stocks.trading_days, stocks.sp500, 'r-o', markersize='4', 
    linewidth='3', markeredgecolor='r', label='S&P500')
plt.plot(stocks.trading_days[2:], moving_average(stocks.sp500), 'g-o', 
    markersize='4', linewidth='3', markeredgecolor='g', label='S&P500 Mov Avg')
plt.xlabel('Trading Days since June 1, 2016 (Day 0)')
plt.ylabel('Closing price ($ USD)')
plt.title("S&P500 index and Moving Avg. (3-day SMA)")
plt.legend(loc='lower right')
plt.savefig('SP500MA.png', dpi=300)

# DJIA Moving Avg. Plot
plt.figure("DJIA With Moving Average")
plt.plot(stocks.trading_days, stocks.djia, 'r-o', markersize='4', linewidth='3',
    markeredgecolor='r', label='DJIA')
plt.plot(stocks.trading_days[2:], moving_average(stocks.djia), 'g-o', 
    markersize='4', linewidth='3', markeredgecolor='g', label='DJIA Mov Avg')
plt.xlabel('Trading Days since June 1, 2016 (Day 0)')
plt.ylabel('Closing price ($ USD)')
plt.title("DJIA index and Moving Avg. (3-day SMA)")
plt.legend(loc='lower right')
plt.savefig('DJIAMA.png', dpi=300) 
plt.show()  