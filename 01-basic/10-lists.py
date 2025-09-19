print("lists --------------------------------")
print("Lists are used to store multiple items in a single variable.")

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

mixed_list = ["apple", 1, True, 3.14]
print(mixed_list)

amazon_cart = ["notebook", "sunglasses", "toys", "grapes"]
print(amazon_cart)
print(amazon_cart[0])
print(amazon_cart[1])
print(amazon_cart[2])
print(amazon_cart[3])

print("    ")
print("List slicing --------------------------------")
print(fruits[0:2])  # prints items from index 0 to 1
print(amazon_cart[1:3])  # prints items from index 1 to 2
print(amazon_cart[0:4])  # prints items from index 0 to 3
print(amazon_cart[0:2])  # prints items from index 0 to 1
print(amazon_cart[2:4])  # prints items from index 2 to 3
print(amazon_cart[0:1])  # prints item at index 0
print(amazon_cart[1:2])  # prints item at index 1
print(amazon_cart[2:3])  # prints item at index 2
print(amazon_cart[3:4])  # prints item at index 3
print(amazon_cart[:-1])  # prints all items except the last one
print(amazon_cart[1:])  # prints all items from index 1 to the end
print(amazon_cart[:3])  # prints all items from the start to index 2
print(amazon_cart[:])  # prints all items in the list
print(amazon_cart[::2])  # prints every second item in the list
print(amazon_cart[::-1])  # prints the list in reverse order
print(amazon_cart[::-2])  # prints every second item in the list in reverse order
print(amazon_cart[-2])  # prints the second last item in the list
print(amazon_cart[-3])  # prints the third last item in the list


print("    ")
print("List mutable --------------------------------")
print("Lists are mutable, meaning their items can be changed.")
amazon_cart[0] = "laptop"
print(amazon_cart)
amazon_cart[1] = "earphones"
print(amazon_cart)
amazon_cart[2] = "keyboard"
print(amazon_cart)
amazon_cart[3] = "mouse"
print(amazon_cart)


print("    ")
print("List slicing mutable --------------------------------")
amazon_cart[0:2] = ["notebook", "sunglasses"]
print(amazon_cart)
amazon_cart[1:3] = ["toys", "grapes"]
print(amazon_cart)
amazon_cart[0:4] = ["notebook", "sunglasses", "toys", "grapes"]
print(amazon_cart)
amazon_cart[0:2] = ["laptop", "earphones"]
print(amazon_cart)
amazon_cart[2:4] = ["keyboard", "mouse"]
print(amazon_cart)
amazon_cart[0:1] = ["notebook"]
print(amazon_cart)
amazon_cart[1:2] = ["sunglasses"]
print(amazon_cart)
amazon_cart[2:3] = ["toys"]
print(amazon_cart)
amazon_cart[3:4] = ["grapes"]
print(amazon_cart)
amazon_cart[-1] = "grapes"
print(amazon_cart)
new_cart = amazon_cart
new_cart[-1] = "tomatoes"
print(new_cart)
print(amazon_cart)

print("    ")
print("List methods --------------------------------")
print("List methods are functions that can be used on lists to perform various operations.")
copy_amazon_cart = amazon_cart.copy()
print(copy_amazon_cart)
copy_amazon_cart.append("mangoes")
print(copy_amazon_cart)
copy_amazon_cart.append("pears")
print(copy_amazon_cart)
copy_amazon_cart.append("bananas")


print("    ")
print("matrix ------")
print("Matrices are used to store data in a tabular format.")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])

print("    ")
print("list methods ------")
print(len(amazon_cart))
print(amazon_cart.count("grapes"))
print(amazon_cart.index("toys"))

basket = [1, 2, 3, 4, 5]
print(basket.append(200)) # prints None because append() returns None
print(basket) # prints [1, 2, 3, 4, 5, 200]
basket.insert(4, 100) # inserts 100 at index 4
print(basket)   # prints [1, 2, 3, 4, 100, 5, 200]
basket.remove(3) # removes the first occurrence of 3
print(basket)   # prints [1, 2, 4, 100, 5, 200]
basket.pop() # removes and returns the last item
print(basket) # prints [1, 2, 4, 100, 5]
basket.clear() # removes all items
print(basket) # prints []
basket.extend([100, 200, 300]) # extends the list by appending elements from the iterable
print(basket) # prints [100, 200, 300]
basket.reverse() # reverses the elements of the list in place
print(basket) # prints [300, 200, 100]
basket.sort() # sorts the items of the list in place
print(basket) # prints [100, 200, 300]
basket.sort(reverse=True) # sorts the items of the list in place in descending order
print(basket) # prints [300, 200, 100]
print(basket.index(200)) # prints the index of the first occurrence of 200
print(basket.count(100)) # prints the number of occurrences of 100

print(300 in basket) # prints True
print(500 in basket) # prints False
print(300 not in basket) # prints False
print(500 not in basket) # prints True


sorted_basket = sorted(basket) # returns a new sorted list from the items in basket
print(sorted_basket) # prints [100, 200, 300]
print(basket) # prints [300, 200, 100]
sorted_basket_desc = sorted(basket, reverse=True) # returns a new sorted list from the items in basket in descending order
print(sorted_basket_desc) # prints [300, 200, 100]
print(basket) # prints [300, 200, 100
print(basket[::-1])
print(basket)


print(list(range(1, 100))) # prints numbers from 1 to 99
print(list(range(0, 101))) # prints numbers from 0 to 100
sentence = ["hi", "my", "name", "is", "john"]
print(" ".join(sentence))

print("    ")
print("list unpacking --------------------------------")
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

a, b, c, *other = [1, 2, 3, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)