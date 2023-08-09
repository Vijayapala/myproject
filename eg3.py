#extend() meand add multiple elements at the end of the list
l1=[10,20,30,40,50]
l1.extend([60,70,80])
print(l1)

l2=['cat','rat','cow']
l2.extend(['dog','pegion'])
print(l2)

l3=(['red','blue','green','purple'])
l4=(['white','brown'])
l3.extend(l4)
print(l3)
print(len(l3))

l6=[]
l6.extend('java')
print(l6)