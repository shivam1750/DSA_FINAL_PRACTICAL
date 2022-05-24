set1 = set()
set2 = set()
n = int(input("Enter the size of set1: "))
for i in range(n):
    a = input("Enter the element: ")
    set1.add(a)
m = int(input("Enter the size of set2: "))
for i in range(m):
    b = input("Enter the element: ")
    set2.add(b)
print("Set1 = ",set1)
print("Set2 = ",set2)
print("\n")

#union
set3 = set1.union(set2)
print("Union of set1 and set2 : ",set3)

#intersection
set4 = set1.intersection(set2)
print("Intersection of set1 and set2 : ",set4)

#relation between set

if set3>set4:
    print("Set3 is superset of set4")
elif set3<set4:
    print("set3 is subset of set4")
else :
    print("set3 is same as set4")

#difference
set5 = set3 - set4
print("Elements of set3 not present in set4: ",set5)

#removing all the values of set5
set5.clear()
print("After applying clear on sets Set5: ")
print("Set5 = ", set5)
