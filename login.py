from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter
import mysql.connector
import random
import cv2
import os
import csv
import numpy as np
from time import strftime
from datetime import datetime
from tkinter import filedialog
from main import Face_Recognition_System
from face_recognition import Face_recognition
from attendence import Attendance
from student import Student
from train import Train
from tkinter import Toplevel


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        lbl_bg=Label(self.root,bg="purple")
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg="lightblue")
        frame.place(x=610,y=170,width=340,height=450)

        title_lbl=Label(text="Login System",font=("times new roman",30,"bold"),fg="white",bg="Purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)

    #label
        username=lbl=Label(frame,text="Username",font=("times new roman",16,"bold"),fg="Black",bg="lightblue")
        username.place(x=100,y=10)

        self.txtuser=ttk.Entry(frame,font=("times new roman",16,"bold"))
        self.txtuser.place(x=10,y=50,width=320)

        password=lbl=Label(frame,text="Password",font=("times new roman",16,"bold"),fg="Black",bg="lightblue")
        password.place(x=100,y=100)

        self.txtpass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        self.txtpass.place(x=10,y=140,width=320)

        #loginbutton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="Black",bg="white",activebackground="darkblue",activeforeground="white")
        loginbtn.place(x=100,y=200,width=120,height=35)


        #registerbutton
        registerbtn=Button(frame,text="New user register",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,bg="lightblue",fg="Black",activebackground="darkblue",activeforeground="lightblue")
        registerbtn.place(x=(-5),y=240,width=220,height=35)

        #forgetpassbtn
        registerbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",11,"bold"),borderwidth=0,fg="Black",bg="lightblue",activebackground="darkblue",activeforeground="lightblue")
        registerbtn.place(x=190,y=240,width=160,height=35)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    # def clear(self):
    #     self.txtuser.delete(0, 'end')  # Clear the username entry field
    #     self.txtpass.delete(0, 'end')  # Clear the password entry field


    def login(self):
          if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
          elif self.txtuser.get()=="abhi" and self.txtpass.get()=="abhipass":
              messagebox.showinfo("Success","Welcome Face Recognition Attendence System",parent=self.root)
          else:
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,plese login new password",parent=self.root2)
                









    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to rset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="mydata")
            my_cursor=conn.cursor() 
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)           
            if row==None:
                messagebox.showerror("Error","Enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="Black",bg="lightblue")              
                l.place(x=0,y=10,relwidth=1)
        
                security_Q=Label(self.root2,text="Select Security Questions?",font=("times new roman",17,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",17,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Fav Gym session","Your Fav Food")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",17,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",17,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=260,width=250)

                btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white", bg="green")
                btn.place(x=100,y=300)

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
#variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()        
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()        
        self.var_pass=StringVar()
        self.var_confpass=StringVar()        
        self.var_check=IntVar()
        
        
        lbl_bg=Label(self.root,bg="purple")
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=360,y=100,width=640,height=650)

        register_lbl=Label(text="Register",font=("times new roman",30,"bold"),fg="white",bg="Purple")
        register_lbl.place(x=0,y=0,width=1530,height=45)

        fname=Label(frame,text="First Name",font=("times new roman",17,"bold"),bg="white")
        fname.place(x=20,y=20)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",17,"bold"))
        fname_entry.place(x=20,y=60,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",17,"bold"),bg="white")
        l_name.place(x=300,y=20)

        self.txt_lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",17,"bold"))
        self.txt_lname_entry.place(x=300,y=60,width=250)

        contact=Label(frame,text="Contact",font=("times new roman",17,"bold"),bg="white")
        contact.place(x=20,y=100)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",17,"bold"))
        self.txt_contact.place(x=20,y=140,width=250)


        email=Label(frame,text="Email",font=("times new roman",17,"bold"),bg="white")
        email.place(x=300,y=100)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",17,"bold"))
        self.txt_email.place(x=300,y=140,width=250)


        
        security_Q=Label(frame,text="Select Security Questions?",font=("times new roman",17,"bold"),bg="white")
        security_Q.place(x=20,y=190)

        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",17,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Fav Gym session","Your Fav Food")
        self.combo_security_Q.place(x=20,y=230,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",17,"bold"),bg="white")
        security_A.place(x=300,y=190)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=300,y=230,width=250)

        pswd=Label(frame,text="Password",font=("times new roman",17,"bold"),bg="white")
        pswd.place(x=20,y=280)


        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",17,"bold"))
        self.txt_pswd.place(x=20,y=320,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",17,"bold"),bg="white")
        confirm_pswd.place(x=300,y=280)


        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",17,"bold"))
        self.txt_confirm_pswd.place(x=300,y=320,width=250)

#check button
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",17,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=20,y=380)


        b1=Button(frame,text="Register Now",command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="Green")
        b1.place(x=20,y=440,width=220)

        b1=Button(frame,text="Login Now", borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="Green")
        b1.place(x=300,y=440,width=220)
    

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="rootpassword",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")    



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
    main()
