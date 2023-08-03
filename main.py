from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from student import Student
from train import Train
import os
import cv2
from time import strftime
from datetime import datetime
from face_recognition import Face_recognition
from attendence import Attendance
from tkinter import Toplevel


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # bg_img=Label(self.root,image=self.photoimg3)
        # bg_img.place(x=0,y=130,width=1530,height=710)
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(font=('times new roman', 20,'bold'),bg="black", fg="white")
        lbl.place(x=550,y=(-15),width=410,height=60)
        time()
#student button
        img4=Image.open(r"clzphoto\abhi1.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(image=self.photoimg4, command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220, height=220)

        b1_1=Button(text="Students Details",command=self.student_details, cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=200,y=300,width=220, height=40)

        #detect face
        img5=Image.open(r"clzphoto\deetcface.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220, height=220)

        b1_1=Button(text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=500,y=300,width=220, height=40)


        #Attendence face
        img6=Image.open(r"clzphoto\attend.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220, height=220)

        b1_1=Button(text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=800,y=300,width=220, height=40)


        # #Help Desk
        # img7=Image.open(r"clzphoto\helpdesk.jpg")
        # img7=img7.resize((220,220),Image.ANTIALIAS)
        # self.photoimg7=ImageTk.PhotoImage(img7)

        # b1=Button(image=self.photoimg7,cursor="hand2")
        # b1.place(x=1100,y=100,width=220, height=220)

        # b1_1=Button(text="Help Desk",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        # b1_1.place(x=1100,y=300,width=220, height=40)


#Train Button
        img8=Image.open(r"clzphoto\Traind.jfif")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(image=self.photoimg8,cursor="hand2",command=self.tain_data)
        b1.place(x=200,y=400,width=220, height=220)

        b1_1=Button(text="Train Data",cursor="hand2",command=self.tain_data,font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=200,y=600,width=220, height=40)



#Photos Button
        img9=Image.open(r"clzphoto\photos.jfif")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220, height=220)

        b1_1=Button(text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=500,y=600,width=220, height=40)



# #Developer Button
#         img10=Image.open(r"clzphoto\developerss.jpg")
#         img10=img10.resize((220,220),Image.ANTIALIAS)
#         self.photoimg10=ImageTk.PhotoImage(img10)

#         b1=Button(image=self.photoimg10,cursor="hand2")
#         b1.place(x=800,y=400,width=220, height=220)

#         b1_1=Button(text="Developer",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
#         b1_1.place(x=800,y=600,width=220, height=40)


#Exit Button
        img11=Image.open(r"clzphoto\exitBut.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(image=self.photoimg11,cursor="hand2",command=self.isExit)
        b1.place(x=800,y=400,width=220, height=220)

        b1_1=Button(text="Exit",cursor="hand2",command=self.isExit,font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=800,y=600,width=220, height=40)



    def open_img(self):
        os.startfile("data")







#function button

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def tain_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
 
    def open_img(self):
        os.startfile("data")

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
 

    def isExit(self):
        self.isExit=tkinter.messagebox.askyesno("Face recognition system","Are you sure want to exit?")
        if self.isExit>0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
