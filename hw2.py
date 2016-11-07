import stocks
import scipy
import matplotlib.pyplot as plt
import copy

# 1  
def percent_of_mean(stock_index_list):
    """Calculates the daily value as a percent of the mean.
    
    This function calculates the daily value of each stock index
    as a percent of the mean value for the stock index over period
    in the list.
    
    Args:
        stock_index_list - the list of a given stock index
        
    Returns:
        The list of stock index values as a percent of the mean
    
    """
    daily_values = []
    for idata in stock_index_list:
        daily_values.append((idata/scipy.mean(stock_index_list))
            * 100)
    return daily_values
# TEST
print(percent_of_mean(stocks.nasdaq))
print(stocks.nasdaq[5]/scipy.mean(stocks.nasdaq))

# 2
# This code makes plots all three stock indices on one figure showing
# the value of each index as a percentage of the mean of that index
# vs. trading day since Jun 1, 2016.
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
plt.show() 

# 3
def num_days_big_percent_chg(index_list, pct):
    """ Calculates the number of days above a given percentage change.
    
    This function calculates and returns the total number of trading
    days where the magnitude of the percent change (+/-) in the index
    is greater than the given percent change.
    
    Args:  
        index_list - the list of a given stock index (from stocks.py)
        pct - the percentage threshold to check the magnatude against
        
    Returns:
        The number of days a given stock index percentage change is greater
        than the percentage given.
        
        """
    days = 0
    if len(index_list) == 0:
        return "Empty list!"
    else:
        # This funtion wants to check the percentage change of a given
        # day in the list vs. the previous day, so it starts with the ith
        # element in the list and divides it by the [ith -1] element.
        # To get the percentage change, we subtract this number from 1,
        # multiply the result by 100, then take the absolute value (in
        # case the number is negative). The function then checks if this 
        # percentage is greater than the percentage given as the second 
        # argument in the function. If so, days is incremented by 1.
        # Note: We assume every element in the index list is a float.
        for i in range(1, len(index_list)):
            if index_list[i-1] == 0:
                return "Division by zero error"
            else:
                if (abs((1 - (index_list[i] / index_list[i-1]))) * 100) > pct:
                    days += 1
        return days
# Test to see if it's working
print(num_days_big_percent_chg(stocks.nasdaq, .02))
 
# 4
def find_occurrences(index_list, magnitudes):
    """Finds the number of occurrences greater than a given pct change.
    
    Find the number of days that the magnitude of the percent change
    (+/-) in the indices is greater than 0.2%, 0.4%, 0.6%, 0.8%, and
    1.0%, respectively. Then make a plot of all three stock indices 
    showing the number of days vs. the percentage threshold.
    
    Precondition:
        Assumes all values in index_list and magnitude are floats.
        
    Args:  
        index_list - the list of a given stock index (from stocks.py)
        magnitude - the list of the threshold magnitudes.
    
    Returns:
        A list of the number of times each percentage change is more 
        than a given set of percentages for a given index.
    
    """
    # Build an array (occurrences) that has an equal number of
    # elements as the magnitude array. This expands the capability
    # of the funtion to allow more than the given 5 magnitudes.
    occurrences = []
    for n in range(len(magnitudes)):
        occurrences.append(0)
    for i in range(1, len(index_list)):
        for j in range(len(occurrences)):
            if index_list[i-1] == 0:
                return "Division by zero error"
            else:
                if (abs((1 - (index_list[i] / index_list[i-1]))) * 100) > magnitudes[j]:
                    occurrences[j] += 1
    return occurrences
 
# Test
print(find_occurrences(stocks.nasdaq, [0.2, 0.4, 0.6, 0.8, 1.0]))
 
# Plot the output
plt.figure("Days Above Threshold")
plt.plot(find_occurrences(stocks.nasdaq, [0.2, 0.4, 0.6, 0.8, 1.0]),
    [0.2, 0.4, 0.6, 0.8, 1.0], 'r-o', 
    markersize='4', linewidth='3', markeredgecolor='r',
    label='NASDAQ')
plt.plot(find_occurrences(stocks.sp500, [0.2, 0.4, 0.6, 0.8, 1.0]), 
    [0.2, 0.4, 0.6, 0.8, 1.0], 'g-o',
    markersize='4', linewidth='3', markeredgecolor='g',
    label='S&P500')
plt.plot(find_occurrences(stocks.djia, [0.2, 0.4, 0.6, 0.8, 1.0]),
    [0.2, 0.4, 0.6, 0.8, 1.0], 'b-o',
    markersize='4', linewidth='3', markeredgecolor='b',
    label='DJIA')
plt.ylabel('Percent threshold value')
plt.xlabel('Number of days exceeding threshold')
plt.title('Days exceeding percent threshold')
plt.legend(loc='lower right')
plt.savefig('days_above_threshold.png', dpi=300)
plt.show()      
                
# 5
def ascending_trading_days(trading_days, stock_list):
    """Sorts the stock index by trading day in ascending order of value.
    
    This function sorts a stock index list into ascending order (based on the
    daily closing value of the stock) and using a selection sort algorithm. 
    The function then creates a second list (whose indices represent the number
    of trading days since June 1, 2016) and returns the list.
    
    Precondition:
        Assumes all values in trading_days and index_list floats.
        
    Args:
        trading_days - the number of days since June 1, 2016 in any given
            stock index
        stock_list - the list of the daily closing values of a given stock index
        
    Returns:
        The list of trading days in ascending order by value.
    
    
    """
    ascending_price_indices = copy.deepcopy(trading_days)
    for i in range(len(stock_list) - 1):
        min_index = i
        for j in range(i + 1, len(stock_list)):
            if stock_list[j] < stock_list[min_index]:
                min_index = j
        if min_index != i:
            temp = ascending_price_indices[i]
            ascending_price_indices[i] = ascending_price_indices[min_index]
            ascending_price_indices[min_index] = temp
    return ascending_price_indices

# TEST
print(ascending_trading_days(stocks.trading_days, stocks.nasdaq))

# 6
# This code prints the five highest trading day values using the 
# ascending_trading_days function defined above
def five_highest(stock_index):
    """Finds the five highest stock index values using ascending_trading_days
    
    This function finds and returns the five highest value trading days
    in a given stock index using the ascending_trading_days function.
    
    Precondition:
        The values in the list stock_index is a float.
    
    Args:
        stock_index - the list of a given stock index.
        
    Returns:
        A list of the five highest value trading days.
        
    """
    index_list = ascending_trading_days(stocks.trading_days, stock_index)
    five_highest = []
    for idata in index_list[60:]: 
        five_highest.append(idata)
    return five_highest
# Print the output
print(five_highest(stocks.nasdaq))
print(five_highest(stocks.sp500))
print(five_highest(stocks.djia))