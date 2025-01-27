SEQUENCE DATA TYPES

Sequence Catagery Data Types are used for storing Sequence of Values.

We have 4 types of Sequence data types.
1.String
2.Bytes
3.Bytearray
4.Range

STRING--> The collection or sequence of characters enclosed within single / double Quotes  is called String (Python). STR is one of the pre-defined class and treated as Sequence Data Type.
On the String data, we can two types of Operations. They are 
a) Indexing 
The Process of obtaining one value at a time from given string object is called  
Indexing.
b) Slicing
The process of obtaining range of characters   
object is called  String Slicing.

We have two types of String data. They are 
a) Single Line String Data 
b) Multi Line String data 

On the String data, we can two types of Operations. They are 
a) Indexing 
The Process of obtaining one value at a time from given string object is called  
Indexing.
Ex : s="PYTHON" 
 print(s[0])
 print(s[-6])

b) Slicing
The process of obtaining range of characters   
object is called  String Slicing. 
Ex:  s="PYTHON" 
print(s[3:6])

Ex: a="Redefining Sollutions" 
 print(a,type(a))--Redefining Sollutions

 b='K' 
 print(b,type(b))--K 

 c="A" 
 print(c,type(c))--A

 d='Python Programming' 
 print(d,type(d))--Python Programming 

 ani="Caratred tech" 
 print(ani,type(ani))--Caratred tech 


Bytes--> Bytes is one of the pre-defined class and treated as a sequential data type.
The data type is that To Store Sequence of Posstive Integer values within the range of (0,256). ie. It stores (0,255 only) 

Ex : C1=[10,20,30,255]  
 b=bytes(C1) print(b[0]) 
 type(b) print(b[1])
 print(b[2])

Bytearray--> Bytearray is one of the pre-defiend data type and treated as Sequence data type. 
The bytearray data type is that To organize sequece of Possitive Numerical Integer values ranges from (0,256).

Ex: string = "Hello" 
    byte_array = bytearray(string, 'utf-8')  
    print(byte_array) 

    size = 5 
    empty_array = bytearray(size)  
    print(empty_array) 
    

    int_list = [65, 66, 67]  
    byte_array = bytearray(int_list)  
    print(byte_array)

    data = bytearray(b"abcd") 
    data[1] = 98  
    print(data)

Range--> Range is one pre-defined class and treated as sequence data type. The purpose of range data type is that "To store sequence of Numerical Integer    values by maintaining equal Interval of value ". 

Ex:1   2    3     4     5    6     7    8   9   10--range(1,11)  

10    20   30  40 50   60  70   80   90  100--range(10,101,10) 
 
100  105   110   115   120--range(100,121,5) 
 
100  90   80  70  60  50 --range(100,49,-10) 

-5   -4   -3   -2  -1   0   1  2   3   4   5--range(-5,6,1) 
 





