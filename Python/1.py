f1=open("Doctors.txt","r")
list1=f1.readlines()
f2=open("1.html","r")
info1=f2.read()
print(list1)
print(info1)
for i in list1:
    with open(f"{i.rstrip().html}") as file:
        file.write(info1.replace("DOCTOR",i))
    
