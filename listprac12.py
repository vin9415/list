#its represented by square bracket .its always in ordered.
#1.we can add duplicate values in list.
#we can add different type of data in list.
#we can add index also
x=["red","blue","black"]
y=["bmw","ino","nano"]
print(x[1])

x[2]= "green"#repacement

print(x)

x[1:2]="yellow", "pink"
print(x)
x.insert(2,"indigo") #it can add the object
print(x)
x.append("nhkk")#it can add object but in lasst
print(x)
x.extend(y)#we can add two list in one
print(x)
x.remove("green")
print(x)
x.pop(1)
print(x)#pop removes specific indexx
del x[2]
print(x)

for k in x:
    print(k)
for k in range(len(x)):
    print(x)
while k< len(x):
    k+=1