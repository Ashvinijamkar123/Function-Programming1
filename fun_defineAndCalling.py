# #function define and calling

# def sum():
#     n1=eval(input("num1:"))
#     n2=eval(input("num2:"))
#     sum=n1+n2
#     print(sum)


# # create a function to check number is even or not
# def EvenOdd(num):
#     #num=eval(input("num:"))
#     if num%2==0:
#         print(f"{num} is even number.")
#     else:
#         print(f"{num} is odd number.")
# print(EvenOdd(4))        
        
'''
#check the number is Armstrong or not
num=eval(input("num:")) #407----4^3+0^3+7^3
numstr=str(num)
n=len(numstr)
sum=0
for i in numstr:
    sum=sum+int(i)**n
if num==sum:
    print("Yes")
else:
    print("No")  '''   
     
# #create function count vowel of char/element/keys
# def vowel():
#     string="ashvini"    
#     count=0 
#     for char in string.lower():
#         if char in "aeiou":
#             count=count+1
#     print(count)
# vowel() 


# def vowel():
#     name="kajal"
#     count=0
#     for i in name:
#         if i in "aeiou":
#             count=count+1
#     print(count)
# vowel()



#create function count number of char/element/keys
# def mylen():
#     string=input("Enter string:")
#     length=0
#     for char in string:
#         length=length+1
#     print(length) 
# mylen()   

'''l=["Akshada","Rani","Sita","Geeta","vijay","virat"]
count=0
for name in l:
    if name[0]=="V".lower():
        count=count+1
print(count) 
'''       

# #create a fun arrange min to max  
# l=[7,1,6,2,4]
# def my_asc(seq):
#      for i in range(len(seq)):
#       for j in range(i+1,len(seq)):
#         if seq[i]<seq[j]:
#             seq[i],seq[j]=seq[j],seq[i]
#      return seq
# print(my_asc(l))


#  print(my_asc(l)) 
# #create a fun arrange max to min
# l=[7,1,6,2,4]  
# def my_asc(seq):
#     for i in range(len(seq)):
#         for j in range(i+1,len(seq)):
#             if seq[i]<seq[j]:
#                 seq[i],seq[j]=seq[j],seq[i]
#     return seq
# print(my_asc(l))

# #create a function to check number is prime or not
# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return "not prime"
#     return "prime"
            
# print(prime(9))

# num=eval(input("Enter num:"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"{num} is not prime")
#         break
#     else:
#         print(f"{num}is prime")


# n1=10
# n2=20
# n1=n2
# n2=n1
# print(n1) 
# print(n2)       

# l=[11,22,33,44]
# l[1],l[2]=l[2],l[1]
# print(l[1])
# print(l[2])

#create a fun input a2b3c1=>aabbbc
# def alpa_mul(string):
#     out=""
#     for i in range(0,len(string),2):
#         out=out+string[i]*int(string[i+1])
#     return out    
# print(alpa_mul("a2b3c5"))  

# # 
# def is_arm(number):
#     numstr=str(number)
#     n=len(numstr)
#     sum=0
#     for i in numstr:
#         sum=sum+int(i)**n
#     if number==sum:
#         return True
#     else:
#         return False
# print(is_arm(407))   

# #create a function to return armstromg list
# l=[101,33,153,407,56,789,9]
# def arm(seq):
#     l=[]
#     for num in seq:
#         numstr=str(num)
#         n=len(numstr)
#         sum=0
#         for i in numstr:
#             sum=sum+int(i)**n
#         if num==sum:
#             l.append(num)
#     return l
       
# print(arm(l))   

# #create a fun to calculate sum of all armstrong numbers from an iterable
# l=[5,153,407,123,66]
# def arm_sum(seq):
    
#     allsum=0
#     for num in seq:
#         numstr=str(num)
#         n=len(numstr)
#         sum=0
#         for i in numstr:
#             sum=sum+int(i)**n 
#         if num==sum:
#          allsum=allsum+num
#     return allsum      
# print(arm_sum(l))



# def mylen(string):
#     #string=input("Enter string:")
#     length=0
#     for char in string:
#         length=length+1
#     return length
# print(mylen("Akshada")) 


# def count1():
#     string="ashvini"
#     count=0
#     for i in string:
#         if i in "eaiou":
#           count=count+1
#     print(count)
# count1()



# def vowel():
#     string="vAibhav"    
#     count=0 
#     for char in string.lower():
#         if char in "aeiou":
#             count=count+1
#     print(count)
# vowel() 

    
# l=[7,5,4,9,2,1,6]
# def min(seq):
#     for i in range(len(seq)):
#         for j in range(i+1,len(seq)):
#             if seq[i]>seq[j]:
#              seq[i],seq[j]=seq[j],seq[i]
#     return seq
# print(min(l))

# l=[7,1,6,2,4]
# def my_asc(seq):
#      for i in range(len(seq)):
#       for j in range(i+1,len(seq)):
#         if seq[i]>seq[j]:
#             seq[i],seq[j]=seq[j],seq[i]
#      return seq
# print(my_asc(l))







# ##a2b3 solve it. 
# def alnum(string):
#     out=" "
#     for i in range(0,len(string),2):
#         out=out+string[i]*int(string[i+1])
#     return out
# print(alnum("a2b3"))


# #aabbbb
# def alnum(string):
#     out=" "
#     c=0
#     for i in range(0,len(string)):
#         out=out+string[i]+str(c)
#         c=c+1
#     return out
# print(alnum("abbbb"))

# def alnum(string):
#     out=" "
#     for i in range(0,len(string)):
#         out=out+string[i]+str(i+1)
#     return out
# print(alnum("abbbss"))


# def vovel():
#     name="ashvini"
#     count=0
#     if char in name.lower():
#         if char"aeiou":
#      count=count+1
    


