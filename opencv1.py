import cv2
def opencv1(n1,n2,n3,n4,n5,n6):
    import numpy as np
    
    src1 = cv2.imread(n1)
    src2 = cv2.imread(n2)
    src3 = cv2.imread(n3)
    src4 = cv2.imread(n4)
    src5 = cv2.imread(n5)
    src6 = cv2.imread(n6)

    r1=cv2.hconcat((src1,src2))
    r2=cv2.hconcat((src3,src4))
    r3=cv2.hconcat((src5,src6))
    
    matrixcollage=cv2.vconcat((r1,r2,r3))
    cv2.imwrite('please.png',matrixcollage)
    cv2.resize((800,600))
    cv2.imshow('temp',matrixcollage)

f1=open("cv.txt","r")
list1=[]
while f1:
    a1=f1.readline().replace('\n','')
    list1.append(a1)
    if f1=="":
        break
opencv1(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5])
f1.close()
