# DICTIONARY & SETS

# DICTIONARY IN PYTHON
# Are used to store data values in key:values pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys
# in strings, list, tuple we have index, so we can know where is value

dictInfo = {
    'name':"vineet",
    'city': "ahmedabad",
    'age':28,
    'skills':['react, nodejs'],
    'company':('tecmantras, bankai')
}

print(type (dictInfo))
print(dictInfo['company'])
dictInfo['company'] = ('tecmantras, bankai','nexgin')
dictInfo['surname'] = 'Baghel'
print(dictInfo)

null_dict = {} # add later

# NESTED DICTIONARY

studentDict = {
    "name":"vineet baghel",
    'subjects':{
        'phy':"97",
        "chem":'77',
        "math":"88"
    }
}
print(studentDict['subjects']["math"])

# METHODS

print(dictInfo.keys()) # nested wali nahi aaegi
print(len(dictInfo))
print(list(dictInfo.values()))
print(list(dictInfo.items())) #returns all key, val pairs as tuples
print(dictInfo.get('')) #returns the key according to value
#we two ways to get value
#print(dictInfo['name2']) #error
#print(dictInfo.get('name2')) #None
dictInfo.update({"city":'bhilwara'})


# SETS IN PYHTON
#Set is the collection of the unordered items.
#Each element in the set must be unique & immutable

# List adn dictionary ko set k andar store nahi krwa skte bcz they are mutable

collection = {1,2,3,4,5,2,3,4,1,1}
print(type (collection))
print(collection)

newCollection = {} #empty dictionary
setCollection = set()
print(type (setCollection))

# SET METHODS
# set are mutable but it's element/values are immutable

setCollection.add(1)
setCollection.add(2)
setCollection.add(3)
setCollection.add((4,5,6))
#setCollection.add([8,9,1]) #unhashable means jo value change ho jae jinki value diff aa jae baad me
setCollection.pop() #randomly remove
# setCollection.clear()
print(setCollection)

print(collection.union(setCollection))
print(collection.intersection(setCollection))

# WAP TO STORE THE FOLLOWING WORD MEANING IN DICTIONARY

wordMeaning = {
    "table": ['A furniture','list of facts'],
    "cat":"Animal"
}
print(wordMeaning)

# You are given a list of subjects for students. Assume one classroom is reuired for 1 subject. How many classrooms are needed for all students

subjects = {"python", 'Java','C++', "python", 'JS',"C++","C","Java","JS"}

print(len(subjects))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value

val1 = input("enter phy :")
val2 = input("enter chem :")
val3 = input("enter math :")

studentsMark = {}
studentsMark['phy'] = val1
studentsMark['chem'] = val2
studentsMark['math'] = val3
print(studentsMark)

# Figure out a way to store 9 & 9.0 as separate value in the SET
values = {
    ('float',9.0),
    ('int',9)
}
print(values)