# pip install pywin32
# pip install pillow
# pip install win10toast
import win32clipboard as clip
import win32con
from io import BytesIO
from PIL import ImageGrab
import datetime as date
import os
from win10toast import ToastNotifier


image = ImageGrab.grab(bbox = [])
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
toast.show_toast("ScreenShot","Full Screenn Screenshot is saved and copied to clipboard",duration=2,threaded=False)



