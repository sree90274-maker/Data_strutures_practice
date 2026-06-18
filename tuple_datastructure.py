#tuple create in 4 ways:
#empty
tuple=()
print(type(tuple))
#creating tuple with elements
tuple=("tree","cat",1,3,10)
print(type(tuple))
print("___________________")
t=(10,)
print(type(t))
print("____________________")
name=input("Enter student name: ")
rollno=int(input("Enter roll number: "))
student=(name, rollno)
print(student)
print("__________________________")
t=eval(input("Enter tuple elements:"))
print(t)
#without parenthesis
t=10,20,30
print(type(t))
print("______________________")
emp_name=input("Enter employee name:")
salary=int(input("Enter salary:"))
employee=emp_name,salary
print(employee)
print("__________________________________")
tuple_1=20
print(type(tuple_1))
tuple_2=30,
print(type(tuple_2))





