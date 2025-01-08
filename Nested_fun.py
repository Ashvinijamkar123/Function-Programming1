def f1():
    print("f1 function")
    x=100
    def f2():
        print("f2 function")
        y=200
f1()      

def f1():
    print("f1 function")
    x=100
    def f2():
        print("f2 function")
        y=200
    f2() 
f1()       

a=10   
def f1():
    print("f1 function")
    x=100
    print(x)
    def f2():
        print("f2 function")
        y=200
        print(y)
        print(x)
        print(a)
        return y
    y=f2() 
    print(x)  
    print(y) 
f1()   

num1=10
def f1():
    num2=20
    def f2():
        num3=30
        return num3
    num3=f2()
    return num2,num3
num2,num3=f1()
print(num1+num2+num3) 

def f1():
    print("f1 function")
    x=100
    def f2():
        print("f2 function")
        y=200
    return f2,x
f2,x=f1()   
f2()
'''
def f1():
    print("f1 function")
    x=100
    def f2():
        print("f2 function")
        y=200
        def f3():
            print("f3 function")
            z=300
    return f2,f3
f2,f3=f1() 
f2()      
'''
def detail1():
    name="Akshada"
    def detail2():
        last_name="Jamkar"
        return last_name
    return  detail2,name  
detail2,name=detail1() 
last_name=detail2()    
print(name+" "+last_name) 

def number1():
    n1=100
    def number2():
        n2=200
        return n2
    return number2,n1
number2,n1=number1()   
n2=number2()
print(n1+n2)  

def f1():
    n1=10
    def f2():
        n2=20
        def f3():
            n3=30
            return n3
        return n2,f3
    return n1,f2
n1,f2=f1()
n2,f3=f2()
n3=f3()
print(n1+n2+n3)


def n1():
    name="Akshada"  
    def n2():  
        middle_name="Babasaheb"  
        def n3():
            last_name="Jamkar"  
            return last_name 
        return  n3,middle_name   
    return n2,name  
n2,name=n1()      
n3,middle_name=n2() 
last_name=n3()  
print(name+" "+middle_name+" "+last_name)
