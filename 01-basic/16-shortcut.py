print("ternery operator ----")
okay = True
# shortcut for if-else
msg = "Everything is OK" if okay else "Something went wrong"
print(msg)


print("    ")
print("shortcuit operators ----")
is_friend = True
is_user = True
print(is_friend and is_user) # True if both are True
print(is_friend or is_user) # True if at least one is True
print(not is_friend) # True if is_friend is False


print("    ")
print("logical operator-----")
# using logical operators in conditions
is_friend = True
is_user = False
if is_friend and is_user:
    print("Best friends forever")
elif is_friend or is_user:
    print("Good friends")
else:
    print("Strangers")
print(4<5 and 5>6)
print(4<5 and 5>6 or 5==5)
print('a' > 'A')
print(1 >= 2 < 2 > 3 >4) # chaining comparisons
print(1 == 1.0) # True, because values are equal
print(1 is 1.0) # False, because they are different types
print(1 is not 1.0) # True, because they are different types
print([] == ()) # False, different types
print([] is ()) # False, different types
print([] is not ()) # True, different types
print([] == []) # True, same type and content
print([] is []) # False, different objects in memory
print([] is not []) # True, different objects in memory
print(not(True and False)) # True, because not(False) is True
print(not(True or False)) # False, because not(True) is False
print(not False) # True, because not(False) is True
print(not True) # False, because not(True) is False


is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("You need more practice")
elif not is_magician and is_expert:
    print("You need to learn magic")
else:
    print("You need to learn magic and practice more")

print("    ")
print("is vs == ----")
# 'is' checks for identity (same object in memory)
# '==' checks for equality (same value)
a = [1, 2, 3]
b = a
c = a[:]  # creates a new list with the same content
print(a == b)  # True, because values are equal
print(a is b)  # True, because both refer to the same object
print(a == c)  # True, because values are equal
print(a is c)  # False, because they are different objects in memory
print(a is not c)  # True, because they are different objects in memory
print(a is not b)  # False, because both refer to the same object
print(a == [1, 2, 3])  # True, because values are equal
print(a is [1, 2, 3])  # False, because they are different objects in memory
print(a is not [1, 2, 3])  # True, because they are different objects in memory
print([] == [])  # True, because values are equal
print([] is [])  # False, because they are different objects in memory
print([] is not [])  # True, because they are different objects in memory
print(() == ())  # True, because values are equal
print(() is ())  # True, because both refer to the same empty tuple object in memory
print(() is not ())  # False, because both refer to the same empty tuple object in memory
print({} == {})  # True, because values are equal
print({} is {})  # False, because they are different objects in memory
print({} is not {})  # True, because they are different objects in memory
print(set() == set())  # True, because values are equal
print(set() is set())  # False, because they are different objects in memory
print(set() is not set())  # True, because they are different objects in memory
print(1 == 1.0)  # True, because values are equal
print(1 is 1.0)  # False, because they are different types
print(1 is not 1.0)  # True, because they are different types
print("hello" == "hello")  # True, because values are equal
print("hello" is "hello")  # True, because of string interning in Python
print("hello" is not "hello")  # False, because both refer to the same object
print(1 == True)  # True, because True is equivalent to 1
print(1 is True)  # False, because they are different types
print(1 is not True)  # True, because they are different types
print(0 == False)  # True, because False is equivalent to 0
print(0 is False)  # False, because they are different types
print(0 is not False)  # True, because they are different types