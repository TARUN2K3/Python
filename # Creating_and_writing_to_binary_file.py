# Creating and writing to a binary file
with open("sample.bin", "wb") as f:
    data = b"Hello Binary World!"   # b prefix means bytes
    f.write(data)

print("Binary file created successfully.")

# Using Struct
import struct

with open("numbers.bin", "wb") as f:
    f.write(struct.pack("i", 100))    # store integer 100
    f.write(struct.pack("f", 3.14))   # store float 3.14

#Reading Back Binary Data
import struct

with open("numbers.bin", "rb") as f:
    int_data = struct.unpack("i", f.read(4))[0]   # read 4 bytes (int)
    float_data = struct.unpack("f", f.read(4))[0] # read 4 bytes (float)

print("Integer:", int_data)
print("Float:", float_data)
