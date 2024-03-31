f1=open("CSK.txt","r")
names=[]
countries=[]
while f1:
    s1=f1.readline().replace("\n","")
    if s1=="":
        break
    csk=s1.split(",")
    names.append(csk[0])
    countries.append(csk[1])
for i in range(0,len(names),1):
    print(names[i])
