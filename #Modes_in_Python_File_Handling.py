#Modes in Python File Handling
'''
'r' <- Read Mode
'w' <- Write Mode
'a' <- Append Mode
'x' <- Exclusive Creation
't' <- Text Mode
'b' <- Binary Mode
'r+' <- Read + Write Note:- File must Exist
'w+' <- Write + read Note:- overwrites File or Creating new file
'a+' <- Append + Read Note:- Create File if file not Exist

'''

#Read Mode

f = open("Example.txt",'r')
print(f.read())
print(f.read(10)) # its reads 10 characters
print(f.readline()) #it read first line
print(f.readlines()) #it reads all Lines
f.close()

fw = open("Example.txt", 'r+')
print(fw.read())  # 1. Reads the entire file and moves the cursor to the end
content = "\n this is new content for checking r+ mode"
fw.write(content)  # 2. Writes content where the cursor is now (end of file)
print(fw.read())  # 3. Tries to read again, but the cursor is already at the end, so this returns ''
fw.close()

fb = open("Example.txt",'rb')
print(fb.read())
print(type(fb.read()))
fb.close()
