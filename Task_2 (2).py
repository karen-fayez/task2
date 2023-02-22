#!/usr/bin/env python
# coding: utf-8

# #**Task_2**
# 
# ---
# 
# 

# # <font color='red'> 1) Mark down all the Valid function-calls for this function: </font> 
# 
# 
# # def fun1(name, age):<br> ..... print(name,age)
# 
# 
# 
# 
# 
# 
# <br> </br>
# #### A) fun1( "Emma"  ,  23 )
# <br> </br>
# #### B) fun1( age = 23  ,  name = "Emma" )
# <br> </br>
# #### C) fun1( "Emma"  ,  age = 23 ) 
# <br> </br>
# #### D) fun1( name = "Emma" ,  23 )
# <br> </br>
# #### E) fun1( age = 23  ,  "Emma" )

# In[ ]:


A = true #@param {type:"boolean"} 
B = true #@param {type:"boolean"} 
C = true #@param {type:"boolean"} 
D = False #@param {type:"boolean"} 
E = False #@param {type:"boolean"}


# # <font color='red'> 2) Debug the following code and correct the Error to make the output = 15: </font> 
# 
# 
#     
#     def outer_fun(a, b,c ):
#         def inner_fun(d , e):
#             return d + e
# 
#         return inner_fun(a, b,c)
#         return a   
# 
#     result = outer_fun(5, 10)
#     print(result)
# 

# In[21]:


def outer_fun(a, b ):
        def inner_fun(d , e):
            return d + e

        return inner_fun(a, b)
           

result = outer_fun(5, 10)
print(result)


# # <font color='red'> 3) Debug the following code and correct the Error to make the output = 16: </font> 
# 
#     def f1(x):
#         global x
#         x+=1
#         print(x)
#     f1(15)
# 

# In[23]:


def f1(x):
    x+=1
    print(x)
f1(15)


# # <font color='red'> 4) Write a function that takes any variable "n" and return its factorial: </font>
# 
# ##### **hint:** factorial of 5 = 5 x 4 x 3 x 2 x **1**

# In[25]:


def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
fact(5)    


# # <font color='red'> 5) Write a code to print the following dictionary after: </font> 
# * # Ordering the values of each Key and the print the key witht highest value. 
# 
# 
# > **`dict ={ "Ahmed": (50 , 30 , 40) , "Mohammed": (15 , 10 , 25) , "Khaled": (10 , 40 , 20) }`**
# 
# <br> </br>
# # The output should be:
# * `{"Ahmed": (50 , 40 , 30) , "Mohammed": (25 , 15 , 10) , "Khaled": (40 , 20 , 10)}`
# * `Ahmed`
# 

# In[18]:


dict ={ "Ahmed": (50 , 30 , 40) , "Mohammed": (15 , 10 , 25) , "Khaled": (10 , 40 , 20) }
data=[]
s=list()
m=dict.keys()
for x in dict:
    y=sorted(dict[x],reverse=True)
    data.append(y)
for i in data:
     dict.update({"Ahmed" : data[0],"Mohammed" : data[1],"khaled" : data[2]})
print(dict)


        

    


# # <font color='red'> **Solve these problems with python**:<br>
# <a href='https://codeforces.com/group/6Yv6FRlDFU/contest/327653/problem/C'> **problem 1** </a> </font> 
#     <br>
#     <br>
# <a href='https://codeforces.com/group/6Yv6FRlDFU/contest/327653/problem/A'> **problem 2** </a> </font>
#     <br>
#     <br>
# <a href='https://codeforces.com/group/6Yv6FRlDFU/contest/327650/problem/D'> **problem 3** </a> </font>
#     <br>
#     <br>
# <a href='https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true'> **problem 4** </a> </font>
#     <br>
#     <br>
# <a href='https://codeforces.com/group/6Yv6FRlDFU/contest/327653/problem/B'> **problem 5** </a> </font>
#     <br>
#     
# 
#  
# 
# 
#     

# In[10]:


#problem 1
s=int(input("enter number of stones"))
c=input("enter sequence").split()
count=0
for i in range(0,n):
    if c[i]==c[i-1]:
        count+=1
print(count)        


    
    
        


# In[17]:


#problem 2
n=int(input("number of lines"))
m=int(input("number of elements"))
x = '.' * (m - 1)
y= '#'
z= '#' * m
for i in range(n):
    if i % 2 == 0:
        print(z)
    else:
        print(x,y)
        x,y=y,x


# In[26]:


#problem 3
s = input()
m = "hello"
x = 0
for i in range(len(s)):
    if s[i] == m[x]:
          x += 1
    if x == 5:
        print("Yes")
        break
if x<5:
    print("No")


# In[52]:


#problem 4
term=int(input("enter number of terms"))
x=0
a1,a2=0,1
data=[]
cube=lambda y:y*y*y
if term <= 0:
    print("Please enter a positive integer")
elif term == 1:
    print(a1)
else:
    while(x<term):
        data.append(cube(a1))
        s=a1+a2
        a1=a2
        a2=s
        x+=1
print(data)        


# In[5]:


#problem5 

s=input("enter calories").split(" ")
y=input("enter sequence")
x=[int(i) for i in s]
totalcalories= x[0]*y.count("1")+x[1]*y.count("2")+x[2]*y.count("3")+x[3]*y.count("4")
print(totalcalories)


# In[ ]:




