""" string index """

first_str = 'Hello world'

first_index = first_str[0]
last_index = first_str[-1]

print('length of the string: ' + str(len(first_str)))  # 11

""" string slicing """

second_str = 'abcdefgh'

# abc -> this says go upto but not including that position.
second_first_substring = second_str[:3]
second_last_substring = second_str[2:]  # cdefgh

print(second_str[3:6])

print(second_str[::2])  # will have step of 2 from first to last charater.

print(second_str[::-1])  # TRICK: will reverse the string

print("z" * 10)  # will multiple the string with n numbers of time

string_method = 'METHODS PASS'

string_method.upper()
print(string_method.split())  # converts to list had the space as delimiter
