print("conditional logic -------")
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print("    ")
temperature = 25
if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a warm day.")
elif temperature > 10:
    print("It's a cool day.")
else:
    print("It's a cold day.")

print("    ")
# Ternary conditional operator
is_raining = True
print("Take an umbrella." if is_raining else "No need for an umbrella.")

print("    ")
# Nested conditionals
num = 15
if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")
else:
    print(f"{num} is not a positive number.")

print("    ")
# Logical operators
username = "admin"
password = "1234"
if username == "admin" and password == "12345":
    print("Access granted.")
else:
    print("Access denied.")
if username == "admin" or password == "12345":
    print("Partial access granted.")
else:
    print("No access granted.")

print("    ")
# Membership operators
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list.")
if "grape" not in fruits:
    print("Grape is not in the list.")

print("    ")
# Identity operators
a = [1, 2, 3]
b = a
c = a[:]
print(a is b)  # True, because b references the same object as a
print(a is c)  # False, because c is a new object with the same content
print(a == c)  # True, because a and c have the same content


print("    ")
