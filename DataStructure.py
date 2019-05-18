from pprint import pprint
from array import array
from collections import deque
alpabets = ["a", "b", "c"]
multipy = [0] * 5
combined = multipy + alpabets
print(combined)

iterableObj = list(range(10))
print(iterableObj)

print(alpabets[1:3], "slice part of list")
print(alpabets[::-1], "step")

first, second, *others = multipy
print(first)
print(others)

alpabets.append("d")
alpabets.append("e")
alpabets.insert(0, "-")
alpabets.remove("b")
# del alpabets[0:3]
alpabets.clear()
print(alpabets)

""" letters = [1, 2, 3, 4, 5, 6]
print(letters.count())
for index, letter in enumerate(letters):
    print("Looping the list", index, letter)
 """

items = [
    ("Product1", 10),
    ("Product2", 5),
    ("Product3", 13)
]

""" items.sort(key=lambda item: item[1], reverse=True)
print(items) """

x = map(lambda item: item[1], items)
x = list(x)
print(x)

y = list(filter(lambda item: item[1] >= 10, items))

# List Comprehension -> Used in case of map and filter
y = [item[1] for item in items if item[1] > 10]
print(y)

# making a tuple for the more than one list
list1 = [12, 51, 91]
list2 = [31, 61, 71]

print(list(zip(list1, list2, "abc")))

# Queue DataStructure
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)


# tuple
tu = (1, 2, 3, 4, 'Abhijit')
print(tu)

# array
numbers = array("i", [1, 2, 3, 4])  # passing the typed
print(numbers)

# set -> to remove the duplicate
numbers = [1, 1, 9, 3, 4]
first = set(numbers)
print(first)
second = {5, 1, 6}
third = second | first  # union
third = first & second  # intersection
third = first - second  # differnce
third = first ^ second  # either first or secind but not both

print(third)


# Dictionary
point = {"x": 1, "y": 2}
point = dict(x=12, y=15)
point["y"] = 16
point["b"] = "Hello"


if point.get("a") is None:
    print("No a in the dict")
del point["b"]
print(point)

for key, value in point.items():
    print(key, value)

# inpacking operator -> just like spread in JS
values = [*range(5), *"hello"]
print(values)

# Exerise
""" To find the character which has max count in sentence  """
sentence = "This is the common interview question"
char_seq = {}
for char in sentence:
    if char in char_seq:
        char_seq[char] += 1

    else:
        char_seq[char] = 1

char_seq_sorted = sorted(char_seq.items(), key=lambda kv: kv[1], reverse=True)
print(char_seq_sorted[0])
