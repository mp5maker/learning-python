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