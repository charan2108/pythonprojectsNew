a = [10, 20, 30 ,40]
b = bytes(a)
print(a)
print(type(a))
print(b[0])
print(b[-1])

# byte values can not be changed
# a = [10, 20, 30 ,40]
# b = bytes(a)
# b[0] = 100
# print(b)

# bytearrays

a = [10, 20, 30 ,40]
b = bytearray(a)

for c in b:
    print(c)
    
#editable
a = [10, 20, 30 ,40]
b = bytearray(a)
b[0] = 250 
for c in b:
    print(c)
    