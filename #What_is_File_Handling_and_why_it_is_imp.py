#What is File Handling and why it is important?
# File handling in Python refer to the managing the file using inbuilt function like open(), close(), read(), write().
'''
it is important because :-
1.Persistence of data
2.Data sharing 
3.Handling large data
'''

f = open("Example.txt",'w')
content = "Hii, This is Tarun kumar sharma"
f.write(content)
f.close
f = open("Example.txt",'r')
print(f.read())
f.close()