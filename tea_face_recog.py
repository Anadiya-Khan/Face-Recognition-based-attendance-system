from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import os
import numpy as np
from time import strftime
from datetime import datetime

class face_recognition2:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face recognition system")
        self.root.wm_iconbitmap("face.ico")

        title_lbl = Label(self.root, text="Face Recognition of Teacher", font=("times new roman", 30, "bold"), fg="blue")
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

        # Store the attendance status for the current day
        self.attendance_marked_today = set()  # A set to store student IDs whose attendance is marked today

    '''def mark_attendance(self, student_id, name, department):
        # Check if the attendance for the student is already marked today
        if student_id in self.attendance_marked_today:
            print(f"Attendance for {student_id} already marked today.")
            return  # Exit without marking attendance again

        # Mark the attendance
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")  # Get today's date in format dd/mm/yyyy
        time_str = now.strftime("%H:%M:%S")  # Get the current time in format hh:mm:ss
        
        # Read all the lines in the CSV file
        with open("Attendance_Teacher/teacher.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()  # Read all lines from the file
            attendance_list = []  # List to store the current attendance records

            # Check each line in the file
            for line in myDatalist:
                entry = line.split(",")  # Assuming CSV format: student_id,name,department,time,date,attendance_status
                attendance_list.append(entry)  # Store the full entry for later comparison # Check if the student already has an attendance record for today# entry[0] is the name, entry[1] is student_id, entry[4] is the date (assuming it's the 5th column)
                if entry[0] == student_id and entry[4] == date_str:
                    # Student already has an attendance record for today, so return without writing
                    messagebox.showinfo("Info",f"Attendance for {student_id} on {date_str} is already marked.",parent=self.root)
                    return

            # If the student doesn't have attendance for today, write a new record
            f.write(f"{student_id},{name},{department},{time_str},{date_str},Present\n")
            messagebox.showinfo("Info",f"Attendance for {student_id} on {date_str} marked successfully.",parent=self.root)

            # Add this student to the set to mark that their attendance has been recorded today
            self.attendance_marked_today.add(student_id)'''
    
    def mark_attendance(self, student_id, name, department):
        # Check if the attendance for the student is already marked today
        if student_id in self.attendance_marked_today:
            print(f"Attendance for {student_id} already marked today.")
            return  # Exit without marking attendance again

        # Mark the attendance
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")  # Get today's date in format dd/mm/yyyy
        time_str = now.strftime("%H:%M:%S")  # Get the current time in format hh:mm:ss
        
        attendance_exists = False
        # Open the file for reading to check if the student already has attendance for today
        with open("Attendance_Teacher/teacher.csv", "r") as f:
            myDatalist = f.readlines()  # Read all lines from the file
            
            # Check each line in the file to see if the student is already marked for today
            for line in myDatalist:
                entry = line.split(",")  # Assuming CSV format: student_id,name,department,time,date,attendance_status
                if entry[0] == student_id and entry[4] == date_str:
                    attendance_exists = True
                    break

        # If attendance already exists for the student today
        if attendance_exists:
            print(f"Attendance for {student_id} on {date_str} is already marked.")
            return

        # If the student doesn't have attendance for today, append the new record
        with open("Attendance_Teacher/teacher.csv", "a") as f:
            f.write(f"{student_id},{name},{department},{time_str},{date_str},Present\n")
            print(f"Attendance for {student_id} on {date_str} marked successfully.")

        # Add this student to the set to mark that their attendance has been recorded today
        self.attendance_marked_today.add(student_id)

    def face_reco(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbor, color, text, clf):
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

                    # Get student details
                    student_id = fetch_single_value(f"SELECT ID FROM teacher WHERE ID={id}")
                    name = fetch_single_value(f"SELECT Name FROM teacher WHERE ID={id}")
                    department = fetch_single_value(f"SELECT Department FROM teacher WHERE ID={id}")

                # Draw the recognized information
                if confidence > 77:
                    #cv2.putText(img, f"ID:{id}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255 ,255),3)
                    cv2.putText(img, f"Id: {student_id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {department}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(student_id, name, department)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]  # Update coordinates
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        face = cv2.CascadeClassifier("haarcascade_frontalface_default_teacher.xml") 
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier_teacher.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, face)
            cv2.imshow("Welcome to face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to stop the video stream
                break

        video_cap.release()
        cv2.destroyAllWindows()   

if __name__ == "__main__":
    root = Tk()
    obj = face_recognition2(root)
    root.mainloop()

