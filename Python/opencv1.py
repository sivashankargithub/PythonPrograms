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
    cv2.imwrite('2_3img2_280923.png',matrixcollage)

f1=open("cv.txt","r")
a1=f1.readline().replace('\n','')
a2=f1.readline().replace('\n','')
a3=f1.readline().replace('\n','')
a4=f1.readline().replace('\n','')
a5=f1.readline().replace('\n','')
a6=f1.readline().replace('\n','')
opencv1(a1,a2,a3,a4,a5,a6)
f1.close()
