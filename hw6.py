import numpy
from scipy import genfromtxt
import matplotlib.pyplot as plt

# 1
# Write a function convert_date_to_float that takes a string of the format 
# yyyy-mm-dd and converts it to a floating point number. Thus, '19500131' as 
# input results in a return value of 19500131.0
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
        

# 2
# Reads the contents of the data file into an array data2 without using 
# genfromtxt or any other pre-written file-reading function. Thus, you have to 
# create a file object, use string methods, etc.  Make the first column be 
# yyyy-mm-dd as a floating point number.  You can use the function you wrote 
# for #1 to do this.  For this task, you do not have to write a function.
fileobj = open('sp500_1950-01-03_to_2016-10-07.csv', 'r')
data2 = []

# Iterate through the csv file, and add each value between the commas to a list
for iline in fileobj:
    data2.append(iline.split(","))

# Convert all of the strings in data2 to floats         
for i in range(1, len(data2)): #  Exclude the header line
    data2[i][0] = convert_date_to_float(data2[i][0])
    for j in range(1, len(data2[i])):
        data2[i][j] = float(data2[i][j])

# Build the array
data2 = numpy.array(data2[1:], dtype='f')

# Test
print("data2 shape: " + str(numpy.shape(data2)))

# 3
# Reads the contents of the data file into an array data3 using genfromtxt. 
# Using what we've covered in this class, the first column of the array this 
# call to genfromtxt returns will be filled with "nan"s (i.e., "not-a-number" 
# values). That's okay.  For this task, you do not have to write a function.
data3 = genfromtxt('sp500_1950-01-03_to_2016-10-07.csv', skip_header=1, 
    skip_footer=0, dtype='f', delimiter=',')
   
# Test
print("data3 shape: " + str(numpy.shape(data3)) + '\n')

# 4
# Compare all values (except the first column) in data2 and data3 to confirm 
# they are "equal" to each other. Since they're all floating point values, 
# you're checking that they are "close" to each other. Hint: There's a function 
# in NumPy called allclose that will help here.  For this task, you do not have 
# to write a function.
print("All values in data2 & data3 are 'equal': " + 
    str(numpy.allclose(data2[:,1:], data3[:,1:])))

# 5
# Create an x-y plot of the adjusted close (y-axis) versus trading day (x-axis). 
# You don't need to plot a date on the x-axis; "days since Jan 3, 1950" would be 
# fine.  For this task, you do not have to write a function.
plt.figure("Adjusted close vs. trading day")
plt.plot(range(len(data2)), data2[:,6], 'b-o', markersize='1', linewidth='1', 
    markeredgecolor='b', label='Adj. Close') # use range so we don't get 
                                             # sci-notation on x-axis
plt.axis([0, 16801, 0, 2500])
plt.xlabel('days since Jan 3, 1950')
plt.ylabel('Adjusted Closing Price ($ USD)')
plt.title("Adjusted Closing Price of S&P500")
plt.legend(loc='upper left')
plt.savefig('adj_close.png', dpi=300)

# 6
# Create an x-y plot of the difference between the high and low value for the 
# day (y-axis) versus trading day (x-axis). You don't need to plot a date on the 
# x-axis; "days since Jan 3, 1950" would be fine.  For this task, you do not 
# have to write a function.
plt.figure("Difference in High and Low Stock Values")
plt.plot(range(len(data2)), data2[:,2] - data2[:,3], 'g-o', markersize='1', 
    linewidth='1', markeredgecolor='g', label='High - Low')
plt.axis([0, 16801, 0, 120])
plt.xlabel('days since Jan 3, 1950')
plt.ylabel('High - Low ($ USD)')
plt.title("Difference in High and Low Stock Values")
plt.legend(loc='upper left')
plt.savefig('HighLow.png', dpi=300)
plt.show()