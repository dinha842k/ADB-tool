from ppadb.client import Client
import os
import cv2
from time import sleep
adb = Client(host='127.0.0.1', port=5037)

devive = adb.devices()[0]


def ScreenCap(device,filename,isDelete = False):
    png = devive.screencap()
    with open(filename, 'wb') as f:
        f.write(png)
    img = cv2.imread(filename)
    if isDelete:
        os.remove(filename)
    print("[note]size of img : ",end="")
    print(img.shape)
    return cv2.resize(img, (360, 640))
       
img = ScreenCap(devive, "01.png",True)
# listIMG = [img]
print(img.shape)
xh = 1280 / 640
xw = 720 / 360

def callback(event,x,y,flag,param):
    if event == cv2.EVENT_MOUSEMOVE:
        print("x = " + str(x), end="\t")
        print("y = " + str(y))
    
    if event == cv2.EVENT_RBUTTONDBLCLK:
        print("msg from double click!")
        text = input('enter text to send : ')
        text = text.replace(" ", "%s")
        print(text)
        devive.input_text(text)

    if event == cv2.EVENT_RBUTTONUP:
        print("got a msg!")
        try:
            global xh
            global xw
            devive.input_tap(x*xh,y*xw)
        except:
            return
        sleep(1)
        print("sleep done!")
        img = ScreenCap(devive, "01.png", True)
        cv2.imshow('1',img)
        
cv2.namedWindow('1')
cv2.setMouseCallback('1',callback)

cv2.imshow('1', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
