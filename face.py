from tkinter import *  
from tkinter import ttk # stylish
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import os  # for accessing the file
import numpy as np
from time import strftime
from datetime import datetime


class face_recognition1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face recognition system")
        self.root.wm_iconbitmap("face.ico")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 30, "bold"), fg="blue")
        title_lbl.place(x=0, y=0, width=1550, height=50)

        button = Button(title_lbl, text="Back", command=self.root.destroy, font=("times new roman", 13, "bold"), fg="black", bg="skyblue")
        button.place(x=0, y=0, width=80, height=20)

        # Third image 
        imgtop = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face3.webp")
        imgtop = imgtop.resize((750, 700), Image.LANCZOS)
        self.photoimgtop = ImageTk.PhotoImage(imgtop)

        f_lbl = Label(self.root, image=self.photoimgtop)
        f_lbl.place(x=0, y=47, width=750, height=800)

        imgtop1 = Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face2.webp")
        imgtop1 = imgtop1.resize((800, 700), Image.LANCZOS)
        self.photoimgtop1 = ImageTk.PhotoImage(imgtop1)

        f_lbl = Label(self.root, image=self.photoimgtop1)
        f_lbl.place(x=750, y=47, width=800, height=800)

        b1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_reco, fg="blue", font=("times new roman", 12, "bold"))
        b1.place(x=300, y=670, width=200, height=40)
        
    def mark_attendance(self, id, name, department, entity_type="student"):
        # This function handles both student and teacher attendance based on `entity_type`.
        file_path = "attendance_report/student.csv" if entity_type == "student" else "attendance_report/teacher.csv"
        
        with open(file_path, "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []

            for line in myDatalist:
                entry = line.split(",")
                name_list.append(entry[0])  # Assuming name is the first entry

            # Check if the student/teacher is already marked
            if (id not in name_list) and (name not in name_list) and (department not in name_list):
                now = datetime.now()
                date_str = now.strftime("%d/%m/%Y")
                time_str = now.strftime("%H:%M:%S")
                f.write(f"{id},{name},{department},{time_str},{date_str},Present\n")

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbor, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbor)

        coord = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                
            # Predict the ID
            id, predict = clf.predict(gray_image[y:y + h, x:x + w]) 
            confidence = int((100 * (1 - predict / 300)))

            # Establish the database connection
            with mysql.connector.connect(host="localhost", username="root", password="Anadiya@786", database="face_recognition") as conn:
                my_cursor = conn.cursor()

                # Helper function to fetch and format data
                def fetch_single_value(query):
                    my_cursor.execute(query)
                    result = my_cursor.fetchone()
                    return result[0] if result else "N/A"  # Return first value or "N/A"

                # Get student or teacher details based on the ID
                student_id = fetch_single_value(f"SELECT Student_id FROM student WHERE Student_id={id}")
                teacher_id = fetch_single_value(f"SELECT ID FROM teacher WHERE ID={id}")
                name = fetch_single_value(f"SELECT Name FROM student WHERE Student_id={id}") if student_id else fetch_single_value(f"SELECT Name FROM teacher WHERE ID={id}")
                department = fetch_single_value(f"SELECT Department FROM student WHERE Student_id={id}") if student_id else fetch_single_value(f"SELECT Department FROM teacher WHERE ID={id}")
                
                if student_id:
                    entity_type = "student"
                elif teacher_id:
                    entity_type = "teacher"
                else:
                    entity_type = "unknown"

            # Draw the recognized information
            if confidence > 77:
                # Display the student or teacher info
                cv2.putText(img, f"Id: {student_id if student_id else teacher_id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Department: {department}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                
                # Mark attendance for student or teacher
                self.mark_attendance(student_id if student_id else teacher_id, name, department, entity_type)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            coord = [x, y, w, h]  # Update coordinates
        return coord

    def recognize(self, img, clf, faceCascade):
        coord = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face", clf)
        return img

    def face_reco(self):
        face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, clf, face)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to stop the webcam
                break

        video_cap.release()  # Release the webcam
        cv2.destroyAllWindows()  # Close OpenCV windows


if __name__ == "__main__":
    root = Tk()
    obj = face_recognition1(root)
    root.mainloop()

