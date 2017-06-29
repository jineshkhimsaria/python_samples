my_set =  set()
my_set.add("a")
my_set.add(1)
my_set.add("b")
my_set.add(2)
print("-------------------------------------------------- Hello -----------------------------------------------------")
#print("-------------------------------------------------- Hello 2 ---------------------------------------------------")
#print("-------------------------------------------------- Hello 3 ---------------------------------------------------")
#print("-------------------------------------------------- Hello 4 ---------------------------------------------------")
#print("-------------------------------------------------- Hello 5 ---------------------------------------------------")

print("Sample program related to various data structures in python")
print("Set - ")
print(my_set)
my_set.add("b")
print("adding same item in Set, Set removes the duplicate - ")
print(my_set)
my_set.add(2)
print("adding same item in Set, Set removes the duplicate - ")
print(my_set)

my_tuple = (0, 9, "x", "y")
print("Tuple - ")
print(my_tuple)

my_list = [3, 4, "h", "j"]
print("List - ")
print(my_list)
my_list.append(3)
my_list.append("j")
print("Adding same item in List, List keeps on appending the data - ")
print(my_list)

my_dict = {"a" : 1, "b": 2, 3 : "c"}
print("Dict - ")
print(my_dict)
my_dict[3] = "d"
print("Adding same key in Dict with different value updates the value of the Key - ")
print(my_dict)
my_dict["c"] = 3
print("Swapping key-value pair will add new key-value commbination in Dict - ")
print(my_dict)
print("------------------- Program Done ----------------------")

#List are mutable, ordered data structures
#Tuples are immutable ordered data structures
#Set are unordered, no duplicate
#Dictionary are unordered, key-value paired. Keys can be string, numbers, tuples but tuples should not contain mutable objects
