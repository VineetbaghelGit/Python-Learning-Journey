# FILE INPUT/OUTPUT

# Python can be used to perform operation on a file (read,write data)

# Types of all files
# 1. Text files : .txt, .docx, .log etc
# 2. Binary files : .mp4, .mov, .jpeg etc

# We have to open a file before reading or writing

files = open("Lecture6.py",'r')
data = files.read()
print(data)
print(type(data))
files.close()

# data = files.read() reads entire file
# data = files.readline() reads one line at a time

# Writing to a file
#  W write mode overwrite the entire file
#  A append mode add at the end in the file
#  If file does not exist in W or A mode it will create new

# r+ --> read + overwrite + cursor pointer starting + no truncate
# w+ --> read + overwrite + truncate
# a+ --> read + append + cursor pointer end + no truncate

f = open('demo.txt',"a")
f.write("\nI want to learn javascript")
f.close()

# With automatic close the file

with open('demo.txt','r') as f:
    data = f.read();
    print("data",data)

# DELETING A FILE
# Using the OS module, Module is a library
import os
os.remove("demo.txt")

# Practice question

with open("practice.txt",'w') as f:
    f.write("Hi everyone\nwe are learning file I/o\n")
    f.write("Using Javascript.\nI like programming in Javascript\n")

with open('practice.txt','r') as f:
    data = f.read()
    new_data = data.replace("Javascript","Python")
    print(new_data)

with open('practice.txt','w') as f:
    f.write(new_data)

# Search if the word "learning" exists in the file or not.

word = "learning"
with open('practice.txt','r') as f:
    data  = f.read()
    if(data.find(word) != -1):
        print("Found word")
    else:
        print("not found word")

# WAF to find in which line of the file does the word "learning" occur first

def check_for_line(w):
    data = True
    line_no = 1
    with open('practice.txt','r') as f:
        while data:
            data = f.readline()
            if(w in data):
                return line_no
            line_no +=1 
    return -1   

print(check_for_line(word))

# From a file containing numbers separated by comman, print the count of even numbers

with open('practice.txt','r') as f:
    data = f.read()

    tcp gurantee that any of the packet is not going to be lost while transfering (more reliable)
    