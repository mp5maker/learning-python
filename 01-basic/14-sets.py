print("sets -------")
print("sets are unordered collections of unique elements")
my_set = {1,2,3,4,5,5}
print(my_set)
print(type(my_set))
my_set.add(100)
my_set.add(2)
print(list(my_set))
my_set.clear()
print(my_set)

my_set_with_tuple_values = {(1,2), (3,4), (5,6)}
print(my_set_with_tuple_values)
print(type(my_set_with_tuple_values))
my_set_with_tuple_values.add((7,8))
print(my_set_with_tuple_values)

print("    ")
print("set operations -------")
a_set = {1,2,3,4,5}
b_set = {4,5,6,7,8, 9, 10}
print(a_set.difference(b_set)) # elements in a_set but not in b_set
print(a_set.intersection(b_set)) # elements in both sets
print(a_set.union(b_set)) # all elements in both sets
print(a_set.isdisjoint(b_set)) # are there no common elements?
print(a_set.issubset(b_set)) # is a_set a subset of b_set
print(a_set.issuperset(b_set)) # is a_set a superset of b_set
print(a_set.symmetric_difference(b_set)) # elements in either set but not both
print(a_set.union(b_set) == a_set.symmetric_difference(b_set).union(a_set.intersection(b_set))) # check that union is symmetric difference + intersection
print(a_set.difference_update(b_set)) # remove elements in b_set from a_set
print(a_set)