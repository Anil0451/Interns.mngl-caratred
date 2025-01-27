'''sequence data type in python
************************************
In python there are four types of sequence data types. They are 


1) Str
2) Bytes
3) Bytearray
4) Range

 Str: The str datatype in Python is used to represent textual data. A string is a sequence of characters enclosed in single quotes ('), double quotes (""), or triple quotes  for multi-line strings.

 Bytes: The bytes datatype represents immutable sequences of bytes. 

 Bytearray: The bytearray datatype represents a mutable sequence of bytes. Unlike bytes, it allows modification of its content.

 Range: The range datatype is used to represent a sequence of numbers. It is commonly used in loops and can generate numbers in a specified start, stop, and step format


'''
# str examples

name = "Python"
print(name)

sentance = """This is
a multiline string."""
print(sentance)

adding = "Hello, " + "World!"
print(adding)

word = "Python String"
print(word[0])  
print(word[-1])

text = "hello sir"
print(text.upper())  
print(text.capitalize())

# Bytes

data = bytes("Hello", "utf-8")
print(data) 

data = b"Binary Data"
print(data) 

data = b"Python"
print(data[0])

data = b"abc"
for byte in data:
    print(byte)

    data = b"Hello, World!"
print(len(data))

# bytearray

data = bytearray(b"Hello")
print(data)

data = bytearray(b"Hello")
data[0] = 72  
print(data)

data = bytearray(b"Hello")
data.append(33)
print(data)

data = bytearray(b"Python")
print(data[1:4])


data = bytearray(b"Data")
immutable_data = bytes(data)
print(immutable_data)

#Range

r = range(5)
print(list(r))

r = range(2, 7)
print(list(r))

r = range(1, 10, 2)
print(list(r))

r = range(10, 0, -2)
print(list(r))

for i in range(3):
    print("Iteration", i)


