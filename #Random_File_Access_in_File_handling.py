#Random_File_Access_in_File_handling

'''
Random File Access allow to read and write data from any where in the file Insted of beigning or the end of the binary file only.

Method:-
1. seek(offset, whence) <- offset(how many position want to cursor move), Whence(position 0(Beginning),1(current),2(end))
2. tell() <- Return Cursor Position
3. read(size) or write(data)

'''
with open("Example.txt",'rb+') as f: #When you open a file in read-only mode ('r'), you can only move the cursor to specific byte positions relative to the start or current position. This is because the file is opened as read-only, and Python doesn't allow you to perform certain operations like relative seeks from the end of the file in this mode.
    print(f.read(10))
    print(f.tell())
    f.seek(14)
    # Move to beginning
    f.seek(0)
    print("File content:", f.read())

    # Move pointer to 7th byte
    f.seek(7)
    print("Pointer at:", f.tell())
    print("Reading from here:", f.read(4))  # reads 'File'

    # Move pointer near end
    f.seek(-7, 2)   # 7 bytes before end
    print("Reading last part:", f.read())