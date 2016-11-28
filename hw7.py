import csv
import os.walk

# 1
# Write a function list_files_walk that returns a list of the paths of all the 
# parts.txt files, using the os module's walk generator. The function takes no 
# input parameters. Part of the output would look like this:
#     CarItems/Chevrolet/Chevelle/2011/parts.txt
#     CarItems/Chevrolet/Chevelle/1982/parts.txt
#     CarItems/Chevrolet/Volt/1994/parts.txt
#     CarItems/Chevrolet/Volt/1999/parts.txt
# if I printed each element of the output list on one line at a time. In the 
# above example, the current working directory from which I called the function 
# was the parent directory of CarItems.
def list_files_walk():
    """Returns a list of the paths of all the parts.txt files.
    
    This function returns a list of the paths of all the parts.txt files.
    
    Postitional Input Parameters:
        none
        
    Returns:
        paths | list:
            The paths of all the parts.txt files.
    """

        
# 2
# Write a function list_files_recursive that returns a list of the paths of all 
# the parts.txt files without using the os module's walk generator. Instead, the 
# function should use recursion. The input will be a directory name and the 
# output should be the same as the output in Task #1 above.
def list_files_recursive():
    """Returns a list of the paths of all the parts.txt files.
    
    This function returns a list of the paths of all the parts.txt files, using
    recursion.
    
    Postitional Input Parameters:
        none
        
    Returns:
        paths | list:
            The paths of all the parts.txt files.
    
    """


# 3
# Make calls to list_files_walk and list_files_recursive and compare whether the 
# output is the same. Print to screen the result as to whether or not both calls 
# return the same list.  (The result should be True.)
# test
print(list_files_walk())
print(list_files_recursive())

# 4
# Create a copy of the CarItems tree called CarItemsCopy where all files, 
# instead of being in directories named after years, rather have the year as 
# part of the filename, and the year directories are entirely absent.  That is, 
# when you're done, the CarItems directory tree will look like: (image omitted)
# Do this using Python (you can't create the copy by manually rearranging 
# things).  You may use the os module's walk generator. Hint: You might find the 
# os.path module's split function to be helpful. You don't have to use it though.