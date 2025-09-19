print("booleans -----")
name = "Alice"
is_cool = False
is_student = True
is_employee = False

print(name)
print(is_cool)
print(is_student)
print(is_employee)
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("Hello"))  # True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True
print(bool(None))  # False
print(bool(3.14))  # True
print(bool(-1))  # True
print(bool({}))  # False
print(bool({"key": "value"}))  # True
print(bool(()))  # False
print(bool((1, 2)))  # True
print(bool(set()))  # False
print(bool({1, 2}))  # True
print(bool(range(0)))  # False
print(bool(range(5)))  # True