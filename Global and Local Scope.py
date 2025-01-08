
x=10  #Global- entire space out side of function is called as global scope.
y=20
def fun():
    a=100 #Local- space inside of function is called as local scope.
    b=200
x=10
def fun():
    y=20
    print(y)    
print(x) #10   

x=10
def fun():
    y=20
    print(x)#10 we can access
fun()    
#we can access global scope data within function but we cant modify it.
'''
num=10
def fun():
    num=num+1
    print(num)
fun()
'''    

#update modify-keyword global
x=10
def fun():
    z=20
    print(z)
    global x
    x=x+1
    print(x)
print(x)   
fun()

fname="Akshada"
def details():
    lname="Jamkar"
details()  
print(fname) 


#return statement in python
#send data to the caller
def fun():
    x=10
    y=20
    return x,y
print(fun())

# def sum():
#     num1=eval(input("Enter num1"))
#     num2=eval(input("Enter num2"))
#     sum=num1+num2
#     return sum
# print(sum())

#create a function check number is even or not
def iseven(num):
    #num=eval(input("enter num:"))
    if num%2==0:
        return True
    else:
         return False
print(iseven(23))    

#create a fun to check number is perfect or not
def isperfect(num):
   # num=eval(input("num:"))
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if num==sum:
        return True
    else:
     return False
print(isperfect(6))    

#create function to reverse any string without using any predefine method or function or slicing
# def rev():
#     word=input("Enter string")
#     reverse=""
#     for char in word:
#         reverse=char+reverse
#     return reverse  
# print(rev())   


# def rev(word):
#     revers=" "
#     for i in word:
#         revers=i+revers
#     return revers
# print(rev("ashvini"))


# def rev(string):
#     out=" "
#     for i in string:
#         out=i+out
#     return out
# print(rev("kajal"))
            







