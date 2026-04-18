# LISTS and TUPLES

# can store mutiple data type in a list
marks = [45,34,85.45,92.22,55]
print(type(marks)) #list
print(marks[1])
print(len(marks))

# strings are immutable (can not change value)
# lists are mutable (can change value)
marks[1] = 90
print(marks[1])

# Slicing
#list_name[startingIndex, endingINdex]

print(marks[1: 4])

# Methods
marks.append(66)
marks.sort()
marks.sort(reverse=True)
marks.insert(1,10)
marks.remove(90)
marks.reverse() #remove first occurence of element
marks.pop(5) #index
print(marks)
#print(list.append(5))# return None


# Tuples (immutable just like strings)
# for single value k comma lagana h (1,)
tup = (2,3,1,7,8,10)
print(tup[1])
#tup[0] = 5 not allowed in tuples
#tup = (1,) #include comma for single value otherwise pyhton consider this as string 
print(tup[1:3])
print(tup.index(10)) #returns index of first occurence of elment
print(tup.count(10))


# WAP TO ASK THE USER TO ENTER OF THEIR 3 FAVORITE MOVIES & STORE THEM IN A LIST
# movies = []
# mov1 = input('Enter 1st movie')
# mov2 = input("Enter 2nd movie")
# mov3 = input("Enter 3rd movie")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.

# listQ1 = [1,2,1]
# listQ2 = [1,2,3]

# copy_list1 = listQ1.copy()
# copy_list1.reverse()

# copy_list2 = listQ2.copy()
# copy_list2.reverse()

# if(copy_list2 == listQ2):
#     print("palindrome")
# else: print("not palindrome")

# WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADES IN THE FOLLOWING TUPLE
# STORE THE VALUES IN A LIST & SORT THEM FROM 'A' TO 'D'

tupGrade = ('C','D','A','B','A','C','A','B')
print(tupGrade.count('A'))

listGrade = ['C','D','A','B','A','C','A']
listGrade.sort()
print(listGrade)
