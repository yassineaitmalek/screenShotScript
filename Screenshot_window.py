
import win32clipboard as clip
import win32con
from io import BytesIO
from PIL import ImageGrab
import datetime as date
import os
import pyautogui as w
import time as t
from win10toast import ToastNotifier
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
      if pressed == True  : return False

with Listener( on_click=on_click) as listener:
    listener.join()

t.sleep(0.1)
win = w.getActiveWindow()
title = w.getActiveWindowTitle()
dic = win.__dict__
rect = dic["_rect"]

if rect.x ==-9 :a = 0
else : a = rect.x
if rect.y ==-9 :b = 0
else : b = rect.y
if rect.w ==1938 :wi = 1920
else : wi = rect.w
if rect.h ==1048 :hi = 1030
else : hi = rect.h
c = a + wi
d = b + hi


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
toast = ToastNotifier()
toast.show_toast("ScreenShot","window Screenshot of "+title+" is saved and copied to clipboard",duration=4,threaded=False)