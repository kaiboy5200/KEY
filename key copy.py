import win32gui, win32api, win32con,time
from win32api import GetSystemMetrics
from PIL import ImageGrab

def PilImage(x,y):
    a, b = GetSystemMetrics(0), GetSystemMetrics(1)  # Python獲取屏幕分辨率
    im = ImageGrab.grab((0,0,a,b))#與座標不同，這裏0，0，1，1是一個像素，而座標是從0~1919的
    pix = im.load()

    return pix[x,y]

def DisplaySize():
    return GetSystemMetrics(0), GetSystemMetrics(1)  # Python獲取屏幕分辨率

def LeftClick(x, y):    # 鼠標左鍵點擊屏幕上的座標(x, y)
    win32api.SetCursorPos((x, y))    # 鼠標定位到座標(x, y)
    print(x,y)
    # 注意：不同的屏幕分辨率會影響到鼠標的定位，有需求的請用百分比換算
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)    # 鼠標左鍵按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 鼠標左鍵彈起
    
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN + win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 測試

def PressOnce(x):    # 模擬鍵盤輸入一個按鍵的值，鍵碼: x
    win32api.keybd_event(x, 0, 0, 0)


'''
# 測試
a, b = DisplaySize()
print(a,b)
LeftClick(30, 30)  # 點擊
PressOnce(13)  # Enter
PressOnce(9)   # TAB
print(PilImage(80,546))
'''
# SetCursorPos', 'No error message is available' 用管理員身份運行pycharm
if __name__=="__main__":
    jisu=0
    ltime=0
    ntime=0
    time.sleep(5)
    print(PilImage(195, 1103))
    print(PilImage(513, 1336))
    print(PilImage(594, 1337))
    print(PilImage(682, 1343))
    print(PilImage(769, 1339))


    while 1:

        if PilImage(195, 1103)==(36, 38, 36):
            win32api.keybd_event(81,0,0,0) 
            win32api.keybd_event(81,0,win32con.KEYEVENTF_KEYUP,0)       
            jisu += 1
            ntime = time.time()-ltime
            ltime = time.time()
        elif PilImage(513, 1336)==(183, 180, 197):
            win32api.keybd_event(65,0,0,0) 
            win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)  
            jisu += 1
            ntime = time.time()-ltime
            ltime = time.time()
        elif PilImage(594, 1337)==(95, 155, 198):
            win32api.keybd_event(87,0,0,0) 
            win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)   
            jisu += 1
            ntime = time.time()-ltime
            ltime = time.time()
        elif PilImage(682, 1343)==(21, 48, 93):
            win32api.keybd_event(68,0,0,0) 
            win32api.keybd_event(68,0,win32con.KEYEVENTF_KEYUP,0)   
            jisu += 1
            ntime = time.time()-ltime
            ltime = time.time()
        elif PilImage(769, 1339)==(198, 142, 67):
            win32api.keybd_event(83,0,0,0) 
            win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0) 
            jisu += 1
            ntime = time.time()-ltime
            ltime = time.time()
        elif PilImage(594, 1337)==(95, 155, 198):
            win32api.keybd_event(87,0,0,0) 
            win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)   
            jisu += 1
            ntime = time.time()-ltime
            ltime = time.time()
        elif PilImage(682, 1343)==(211, 203, 218):
            win32api.keybd_event(68,0,0,0) 
            win32api.keybd_event(68,0,win32con.KEYEVENTF_KEYUP,0)                     
            jisu += 1
            ntime = time.time()-ltime
            ltime = time.time()
            pass

        time.sleep(0.1)








