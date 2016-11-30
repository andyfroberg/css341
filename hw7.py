import os
import shutil

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
    #for dirpath in os.walk("CarItems"):
    #    #if os.path.isfile(dirpath.split("/")[-1]):
    #    print(str(dirpath))
    paths = []
    for dirpath, dirnames, filenames in os.walk("CarItems"):
        for ifile in filenames:
            if "parts" in ifile: # only add parts files
                paths.append(os.path.join(dirpath, ifile))
    return paths

# Output the items in the list
#print("\nList files using os.walk() function:")
#parts_list = list_files_walk()
#for i in range(len(parts_list)):
#    print(parts_list[i])
        
# 2
# Write a function list_files_recursive that returns a list of the paths of all 
# the parts.txt files without using the os module's walk generator. Instead, the 
# function should use recursion. The input will be a directory name and the 
# output should be the same as the output in Task #1 above.
def list_files_recursive(top_dir):
    """Returns a list of the paths of all the parts.txt files.
    
    This function returns a list of the paths of all the parts.txt files, using
    recursion.
    
    Postitional Input Parameters:
        none
        
    Returns:
        paths | list:
            The paths of all the parts.txt files.
    """
    dir_contents = os.listdir(top_dir)
    paths = []
    for item in dir_contents:
        item_path = os.path.join(top_dir, item)
        if os.path.isdir(item_path):
            paths += list_files_recursive(item_path)
        else:
            if "parts" in item: # only add parts files
                if os.path.splitext(item)[-1].lower() == '.txt':
                    paths += [item_path]
    return paths
    
# Output the items in the list
#print("\nList files using recursive function:")
#parts_list_recursive = list_files_recursive("CarItems")
#for i in range(len(parts_list_recursive)):
#    print(parts_list_recursive[i])

# 3
# Make calls to list_files_walk and list_files_recursive and compare whether the 
# output is the same. Print to screen the result as to whether or not both calls 
# return the same list.  (The result should be True.)
print("\nCalls to list_files_walk() and list_files_recursive() return the same" 
    " list: " + str(list_files_walk() == list_files_recursive("CarItems")))

# 4
# Create a copy of the CarItems tree called CarItemsCopy where all files, 
# instead of being in directories named after years, rather have the year as 
# part of the filename, and the year directories are entirely absent.  That is, 
# when you're done, the CarItems directory tree will look like: (image omitted)
# Do this using Python (you can't create the copy by manually rearranging 
# things).  You may use the os module's walk generator. Hint: You might find the 
# os.path module's split function to be helpful. You don't have to use it though.
def copy_car_items():
    shutil.copytree("CarItems", "CarItemsCopy")
    for dirpath, dirnames, filenames in os.walk("CarItemsCopy"):
        for ifile in filenames:
            
            # Full filepath
            fullpath = os.path.join(dirpath, ifile)
            pieces = os.path.split(fullpath)
            
            # Add the year to the filename
            filename_with_year = os.path.splitext(pieces[1])[0] + "-" + \
                os.path.split(pieces[0])[1] + \
                os.path.splitext(pieces[1])[1]
            
            # New destination of the parts/accessories files (inside the model
            # folder)
            model_path = os.path.split(dirpath)[0]
            
            # Move the file to the model directory
            shutil.move(os.path.join(dirpath, ifile), 
                os.path.join(model_path, filename_with_year))
            
            if  'parts' not in os.listdir(dirpath) and \
                'accessories' not in os.listdir(dirpath):
                shutil.rmtree()
