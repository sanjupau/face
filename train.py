from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        img_top=Image.open(r"images\student3.jpg")
        img_top=img_top.resize((1290,200),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1290,height=200)


        #Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=0,y=250,width=1290,height=60)


        img_bottom=Image.open(r"images\got.jpg")
        img_bottom=img_bottom.resize((1290,400),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=300,width=1290,height=400)



    def train_classifier(self):
        data_dir=(r"data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #Gray_scale_image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        
        #=====Train the Classifier=====
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed !!!",parent=self.root)









       







if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()