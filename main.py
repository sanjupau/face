from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from help import Help
from chatbot import ChatBot



class Face_Recognition_Attendence_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")


        # first img
        img=Image.open(r"images\face.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second img
        img1=Image.open(r"images\au.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third img
        img2=Image.open(r"images\students.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        # bg img
        img3=Image.open(r"images\bg.jpg")
        img3=img3.resize((1600,580),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1600,height=580)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)


        #===================== TIME==================
        def time():
            string = strftime('%H:%M:%S ')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=45) 
        time()  



        # student button
        img4=Image.open(r"images\stud.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
  
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=150)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=250,width=220,height=30)


        # detect face button
        img5=Image.open(r"images\face detector.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=100,width=220,height=150)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=250,width=220,height=30)


        # attendance button
        img6=Image.open(r"images\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_pannel)
        b1.place(x=700,y=100,width=220,height=150)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_pannel,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=250,width=220,height=30)


        # help desk button
        img7=Image.open(r"images\help desk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=150)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=250,width=220,height=30)


        # train button
        img8=Image.open(r"images\train data.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=300,width=220,height=150)

        b1_1=Button(bg_img,text="train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=450,width=220,height=30)


        # photos button
        img9=Image.open(r"images\photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=220,height=150)

        b1_1=Button(bg_img,text="photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=450,width=220,height=30)



        # chatbot button
        img10=Image.open(r"chatbot.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=700,y=300,width=220,height=150)

        b1_1=Button(bg_img,text="ChatBot",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=450,width=220,height=30)

        # exit button
        img11=Image.open(r"images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=300,width=220,height=150)

        b1_1=Button(bg_img,text="exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=450,width=220,height=30)


    def open_img(self):
        os.startfile(r"data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project?", parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


    #======function buttons=======

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)






if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_Attendence_System(root)
    root.mainloop()        
