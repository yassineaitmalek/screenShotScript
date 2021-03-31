# pip install pywin32
# pip install pillow
# pip install win10toast
# pip install pynput

import win32clipboard as clip
import win32con
from io import BytesIO
from PIL import ImageGrab
import datetime as date
import os
import pyautogui as w
from time import sleep
from win10toast import ToastNotifier
from pynput.mouse import Listener


class Screenshot():
    def __init__(self,mode):
        self.box = []
        self.msg = None
        self.mode = mode
        self.output = BytesIO()
        self.y,self.m,self.d = str(date.datetime.now().year),str(date.datetime.now().month),str(date.datetime.now().day)
        self.h,self.min,self.s = str(date.datetime.now().hour),str(date.datetime.now().minute),str(date.datetime.now().second)
        self.path = str(os.path.expanduser("~"))+"\Pictures\Screenshots\\"+'ScreenShot ('+self.y+"-"+self.m+"-"+self.d+"-"+self.h+"-"+self.min+"-"+self.s+").png"
        self.title = ""
        self.win = w.getActiveWindow()
        self.toast = ToastNotifier()   
        self.run()

    def on_click(self,x, y, button, pressed):
        if self.mode == 'f' : return False
        elif self.mode == 'w' :
            if pressed == True  : 
                self.win = w.getActiveWindow()
                self.title = w.getActiveWindowTitle()
                return False
        elif self.mode == 'a' :
            self.box.append([x, y])
            if not pressed: return False

    def full(self) :
        self.box = [0,0,1920,1080]
        self.msg = "Full Screenn Screenshot is saved and copied to clipboard"

    def window(self) : 
        dic = self.win.__dict__
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

        self.box =  [a,b,c,d]
        self.msg = "window Screenshot of "+self.title+" is saved and copied to clipboard"

    def area(self) :
        
        a,b,c,d = self.box[0][0],self.box[0][1],self.box[1][0],self.box[1][1]
        
        wid = c - a
        hei = d - b

        if wid<0 and hei<0 : a,b,c,d = c,d,a,b
        elif hei < 0 : a,b,c,d = a,b+hei,c,d-hei
        elif wid < 0 : a,b,c,d = a+wid,b,c-wid,d

        self.box =  [a,b,c,d]
        self.msg = "The selected area Screenshot is saved and copied to clipboard"

    def take_a_shot(self) :
        image = ImageGrab.grab(bbox = self.box)
        
        image.convert('RGB').save(self.output, 'BMP')
        data = self.output.getvalue()[14:]
        self.output.close()

        clip.OpenClipboard()
        clip.EmptyClipboard()
        clip.SetClipboardData(win32con.CF_DIB, data)
        clip.CloseClipboard()
       
        image.save(self.path)
        
        # self.toast.show_toast("ScreenShot",self.msg,duration=4,threaded=False)

    def run(self) :

        with Listener( on_click=self.on_click) as listener:
            listener.join()

        if self.mode =='f': 
            self.full()
        elif self.mode =='a': 
            self.area()
        elif self.mode =='w': 
            self.window()
        self.take_a_shot()
        print ("taken")


a = Screenshot('f') 

