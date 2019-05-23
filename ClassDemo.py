class Car:
    default_value = "All remain same"  # static

    def __init__(self, wheels_count=2):
        self.wheels_count = wheels_count  # property

    def __str__(self):
        # default function is when calling print
        return(f"This is default print")

    @classmethod
    def zeroWheel(cls):  # class method, cls points to the class itself
        return cls(0)

    def wheels(self, wheels_count):  # method
        self.wheels_count = wheels_count
        print(f"{wheels_count} number of wheels")


Car.default_value = "changed"
honda = Car(4)
print(honda.default_value)
honda.default_value = "lamda"
honda.wheels(15)
another = Car(3)
print(another.default_value)

nullWheel = Car.zeroWheel()
print(nullWheel)