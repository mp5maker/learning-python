print("tuples------")
# tuples are immutable lists
t = (1, 2, 3)
print(t[0])
# t[0] = 10  # This will raise an error
print(len(t))
print(t + (4, 5))
print(t * 2)
print(2 in t)
for item in t:
    print(item)

my_tuple = ("Alice", 30, True, ["reading", "traveling"])
new_tuple = my_tuple + ("extra", 99)
print(new_tuple)
print(new_tuple[3][1])
print(len(my_tuple))  # traveling


my_tuple_2 = (1,2,3,4,5)
user = {
  'basket': [1, 2, 3],
  'greet': 'hello',
  'age': 20,
  (1,2): [1,2,3]  # tuple as a key (immutable)
}
print(user.items())  # dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])
for key, value in user.items():
    print(key, value)
print(5 in my_tuple_2)  # True
print(10 in my_tuple_2)  # False
print(my_tuple_2.index(3))  # 2
print(my_tuple_2.count(2))  # 1
# my_tuple_2[0] = 10  # This will raise an error
# my_tuple_2.append(6)  # This will raise an error
# my_tuple_2.remove(2)  # This will raise an error
# my_tuple_2.pop()  # This will raise an error  # 32
print(user[(1,2)])  # [1, 2, 3]
print(user.get((1,2)))  # [1, 2, 3]


my_tuple_3 = (1, 2, 3, 4, 5)
print(my_tuple_3[1:4])  # (2, 3, 4)
print(my_tuple_3[:3])   # (1, 2, 3)
print(my_tuple_3[2:])   # (3, 4, 5)
print(my_tuple_3[-1])   # 5
print(my_tuple_3[-3:])  # (3, 4, 5)
print(my_tuple_3[:-2])  # (1, 2, 3)
print(my_tuple_3[::-1]) # (5, 4, 3, 2, 1)
a, b, c, d, e = my_tuple_3
print(a, b, c, d, e)  # 1 2 3 4 5
x, y, *rest = my_tuple_3
print(x, y, rest)  # 1 2 [3, 4, 5]
x, *middle, z = my_tuple_3
print(x, middle, z)  # 1 [2, 3, 4] 5
*beginning, y, z = my_tuple_3
print(beginning, y, z)  # [1, 2, 3] 4 5