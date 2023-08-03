from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
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
from tkinter import Toplevel

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









if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()