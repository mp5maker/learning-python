print("string-------")
print("double quotes")
print("single quotes")
print("triple quotes")
print("multiline strings")
print("string interpolation")
print("raw strings")
print(type("hello"))

username = "supercode"
password = "supersecret"
print("username:", username)
print("password:", password)
long_string = '''
WOW
0 0
---
'''
print(long_string)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)


print("     ")
print("string concatenation-------")
print("hello" + " " + "world")
print("hello" + " world")
print("hello world")
print("hello" * 3)
print("hello " * 3)
print("hello" * 3 + "world")
print("hello " * 3 + " world")
print("hello " * (3 + 2))

print("     ")
print("str-------")
print(str(100))
print(str(100.5))
print(str(True))
print(str(False))
print(str(None))
print(str([1, 2, 3]))
print(str((1, 2, 3)))
print(str({1, 2, 3}))
print(str({"a": 1, "b": 2, "c": 3}))
print(type(str(100)))


print("     ")
print("escape sequence-------")
print("hello\nworld")
print("hello\tworld")
print("hello\\world")
print("hello\'world")
print("hello\"world")
print("hello\rworld")
print("hello\bworld")
print("hello\fworld")
print("hello\vworld")
print("hello\0world")
print("hello\x41world")
print("hello\u0041world")
print("hello\u03A9world")
print("hello\u03C0world")
print("hello\U0001F600world")
print("hello\U0001F601world")
print("hello\U0001F602world")


print("     ")
print("formatted strings-------")
name = "John"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")
print("Hello, my name is {} and I am {} years old.".format(name, age))
print("Hello, my name is {0} and I am {1} years old.".format(name, age))
print("Hello, my name is {name} and I am {age} years old.".format(name=name, age=age))
print("Hello, my name is %s and I am %d years old." % (name, age))

print("     ")
print("string indexes-------")
word = "Hello"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[4] == word[-1])
print("-----")
print(word[1:4]) # from index 1 to index 4 (4 not included)
print(word[:3]) # from start to index 3 (3 not included)
print(word[2:]) # from index 2 to end
print(word[:]) # whole string
print(word[::2]) # every second character
print(word[1:4:2]) # from index 1 to 4 (4 not included), every second character
print(word[::-1]) # reverse string
print(len(word))