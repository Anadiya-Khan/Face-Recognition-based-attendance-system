from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import face_reconition_system
def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("face.ico")
        #First image
        img=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face3.webp")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#second image
        img1=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
#third image 
        img2=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\f3.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        img0=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\f3.jpg")
        img0=img0.resize((500,130),Image.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        f_lbl=Label(self.root,image=self.photoimg0)
        f_lbl.place(x=1500,y=0,width=500,height=130)
# bg image 
        img3=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\bg5.jpg")
        img3=img3.resize((1550,800),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1550,height=800)
        title_lbl=Label(bg_img,text="FACE RECOGNITION-BASED ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",20,"bold"),fg="white",bg="darkBlue")
        title_lbl.place(x=0,y=0,width=1550,height=30)
        frame=Frame(self.root,bg="darkblue")
        frame.place(x=610,y=170,width=340,height=450)
        get_start=Label(frame,text="Login here",font=("time new roman",20,"bold"),fg="white",bg="darkblue")
        get_start.place(x=90,y=70)
        username=Label(frame,text="Username : ",font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        username.place(x=70,y=150)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        password=Label(frame,text="Password : ",font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        loginbutton=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="darkblue",activebackground="darkblue")
        loginbutton.place(x=110,y=300,width=120,height=35)
        registrationbutton=Button(frame,text="New user register here",command=self.registerwindow,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="darkblue",activebackground="darkblue")
        registrationbutton.place(x=40,y=360,width=160)
        forgetbutton=Button(frame,text="Forgot Password",command=self.forgot_password,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="darkblue",activebackground="darkblue")
        forgetbutton.place(x=20,y=380,width=160)
    def registerwindow(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        elif self.txtuser.get()=="Anadiya" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success" ,"Welcome and mark your attendence",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Anadiya@786",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register1 where emailid=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                       ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and password",parent=self.root)
            else:
                open_main=messagebox.askyesno("Yes No","Access only admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=face_reconition_system(self.new_window)
                else:
                    if not open_main:
                        return    
                
            conn.commit() 
            conn.close()  
             
    def reset_password(self):
        if self.var_security.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root)
        elif self.var_securityconfirm.get()=="":
            messagebox.showerror("Error","Please Enter the answer",parent=self.root)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Anadiya@786",database="mydata")
            my_cursor=conn.cursor()
            query=("Select * from register1 where emailid=%s and SecurityQuestion=%s and securityanswer=%s")
            value=(self.txtuser.get(),self.var_security.get(),self.var_securityconfirm.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root)
            else:
                qury=("update register1 set password=%s where emailid=%s")
                value=(self.txt_newpass.get(),self.txtuser.get(),)
                my_cursor.execute(qury,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset , Login new password",parent=self.root)
                self.root2.destroy()   

    def forgot_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Anadiya@786",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register1 where emailid=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            ##print(row)
            if row==None:
                messagebox.showerror("My Error ","Please enter the valid username",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="white",bg="darkblue")
                l.place(x=0,y=10,relwidth=1)

                security=Label(self.root2,text="Security Question : ",font=("times new roman",15,"bold"),fg="white",bg="darkblue")
                security.place(x=50,y=100)

                self.var_security=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="reasonly")
                self.var_security["values"]=("Select","Your hobby","Your favourite food name","Your favourite game")
                self.var_security.place(x=50,y=130,width=250)
                self.var_security.current(0)

                security_confirm=Label(self.root2,text="Confirm security :",font=("times roman new ",15,"bold"),fg="white",bg="darkblue")
                security_confirm.place(x=50,y=180)

                self.var_securityconfirm=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.var_securityconfirm.place(x=50,y=210,width=250)

                new_password=Label(self.root2,text="New Password : ",font=("times roman new ",15,"bold"),fg="white",bg="darkblue")
                new_password.place(x=50,y=260)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=290,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("Times new rooman",15,"bold"),fg="white",bg="darkblue",activebackground="darkblue")
                btn.place(x=130,y=350)

##************************************Register window***************************************************
class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration form")
        self.root.geometry("1600x800+0+0")

        self.var_frname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.roll=StringVar()
        self.var_security=StringVar()
        self.var_securityconfirm=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()
        img3=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\bg5.jpg")
        img3=img3.resize((1550,800),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1550,height=800)
        frame = Frame(self.root,bg="darkblue")
        frame.place(x=520,y=100,width=550,height=550)
        registration_label=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="white",bg="darkblue")
        registration_label.place(x=170,y=20)
        first_name=Label(frame,text="First name : ",font=("times roman new ",12,"bold"),fg="white",bg="darkblue")
        first_name.place(x=50,y=80)
        self.var_frname=ttk.Entry(frame,font=("times new roman",13,"bold"))
        self.var_frname.place(x=50,y=110,width=200)
        last_name=Label(frame,text="Last name : ",font=("times roman new ",12,"bold"),fg="white",bg="darkblue")
        last_name.place(x=300,y=80)
        self.var_lname=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.var_lname.place(x=300,y=110,width=200)
        contact_num=Label(frame,text="Contact number : ",font=("times roman new ",12,"bold"),fg="white",bg="darkblue")
        contact_num.place(x=50,y=170)
        self.var_contact=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.var_contact.place(x=50,y=200,width=200)
        var_email=Label(frame,text="Email Id : ",font=("times roman new ",12,"bold"),fg="white",bg="darkblue")
        var_email.place(x=300,y=170)
        self.var_email=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.var_email.place(x=300,y=200,width=200)
        security=Label(frame,text="Security :",font=("times new roman",12,"bold"),fg="white",bg="darkblue")
        security.place(x=50,y=250)
        password=Label(frame,text="Password :",font=("times roman new ",12,"bold"),fg="white",bg="darkblue")
        password.place(x=50,y=250)
        self.var_pass=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.var_pass.place(x=50,y=280,width=200)
        password_confirm=Label(frame,text="Confirm password : ",font=("times roman new ",12,"bold"),fg="white",bg="darkblue")
        password_confirm.place(x=300,y=250)
        self.var_conpass=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.var_conpass.place(x=300,y=280,width=200)
        security=Label(frame,text="Security Question : ",font=("times new roman",12,"bold"),fg="white",bg="darkblue")
        security.place(x=50,y=330)
        self.var_security=ttk.Combobox(frame,font=("times new roman",12,"bold"),state="reasonly")
        self.var_security["values"]=("Select","Your hobby","Your favourite food name","Your favourite game")
        self.var_security.place(x=50,y=360,width=200)
        self.var_security.current(0)
        security_confirm=Label(frame,text="Confirm Security : ",font=("times roman new ",12,"bold"),fg="white",bg="darkblue")
        security_confirm.place(x=300,y=330)
        self.var_securityconfirm=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.var_securityconfirm.place(x=300,y=360,width=200)
        button=Button(frame,command=self.registration_dec,text="Ragister Now",font=("times new roman",12,"bold"),fg="white",bg="darkblue",activebackground="darkblue")
        button.place(x=100,y=450)
        cancel=Button(frame,text="Login Now",command=self.return_login,font=("times new roman",12,"bold"),fg="white",bg="darkblue",activebackground="darkblue")
        cancel.place(x=300,y=450)
        self.var_check=IntVar()
        self.checkbox=Checkbutton(frame,variable=self.var_check,text="I Agree with the terms and condition",font=("times new roman",12,"bold"),fg="white",bg="darkblue",activebackground="darkblue")
        self.checkbox.place(x=50,y=400)
    def registration_dec(self):
        if self.var_frname.get()=="" or self.var_contact.get()=="" or self.var_security.get()=="Select":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.var_pass.get()!=self.var_conpass.get():
            messagebox.showerror("Error","Password and confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree on term and condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Anadiya@786",database="mydata")
            my_cursor=conn.cursor()
            query=("Select * from register1 where emailid=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register1 values(%s,%s,%s,%s,%s,%s,%s)" ,(
                                                                                           self.var_frname.get(),
                                                                                           self.var_lname.get(),
                                                                                           self.var_contact.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_security.get(),
                                                                                           self.var_pass.get(),
                                                                                           self.var_securityconfirm.get()
                                                                                        ))
                
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successfully",parent=self.root)
    def return_login(self):
        self.root.destroy()
if __name__ == "__main__":
    main()