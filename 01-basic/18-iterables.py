print('iterables -----')
print("an iterable is an object capable of returning its members one at a time, allowing it to be iterated over in a for-loop.")
print('range(5):', list(range(5)))
print('list:', [10, 20, 30])
print('string:', list("hello"))
print('list of strings:', ["hello", "world"])


user = {
  "name": "golem",
  "age": 5006,
  "can_swim": False
}

for (key, value) in user.items():
  print(key, value)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)

print("counter -----")
my_list = [1,2,3,4,5,6,7,8,9]
for i in range(len(my_list)):
  print(i, my_list[i])