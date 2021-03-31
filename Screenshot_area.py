
import win32clipboard as clip
import win32con
from io import BytesIO
from PIL import ImageGrab
import datetime as date
import os
import pyautogui as w
import time as t
# from win10toast import ToastNotifier
from pynput.mouse import Listener

l = []

def on_click(x, y, button, pressed):
        
    l.append((x, y))
    if not pressed: return False

with Listener( on_click=on_click) as listener:
    listener.join()

a,b,c,d = l[0][0],l[0][1],l[1][0],l[1][1]



print(a,b,c,d)

wid = c - a
hei = d - b

print(wid,hei)

if wid<0 and hei<0 : a,b,c,d = c,d,a,b
elif hei < 0 : a,b,c,d = a,b+hei,c,d-hei
elif wid < 0 : a,b,c,d = a+wid,b,c-wid,d
print(a,b,c,d)

image = ImageGrab.grab(bbox = (a,b,c,d))
output = BytesIO()
image.convert('RGB').save(output, 'BMP')
data = output.getvalue()[14:]
output.close()
clip.OpenClipboard()
clip.EmptyClipboard()
clip.SetClipboardData(win32con.CF_DIB, data)
clip.CloseClipboard()
y,m,d = str(date.datetime.now().year),str(date.datetime.now().month),str(date.datetime.now().day)
h,min,s = str(date.datetime.now().hour),str(date.datetime.now().minute),str(date.datetime.now().second)
path = str(os.path.expanduser("~"))+"\Pictures\Screenshots\\"+'ScreenShot ('+y+"-"+m+"-"+d+"-"+h+"-"+min+"-"+s+").png"
image.save(path)



# toast = ToastNotifier()
# toast.show_toast("ScreenShot","area Screenshot"+" is saved and copied to clipboard",duration=4,threaded=False)