#assigning elements to different lists
a=[int(x) for x in input().split()]
print("How many nos. you want to add = ")
n=int(input())
for i in range(n):
    print("no. which you want to add = ")
    f=input()
    a.append(f)
print(a)

#accessing elements from a tuple
tu=("c","c++","python","java","ruby","PHP")
print(tu)
print("how many elements you want to access = ")
m=int(input())
for i in range(m):
    print("which element you want to access = ")
    b=int(input())
    print(tu[b])

#deleting different dictionary elements
ipl={"csk":"MS Dhoni",
    "rcb":"Virat kohli",
    "mi":"Rohit Sharma",
    "dd":"Rishabh Pant"}
print(ipl)
print("how many elements you want to delete = ")
o=int(input())
for i in range(o):
    print("which element you want to delete = ")
    c=input()
    ipl.pop(c)
print(ipl)
