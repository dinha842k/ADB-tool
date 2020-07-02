import cv2
import pytesseract
import numpy

img = cv2.imread("test1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
tem = cv2.imread("test1TEM.png")
tem = cv2.cvtColor(tem,cv2.COLOR_BGR2GRAY)


result = cv2.matchTemplate(img,tem,cv2.TM_CCOEFF_NORMED)

cv2.imshow("1", img)
#cv2.imshow("2",tem)
cv2.imshow("result",result)


print(result)
print("result shape : ", end="")
print(result.shape)
print(tem.shape)
print(img.shape)
print("where is : ", end="")
print(numpy.where(result >= 0.7))

cv2.waitKey(0)

cv2.destroyAllWindows()
