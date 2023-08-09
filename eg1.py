#list
#we can create a list using square bracket and object even
#inside the list we can use diiferent types of elements(any datatype)
#in list duplicate are allowed and maintents insertion order
#note: list is unsafe(we have methodsto modify the list data

li=[int,float,str,set,complex,bool,dict,frozenset,list,tuple,range,bytes,bytearray]
print(li)


l2=[int(),float(),str(),set(),complex(),bool(),dict(),frozenset(),list(),tuple(),range(0),bytes(),bytearray()]
print(l2)

l3=[10,20,30,40,10,20]
#   0   1  2  3  4 5
print(l3)


#id is build_in
print(id(l3[0]))
print(id(l3[5]))

#len is build_in function
# len()
l4=[10,20,30,40,50]
print(len(l4))


#object()
l5=list([10])
print(l5)

