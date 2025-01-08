# def ase(seq):
#     for i in range(len(seq)):
#         for j in range()


# def isperfect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum=sum+i
#     if sum==num:
#         return True
#     else:
#         return False
# print(isperfect(6))


# def prime(num):
#    for i in range(2,num):
#       if num%i!=0:
#          return True
#       else:
#          return False

# def ams(num):
#     sname=str(num)
#     n=len(sname)
#     sum=0
#     for i in sname:
#         sum=sum+int(i)**n
#     if sum==num:
#         return True
#     else:
#         return False
# print(ams(407))

# def pall(num):
#    rnum=str(num)
#    if num==int(rnum[::-1]):
#     return True
#    else:
#     return False
# print(pall(11))



# def fact1(num):
#    fact=1
#    for i in range(1,num+1):
#       fact=fact*i
#    return fact
# print(fact1(5))




# def feb(number):
#    s=[]
#    a,b=11,12
#    for i in range(number):
#       s.append(a)
#       a,b=b,a+b
#    return s
# print(feb(20))

# # def strpali(string):
# #     for i in string:
       
# #         r_string= string[::-1]
# #         if r_string==string:
# #           return True
    
# #         else:
# #          return False  
# # print(strpali("madam"))    

# # def prime(num):
# #    for i in range(2,num):
# #       if num%i!=0:
# #          return True
# #       else:
# #          return False
# # print(prime(7))
# '''
# def ams(num):
#     sname=str(num)
#     n=len(sname)
#     sum=0
#     for i in sname:
#         sum=sum+int(i)**n
#     if sum==num:
#          return True
#     else:
#          return False
# print(ams(153))

# def per(num):
#     sum=0
#     for i in range(1,num):
#       if num%i==0:
#           sum=sum+i
#     if sum==num:
#         return True
#     else:
#        return False
# print(per(6))
          

   

# b=[9,34,56,87,153]
# def ams(seq):
#     l=[]
#     for num in seq:
#         sname=str(num)
#         n=len(sname)
#         sum=0
#         for i in sname:
#          sum=sum+int(i)**n
#         if sum==num:
#            l.append(num)
#     return l
# print(ams(b))
# '''

# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return "not prime"
#     return "prime"   
# print(prime(7)) 

# def isperfect(num):
#     sum=0
#     for i in range(1,num):
#        # sum=sum+i
#         if num%i==0:
#               sum=sum+i
#     if num==sum:
#         return "is perfect"     
#     else:
#         return "not prime" 
# print(isperfect(6))    

# def ispalindrome(string):
#     if string==string[::-1]:
#         return "palindrome"
#     else:
#         return "not palindrome"
# print(ispalindrome("madam"))   

# def palindrome(num):
#     numstr=str(num)
#     #revstr=numstr[::-1]
#     if num==int(numstr[::-1]):
#         return "palindrome"
#     else:
#         "not palindrome"
# print(palindrome(77))    


# def armstrong(num):
#     numstr=str(num)
#     n=len(numstr)
#     sum=0
#     for i in numstr:
#       sum=sum+int(i)**n
#     if num==sum:        
#         return True
#     else:
#         return False
# print(armstrong(407))        
        
# #create a function input='a1b2c3',output='abbccc'    
# def alpa_mul(string):
#     out=""
#     for i in range(0,len(string),2):
#         out=out+string[i]*int(string[i+1])
#     return out    
# print(alpa_mul("a1b2c3")) 


# #create a function input= 'm3n5b1'output='mmmmnnnnnb'
# # def alpa_mul(string):
# #     out=""
# #     for i in range(0,len(string),2):
# #         out=out+string[i]*int(string[i+1])
# #     return out    
# # print(alpa_mul("m3n5b1"))


# #input=mmnnnuuuuoutpt=m2n3u4
# def compress_string(s):
#     if not s:
#         return ""
    
#     compressed = []
#     count = 1

#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             compressed.append(s[i - 1] + str(count))
#             count = 1

#     # Add the last character and its count
#     compressed.append(s[-1] + str(count))
    
#     return ''.join(compressed)
# print(compress_string("mmmuuu"))


# #reverse list by using for lop.

# l=[11,22,33,44]
# l1=[]
# for i in range(len(l)-1,-1,-1):
#     l1.append(l[i])
# print(l1)


# # reverse list by using while .
# l=[11,22,33,44]
# l1=[]
# i=len(l)-1
# while i>0:
#     l1.append(l[i])
# i=i-1
# print(l1)


#remove duplicate
# l=[1,2,2,3,4,6,8,8]
# def remove(value):
#     i=0
#     while i<len(value):
#         j=i+1
#         while j <len(value):
#             if value[i]==value[j]:
#                 value.remove(value[j])
#             else:
#                 j += 1
#         i += 1
#     return i
# print(remove(l))

# l=[1,2,3]
# print(l[::-1])

# l=[1,2,3,4]
# l1=[]
# for i in range(len(l)-1,-1,-1):
#     l1.append(l[i])
# print(l1)


# l=[2,34,6,7,8,9,0]
# l1=[]
# for i in range(len(l)-1,-1,-1):
#     l1.append(l[i])
# print(l1)


# def ams(num):
#     sname=str(num)
#     n=len(sname)
#     sum=0
#     for i in sname:
#         sum=sum+int(i)**n
#     if sum==num:
#         return True
#     else:
#         return False
# print(ams(153))


# def per(num):
#     sum=0
#     for i in range(2,num):
#         if num%i==0:
#          sum=sum+num
#          if sum==num:
#             return True
#          else:
#             return False

# print(per(6))


# #121
# def pali(num):
#     sname=str(num)
#     if num==int(sname[::-1]):
#         return True
#     else:
#         return False
# print(pali(121))

 
# def rev(string):
#     sname= " "
#     for i in string:
#         sname=i+sname
#     return sname
# print(rev("ashuuu"))


# l=[1,4,3,8,9,5]
# def min(seq):
#     for i in range(len(seq)):
#      for j in range(i+1,len(seq)):
#         if seq[i]>seq[j]:
#             seq[i],seq[j]=seq[j],seq[i]
#     return seq
# print(min(l))



#a3v5
# def alnum(string):
#     out=" "
#     for i in range(0,len(string)):
#         out=out+string[i]*int(string[i+1])
#     return out
# print(alnum("a3v4"))


# def remo(string):
#     out=" "
#     for i in string:
#         if i!=" ":
#             out=out+i
#     return out
# print(remo("java by kiran"))
            







