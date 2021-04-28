# List is mutable and we can perform indexing ans slicing to it.

my_list = [1, 2, 3, 4]

len(my_list)  # 4

my_list.pop()

my_list.append(5)


# Dictioniary

my_dict = {'key': 'value'}

my_dict.values()

my_dict.items()


# Tuples is immutable -> They won't change after assigning once.
my_tuple = (1, 2, 3, 3)

type(my_tuple)

print(len(my_tuple))

my_tuple.count(3)  # counts the number of freqency of the value

# Sets are the unordered collection of unqiue values.

my_set = set()

# output -> {1} even though its look like dict but in reality its only have unique values.
my_set.add(1)


# None -> This means null you don't have any value to it.

my_none = None
