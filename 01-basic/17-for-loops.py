print("for loops ----")
for i in range(5):
    print(i)
print("for loops end ----")
print("for loops with list ----")
for i in [10, 20, 30]:
    print(i)
print("for loops with list end ----")
print("for loops with string ----")
for char in "hello":
    print(char)
print("for loops with string end ----")
print("for loops with list of strings ----")
for word in ["hello", "world"]:
    print(word)
print("for loops with list of strings end ----")
print("for loops with list of strings and break ----")
for word in ["hello", "world"]:
    if word == "world":
        break
    print(word)
print("for loops with list of strings and break end ----")
print("for loops with list of strings and continue ----")
for word in ["hello", "world"]:
    if word == "world":
        continue
    print(word)