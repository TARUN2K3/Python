# Write_Mode
fw = open("Written_file",'w')
content = "This is the New file created"
fw.write(content)
fw.close()

fb = open("Written_file",'wb')
contentb = "This Content written in Binary Mode"
fb.write(contentb.encode('utf-8'))
fw.close()

fwb = open("Written_file",'w+')
contentw = "this is Overwritten content"
fwb.write(contentw)
fwb.seek(0)
print(fwb.read())
fwb.close()