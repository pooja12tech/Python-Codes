# class Student:
#     name="karan kumar"
#     def __init__(self):
#         print(self)
#         print("adding new students to database")
# s1=Student()
# print(s1)
# class Car:
#     color="blue"
#     brand="mercedes"
# car1= Car()
# print(car1.color)
# print(car1.brand)
class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("addding new studens to the databases")
s1=Student("karan")
print(s1.name)
s2=Student("arjun")
print(s2.name)