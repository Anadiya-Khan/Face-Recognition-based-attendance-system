from tkinter import *  # GUI 
from tkinter import ttk  # Stylish
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import os  # For accessing files
import numpy as np

class Train_data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        title_lbl = Label(self.root, text="Train Dataset", font=("times new roman", 20, "bold"), fg="white", bg="darkblue")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        button = Button(title_lbl, text="Back", command=self.root.destroy, font=("times new roman", 13, "bold"), fg="black", bg="skyblue")
        button.place(x=0, y=0, width=80, height=20)

        # Image Top
        imgtop = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\p3.jpg")
        imgtop = imgtop.resize((1550, 325), Image.LANCZOS)
        self.photoimgtop = ImageTk.PhotoImage(imgtop)
        f_lbl = Label(self.root, image=self.photoimgtop)
        f_lbl.place(x=0, y=55, width=1550, height=325)

        # Train Buttons
        b5 = Button(self.root, text="Train Student Data", command=self.train_classifier, cursor="hand2", font=("times new roman", 20, "bold"), fg="white", bg="darkblue")
        b5.place(x=0, y=320, width=1550, height=60)

        b5 = Button(self.root, text="Train Teacher Data", command=self.train_classifier1, cursor="hand2", font=("times new roman", 20, "bold"), fg="white", bg="darkblue")
        b5.place(x=0, y=370, width=1550, height=60)

        # Image Bottom
        imgtop1 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\p3.jpg")
        imgtop1 = imgtop1.resize((1550, 325), Image.LANCZOS)
        self.photoimgtop1 = ImageTk.PhotoImage(imgtop1)
        f_lbl = Label(self.root, image=self.photoimgtop1)
        f_lbl.place(x=0, y=420, width=1550, height=325)

    def train_classifier(self):
        data_dir = "data"  # Teacher Data directory
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png'))]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # Convert to grayscale
            imagenp = np.array(img, "uint8")
            # Assuming filenames like 'user.ID.1.jpg', splitting and extracting the ID
            try:
                id = int(os.path.split(image)[1].split('.')[1])  # Extract ID from filename
            except IndexError:
                messagebox.showerror("Error", f"Filename {image} format is incorrect")
                continue

            faces.append(imagenp)
            ids.append(id)

            cv2.imshow("Training", imagenp)
            if cv2.waitKey(1) & 0xFF == 13:  # Enter key to break
                break

        ids = np.array(ids)

        # ==================== Train the classifier ==========================
        clf = cv2.face.LBPHFaceRecognizer_create()  # LBPH Face Recognizer
        clf.train(faces, ids)  # Train classifier
        clf.write("classifier_student.xml")  # Save the trained classifier
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets are completed", parent=self.root)


    def train_classifier1(self):
        data_dir = "data1"  # Teacher Data directory
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png'))]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # Convert to grayscale
            imagenp = np.array(img, "uint8")
            # Assuming filenames like 'user.ID.1.jpg', splitting and extracting the ID
            try:
                id = int(os.path.split(image)[1].split('.')[1])  # Extract ID from filename
            except IndexError:
                messagebox.showerror("Error", f"Filename {image} format is incorrect")
                continue

            faces.append(imagenp)
            ids.append(id)

            cv2.imshow("Training", imagenp)
            if cv2.waitKey(1) & 0xFF == 13:  # Enter key to break
                break

        ids = np.array(ids)

        # ==================== Train the classifier ==========================
        clf = cv2.face.LBPHFaceRecognizer_create()  # LBPH Face Recognizer
        clf.train(faces, ids)  # Train classifier
        clf.write("classifier_teacher.xml")  # Save the trained classifier
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets are completed", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Train_data(root)
    root.mainloop()
