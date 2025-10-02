#Append_Mode

# fa = open("Example.txt",'a')
# content = '\n Appended Text'
# fa.write(content)
# fa.close()

with open("Example.txt",'a+') as fr:
    contentr = "The new Appended Text"
    fr.write(contentr)
    fr.seek(0)
    print(fr.read())

with open("Example.txt", 'ab+') as f:
    f.seek(0)
    content_before = f.read()
    print("Before appending:", content_before)

    # Data must be in bytes
    new_content = b"\nThis is appended in binary mode"
    f.write(new_content)

    # Move back to start to read updated conten
    f.seek(0)
    content_after = f.read()
    print("\nAfter appending:", content_after)