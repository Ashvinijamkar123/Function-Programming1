
#Higher Order Function
#Syntax:

#1.filter()
#syntax:filter(fun,seq)
l=[11,22,33,44,55]
def even(iterable):
    l1=[]
    for i in iterable:
        if i%2==0:
            l1.append(i)
    return l1
print(even(l))

#filter() ex.
l=[11,22,33,44,55]
def even(num):
    if num%2==0:
        return True
f=filter(even,l)  
print(f)  

l=[11,22,33,44,55]
def even(num):
    if num%2==0:
        return True
f=list(filter(even,l))  
print(f) 

#using filter with lambda
l1=list(filter(lambda num:num%2==0,l))
print(l1)

l=[11,22,-33,44,-55]
f=list(filter(lambda num:num>0,l))
print(f)

l=[11,22,33,44,55,66]
f=list(filter(lambda num:num%2==1,l))
print(f)

student=("ajay","VIJAY","sujay","KUNAL","pavan")
f=tuple(filter(lambda name:name.isupper(),student))
print(f)

student=("ajay","vijay","sujay","kunal","pavan","arun","avinash")
f=tuple(filter(lambda name:name.startswith("a"),student))
print(f)

student=("ajay","vijay","sujay","kunal","pavan","arun","avinash")
f=tuple(filter(lambda name:name[0]=="a",student))
print(f)

student=("ajay","vijay","sujay","kunal","pavan","arun","avinash")
f=tuple(filter(lambda name:name.endswith("jay"),student))
print(f)
student=("ajay","vijay","sujay","kunal","pavan","arun","avinash")
f=tuple(filter(lambda name:name[-3:]=="jay",student))
print(f)

result={"ajay":20,"vijay":78,"sujay":35,"kunal":67,"pavan":21,"arun":69,"avinash":89}
f=list(filter(lambda name:result[name]>40,result))
print(f)

employee={"chitanya":34000,"Amruta":56000,"anushka":76000}
f=list(filter(lambda name:employee[name]>50000,employee))
print(f)

l=["ashu","kajal","kumaaaaaar","pari","nidhi"]
s=list(filter(lambda name:name.endswith("i"),l))
d=list(filter(lambda name:name,l))
print(d)
print(s)

#dict
d=dict(filter(lambda tuple:tuple[1]>50000,employee.items()))
print(d)

votting={"Akshada":21,"Aarti":20,"Rani":17,"Manu":15}
d=dict(filter(lambda tuple:tuple[1]<18,votting.items()))
print(d)

#2.map()
#map(fun,iterable)
number=[11,22,33,44,55]
def inc_2(iterable):
    l=[]
    for num in iterable:
        l.append(num+2)
    return l
print(inc_2(number))

# by using map fnction
l=[11,22,33,44,55]
def inc(num):
    return num+2
m=list(map(inc,l))
print(m)

# map with lambda
l=[11,22,33,44,55]
f=list(map(lambda num:num+2,l))
print(f)

l=["Ajay","vijay","Ram","Lakhan"]
f=list(map(lambda name:name.upper(),l))
print(f)

result={"Ajay":45,"Vijay":67,"Raghav":60}
f=dict(map(lambda tuple:(tuple[0],tuple[1]+5),result.items()))
print(f)

employee={"chitanya":34000,"Amruta":56000,"anushka":76000}
f=dict(map(lambda tuple:(tuple[0],tuple[1]+10000),employee.items()))
print(f)

#3 reduce()
from functools import reduce
l=[11,22,33,44,55]
mul=reduce(lambda x,y:x*y,l)
print(mul)                                                                                       

