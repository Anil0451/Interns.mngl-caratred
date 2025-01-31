#SET DATA TYPES:
#set is used to store multiple values either same type or different type with unique values in a single variable
#it does not allow duplicates and we cannot maintain index and slicing operations
#there are two types:
#1) SET(Mutable and immutable)
#2) Frozenset(immutable)
'''a={10,20,30,40,50,60,70}
print(a,type(a))'''

'''a={10,"raji","lucky",True,"vjd"}
a.add("reena")
print(a,type(a))'''

'''s={1,2,3,4,5}
print(s,type(s),id(s))
s.add("raji")
s.add("rani")
print(s,type(s),id(s))'''

#Pre-defined functions in set:
#1)add() : it is used for adding the element to the set
'''s={1,2,3,4,5,"python","java"}
print(s,type(s),id(s))
s.add("devops")
s.add("frontend")
print(s,type(s),id(s))'''

#2)remove(): it is used for removing the specified element from set
'''a={10,20,"dsa","bli"}
print(a,id(a))
a.remove("dsa")
print(a,id(a))
a.remove(20)
print(a,id(a))
a.remove(100)
print(a)'''#it shows keyerror


#3)discard(): it is used for removing the specified elements from set
'''a={10,20,"dsa","bli"}
print(a,id(a))
a.discard("dsa")
print(a,id(a))
a.discard(20)
print(a,id(a))
a.discard(100)
print(a)''' # it doesnot shows any error  


#4)pop(): it is used for removing an arbitary  elements from set
'''a={"raji","reena",10,20}# in this any arbitary element is removed
a={"apple","banana","orange","kiwi"}
a.pop()
'orange'
a.pop()
'kiwi'
a.pop()
'apple'
a.pop()
'banana'
a.pop()
print(a)'''#it shows keyerror coz of empty set
#it another case if you want to pop the elements like order way {"apple","banana","orange"}
#you must print the input and then pop the elements its gives the output you expected
'''a={"apple","banana","orange","kiwi"}
print(a)
{'orange', 'kiwi', 'apple', 'banana'}
a.pop()
'orange'
a.pop()
'kiwi'
a.pop()
'apple'
a.pop()
'banana'
'''

#5)isdisjoint(): it returns True when set1 and set2 has no common values 
#it returns False when set1 and set2 has atleast one common values 
'''a={1,2,3,4}
b={2,9,8,5}
c={20,30,40,50}
a.isdisjoint(b)
False
a.isdisjoint(c)
True
a.isdisjoint(set())
True
set().isdisjoint(set(set))#here id will be considered and excuting the result
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set().isdisjoint(set(set))
TypeError: 'type' object is not iterable
set().isdisjoint(set())
True'''

#6)issuperset(): it returnss True when all elements of set2 must present in set1
'''s={10,20,30}
s1={20,60,80}
s2={90,70,100}
s.issuperset(s1)
False
s.issuperset(s2)
False
s3={10,20}
s.issuperset(s3)
True
s.issuperset(set())#every empty set is an superset to it self
True
set().issuperset(set())
True'''

#7)issubset() : it returns True when all the elements of set1 are present in set otherwise we get False

'''a={10,20,30}
b={10,20}
c={15,2}
b.issubset(a)
True
c.issubset(a)
False
set().issubset(set())
True
c.issubset(b)
False
a.issubset(b)
False'''

#8)union():it takes all the elements of set1 and set2 combine them and gives the output and also(|)used that symboll as union
'''a={'rj','ra','re','rt'}
b={"tv","ty","te","ta"}
print(a)
{'ra', 're', 'rj', 'rt'}
print(b)
{'te', 'ta', 'tv', 'ty'}
c=a.union(b)
print(c)
{'tv', 're', 'rj', 'ty', 'ta', 'ra', 'te', 'rt'}'''

#9)difference():it removes the common elements from set1 and set2 and takes remaining elements from set1 and place them in set3
'''d1={"rj","ra","re","rt"}
d2={"tv","ty","te","ta"}
d3=d1-d2
print(d3)
{'ra', 're', 'rj', 'rt'}
d3=d2.difference(d1)
print(d3)
{'te', 'ta', 'tv', 'ty'}
d3=d1.difference(d2)
print(d3)
{'ra', 're', 'rj', 'rt'}'''

#10)Intersection():this obtains common elements from set1 and set2
'''a={10,20,30,40}
b={20,60,50,90}
c=a.intersection(b)
print(c)
{20}
c=b.intersection(a)
print(c)
{20}'''

#11)symmetric_difference(): in this common elements are removed
'''a={10,20,30,40}
b={20,60,50,90}
c=a.symmetric_difference(b)
print(c)
{40, 10, 50, 90, 60, 30}'''

#12)update(): it updates/add the elements of set1 to set2
'''a={"python","dsa","c","cpp"}
b={"html","css","js","bt"}
a.update(b)
print(a)
{'js', 'c', 'cpp', 'dsa', 'css', 'python', 'html', 'bt'}'''











