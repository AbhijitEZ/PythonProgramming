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
