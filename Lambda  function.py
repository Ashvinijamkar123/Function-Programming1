
sum=lambda n1=10,n2=20:n1+n2
print(sum())

sum=lambda n1,n2:n1+n2
print(sum(10,20))

calci=lambda n1,n2:(n1+n2,n1-n2,n1*n2,n1/n2)
print(calci(10,20))

#Nested lambda function
#syntax:lambda arg:lambda arg:exp
f1=lambda n1=10:lambda n2=5:n1+n2
f2=f1()
print(f2()) 

f1=lambda n1:lambda n2:n1+n2
f2=f1(10)
print(f2(5))

#create a lambda function
sqr=lambda n:n**2
print(sqr(5))

#
string=lambda name:name.upper()
print(string("Akshada"))

#return sum of all numbers
l=[1,2,3,4,5]
sum=lambda seq:sum(seq)

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

result={"ajay":2,"vijay":78,"sujay":35,"kunal":67,"pavan":21,"arun":69,"avinash":89}
f=list(filter(lambda name:result[name]>40,result))
print(f)


