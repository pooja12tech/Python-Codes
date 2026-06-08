#dictionary
info={ 
    "key" : "value",
    "student1" : "pooja",
    "learning": "coding",
    "topics" : ("dict","set"),
    "subjects": ["python","C++","R"]
}
print(info)
print(type(info))
print(info["learning"])
      #update some value
info["student1"]="somename"
print(info)
# empty dictionary
null_dict={}
#nested dictionary 
student={
    "name": "Rahul ",
    "subject":{
        "phy": 97,
        "chem":98,
        "maths":96
    }     
}
print(student["subject"]["chem"])
print(student.keys())
print(list(student.keys()))
print(len(student))
print(student.values())
print(student.items())
print(student.get("name"))
#update an insert some other details
student.update({"city" : "delhi"})
print(student)
#SETS IN PYTHON 
collection ={1,2,2,2,"hello,""world",4}
bundle={2,3,5,"pooja",0}
print(collection)
print(len(collection)) #total bumber of items
#empty set syntax
house=set()
#add elements 
collection.add(3)
collection.add(0)
print(collection)
#elminate and remove some element
collection.remove(2)
print(collection)
#random value elimination
print(collection.pop())
#union and intersection 
print(collection.union(bundle))
print(bundle)
print(collection.intersection(bundle))
#practice time
dict_1={
    "cat":"an animal",
    "table":["a piece of furniture", "list of facts and figures"]
}
print(dict_1)
 #2 quetsion
subjects_c={
    "python","java","C++","pyhton","javascript","java","python","java","C++","C"
}
print("class required",len(subjects_c))
#question 3
marks={}
x=int(input('ENTER PHYSICS MARK:'))
marks.update({"PHYSICS": x})
x=int(input('ENTER MATHS MARKS : '))
marks.update({"MATHS": x})
x=int(input('ENTER CHEM MARKS :' ))
marks.update({"CHEM": x})
print(marks)
# 4th question 
values={
    ("float",9.0),
    ("int",9),
}

print(values)
