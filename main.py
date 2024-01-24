from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb 
from PIL import Image, ImageTk

welcom_splash=tb.Window(themename="solar")
Wellcom_img = Image.open("F:\SmartGUI\Edu-Smart(white).png")
eduimage = ImageTk.PhotoImage(Wellcom_img)
L_eduimage = tb.Label(image=eduimage)
L_eduimage.image = eduimage 
L_eduimage.place(relx=.5, rely=.5,anchor= CENTER)#make Edu smart photo in the center
welcom_splash.attributes("-fullscreen", True)
welcom_splash.geometry('1200x600')#set the splash geometer
welcom_splash.overrideredirect(True)#hide the bar
def main_window():
    welcom_splash.destroy()#destroy the splash screen
    root = tb.Window(themename="superhero")
    root.title("EDU Smart")
    root.iconbitmap('F:\SmartGUI\Edu-Smart(white).ico')
    root.attributes("-fullscreen", True)
    root.geometry('500x600')

    


    



welcom_splash.after(3000,main_window)








mainloop()