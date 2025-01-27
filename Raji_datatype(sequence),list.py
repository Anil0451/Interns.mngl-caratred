#SEQUENCE DATA TYPES:
# =>Sequence Catagery Data Types are used for storing Sequence of Values / Multiple values of same type
#i) str
#ii) bytes
#iii) bytearray
#iv) range
##STRING:
#=>The collection or sequence of characters enclosed within single / double Quotes is called String (Python)
#=>'str' is one of the pre-defined class and treated as Sequence Data Type
'''a="Raji"
print(type(a))'''

'''b="Python Programming"
print(type(b))'''

'''c="Lakshmi"
print(type(c))'''

'''d="chandu"
print(type(d))'''

'''e="Python"
f="Programming"
g=e+f
print(g)'''

#=>We have two types of String data. They are
#a) Single Line String Data : =>Single Line String Data must be enclosed within Single or Double Quotes or tripple single / double Quotes.
#b) Multi Line String data : =>Multi Line String Data must be enclosed within tripple single (or tripple double Quotes).
#Operations on Strings:
# Indexing : =>The Process of obtaining one value at a time from given string object is called Indexing.
#a) Forward Indexing and starts from Left to Right (0,1,2.......)
#b) Backward Indexing and starts from Right to Left (-1, -2 -3.......)
#Forward Indexing :
'''a="Rajyalakshmi"'''
'''print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])'''
#Backward Indexing :
'''print(a[-7])
print(a[-6])
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])'''

#Slicing:=>The process of obtaining range of characters (or) sub string from given string object is called String Slicing.
#=>Syntax1:- strobj [ Begin : End ]
'''a="welcome to caratred"
print(a[:7])
print(a[8:10])
print(a[11:])
print(a[3:7])
print(a[16:])'''

#Striding:Here the Index values of Begin, End and Step can be Possitive and Negative
'''a=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
print(a[0:9:2])
print(a[4:20:5])
print(a[:20:4])
print(a[::6])
print(a[10:20:1])'''

# Bytearray: =>The purpose of bytearray data type is that "To organize sequece of Possitive Numerical Integer values ranges from (0,256). It Stores the values from 0 to 255(256-1) only ".
'''lst=[10,20,30,40,255]
b=bytearray(lst)
print(type(b))'''

#Range
#=>The purpose of range data type is that "To store sequence of Numerical Integer values by maintaining equal Interval of value ".
#=>Syntax1: varname= range(value)
'''a=range(6)
print(a,type(a))
for i in a:
    print(i)'''

'''a=range(1,10)
print(a,type(a))
for i in a:
    print(i)'''

'''a=range(10,50,5)
print(a,type(a))
for i in a:
    print(i)'''

'''a=range(10,0,-1)
print(a,type(a))
for i in a:
    print(i)'''
'''a=2
for i in range(1,11):
    print(a,"x",i,"=",a*i)'''

#LIST DATA TYPES:
#list data types are used for storing multiple values either of same type or different type or both types with unique and duplicate values in a single variable
#=>We create two types of lists. They are
#a) Empty List : An Empty List is one, whose length=0 (no elements presents)
#b) Non-empty list : An Non Empty List is one, whose length>0 (elements presents)
'''a=[10,20,30,40,50]
print(a,type(a))'''

'''a=["raji","anil","gopi","shannu"]
print(a[2])'''

'''a=["wlcome","caratred","to"]
print(a[0]+a[2]+a[1])'''

'''a=[10,"raji",11.3,"chan",2+3j,True]'''
'''print(a,type(a))
print(a[-1])
print(a[::2])'''
#Pre-defined Functions in list:
#1. append() 
#2. insert()
#3. clear()
#4. remove()
#5. POP
#6. POP(Index)
#7. Copy()
#8. Count()
#9. Index()
#10. Reverse()
#11. Sort()
#12. Extend()

#append(): It is used for adding the value at the end of the list
'''a=["akki","akka","akko"]
a.append("akkl")
print(a)'''

# insert(): it is used for inserting a Value at partucular index.
'''a=["java","dsa"]
a.insert(1,"python")
print(a)'''

#clear(): it is used for removing all the elements in list
'''a=[10,20,30] 
a.clear()'''

# remove(): it is used removing / deleting First Occurence of the element
'''a=["anil","sneha","pandu"]
a.remove("anil")
print(a)'''

# pop(Index) : This function is used for deleting the element of list based on Valid Exiting index otherwise we get IndexError.
'''a=["raji","anil","shannu","gopi"]
a.pop(2)
print(a)'''

# pop(): it is used for removing last element of list
'''a=["tv","ac","mv"]
a.pop()
print(a)'''

# copy(): it is used copying the content of one list into another list
a=["av","ac","ar"]

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#   





