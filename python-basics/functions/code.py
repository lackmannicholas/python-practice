def greet_person(name = "buddy"):
    print("Hello there, " + str(name))

greet_person()
greet_person("Nick")

def remainder(numerator, demoninator):
    return int(numerator) % int(demoninator)

print(remainder(10,3))

# arg = arguments, kwargs = key word arguments
def sum_plus_one(*args):
    return sum(args, 1)

print(sum_plus_one(1,2,265))

def key_value(**kwargs):
    print(kwargs)

key_value(name="Mike", weight=180, age=27)