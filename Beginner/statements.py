from random import shuffle, randint

if False:
    print('TRUE condition')
elif not False:
    print('Else if condition')
else:
    print('ELSE condition')


for item in [1, 2, 3]:
    print(item)

for item in (3, 4, 5):
    print(item)

# tuple unpacking
for first, second in [(6, 7), (8, 9)]:
    print(f'{first}-{second}')

dict_var = {
    "key": 'Value'
}

for key, value in dict_var.items():
    print(f'{key}_{value}')

for num in range(10):
    print(num)

# unpack the index and values
for index, letter in enumerate('abcde'):
    print(index, letter)

# unpack values to tuples
for items in zip([1, 2, 3, 4], [20, 12, 32, 44]):
    print(items)


my_list = [1, 3, 5, 7]
shuffle(my_list)
print(my_list)

print(randint(1, 100))

# List comprehensive
# need to give the same name for item to work
lettter_com = [letter ** 2 for letter in [1, 2, 3]]
print(lettter_com)

my_list_1 = [x + 2 for x in range(0, 10) if x % 2 == 0]
print(my_list_1)
