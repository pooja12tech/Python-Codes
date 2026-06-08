#LISTS
marks=[12.00,89.7,67.5,45,98.1,78.3]
print(type(marks))
print(marks[0])
print(marks[2])
#changing the number in 4th indexing
marks[4]=77
print(marks[4])
#lists slicing
print(marks[2:5])
#negative slicing
print(marks[-5:-1])
print(marks.append(85.4))
print(marks)
print(marks.sort())
print(marks)
print(marks.sort(reverse=True))
print(marks)
marks.reverse()
print(marks)
marks.insert(2,36)
print(marks)
marks.remove(36)
print(marks)
marks.pop(6)
print(marks)
#tuple
#use of () unlike list which use []
tup=(3,4.5,6,8,5.5)
print(tup[0])
print(tup[4])
print(type(tup))
#tuple indexing
print(tup[3:5])
print(tup.index(8))
print(tup.count(5.5))
#practice time
movies=[]

mov1=input("Name of 1st movie: ")
mov2=input("Name of 2nd  movie :  ")
mov3=input("Name of 3rd movie :  ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies) 