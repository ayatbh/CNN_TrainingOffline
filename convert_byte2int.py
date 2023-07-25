'''
Purpose : Testing the byte to intger converter 
Author  : Ayat B.
'''
# Define a byte array
#byte_array = b'x00x01x02x03'
byte_array = b'\x00\x20\x01\x7f\xcf'

# Convert byte array to integer (Big Endian)
integer_big_endian = int.from_bytes(byte_array, 'big')
print("Big Endian:", integer_big_endian)

# Convert byte array to integer (Little Endian)
integer_little_endian = int.from_bytes(byte_array, 'little')
print("Little Endian:", integer_little_endian)