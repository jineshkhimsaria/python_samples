my_set =  set()
my_set.add("a")
my_set.add(1)
my_set.add("b")
my_set.add(2)
print("Set ")
print(my_set)
my_set.add("b")
print("Set add same item ")
print(my_set)
my_set.add(2)
print("Set add same item ")
print(my_set)

my_tuple = (0, 9, "x", "y")
print("Tuple ")
print(my_tuple)

my_list = [3, 4, "h", "j"]
print("List ")
print(my_list)
my_list.append(3)
my_list.append("j")
print("List add same item ")
print(my_list)

my_dict = {"a" : 1, "b": 2, 3 : "c"}
print("Dict ")
print(my_dict)
my_dict[3] = "d"
print("Dict add same key with different value ")
print(my_dict)
my_dict["c"] = 3
print("Dict add swapped key-value ")
print(my_dict)

#List are mutable, ordered data structures
#Tuples are immutable ordered data structures
#Set are unordered, no duplicate
#Dictionary are unordered, key-value paired. Keys can be string, numbers, tuples but tuples should not contain mutable objects
