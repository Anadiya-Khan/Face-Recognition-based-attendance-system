from tkinter import*   #GUI 
from tkinter import ttk # stylish
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student import Student 
import os
from student import Student
from train import Train_data
from face_recognition import face_recognition1
from attendence import Atten
from developer import Developer
from help import Help
from chatbot import Chatbot
from Teacher import teacher 
from teacher_attendance import teacher_atten
from tea_face_recog import face_recognition2    # from file name import class name
       
class face_reconition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face recognition system")
        self.root.wm_iconbitmap("face.ico")
#First image
        img=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face3.webp")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#second image
        img13=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face.png")
        img13=img13.resize((500,130),Image.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        f_lbl=Label(self.root,image=self.photoimg13)
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

        title_lbl=Label(bg_img,text="FACE RECOGNITION-BASED ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",20,"bold"),fg="white",bg="darkBlue")
        title_lbl.place(x=0,y=0,width=1550,height=45)
      
        ######################## Time ###############################

        def time():
            string = strftime ("%d-%m-%Y %T:%M%p")
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("times new roman",12,"bold"),background="darkBlue",foreground="white")
        lbl.place(x=0,y=0,width=200,height=50)
        time()    
     # Student details
        img4 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\stud.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_detailes, cursor="hand2")
        b1.place(x=50, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_detailes, cursor="hand2", font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b1_1.place(x=50, y=320, width=220, height=40)

        # Teacher details
        img1 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\teacher.jpg")
        img1 = img1.resize((220, 220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b2 = Button(bg_img, image=self.photoimg1, command=self.teacher_details,cursor="hand2")
        b2.place(x=300, y=100, width=220, height=220)

        b2_1 = Button(bg_img, text="Teacher Details", command=self.teacher_details, cursor="hand2", font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b2_1.place(x=300, y=320, width=220, height=40)

        # Face Detection for Student
        img5 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face4.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b3 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_reconition2)
        b3.place(x=550, y=100, width=220, height=220)

        b3_1 = Button(bg_img, text="Face Detector of Student", cursor="hand2", command=self.face_reconition2, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b3_1.place(x=550, y=320, width=220, height=40)

        # Face Detection for Teacher
        imgb = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\Atten.jpg")
        imgb = imgb.resize((220, 220), Image.LANCZOS)
        self.photoimgb = ImageTk.PhotoImage(imgb)

        b3_t = Button(bg_img, image=self.photoimgb, cursor="hand2", command=self.face_recognition3)
        b3_t.place(x=800, y=100, width=220, height=220)

        b3_1_t = Button(bg_img, text="Face Detector of Teacher", cursor="hand2", command=self.face_recognition3, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b3_1_t.place(x=800, y=320, width=220, height=40)

        # Attendance details
        img6 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\p2.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b4 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.Attenden_data)
        b4.place(x=1050, y=100, width=220, height=220)

        b4_1 = Button(bg_img, text="Students Attendance", cursor="hand2", command=self.Attenden_data, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b4_1.place(x=1050, y=320, width=220, height=40)

        # Chatbot
        img7 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\p1.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b5 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.attendance)
        b5.place(x=1300, y=100, width=220, height=220)

        b5_1 = Button(bg_img, text="Teachers Attendance", cursor="hand2", command=self.attendance, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b5_1.place(x=1300, y=320, width=220, height=40)

        # Train face data
        img8 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\train.png")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b6 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b6.place(x=50, y=400, width=220, height=220)

        b6_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b6_1.place(x=50, y=620, width=220, height=40)

        # Student photos
        img9 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\multiple.png")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b7 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b7.place(x=300, y=400, width=220, height=220)

        b7_1 = Button(bg_img, text="Student Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b7_1.place(x=300, y=620, width=220, height=40)

        # Teacher photos
        imga = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\photo.jpg")
        imga = imga.resize((220, 220), Image.LANCZOS)
        self.photoimga = ImageTk.PhotoImage(imga)

        b7_t = Button(bg_img, image=self.photoimga, cursor="hand2", command=self.open_img1)
        b7_t.place(x=550, y=400, width=220, height=220)

        b7_1_t = Button(bg_img, text="Teacher Photos", cursor="hand2", command=self.open_img1, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b7_1_t.place(x=550, y=620, width=220, height=40)

        # Developer details
        img10 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\std2.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b8 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.develop)
        b8.place(x=800, y=400, width=220, height=220)

        b8_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.develop, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b8_1.place(x=800, y=620, width=220, height=40)

        # Chatbot
        img12 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\chat1.jpg")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b9 = Button(bg_img, image=self.photoimg12, cursor="hand2", command=self.chatbot)
        b9.place(x=1050, y=400, width=220, height=220)

        b9_1 = Button(bg_img, text="Chatbot", cursor="hand2", command=self.chatbot, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b9_1.place(x=1050, y=620, width=220, height=40)

        # Exit details
        img11 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b10 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b10.place(x=1300, y=400, width=220, height=220)

        b10_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), fg="white", bg="darkBlue")
        b10_1.place(x=1300, y=620, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def open_img1(self):
        os.startfile("data1")      

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognize","Are you sure you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return          

######################### function button ####################################
    def student_detailes(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def teacher_details(self):
        self.new_window=Toplevel(self.root)
        self.app =teacher(self.new_window)    

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_data(self.new_window)

    def face_reconition2(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition1(self.new_window)

    def face_recognition3(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition2(self.new_window)    

    def Attenden_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Atten(self.new_window)

    def develop(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    def helpwindow(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)   

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=Chatbot(self.new_window) 

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=teacher_atten(self.new_window)             

if __name__  == "__main__":
    root=Tk()
    obj=face_reconition_system(root)
    root.mainloop()

           
        
