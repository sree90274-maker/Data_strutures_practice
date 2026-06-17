#questions on list methods
#append()
data=[3,4,5.6,10,4,12,"fruits",{"apples":2},2+5j]
data.append("banana")
print(data)
#extend()
list=[12,13,14.1,14,151,10]
list.extend("durga")
print(list)
print("____________________________")
l=[1,2,3,4,5]
l.extend(range(10))
print(l)
print("____________________________________")
l=[1,2,3,4,5]
l_1=[6,7,8,9,10]
l.extend(l_1)
print(l)
print("____________________________")
#insert(index,element)
names=["durga","nani","kayi",1,2,3,4]
names.insert(3,"lakshmi")
print(names)
print("__________________________")
#creating list objects,there are 5 ways
#1.create a empty list
fruits=[]
type(fruits)
print(type(fruits))
print(fruits)
print("_________________________")
#2.creating list object by using some known elaments
student_details_datatypes=[{"name":"durga","age":20,"marks":70,"passed":True},(100,200,300),True,False,10+5j,10.5,[1,2,3,4,5],{10,20,30,40,40,50}]
print(student_details_datatypes)
#3.creating list object with dynamic data
flowers=eval(input("enter a flowers names"))
print(type(flowers))
print("_____________________________")
cal_values=5+4-1
print(eval("cal_values"))
print("____________________________")
numbers=eval(input("Enter list: "))
print(type(numbers))
print("_______________________________")
student=["d","h"]
n=int(input("Enter number of students:"))
for i in range(0):
	student_name=input("Enter student name:")
	student.append(student_name)
print(student)
print("______________________________")
data=eval(input("Enter set:"))
print(data)
print("_____________________________")
fruits=eval(input("Enter a fruit_names:"))
print(fruits)
print("_____________________________")
values=eval(input("enter a values"))
print(values)
print("___________________________")
name="durga"
a=name.split()
print(a)
print("__________________________")
text="my village name is CLVP"
print(text.split())
print("____________________________")
text="applebananamangoorange"
result=text.split(" ", 2)
print(result)
print("_________________________________")
students=["Durga","pooji","Priya"]
print(students)
print("_______________________________")
students=(["Durga", "Ravi", "Priya"])
print(students)