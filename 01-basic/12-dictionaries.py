print("dictionaries -----")
d = {"key1": "value1", "key2": "value2"}
print(d)
print(type(d))
print(d["key1"])
print(d.get("key2"))
print(d.get("key3"))  # None
print(d.get("key3", "default_value"))  # default_value
d["key3"] = "value3"
print(d)

my_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 40}
]

print(my_list[0]["name"])  # Alice
print(my_list[1]["age"])   # 25
print(my_list[2]["name"])  # Charlie
print(my_list[3]["age"])   # 40

dictionary = {
  123: [1,2,3],
  True: "hello"
}
# immutable values can be used as keys
print(dictionary[123])  # [1, 2, 3]
print(dictionary[True])  # hello

user = {
    "name": "John",
    "age": 30,
    "is_active": True,
    "favorites": {
        "color": "blue",
        "food": "pizza"
    },
    "hobbies": ["reading", "traveling", "swimming"]
}
print(user.get("occupation", "unemployed"))  # unemployed
user["age"] = 31  # update age
user["occupation"] = "developer"  # add occupation
print(user)
del user["is_active"]  # remove is_active
print(user)


user2 = dict(name="Jane", age=28, is_active=False)
print(user2)

print("basked" in user2)  # False
print("age" in user2)     # True
print(len(user2))         # 3
print(user2.keys())      # dict_keys(['name', 'age', 'is_active'])
print(user2.values())    # dict_values(['Jane', 28, False])
print(user2.items())     # dict_items([('name', 'Jane'), ('age', 28), ('is_active', False)])
print(user2.clear())    # None
print(user2)            # {}d

user3 = user.copy()
print(user3)
user3.update({"age": 32, "city": "New York"})
print(user3)
user3.pop("age")
print(user3)
user3.popitem()
print(user3)