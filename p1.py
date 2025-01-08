# 1.Syntax import modulname
import fun_defineAndCalling
fun_defineAndCalling.sum()   #modulname.fun
# 2.from modulename import function_name
from fun_defineAndCalling import EvenOdd
#EvenOdd()


# def f1():
#     name="ashu"
#     def f2():
#          mname="babasaheb" 
#          def f3():
#           sname="jamkar"
#           return sname
#          return mname,f3
#     return name,f2
# name,f2=f1()
# mname,f3=f2()
# sname=f3()
# print(name+" "+mname+" "+sname)

def EvenOdd(num):
    #num=eval(input("num:"))
    if num%2==0:
        print(f"{num} is even number.")
    else:
        print(f"{num} is odd number.")
print(EvenOdd(55))   

def prime(num):
    for i in range(2,num):
        if num%i==0:
            return "not prime"
    return "prime"
            
print(prime(9))

def vowel(string):
    count=0 
    for char in string.lower():
        if char in "aeiou":
            count=count+1
    return count
print(vowel("Aai")) 


