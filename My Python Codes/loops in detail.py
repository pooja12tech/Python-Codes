#  print('hello',count)
#     count += 1
# #print numbers from 1-7
# i=1
# while i<=7:
#     print(i)
#     i+=1
# #practice time
# #numbers from 1-100
# o=1
# while(o<=100):
#     print(o)
#     o+=100
# #numbers form 100-1
# q=100
# while(q>=1):
#     print(q)   
#     q-=1
# #multiplication table of number n
# p=1
# n=int(input('enter a number : '))
# while(p<=10):
#     print(n*p)
#     p+=1
# #4th question
# nums=[1,4,9,16,25,36,49,64,81,100]
# heroes=["ironman","thor","superman","batman"]
# #traverse
# i=0
# while i<len(heroes):
#     print(heroes[i])
#     i+=1
# #5th question         
# #not done
# #break 
c=1
while c<=5:
    print(c)
    if(c==3):
     break
    c+=1
#continue    
d=0
while d<=5:
   if(d==3):
      d+=1
      continue
   print(d)
   d+=1
#continue for odd and even
e=1
while(e<=10):
   if(e%2 !=0):
      e+=1
      print(e)
      e+=1
     
#for loop
veggies=["potato","brinjal","ladyfinger","chillies"]
for val in veggies:
   print(val)
tup=(1,3,5,7,8)  
for num in tup:
   print(num)
str="poojachand"
for char in str:
   if (char=='o'):
      print("o found")
      break
   print(char)
else:
   print("code ended")
numbs=[1,4,9,16,25,36,49,64,81,100]
for el in numbs:
   print(el)
nbr=(1,4,9,16,25,36,49,64,81,100,49)
f=49
idx=0
for el in nbr:
   if(el==f):
      print("number found at idx",idx)
      idx+=1
# range       
for g in range(10):#range(stop)
   print(g)
for  h in range(2,10): #range(start,stop)
   print(g)
for j in range(2,10,2):#range(start,stop,step)
   print(j)  
#practice time
#  using for and  range   
for k in range(1,101):
   print(k)
for ab in range(100,0,-1):
   print(ab)
#multiplication of any number 
l=int(input("Enter any number: ")) 
for m in range(1,11):
   print(l* m)
#pass statement
for cd in range(8):
   pass  
#practice time 
# sum of fisrt n numbers
ef=5
sum=0
for gh in range(1,ef+1):
   sum +=gh
#same prblm using while loop
er=7
add=0
ac=1
while ac<=er:
   add +=er
   ac+=1
   print("total sum is :"  , add)
   #factorial of a number   
de=5
fact=1
for ad in  range(1,de+1):
   fact*=ad
   print("factorial of a number is:  ",fact)
