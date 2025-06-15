from tkinter import*   #GUI 
from tkinter import ttk # stylish
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import os



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Chatbot")
        self.root.wm_iconbitmap("face.ico")

        #frame 
        title_lbl=Label(self.root,text="Chatbot",font=("times new roman",30,"bold"),fg="white",bg="darkblue")
        title_lbl.place(x=0,y=0,width=1550,height=50)

        button=Button(title_lbl,text="Back",command=self.root.destroy,font=("times new roman",13,"bold"),fg="black",bg="skyblue")
        button.place(x=0,y=0,width=80,height=20)
        

        imgtop=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face3.webp")
        imgtop=imgtop.resize((1550,700),Image.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)

        f_lbl=Label(self.root,image=self.photoimgtop)
        f_lbl.place(x=0,y=47,width=1550,height=800)

        
        dev_label=Label(f_lbl,text="khananadiya45@gmail.com",font=("times new roman",30,"bold"),bg="blue",fg="white")
        dev_label.place(x=600,y=350)


if __name__  == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()         