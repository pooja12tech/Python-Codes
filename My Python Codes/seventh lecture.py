# f=open("demo.txt","r+")
# data= f.read(5)#for raedimg specifc character ,while in () the whole text is taken into consideration
# print(data)
# print(type(data))
# line1 =f.readline()
# print(line1) 
# f.write("the detsination where to reach")
# f.close()
#use of with syntax
# with open("demo.txt","r")as f:
#     data=f.read()
#     print(data)
# #deleting a file 
# import os
# os.remove("sample.txt")
#practice time
with open("practice.txt","r")as f:
    # f.write("hi ,I'm POOJA\nwe are learning file I/o\n")
    # f.write("using Java.\nI like programming in java.")
    #2nd question
    data=f.read()
new_data=data.replace("Java","Python")
print(new_data)
#3rd question
# def check_for_word():
#     word="xlearning"
#     with open("pratice.txt","r")as f:
#         data=f.read()
#         if (data.find(word)!=-1):
#             print("Found")
#         else:
#             print("not found")
# def check_for_line():
#     word="learning"
#     data=True
#     with open("practical.txt","r")as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 line_no +=1 
#     return -1
# print(check_for_line())        
# #4th question  
count=0
with open("practice.txt","r") as f:
    data=f.read()
    nums=data.split("  ,")
    for val in nums:
        if(int(val) %2 == 0):
            count+=1
print(count)
        