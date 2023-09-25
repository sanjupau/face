# import re
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Pannel")

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()


        # first header image  
        img=Image.open(r"C:\Users\Swaraj\Desktop\FACE RECOGNITION SYSTEM\images\reg1.png")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\Swaraj\Desktop\FACE RECOGNITION SYSTEM\images\student5.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd means border 
        main_frame.place(x=0,y=50,width=1570,height=550)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("verdana",12,"bold"),fg="black")
        left_frame.place(x=5,y=5,width=650,height=450)

        img_left=Image.open(r"C:\Users\Swaraj\Desktop\FACE RECOGNITION SYSTEM\images\student5.jpg")
        img_left=img_left.resize((630,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=630,height=130)

        left_inside_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=5,y=135,width=645,height=290)


        #======================= Text Boxes and Combo Boxes=============

        # Attendence id
        AttendanceId_label = Label(left_inside_frame,text="AttendanceID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        AttendanceId_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_id,font=("verdana",12,"bold"))
        AttendanceId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)


        #Student Roll
        roll_label = Label(left_inside_frame,text="Roll:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        roll_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_roll,font=("verdana",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(left_inside_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_name,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Department
        # dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        # dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        # dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #time
        time_label = Label(left_inside_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_time,font=("verdana",12,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_inside_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_date,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)


        #Attendance
        student_attend_label = Label(left_inside_frame,text="Attendance Status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_inside_frame,width=13,textvariable=self.var_attend,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)


        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=180,width=600,height=50)

        #Import button
        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Export button
        update_btn=Button(btn_frame,text="Export CSV",width=12,command=self.exportCsv,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)



         # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="black")
        right_frame.place(x=660,y=5,width=600,height=450)


         #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=20,width=580,height=400)


        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)


        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Roll","Name","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="Attendance ID")
        self.attendanceReport.heading("Roll",text="Roll")
        self.attendanceReport.heading("Name",text="Name")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attendance",text="Attendance Status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Roll",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attendance",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)
        

        

        # =========================Fetch Data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
            print(i)
        
  

     #==================import Csv================
    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


            #==================Export CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




    #=============Cursor Function========================

    def get_cursor(self,event=""):
        cursor_row = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_row)
        rows = content["values"]

        self.var_id.set(rows[0]),
        self.var_roll.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_time.set(rows[3]),
        self.var_date.set(rows[4]),
        self.var_attend.set(rows[5])  


    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")












if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()