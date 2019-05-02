import math
""" 
for x in range(5):
    for y in range(5):
        print(f"({x}, {y})")
    if x == 3:
        break

print(int(math.degrees(25)), "Math methods")
print(math.exp(10), "exponent to e")
print(math.gcd(158, 79), "GCD")

cond = ""

if cond:
    message = "Lamda"
else:
    mess = "AWS"
print(mess)

 """


def fizzbuzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizz-buzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"

    return input


print(fizzbuzz(7))
