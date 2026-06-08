#conditional statements
age=20
if(age>=18):
    print("eligible to drive")
    #if elif statements
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):
     print("go")
elif(light=="yellow"):
    print('WAIT')
#if else condititons
num=10
if(num<=8):
  print('less than 9')
elif(num==8):
    print('equal to 8')
else:
    print('greater than 9')
#marks 
marks=int(input("Enter the marks : "))
if(marks>=90):
    print("A grade awarded")
elif(marks<90 and marks>=80):
    print('B grade awarded')
elif(80>marks>=70):
    print("C grade is awarded")
elif(70>marks and marks>=60):
    print("D grade is awarded")
else:
    print('Fail')
 #practice time
number=int(input('Enter a number: '))
if(number%2==0):
    print('Number is even')
else:
    print('number is odd')
#multiple of 7
digit=int(input("Enter a number "))
if(digit%7==0):
    print('multiple of 7')
else:
    print('not a multiple of 7')
   