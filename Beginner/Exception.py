try:
    file = open("app.py")
    age = int(input("Enter your age: "))
    xfact = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("Wrong Input")
    print(ex)
else:
    print("No Exception")
finally:
    file.close()
print("Execution Continues")

print("-------------------------")


def yFactor(age):
    if age <= 0:
        raise ValueError("Age cannot be less than 0")
    return age


try:
    yFactor(-1)
except ValueError as error:
    print(error)
print("Raising the exception")
