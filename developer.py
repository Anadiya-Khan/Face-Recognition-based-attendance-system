from tkinter import *  # GUI 
from tkinter import ttk  # Stylish
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Developer")
        self.root.wm_iconbitmap("face.ico")

        # Frame
        title_lbl = Label(self.root, text="Developer", font=("times new roman", 30, "bold"), fg="blue", bg="darkblue")
        title_lbl.place(x=0, y=0, width=1550, height=50)

        button = Button(title_lbl, text="Back", command=self.root.destroy, font=("times new roman", 13, "bold"), fg="black", bg="skyblue")
        button.place(x=0, y=0, width=80, height=20)

        imgtop = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\bg.jpg")
        imgtop = imgtop.resize((1550, 700), Image.LANCZOS)
        self.photoimgtop = ImageTk.PhotoImage(imgtop)

        f_lbl = Label(self.root, image=self.photoimgtop)
        f_lbl.place(x=0, y=47, width=1550, height=800)

        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=500, y=100, width=650, height=600)

        imgtop1 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\p4.jpg")
        imgtop1 = imgtop1.resize((200, 200), Image.LANCZOS)
        self.photoimgtop1 = ImageTk.PhotoImage(imgtop1)

        f_lbl = Label(main_frame, image=self.photoimgtop1)
        f_lbl.place(x=300, y=0, width=200, height=200)

        # Developer's information
        dev_label = Label(main_frame, 
                          text="Hello, my name is Anadiya Khan.\n"
                               "I am a TYBSc(IT) student at Mumbai University.\n"
                               "I have built this project for recognizing faces automatically\n"
                               "and marking attendance in an Excel sheet.\n\n"
                               "Skills: Python, OpenCV, Tkinter, MySQL, Excel Integration\n"
                               "Technologies Used: Face Recognition, Image Processing, GUI Development\n\n"
                               "Contact: anadiya.khan@example.com\n"
                               "LinkedIn: https://linkedin.com/in/anadiya-khan", 
                          font=("Times New Roman", 15, "bold"), bg="blue", fg="white")

        dev_label.place(x=0, y=230)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
