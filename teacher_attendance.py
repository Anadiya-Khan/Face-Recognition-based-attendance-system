from tkinter import *
import tkinter
import mysql.connector
from PIL import Image,ImageTk
import os
import sys
from tkinter import ttk,Tk
from tkinter import messagebox
import csv
from tkinter import filedialog


mydata=[]

class teacher_atten:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Atttendance Record")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("face.ico")


        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_status=StringVar()

        # first image
        imgtop=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face3.webp")
        imgtop=imgtop.resize((500,200),Image.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)

        f_lbl=Label(self.root,image=self.photoimgtop)
        f_lbl.place(x=0,y=0,width=500,height=200)

        
        button=Button(f_lbl,text="Back",command=self.root.destroy,font=("times new roman",13,"bold"),fg="black",bg="skyblue")
        button.place(x=0,y=0,width=80,height=20)
# second image
        img1=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\face.png")
        img1=img1.resize((500,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=200)
# third image
        img2=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\f3.jpg")
        img2=img2.resize((500,200),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=200)

# 4th image
        img3=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\p1.jpg")
        img3=img3.resize((1550,800),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1550,height=800)

        title=Label(bg_img,text="Teacher's Attendance Details",font=("times new roman",18,"bold"),fg="white",bg="darkblue")
        title.place(x=0,y=0,width=1550,height=50)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=53,width=1500,height=600)
# Left frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Teacher Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)

        img_left=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\p2.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=730,height=130)

        left_inside_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        left_inside_frame.place(x=5,y=135,width=720,height=350)

        id = Label(left_inside_frame,text=" ID  = ", font=("times new roman",13,"bold"),fg="black",bg="white")
        id.grid(row=0,column=0,padx=20,pady=10,sticky=W)
        id_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        id_entry.grid(row=0,column=1,padx=20,pady=10,sticky=W)

        name = Label(left_inside_frame,text=" Name  = ", font=("times new roman",13,"bold"),fg="black",bg="white")
        name.grid(row=0,column=2,padx=20,pady=10,sticky=W)
        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=0,column=3,padx=20,pady=10,sticky=W)

        dep = Label(left_inside_frame,text=" Department = ", font=("times new roman",13,"bold"),fg="black",bg="white")
        dep.grid(row=1,column=0,padx=20,pady=10,sticky=W)
        dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=1,padx=20,pady=10,sticky=W)
 #time       
        std_time=Label(left_inside_frame,text="Time : ",bg="white",font=("times new roman",13,"bold"))
        std_time.grid(row=1,column=2,padx=15,pady=10,sticky=W)
        std_time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,font=("times new roman",13,"bold"),width=20)
        std_time_entry.grid(row=1,column=3,padx=15,pady=10,sticky=W)

 #date       
        std_date=Label(left_inside_frame,text="Date : ",bg="white",font=("times new roman",13,"bold"))
        std_date.grid(row=2,column=0,padx=15,pady=10,sticky=W)
        std_date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,font=("times new roman",13,"bold"),width=20)
        std_date_entry.grid(row=2,column=1,padx=15,pady=10,sticky=W)


#status        
        std_status=Label(left_inside_frame,text="Status: ",bg="white",font=("times new roman",13,"bold"))
        std_status.grid(row=2,column=2,padx=15,pady=10,sticky=W)
        std_combo=ttk.Combobox(left_inside_frame,font=("times new roman",13,"bold"),textvariable=self.var_atten_status,width=15,state="readonly")
        std_combo["values"]=("Select","Present","Absent")
        std_combo.current(0)
        std_combo.grid(row=2,column=3,padx=15,pady=10,sticky=W)
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=720,height=40)
        import_btn=Button(btn_frame,text="Import csv",command=self.importCSv,width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        import_btn.grid(row=0,column=0) 
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        export_btn.grid(row=0,column=1)
        delete_btn=Button(btn_frame,text="Delete csv",command=self.delete,width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        delete_btn.grid(row=0,column=2)  
        reset_btn=Button(btn_frame,text="Reset",command=self.reset,width=17,font=("times new roman",13,"bold"),bg="skyblue",fg="white")
        reset_btn.grid(row=0,column=3)    
# Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\khana\OneDrive\Desktop\Face recognition project\images\p2.jpg")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        table_frame=LabelFrame(Right_frame,bd=2,bg="white")
        table_frame.place(x=5,y=135,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.teacher_table=ttk.Treeview(table_frame,columns=("ID","Name","Department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)

        self.teacher_table.heading("ID",text="Id")
        self.teacher_table.heading("Name",text="Name")
        self.teacher_table.heading("Department",text="Department")
        self.teacher_table.heading("time",text="Time")
        self.teacher_table.heading("date",text="Date")
        self.teacher_table.heading("attendence",text="Attendence")
        self.teacher_table["show"]="headings"

        self.teacher_table.column("ID",width=100)
        self.teacher_table.column("Name",width=100)
        self.teacher_table.column("Department",width=100)
        self.teacher_table.column("time",width=100)
        self.teacher_table.column("date",width=100)
        self.teacher_table.column("attendence",width=100)

        
        self.teacher_table.pack(fill=BOTH,expand=1)

        self.teacher_table.bind("<ButtonRelease>",self.get_cursor)

    def fetch_data(self,rows):
        self.teacher_table.delete(*self.teacher_table.get_children())
        for i in rows:
            self.teacher_table.insert("",END,values=i)
# import CSV
    def importCSv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root) 
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata) 
#export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)     
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported to" + os.path.basename(fln) + " Successful" , parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 

    def get_cursor(self, event=""):
        cursor_row = self.teacher_table.focus()
    
        if not cursor_row:  # Check if a row is selected
            print("No row selected.")
            return

        content = self.teacher_table.item(cursor_row)
        rows = content.get('values', [])
    
        if len(rows) < 6:  # Ensure there are enough elements
            print("Selected row does not contain enough data.")
            return
        
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_status.set(rows[5])


    def reset(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("") 


    def delete(self):
        # Get the selected row
        selected_item = self.teacher_table.selection()
        if not selected_item:  # If no row is selected
            messagebox.showerror("No row selected", "Please select a row to delete.", parent=self.root)
            return

        # Get the row data
        item_data = self.teacher_table.item(selected_item[0])["values"]
        if not item_data:
            messagebox.showerror("No data", "Selected row does not have any data.", parent=self.root)
            return
        
        # Ask for confirmation to delete
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the entry: {item_data[2]}?", parent=self.root)
        if confirm:
            # Delete the row from the table
            self.teacher_table.delete(selected_item)

            # Delete the row from the mydata list (if the data is stored in mydata)
            row_id = item_data[0]  # Assuming the first column is 'id'
            for i, data in enumerate(mydata):
                if data[0] == row_id:  # Match the row by 'id'
                    del mydata[i]  # Delete the row
                    break

            messagebox.showinfo("Deleted", "Selected row has been deleted successfully.", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = teacher_atten(root)
    root.mainloop()        


