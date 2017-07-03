dict1 = {'Name' : 'JRK', 'Place': 'NL', 'Age' : 30 }

print ("-------------- Dict Items ------------")
print (dict1.items())

dict1['Designation']='Sr Engineer'
dict1['Age']=29

print
print ("------------ Updated Dict Items -----------------")
print (dict1.items())

dict2 = {'Gender' : 'Male', 'Status':'Married'}
print
print ("------------ Dict2 Items--------------------")
print (dict2.items())
print

print ("------------- Appended Dict2 to Dict1 ------------")
dict1.update(dict2)
print (dict1.items())

print
print ("------------- Dict Keys -------------------")
print (dict1.keys())

print
print ("--------------- Dict Values ------------")
print (dict1.values())

print
print ("------------ Type of Dict -------------------")
print (type(dict1))

print
print ("------------ Deleted Name from Dict -------------")
del dict1['Name']
print (dict1.items())

print
print ("------------------ Dict without items -----------")
dict1.clear()
print (dict1.items())

print
print ("--------------- Deleted Dict ----------------")
del dict1
