--> Set Category Data Types

Set is a collection of well defined elements. Set is a unorder and remove duplicates.
Set category data types are used for storing multiple values either pf same type or diff type of both types with unique values in a single variable.

set category data types are 2 types.
1.Set (Mutable and Immutable)
2.Frozenset (Immutable)

Set Data types
Set is one of the predefined class treated as Set category data type.

Example:
a={10,20,30,40,40,50,60,70}
print(a)
{50, 20, 70, 40, 10, 60, 30}
print(type(a))
<class 'set'>
a1={}
print(a1,type(a1))
{} <class 'dict'>
a1=[]
print(a1,type(a1))
[] <class 'list'>
a1=()
print(a1,type(a1))
() <class 'tuple'>
a1=set()
print(a1,type(a1))
set() <class 'set'>


--> Pre-defined Function in set
add()
This function is used for adding an element to the set object.
Ex:
b={"anil","shannu","raji"}
print(b,type(b))
{'raji', 'shannu', 'anil'} <class 'set'>
b.add("gopi")
print(b)
{'raji', 'shannu', 'anil', 'gopi'}

remove()
This function is used for removing the specified element from from set object.
Ex:
c={"caratred","redefining","technologies"}
print(c,type(c))
{'caratred', 'technologies', 'redefining'} <class 'set'>
c.remove("redefining")
print(c,type(c))
{'caratred', 'technologies'} <class 'set'>

discard()
This function is used for removing the specified element from from set object.
Ex:
a={10,20,30,40,40,50,60,70}
print(a,type(a))
{50, 20, 70, 40, 10, 60, 30} <class 'set'>
a.discard(40)
print(a,type(a))
{50, 20, 70, 10, 60, 30} <class 'set'>
a.discard(90)
print(a,type(a))
{50, 20, 70, 10, 60, 30} <class 'set'>
a.remove(90)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.remove(90)
KeyError: 90

pop()
This function is used for removing any orbitary element from set object.
Ex:
a={'anil','gopi','shannu','raji'}
print(a,type(a))
{'raji', 'shannu', 'anil', 'gopi'} <class 'set'>
a.pop()
'raji'
print(a)
{'shannu', 'anil', 'gopi'}
a.pop()
'shannu'
print(a)
{'anil', 'gopi'}
a.pop()
'anil'
print(a)
{'gopi'}
a.pop()
'gopi'
print(a)
set()
a.pop()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.pop()
KeyError: 'pop from an empty set'
a={10,20,30,40,40,50,60,70}
print(a)
{50, 20, 70, 40, 10, 60, 30}
a.pop()
50
a={10,20,30,40,40,50,60,70}
a.pop()
50
print(a)
{20, 70, 40, 10, 60, 30}
a.pop()
20
a.pop()
70
a.pop()
40
a.pop()
10
a.pop()
60
a.pop()
30
a.pop()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.pop()
KeyError: 'pop from an empty set'

isdisjoint()
This function returns True provided setobj1 and setobj2 does contains common elements.
This function returns False provided setobj1 and setobj2 does contains at least one common element.
Ex:
a1={10,20,30,40}
a2={15,25,35,10}
a3={12,24,36,48}
a1.isdisjoint(a2)
False
a1.isdisjoint(a1)
False
a1.isdisjoint(a3)
True
a1.isdisjoint(set())
True
set().isdisjoint(set())
True

issuperset()

This function returns True provided all the elements of setobj2 must present in setobj1. Otherwise we get False.
Ex:
a1={10,20,30,40}
a2={15,25,35,10}
a3={12,24,36,48}
a1.issuperset(a3)
False
a1.issuperset(a2)
False
a4={10,20}
a1.issuperset(a4)
True
a1.issuperset(a1)
True
a1.issuperset(set())
True
set().issuperset(set())
True

issubset()

This function returns True provided all the elements of setobj1 are present in setobj2. Otherwise we get False.
Ex:
s1={10,20,30,40}
s2={10,20}
s3={15,20}
s2.issubset(s1)
True
s3.issubset(s1)
False
set().issubset(set())
True

union()

This function takes  all the elements of setobj1 and setobj2,combine them and place them in setobj3 uniquely.
Ex:
a1={"raji","anil","gopi","shannu"}
a2={"cratred","tech","gopi"}
print(a1)
{'raji', 'shannu', 'anil', 'gopi'}
print(a2)
{'cratred', 'tech', 'gopi'}
a1a2=a1.union(a2)
print(a1a2)
{'tech', 'anil', 'gopi', 'raji', 'cratred', 'shannu'}

intersection()

This obtains common elements from setobj1 and setobj2 and place them setobj3.
Ex:
a1={"raji","anil","gopi","shannu"}
a2={"cratred","tech","gopi"}
a3=a1.intersection(a1)
print(a3)
{'raji', 'shannu', 'anil', 'gopi'}
a3=a1.intersection(a2)
print(a3)
{'gopi'}
a3=a2.intersection(a1)
print(a3)
{'gopi'}

difference()

This function removes the common elements from setobj1 andsetobj2 and takes remaining elements from setobj1 and place them in setobj3.
Ex:
a1={"raji","anil","gopi","shannu"}
a2={"cratred","tech","gopi"}
print(a1)
{'raji', 'shannu', 'anil', 'gopi'}
print(a2)
{'cratred', 'tech', 'gopi'}
onlya1=a1-a2
print(onlya1)
{'raji', 'anil', 'shannu'}
onlya2=a2-a1
print(onlya2)
{'cratred', 'tech'}
onlya1=a1.difference(a2)
print(onlya1)
{'raji', 'anil', 'shannu'}
onlya2=a2.difference(a1)
print(onlya2)
{'cratred', 'tech'}

symmetric_difference()

This function removes common elements from setobj1 and setobj2 and takes remaining elements from both setobj1 and setobj2 and place them in setobj3.
Ex:
a1={"raji","anil","gopi","shannu"}
a2={"cratred","tech","gopi"}
print(a1)
{'raji', 'shannu', 'anil', 'gopi'}
print(a2)
{'cratred', 'tech', 'gopi'}
exa1a2=a1.symmetric_difference(a2)
print(exa1a2)
{'anil', 'raji', 'cratred', 'shannu', 'tech'}


update()

This function updates/adds the elements of setobj2 to setobj1.
Ex:
a={"caratred","tech"}
a1={"python","html","mysql","ds"}
a.update(a1)
print(a)
{'python', 'tech', 'caratred', 'html', 'ds', 'mysql'}
print(a1)
{'html', 'python', 'mysql', 'ds'}
a={"caratred","tech"}
a1={"redefining","tech"}
a.update(a1)
print(a)
{'caratred', 'redefining', 'tech'}