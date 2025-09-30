#File Handling in Python
'''
Python Provide Built-In function to create, Read, Write and Append File
'''
#Reading the file
# f = open("Example.txt",'r') #open function has two parameter First one is File name and Second one is Mode, Currently it is in read mode
# print(f.read())
# f.close()

#Modes
'''
r <- Read mode
w <- Write mode
a <- Append Mode
x <- Creates File, Fails if file already Exists
b <- Binary mode
t <- text mode(Default)
'''
# Reading Mode
f = open("Example.txt",'r')

print(f.read())
print(f.read(10))
print(f.readline())
print(f.readlines())

f.close()

#Writing the file
w = open("Writing_file.txt",'w')
t = "This is the Writing File"
w.write(t)
w.close()

#Appending to the file
a = open("Writing_file.txt",'a')
append_text = "\n This is Append Text"
a.write(append_text)
a.close()

#Using With 
with open("Example.txt",'r') as f1:
    data = f1.read()
    print(data)
