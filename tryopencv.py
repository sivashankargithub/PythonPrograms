import cv2 as cv
img1=cv.imread("modi.jpg")
img2=cv.imread("manmohan.png")
img3=cv.imread("ATV.png")
img4=cv.imread("IG.jpg")
img5=cv.imread("LBS.jpg")
img6=cv.imread("nehru.jpg")

r1=cv.hconcat((img1,img2))
r2=cv.hconcat((img3,img4))
r3=cv.hconcat((img5,img6))

r4=cv.vconcat((r1,r2,r3))
r5=cv.resize(r4,(1000,800))
cv.imshow("full",r5)
