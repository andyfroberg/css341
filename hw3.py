import stocks
import numpy

# 1
# Create a NumPy array from the Nasdaq list from stocks.py. Do the same with
# the other three lists from stocks.py. Thus, at the end of this task, you will
# have fourn NumPy arrays.
def create_array(a_list):
    """Creates a NumPy array from a given list.
    
    This function creates an array from a given list using the NumPy module and
    returns the list.
    
    Arguments:
        a_list | list of floats, list of ints:
            A list of either floats or ints given (e.g. stocks.nasdaq, or 
            stocks.trading_days)
     
    Returns:  
        the_array | an array:
            Returns a NumPy array created from the input list.
    
    """
    the_array = numpy.array(a_list)
    return the_array

# Build the four arrays.
nasdaq_array = create_array(stocks.nasdaq)
sp500_array = create_array(stocks.sp500)
djia_array = create_array(stocks.djia)
trading_days_array = create_array(stocks.trading_days)

# 2
# Print out the type of each array in # 1 and the data typecode of the elements
# in each array in # 1. Use 8 print statements (no looping needed).
print("#2\nArray Type:\nNasdaq:\t\t" + str(type(nasdaq_array)))
print("S&P 500:\t" + str(type(sp500_array)))
print("Dow Jones:\t" + str(type(djia_array)))
print("Trading Days:\t" + str(type(trading_days_array)))
print("\nData Typecode: \n(d = double precision floating, f = single precision" +
    "floating, i = short integer,\nl = long integer)\nNasdaq:\t\t" 
    + str(nasdaq_array.dtype.char))
print("S&P 500:\t" + str(sp500_array.dtype.char))
print("Dow Jones:\t" + str(djia_array.dtype.char))
print("Trading Days:\t" + str(trading_days_array.dtype.char))

# 3
# Print out the shape of each array in # 1
print("\n#3\nShape of each array:\nNasdaq:\t\t" + str(numpy.shape(nasdaq_array)))
print("S&P 500:\t" + str(numpy.shape(sp500_array)))
print("Dow Jones:\t" + str(numpy.shape(djia_array)))
print("Trading Days:\t" + str(numpy.shape(trading_days_array)))

# 4 
# Print out whether the sizes of each of the four arrays in # 1 are the same.
print("\n#4\nThe sizes of each of the four arrays in #1 the same: " +
    str(numpy.size(nasdaq_array) == numpy.size(sp500_array) ==
    numpy.size(djia_array) == numpy.size(trading_days_array)))

# 5
# Creates a single 2-D array where the first column is the Nasdaq array, the 
# second column is the S&P 500 array, and the third column is the DJIA array.
indices_as_columns = numpy.zeros((65,3), dtype='d')
for i in range(len(nasdaq_array)):
    indices_as_columns[i][0] = nasdaq_array[i]
    indices_as_columns[i][1] = sp500_array[i]
    indices_as_columns[i][2] = djia_array[i]
# Make sure the output is in the correct rows/columns
print("\n#5\nThe indices represented as columns\nNASDAQ\t\tS&P500" + 
    "\t\tDow Jones\n" + str(indices_as_columns))

# 6
# From the 2-D array in #5, extract the 2-D sub-array that consists of trading
# days 21 to 39 of the S&P 500 column and DJIA columns. Then print the shape
# of this extracted sub-array.
sub_array = indices_as_columns[20:39,1:]
print("\n#6\nShape of sub-array: " + str(numpy.shape(sub_array)))