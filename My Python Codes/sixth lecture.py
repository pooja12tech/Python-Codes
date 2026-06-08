#functions-to reduce redundancy
def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum
cal_sum(6,15)
cal_sum(4,9)
#another method of doing this

#function defintion  
def calc_add(c,d):  #paramteters
    return c+d
add=calc_add(155,324) #function call
print(add)
#avgerage of three numbers 
def cal_avg(o,p,q):
    addition=o+p+q
    avg=addition/3
    print(avg)
    return
cal_avg(65,67,61)
#practice time
#1st  and 2nd question
cities=["jaisalmer","barrackpore","gwalior","kharagpur"]
heroes=["soldiers","parents","farmers"]
def print_len(list):
    print(len(list))
print_len(cities)    
print_len(heroes)
#2nd question....
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(heroes)
print()     
# factorial of number n using function
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    cal_fact(6)    
# 4th question
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"usd =",inr_val,"INR")
#recursive function
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
#factorial of anumber using recursive function
def fac(m):
    if (m==1 or m==0):
        return 1
    return fac(m-1)*m
print(fac(6))
#practice time
def calc_add(x):
    if (x==0):
        return 0
    return calc_add(n-1)+n
add=calc_add(16)
print(sum)
#2nd question-to print all elements in a list
def print_list(list,idx=0):
    if (idx==len(list)):
        return 
    print(list(idx))
    print_list(list,idx+1)
fruits=("litchi,chickoo","orange","pineapple")
print_list(fruits)     