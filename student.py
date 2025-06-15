from tkinter import*   #GUI 
from tkinter import ttk # stylish
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import os





class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face recognition system")
        self.root.wm_iconbitmap("face.ico")

        ###########variables##########################

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_Add=StringVar()
        self.var_Tea=StringVar()
        self.lbl=StringVar()
        self.lbl2=StringVar()

#First image
        img=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face3.webp")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        button=Button(f_lbl,text="Back",command=self.root.destroy,font=("times new roman",13,"bold"),fg="white",bg="darkblue")
        button.place(x=0,y=10,width=80,height=20)

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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",18,"bold"),fg="white",bg="darkblue")
        title_lbl.place(x=0,y=0,width=1550,height=40) 

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=53,width=1500,height=600)

      

        #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)

        img_left=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\a2.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=730,height=130)


        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=725,height=110)

#department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo['values']=("Select department","IT","BCOM","BMS","BSC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#course
        course_label=Label(current_course_frame,text="Courses",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo['values']=("Select Courses","BscIT","BscCS","BCOM","BMS","BSC")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo['values']=("Select Year","First Year","Secound Year","Third Year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        sem_combo['values']=("Select Semester","Sem-1","sem-2","sem-3","sem-4","sem-5","sem-6")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

#Class student information 
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=725,height=300)

# Id
        std_id=Label(class_student_frame,text="Your ID",font=("times new roman",13,"bold"),bg="white")
        std_id.grid(row=0,column=0,padx=20,pady=5,sticky=W)
        std_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        std_id_entry.grid(row=0,column=1,padx=20,pady=5,sticky=W)

# name
        std_name=Label(class_student_frame,text="Name",bg="white",font=("times new roman",13,"bold"))
        std_name.grid(row=0,column=2,padx=20,pady=5,sticky=W)
        std_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,font=("times new roman",13,"bold"),width=20)
        std_entry.grid(row=0,column=3,padx=20,pady=5,sticky=W)

#division
        
        std_div=Label(class_student_frame,text="Division",bg="white",font=("times new roman",13,"bold"))
        std_div.grid(row=1,column=0,padx=20,pady=5,sticky=W)
       # std_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
       # std_div_entry.grid(row=1,column=1,padx=20,pady=5,sticky=W)
        std_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly")
        std_combo["values"]=("Select Division","A","B","C","D")
        std_combo.current(0)
        std_combo.grid(row=1,column=1,padx=20,pady=5,sticky=W)

        
#Rollno
#         
        std_roll=Label(class_student_frame,text="Roll No",bg="white",font=("times new roman",13,"bold"))
        std_roll.grid(row=1,column=2,padx=20,pady=5,sticky=W)
        std_roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        std_roll_entry.grid(row=1,column=3,padx=20,pady=5,sticky=W)

#Gender
        
        std_gen=Label(class_student_frame,text="Gender",bg="white",font=("times new roman",13,"bold"))
        std_gen.grid(row=2,column=0,padx=20,pady=5,sticky=W)
        #std_gen_entry=ttk.Entry(class_student_frame,textvariable=self.var_gen,width=20,font=("times new roman",13,"bold"))
        #std_gen_entry.grid(row=2,column=1,padx=20,pady=5,sticky=W)
        std_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gen,font=("times new roman",12,"bold"),state="readonly")
        std_combo["values"]=("Select Gender","Male","Female","other")
        std_combo.current(0)
        std_combo.grid(row=2,column=1,padx=20,pady=5,sticky=W)

        
#DOB
#         
        std_dob_label = Label(class_student_frame, text="DOB", bg="white", font=("times new roman", 13, "bold"))
        std_dob_label.grid(row=2, column=2, padx=20, pady=5, sticky=W)

        # Entry for DOB
        std_dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=18, font=("times new roman", 13, "bold"))
        std_dob_entry.grid(row=2, column=3, padx=20, pady=5, sticky=W)


#Email
        
        std_email=Label(class_student_frame,text="Email",bg="white",font=("times new roman",13,"bold"))
        std_email.grid(row=3,column=0,padx=20,pady=5,sticky=W)
        std_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        std_email_entry.grid(row=3,column=1,padx=20,pady=5,sticky=W)


        
#Mob no
#         
        std_mob=Label(class_student_frame,text="Phone no",bg="white",font=("times new roman",13,"bold"))
        std_mob.grid(row=3,column=2,padx=20,pady=5,sticky=W)
        std_mob_entry=ttk.Entry(class_student_frame,textvariable=self.var_mob,width=20,font=("times new roman",13,"bold"))
        std_mob_entry.grid(row=3,column=3,padx=20,pady=5,sticky=W)

#Address
        
        std_Add=Label(class_student_frame,text="Address",bg="white",font=("times new roman",13,"bold"))
        std_Add.grid(row=4,column=0,padx=20,pady=5,sticky=W)
        std_Add_entry=ttk.Entry(class_student_frame,textvariable=self.var_Add,width=20,font=("times new roman",13,"bold"))
        std_Add_entry.grid(row=4,column=1,padx=20,pady=5,sticky=W)

        
#Class teacher name
#         
        std_Tea=Label(class_student_frame,text="Teacher Name",bg="white",font=("times new roman",13,"bold"))
        std_Tea.grid(row=4,column=2,padx=20,pady=5,sticky=W)
        std_Tea_entry=ttk.Entry(class_student_frame,textvariable=self.var_Tea,width=20,font=("times new roman",13,"bold"))
        std_Tea_entry.grid(row=4,column=3,padx=20,pady=5,sticky=W)

#radio button 
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=5,column=0)

        Radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=5,column=1)

#btn frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=720,height=40)

        Save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        Save_btn.grid(row=0,column=0) 

        update_btn=Button(btn_frame,command=self.update_function,text="Update",width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        update_btn.grid(row=0,column=1) 

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_function,width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,command=self.reset_function,text="Reset",width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn1_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=0,y=240,width=720,height=40)

        
        take_photo_btn=Button(btn1_frame,command=self.generate_dataset,text="Take photo sample",width=35,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn1_frame,text="Update photo sample",command=self.update_photo,width=35,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        update_photo_btn.grid(row=0,column=1)
#right frame 

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\School-Students.jpg")
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
        Label1['values']=("Select","Roll no","ID")
        Label1.current(0)
        Label1.grid(row=1,column=1,padx=4,pady=10,sticky=W)

        Label2_combo=ttk.Entry(right_frame,font=("times row roman",12,"bold"),textvariable=self.lbl2)
        Label2_combo.grid(row=1,column=2,padx=4,pady=10,sticky=W)

        Button1=Button(right_frame,text="Search",bg="skyblue",command=self.search_action,fg="white",font=("times row roman",12,"bold"))
        Button1.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        Button2=Button(right_frame,text="Show All",bg="skyblue",command=self.show_all_action,fg="white",font=("times row roman",12,"bold"))
        Button2.grid(row=1,column=4,padx=2,pady=10,sticky=W)        

#################table frame#############################

        table_frame=LabelFrame(Right_frame,bd=2,bg="white")
        table_frame.place(x=5,y=220,width=710,height=330)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Department","course","year","sem","id","name","div","roll","gender","dob","email","phone no","Address","teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Rollno")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone no",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo Sample")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone no",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("Photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

     ###################3 function declaration ##############################33

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
                if search_by == "Roll no":
                    my_cursor.execute("SELECT * FROM student WHERE Rollno = %s", (search_value,))
                elif search_by == "ID":
                    my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (search_value,))
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




    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gen.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_mob.get(),
                                                                                                                self.var_Add.get(),
                                                                                                                self.var_Tea.get(),
                                                                                                                self.var_radio1.get()


                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("error",f"Due to :{str(es)}",parent=self.root)


     ##################### fetch data #####################

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

        ############### get cursor#########################

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gen.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_mob.set(data[11]),
        self.var_Add.set(data[12]),
        self.var_Tea.set(data[13]),
        self.var_radio1.set(data[14]),

# update function
     
    def update_function(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set `Department`=%s,`Course`=%s,`Year`=%s,`Semester`=%s,`Name`=%s,`Division`=%s,`Rollno`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Phone No`=%s,`Address`=%s,`Teacher`=%s,`Photo Sample`=%s where `Student_id`=%s" ,( 
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                         self.var_dep.get(),
                                                                                                                                                                                                         self.var_course.get(),
                                                                                                                                                                                                         self.var_year.get(),
                                                                                                                                                                                                         self.var_sem.get(),
                                                                                                                                                                                                         self.var_name.get(),
                                                                                                                                                                                                         self.var_div.get(),
                                                                                                                                                                                                         self.var_roll.get(),
                                                                                                                                                                                                         self.var_gen.get(),
                                                                                                                                                                                                         self.var_dob.get(),
                                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                                         self.var_mob.get(),
                                                                                                                                                                                                         self.var_Add.get(),
                                                                                                                                                                                                         self.var_Tea.get(),
                                                                                                                                                                                                         self.var_radio1.get(),
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

#################################### Delete function #################################
    def delete_function(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete info","Do you want to delete the information",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
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

#Reset function 
    def reset_function(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gen.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_mob.set("")
        self.var_Add.set("")
        self.var_Tea.set("")
        self.var_radio1.set("")

       # ===================================Generate data set or take photo sample======================================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anadiya@786",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for xv in my_result:
                    id+=1
                my_cursor.execute("update student set `Department`=%s,`Course`=%s,`Year`=%s,`Semester`=%s,`Name`=%s,`Division`=%s,`Rollno`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Phone No`=%s,`Address`=%s,`Teacher`=%s,`Photo Sample`=%s where `Student_id`=%s" ,( 
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                         self.var_dep.get(),
                                                                                                                                                                                                         self.var_course.get(),
                                                                                                                                                                                                         self.var_year.get(),
                                                                                                                                                                                                         self.var_sem.get(),
                                                                                                                                                                                                         self.var_name.get(),
                                                                                                                                                                                                         self.var_div.get(),
                                                                                                                                                                                                         self.var_roll.get(),
                                                                                                                                                                                                         self.var_gen.get(),
                                                                                                                                                                                                         self.var_dob.get(),
                                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                                         self.var_mob.get(),
                                                                                                                                                                                                         self.var_Add.get(),
                                                                                                                                                                                                         self.var_Tea.get(),
                                                                                                                                                                                                         self.var_radio1.get(),
                                                                                                                                                                                                         self.var_id.get()==id+1
                                                                                                                                                                                                                               
                                                                                                                                                                                                                                         ) )    
                conn.commit()
                self.fetch_data()
                self.reset_function()
                conn.close()

                #========================== load predefiend data on face frontals from opencv===============

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
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped face",face)
                            
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Genetating data sets completed",parent=self.root)
            except Exception as ae:
                messagebox.showerror("Error",f"Due to :{str(ae)}",parent=self.root)


    def update_photo(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Anadiya@786", database="face_recognition")
                my_cursor = conn.cursor()

                # Get the current student ID
                student_id = self.var_id.get()

                # Check if student exists
                my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (student_id,))
                result = my_cursor.fetchone()

                if not result:
                    messagebox.showerror("Error", "Student ID not found!", parent=self.root)
                    return

                # Update student data in the database
                my_cursor.execute("""
                    UPDATE student
                    SET `Department` = %s, `Course` = %s, `Year` = %s, `Semester` = %s, `Name` = %s, `Division` = %s,
                        `Rollno` = %s, `Gender` = %s, `DOB` = %s, `Email` = %s, `Phone No` = %s, `Address` = %s, 
                        `Teacher` = %s, `Photo Sample` = %s
                    WHERE `Student_id` = %s
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gen.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_mob.get(),
                    self.var_Add.get(),
                    self.var_Tea.get(),
                    self.var_radio1.get(),
                    student_id
                ))

                # Start capturing the photo (face image) for the student
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

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
                        file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                # Commit changes to the database
                conn.commit()
                self.fetch_data()
                self.reset_function()
                conn.close()

                messagebox.showinfo("Result", "Student's photo and details updated successfully!", parent=self.root)

            except Exception as ae:
                messagebox.showerror("Error", f"Due to :{str(ae)}", parent=self.root)            

    '''def validate_email(self, *args):
        email_value = self.var_email.get()
        try:
            # Validate the email
            valid = validate_email(email_value)
            self.var_email(style='Valid.TEntry')
        except EmailNotValidError:
            self.var_email(style='Invalid.TEntry')'''                 


              




if __name__  == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
