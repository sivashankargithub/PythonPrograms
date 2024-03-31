names=[]
english=[]
math=[]
engToppers=[]
mathToppers=[]
f1=open("in1.txt","r")
while f1:
    info1=f1.readline()
    if info1=="":
        break
    list1=info1.split(",")
    names.append(list1[0])

    temp1=list1[3]
    list2=temp1.split(":")
    english.append(int(list2[1]))

    temp1=list1[4]
    list2=temp1.split(":")
    math.append(int(list2[1]))   
maxEng=max(english)
maxMath=max(math)
len1=len(names)
for i in range(0,len1,1):
    if(english[i]==maxEng):
        engToppers.append(names[i])
    if(math[i]==maxMath):
        mathToppers.append(names[i])
print(engToppers,"are the toppers in English with",maxEng)
print(mathToppers,"are the toppers in Maths with",maxMath)


    
