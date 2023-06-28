from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+225+215")

    #=================Title======================

        lbl_title=Label(self.root,text="Room Booking Details", font=("times new roman",16,"bold"),bg="white",fg="royalblue",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=35) # width=1295

    #================logo========================

        #img2=Image.open(r"C:\Users\navna\Music\Hotel Management System\Navnathbhoskar.jpg")
        #img2=img2.resize((100,35),Image.ANTIALIAS)
        #self.photoimg2=ImageTk.PhotoImage(img2)

        #lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        #lblimg.place(x=5,y=2,width=100,height=40)

    #================lebel frame===================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=45,width=410,height=200)

        #===============lables and entries=================
        #Floor
        lbl_floor=Label(labelframeleft,text="Floor:-",font=("courier",11),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,width=18,textvariable=self.var_floor,font=("courier new",11,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        #Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No:-",font=("courier",11),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,width=18,textvariable=self.var_roomNo,font=("courier new",11,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type:-",font=("courier",11),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,width=18,textvariable=self.var_RoomType,font=("courier new",11,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)

        #=============btns==================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=115,width=400,height=30)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("courier",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("courier",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.Delete,font=("courier",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("courier",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_reset.grid(row=0,column=3,padx=1)

 #================logo========================

        img3=Image.open(r"C:\Users\navna\Music\Hotel Management System\reception1.jpg")#reception taj
        img3=img3.resize((530,235),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=250,width=530,height=235)

        img4=Image.open(r"C:\Users\navna\Music\Hotel Management System\reception taj.jpg")#reception taj
        img4=img4.resize((530,235),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(self.root,image=self.photoimg4,bd=0,relief=RIDGE)
        lblimg.place(x=540,y=250,width=530,height=235)
        
        #=================table frame search system============================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=440,y=45,width=680,height=200) #y=280,width=860,height=260
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_frame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
    
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomNo.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_roomNo.get(),
                                                                            self.var_RoomType.get(),
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

# =====================Fetch Data in Table===================
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from details")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
          self.room_table.delete(*self.room_table.get_children())
          for i in rows:
              self.room_table.insert("",END,values=i)
      conn.commit()
      conn.close() 

    #getcursor=======================================================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"] 

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])
        

#updateFunction===================================================
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s,RoomNo=%s",(
                self.var_floor.get(),
                self.var_RoomType.get(),
                self.var_roomNo.get()
                ))
    

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been Updated Successfully",parent=self.root)


    #detelet Function
    def Delete(self):

        Delete=messagebox.askyesno("Hotel Management System", "Do You want delete this room details",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:

            if not Delete:

                return

        
        conn.commit()
        self.fetch_data()
        conn.close() 

    def reset(self): 
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_RoomType.set("")  


if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()