from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        img_top=Image.open(r"C:\Users\Swaraj\Desktop\FACE RECOGNITION SYSTEM\images\student3.jpg")
        img_top=img_top.resize((1290,200),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1290,height=200)









if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()