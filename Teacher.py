from tkinter import*   #GUI 
from tkinter import ttk # stylish
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import os  #for Accessing the file
import numpy as np

class teacher:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face recognition system")
        self.root.wm_iconbitmap("face.ico")

        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gen=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_Add=StringVar()
        self.var_dep=StringVar()
        self.lbl=StringVar()
        self.lbl2=StringVar()
# first image
        img=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face3.webp")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_labl=Label(self.root,image=self.photoimg)
        f_labl.place(x=0,y=0,width=500,height=130)

        back_button=Button(self.root,text="Back",font=("Times new roman",10,"bold"),bg="darkblue",fg="white",command=self.root.destroy)
        back_button.place(x=0,y=10,width=80,height=20)
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
#last image
        img0=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\f3.jpg")
        img0=img0.resize((500,130),Image.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(img0)

        f_lbl=Label(self.root,image=self.photoimg0)
        f_lbl.place(x=1500,y=0,width=500,height=130)

# bg image 
        img3=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\bg3.jpg")
        img3=img3.resize((1550,800),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1550,height=800)

        title_lbl=Label(bg_img,text="TEACHER MANAGEMENT SYSTEM",font=("times new roman",18,"bold"),fg="white",bg="darkblue")
        title_lbl.place(x=0,y=0,width=1550,height=40) 

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=53,width=1500,height=600)

      

        #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Teacher Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)

        img_left=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\tea3.webp")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=730,height=130)


        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=725,height=500)

#id

        id_label=Label(current_course_frame,text="ID",font=("times new roman",12,"bold"),bg="white")
        id_label.grid(row=0,column=0,padx=20,pady=5 ,sticky=W)
        id_Entry=ttk.Entry(current_course_frame,textvariable=self.var_id,font=("times new roman",12,"bold"))
        id_Entry.grid(row=0,column=1,padx=20,pady=5,sticky=W) 
#name
        name_label=Label(current_course_frame,text="Full Name",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,sticky=W)
        name_Entry=ttk.Entry(current_course_frame,textvariable=self.var_name,font=("times new roman",12,"bold"))
        name_Entry.grid(row=0,column=3,padx=20,pady=5,sticky=W) 

#Gender
        
        std_gen=Label(current_course_frame,text="Gender",bg="white",font=("times new roman",13,"bold"))
        std_gen.grid(row=2,column=0,padx=20,pady=10,sticky=W)
        #std_gen_entry=ttk.Entry(class_student_frame,textvariable=self.var_gen,width=20,font=("times new roman",13,"bold"))
        #std_gen_entry.grid(row=2,column=1,padx=20,pady=5,sticky=W)
        std_combo=ttk.Combobox(current_course_frame,textvariable=self.var_gen,font=("times new roman",12,"bold"),state="readonly")
        std_combo["values"]=("Select Gender","Male","Female","other")
        std_combo.current(0)
        std_combo.grid(row=2,column=1,padx=20,pady=10,sticky=W)

#Email
        
        std_email=Label(current_course_frame,text="Email",bg="white",font=("times new roman",13,"bold"))
        std_email.grid(row=2,column=2,padx=20,pady=5,sticky=W)
        std_email_entry=ttk.Entry(current_course_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        std_email_entry.grid(row=2,column=3,padx=20,pady=5,sticky=W)

#Mob no
#         
        std_mob=Label(current_course_frame,text="Phone no",bg="white",font=("times new roman",13,"bold"))
        std_mob.grid(row=3,column=0,padx=20,pady=5,sticky=W)
        std_mob_entry=ttk.Entry(current_course_frame,textvariable=self.var_mob,width=20,font=("times new roman",13,"bold"))
        std_mob_entry.grid(row=3,column=1,padx=20,pady=5,sticky=W) 

#Address
        
        std_Add=Label(current_course_frame,text="Address",bg="white",font=("times new roman",13,"bold"))
        std_Add.grid(row=3,column=2,padx=20,pady=5,sticky=W)
        std_Add_entry=ttk.Entry(current_course_frame,textvariable=self.var_Add,width=20,font=("times new roman",13,"bold"))
        std_Add_entry.grid(row=3,column=3,padx=20,pady=5,sticky=W) 

#department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=4,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo['values']=("Select department","IT","BCOM","BMS","BSC")
        dep_combo.current(0)
        dep_combo.grid(row=4,column=1,padx=2,pady=10,sticky=W)        

#radio button 
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(current_course_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=5,column=0,padx=20,pady=10,sticky=W)

        Radiobutton2=ttk.Radiobutton(current_course_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=5,column=1,padx=20,pady=10,sticky=W)

#btn frame

        btn_frame=Frame(current_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=720,height=40)

        Save_btn=Button(btn_frame,text="Save",width=17,command=self.add_data,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        Save_btn.grid(row=0,column=0) 

        update_btn=Button(btn_frame,text="Update",width=17,command=self.update_function,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        update_btn.grid(row=0,column=1) 

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_function,width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_function,width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn1_frame=Frame(current_course_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=0,y=240,width=720,height=40)

        
        take_photo_btn=Button(btn1_frame,text="Take photo sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn1_frame,text="Update photo sample",command=self.update_photo,width=35,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        update_photo_btn.grid(row=0,column=1) 

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\tea3.webp")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #################################  Search button #################################

        right_frame=LabelFrame(Right_frame,text="Search System",relief=RIDGE,bd=2,bg="white",font=("times row roman",12,"bold"))
        right_frame.place(x=5,y=135,width=710,height=80)

        Label1=Label(right_frame,text="Search By",bg="yellow",font=("times row roman",12,"bold"))
        Label1.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        Label1=ttk.Combobox(right_frame,font=("times row roman",12,"bold"),textvariable=self.lbl,state="readonly")
        Label1['values']=("Select","ID")
        Label1.current(0)
        Label1.grid(row=1,column=1,padx=4,pady=10,sticky=W)

        Label2_combo=ttk.Entry(right_frame,textvariable=self.lbl2,font=("times row roman",12,"bold"))
        Label2_combo.grid(row=1,column=2,padx=4,pady=10,sticky=W)

        Button1=Button(right_frame,text="Search",command=self.search_action,bg="skyblue",fg="white",font=("times row roman",12,"bold"))
        Button1.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        Button2=Button(right_frame,text="Show All",command=self.show_all_action,bg="skyblue",fg="white",font=("times row roman",12,"bold"))
        Button2.grid(row=1,column=4,padx=2,pady=10,sticky=W) 

#################table frame#############################
        table_frame=LabelFrame(Right_frame,bd=2,bg="white")
        table_frame.place(x=5,y=220,width=710,height=330)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("ID","Name","Gender","Email","MobileNo","Address","Department","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("MobileNo",text="MobileNo")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"


        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("MobileNo",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=100)
        self.student_table.column("Department",width=100)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


# get cursor function To Focus on the textarea

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_gen.set(data[2]),
        self.var_email.set(data[3]),
        self.var_mob.set(data[4]),
        self.var_Add.set(data[5]),
        self.var_dep.set(data[6]),
        self.var_radio1.set(data[7]),

########## fetch data #######################
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from teacher")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def search_action(self):
        search_by = self.lbl.get()  # Use the global variable
        search_value = self.lbl2.get()  # Use the global variable
    
        if search_by == "Select":
            messagebox.showwarning("Warning", "Please select a search criterion.",parent=self.root)
        elif not search_value:
            messagebox.showwarning("Warning", "Please enter a search value.",parent=self.root)
        else:
            
                messagebox.showinfo("Search", f"Searching for {search_value} by {search_by}",parent=self.root)
                conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                my_cursor=conn.cursor()
                if search_by == "ID":
                    my_cursor.execute("SELECT * FROM teacher WHERE ID = %s", (search_value,))
                results = my_cursor.fetchone()

            # Display results
                if results: # Assuming student_table is a Treeview widget where results will be displayed
                    self.student_table.delete(*self.student_table.get_children())  # Clear previous entries
                    self.student_table.insert("", END, values=results)  # Insert new result
                else:
                    messagebox.showinfo("Search", "No records found.", parent=self.root)
                conn.close()


    def show_all_action(self):
        self.fetch_data()
        messagebox.showinfo("Show All", "Displaying all records.",parent=self.root)           
             

########## Add data############################

    def add_data(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_dep.get()=="Select Department":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into teacher values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_gen.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_mob.get(),
                                                                                                                self.var_Add.get(),
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_radio1.get()


                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("error",f"Due to :{str(es)}",parent=self.root)

############# Update function #################################

    def update_function(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_dep.get()=="Select Department":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update teacher set `Name`=%s,`Gender`=%s,`Email`=%s,`MobileNo`=%s,`Address`=%s,`Photo`=%s,`Department`=%s where `ID`=%s" ,( 
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                         self.var_name.get(),
                                                                                                                                                                                                         self.var_gen.get(),
                                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                                         self.var_mob.get(),
                                                                                                                                                                                                         self.var_Add.get(),
                                                                                                                                                                                                         self.var_radio1.get(),
                                                                                                                                                                                                         self.var_dep.get(),
                                                                                                                                                                                                         self.var_id.get()
                                                                                                                                                                                                                               
                                                                                                                                                                                                                                         ) )
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student detail successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

######################### Delete Function ###########################
    def delete_function(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Teacher id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Teacher delete info","Do you want to delete the information",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from teacher where ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as ae:
                messagebox.showerror("Error",f"Due to :{str(ae)}",parent=self.root)                         

###################### Reset Function #####################################
    def reset_function(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_gen.set("Select Gender")
        self.var_email.set("")
        self.var_mob.set("")
        self.var_Add.set("")
        self.var_dep.set("Select Department")
        self.var_radio1.set("")

################################# Get photo ##########################

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from teacher")
                my_result=my_cursor.fetchall()
                id=0
                for xv in my_result:
                    id+=1
                my_cursor.execute("update teacher set `Name`=%s,`Gender`=%s,`Email`=%s,`MobileNo`=%s,`Address`=%s,`Department`=%s,`Photo`=%s where `ID`=%s" ,( 
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                         self.var_name.get(),
                                                                                                                                                                                                         self.var_gen.get(),
                                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                                         self.var_mob.get(),
                                                                                                                                                                                                         self.var_Add.get(),
                                                                                                                                                                                                         self.var_radio1.get(),
                                                                                                                                                                                                         self.var_dep.get(),
                                                                                                                                                                                                         self.var_id.get()==id+1
                                                                                                                                                                                                                               
                                                                                                                                                                                                                                         ) )    
                conn.commit()
                self.fetch_data()
                self.reset_function()
                conn.close()


                #========================== load predefiend data on face frontals from opencv===============

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default_teacher.xml")  #haarcascada is an algorithm for face recognition 
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #sacling factor 1.3 , minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data1/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped face",face)
                            
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Genetating data sets completed",parent=self.root)
            except Exception as ae:
                messagebox.showerror("Error",f"Due to :{str(ae)}",parent=self.root)
#################### Search function #####################
    def search_action(self):
        search_by = self.lbl.get()  # Use the global variable
        search_value = self.lbl2.get()  # Use the global variable
    
        if search_by == "Select":
            messagebox.showwarning("Warning", "Please select a search criterion.",parent=self.root)
        elif not search_value:
            messagebox.showwarning("Warning", "Please enter a search value.",parent=self.root)
        else:
            
                messagebox.showinfo("Search", f"Searching for {search_value} by {search_by}",parent=self.root)
                conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                my_cursor=conn.cursor()
                if search_by == "ID":
                    my_cursor.execute("SELECT * FROM teacher WHERE ID = %s", (search_value,))
                results = my_cursor.fetchone()

            # Display results
                if results: # Assuming student_table is a Treeview widget where results will be displayed
                    self.student_table.delete(*self.student_table.get_children())  # Clear previous entries
                    self.student_table.insert("", END, values=results)  # Insert new result
                else:
                    messagebox.showinfo("Search", "No records found.", parent=self.root)
                conn.close()


    def show_all_action(self):
        self.fetch_data()
        messagebox.showinfo("Show All", "Displaying all records.",parent=self.root)           

############## Update photo sample #######################
    '''def update_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from teacher")
                my_result=my_cursor.fetchall()
                id=0
                for xv in my_result:
                    id+=1
                my_cursor.execute("update teacher set `Name`=%s,`Gender`=%s,`Email`=%s,`MobileNo`=%s,`Address`=%s,`Department`=%s,`Photo`=%s where `ID`=%s" ,( 
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                         self.var_name.get(),
                                                                                                                                                                                                         self.var_gen.get(),
                                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                                         self.var_mob.get(),
                                                                                                                                                                                                         self.var_Add.get(),
                                                                                                                                                                                                         self.var_radio1.get(),
                                                                                                                                                                                                         self.var_dep.get(),
                                                                                                                                                                                                         self.var_id.get()==id+1
                                                                                                                                                                                                                               
                                                                                                                                                                                                                                         ) )    
                conn.commit()
                self.fetch_data()
                self.reset_function()
                conn.close()


                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #haarcascada is an algorithm for face recognition 
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #sacling factor 1.3 , minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        my_cursor.execute=("Update teacher set `Photo`=%s WHERE `ID`=%s",(file_name_path,id+1))
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped face",face)
                            
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","The photo has been updated",parent=self.root)
            except Exception as ae:
                messagebox.showerror("Error",f"Due to :{str(ae)}",parent=self.root)'''
    
    def update_photo(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Anadiya@786", database="face_recognition")
                my_cursor = conn.cursor()

                # Get the current ID of the teacher
                teacher_id = self.var_id.get()

                # Check if teacher exists
                my_cursor.execute("SELECT * FROM teacher WHERE ID = %s", (teacher_id,))
                result = my_cursor.fetchone()

                if not result:
                    messagebox.showerror("Error", "Teacher ID not found!", parent=self.root)
                    return

                # Update teacher data
                my_cursor.execute("""
                    UPDATE teacher
                    SET `Name` = %s, `Gender` = %s, `Email` = %s, `MobileNo` = %s, `Address` = %s, `Department` = %s
                    WHERE `ID` = %s
                """, (
                    self.var_name.get(),
                    self.var_gen.get(),
                    self.var_email.get(),
                    self.var_mob.get(),
                    self.var_Add.get(),
                    self.var_radio1.get(),
                    teacher_id
                ))

                # Generate new photo for the updated teacher's record
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default_teacher.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data1/user.{teacher_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                # Commit changes to database
                conn.commit()
                self.fetch_data()
                self.reset_function()
                conn.close()

                messagebox.showinfo("Result", "Teacher's photo and details updated successfully!", parent=self.root)

            except Exception as ae:
                messagebox.showerror("Error", f"Due to :{str(ae)}", parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=teacher(root)
    root.mainloop()  








