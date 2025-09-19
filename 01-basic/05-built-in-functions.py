print("builtin functions-------")
print(len("hello"))
print(type(100))

hello = "hello"
print(hello[0:len(hello)])
print("------")

quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.title())
print(quote.find("be"))
print(quote.replace("be", "me")) # immutable
print(quote) # original string is unchanged
print(quote.strip())