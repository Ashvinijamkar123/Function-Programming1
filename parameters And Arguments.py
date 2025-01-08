def sum(n1,n2):#  parameters
    s=n1+n2
    return s
print(sum(10,20)) #Arguments

#Types of Arguments
'''
1.Positional
2.keyword
3.Default
4.Arbitary 
   a.Positional Arbitary
   b.Keyword
'''
#1.Positional Argument:
def details(name,age,city):
    return f"""
            Name:{name}
            Age:{age}
            City:{city}
            """
print(details("Akshada",21,"Nashik"))
'''
def details(name,age,city):
    return f"""
            Name:{name}
            Age:{age}
            City:{city}
            """
#error print(details("Akshada",21))
'''

#2.keyword Argements
#There is no need to maintain position of arguments as per fun defination
#number parameter == number of arguments
def details(name,age,city):
    return f"""
            Name:{name}
            Age:{age}
            City:{city}
            """
print(details(name="Aarti",age=20,city="pune"))

#3.Default Argument
#
def student_details(name,age,city,course="python"):
    return f"""
            Name:{name}
            Age:{age}
            City:{city}
            Course:{course}
            """
print(student_details("Aarti",20,"Nashik","Python"))
print(student_details("Akshada",21,"pune"))
print(student_details("Rani",23,"Mumbai"))

#4.Arbitary 
# a.Positional Arbitary (*x)
def sum(*x):
    print(x) #(10, 20, 30) tuple
sum(10,20,30) 

def sum(*x):
    s=0
    for i in x:
        s=s+i
    return s
print(sum(10,20,30))


#b.Keyword Arbitary
def details(**x):
    s=""
    for i,j in x.items():
        m=f"\n{i}={j}"
        s=s+m
    return s
print(details(name="rani",age=21,city="pune"))

#create a function to count number of char in string
def str_len(string):
    count=0
    for i in string:
       count=count+1
    return count  
print(str_len("Akshada")) 

#
def count_num(string):
    count=0
    for i in string:
        if i.isnumeric():
            count=count+1
    return count
print(count_num("Akshada66"))  

#without using any inbuit function
def count_num(string):
    count=0
    for i in string:
        if i in "4676766":
            count=count+1
    return count
print(count_num("Akshada66"))  

# create a function to count empty space in given string
def count_empty_space(string):
    count=0
    for i in string:
        if i.isspace():
            count=count+1
    return count 
print(count_empty_space("java by kiran academy"))      

# remove all weight space.
def remo(string):
    str1=" "
    for i in string:
        if i!=" ":
            str1=str1+i
    return str1
print(remo("i am ashu"))










