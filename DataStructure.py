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
