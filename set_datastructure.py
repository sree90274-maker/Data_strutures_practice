print("____________________")
# BY using add function we can add only one element
birds = set()
birds.add("peacock")
birds.add(10)
birds.add(20)
birds.add("parrot")
print(birds)
print(type(birds))
print("________________________")
s=set()
s.add(100)
s.add(200)
s.add(300)
print(s)
print(type(s))
#set datastructures
#creating empty set
#set={}
#print(type(set))
#add multiple elements to the set by using update()
birds1="parrot","peacock"
birds=set()
birds.update(birds,range(1,6))
print(birds1)
print(birds)
print("___________________")
birds=set()
birds.update(["peacock","parrot",10, 20])
print(birds)
print("____________________________")
s={10, 20}
s.update([30, 40],(50, 60),{70, 80})
print(s)
print("____________________________")
s = set("num")
s.update([30, 40, 50])
print(s)
print("____________________________")
birds={"peacock","parrot"}
new_birds = ["sparrow","crow"]
birds.update(new_birds,"peacock",[19,90])
print(birds)
print("________________________")
#create cloned object in a set ,by using copy()
birds={"peacock","parrot","crow"}
birds_1=birds.copy()
print(birds_1)
print("________________________")
data={10,20,'d','u',100,2.5}
data_1=data.copy()
print(data_1)
print(id(data))
print(id(data_1))
print("________________________")
set={100,3,4,"durga",(1,2,3),100} #inside the set we cannot use list
set.remove((1,2,3))
print(set)
print("________________________")
birds={"peacock","parrot","crow"}
birds.discard("eagle")
print(birds)
print("________________________")
s={10,90,80}
s.discard(90)
print(s)
print("________________________")
data={100,2,3,4,4,6,"k","U",2.5}
data.pop()#pop takes no arguments
print(data)
print("________________________")
data={100,2,3,4,4,6,"k","U",2.5}
data.clear(100)
print(data)




