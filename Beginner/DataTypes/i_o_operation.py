import os

print(os.getcwd())  # get the working dirctory of the python executable.

current_path = os.path.dirname(__file__)  # current working file directory
print(current_path)

my_file = open(os.getcwd() + '/Resource/myFile.txt')

print(my_file.read())

# second time it empty string because cursor has moved to the end of positon on first read.
print(my_file.read())

my_file.seek(0)  # bring back the cursor to the inital character.
print(my_file.read())

my_file.close()  # should close the file after operation on it is done


"""
with statement is used for exception handling also removes the resource after some time.
There is no need to call file.close() when using with statement. The with statement itself ensures proper acquisition and release of resources
"""
with open(os.getcwd() + '/Resource/myFile.txt') as new_file:
    contents = new_file.read()

print(contents, 'Contents')

with open(os.getcwd() + '/Resource/myAppendFile.txt', 'a') as file:
    file.write('\nAppend Line')
