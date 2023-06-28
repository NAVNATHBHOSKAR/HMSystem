from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+225+215")

        #========================variable=====================
        self.var_mobileno=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        #=================Title======================
        lbl_title=Label(self.root,text="Room Booking Details", font=("times new roman",16,"bold"),bg="white",fg="royalblue",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=35) # width=1295

        #================logo========================
        img2=Image.open(r"C:\Users\navna\Music\Hotel Management System\Navnathbhoskar.jpg")
        img2=img2.resize((100,35),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #================lebel frame===================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=410,height=480)

        #===============lables and entries=================
        #cust_moblie

        cust_moblie=Label(labelframeleft,text="Mobile Number:-",font=("courier",11),padx=2,pady=6)
        cust_moblie.grid(row=0,column=0,sticky=W)

        entry_mobile=ttk.Entry(labelframeleft,width=18,textvariable=self.var_mobileno,font=("courier new",11,"bold"))
        entry_mobile.grid(row=0,column=1,sticky=W)


        #=================fetch data Button==================

        btn_fetchdata=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("courier",8,"bold"),bg="royalblue",fg="black",width=10)
        btn_fetchdata.place(x=322,y=4)

        #check_in_date
        check_in_date=Label(labelframeleft,text="Chech In Date:-",font=("courier",11),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,width=18,textvariable=self.var_checkin,font=("courier new",11,"bold"))
        txtcheck_in_date.grid(row=1,column=1,sticky=W)


        #check_out_date
        check_out_date=Label(labelframeleft,text="Check Out Date:-",font=("courier",11),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        txtcheck_out_date=ttk.Entry(labelframeleft,width=18,textvariable=self.var_checkout,font=("courier new",11,"bold"))#,"bold"
        txtcheck_out_date.grid(row=2,column=1,sticky=W)

        #room type
        check_RoomType=Label(labelframeleft,text="Room Type:-",font=("courier",11),padx=2,pady=6)
        check_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        rt=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",11),width=18,state="readonly")
        combo_RoomType["value"]=rt
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1,sticky=W)

        #AvailableRoom
        lblRoomAvailable=Label(labelframeleft,text="Available Room:-",font=("courier",11),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(labelframeleft,width=18,textvariable=self.var_roomavailable,font=("courier new",11,"bold"))
        #txtRoomAvailable.grid(row=4,column=1,sticky=W)
        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",11),width=18,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        #Meal

        lblMeal=Label(labelframeleft,text="Meal:-",font=("courier",11),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        combo_MealType=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",11),width=18,state="readonly")
        combo_MealType["value"]=("BreakFast","Lunch","Dinner")
        combo_MealType.current(0)
        combo_MealType.grid(row=5,column=1,sticky=W)

        #no of days

        lblNoOfDays=Label(labelframeleft,text="No Of Days:-",font=("courier",11),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,width=18,textvariable=self.var_noofdays,font=("courier new",11,"bold"))
        txtNoOfDays.grid(row=6,column=1,sticky=W)

        #paid_tax

        lbl_paid_tax=Label(labelframeleft,text="Paid Tax:-",font=("courier",11),padx=2,pady=6)
        lbl_paid_tax.grid(row=7,column=0,sticky=W)
        txt_paid_tax=ttk.Entry(labelframeleft,width=18,textvariable=self.var_paidtax,font=("courier new",11,"bold"))
        txt_paid_tax.grid(row=7,column=1,sticky=W)

        #sub_total

        lbl_sub_total=Label(labelframeleft,text="Sub Total:-",font=("courier",11),padx=2,pady=6)
        lbl_sub_total.grid(row=8,column=0,sticky=W)
        sub_total=ttk.Entry(labelframeleft,width=18,textvariable=self.var_actualtotal,font=("courier new",11,"bold"))
        sub_total.grid(row=8,column=1,sticky=W)

        #total cost

        lbl_total_cost=Label(labelframeleft,text="Total Cost:-",font=("courier",11),padx=2,pady=6)
        lbl_total_cost.grid(row=9,column=0,sticky=W)
        txttotal_cost=ttk.Entry(labelframeleft,width=18,textvariable=self.var_total,font=("courier new",11,"bold"))
        txttotal_cost.grid(row=9,column=1,sticky=W)

        #=====================Bill btn==================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("courier",11,"bold"),bg="royalblue",fg="black",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #=============btns==================================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=370,width=400,height=30)

        btn_add=Button(btn_frame,text="Enter",command=self.add_data,font=("courier",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("courier",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.Delete,font=("courier",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("courier",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_reset.grid(row=0,column=3,padx=1)


        #====================right side img=============================
        img3=Image.open(r"C:\Users\navna\Music\Hotel Management System\room.jpg")
        img3=img3.resize((520,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=720,y=55,width=400,height=200)

        #=================table frame search system============================

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=420,y=250,width=700,height=225) #y=280,width=860,height=260


        labelSearchBy=Label(Table_frame,text="Search By:",bg="royalblue",fg="black",font=("arial",11,"bold"))
        labelSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",11,"bold"),width=20,state="readonly")
        combo_search["value"]=("MobileNo","RoomNo")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,width=20,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btn_search=Button(Table_frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_search.grid(row=0,column=3,padx=1) #command=self.search,

        btn_Showall=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="royalblue",fg="black",width=10)
        btn_Showall.grid(row=0,column=4,padx=1) #command=self.fetch_data,

        #=================show data table===============

        detail_table=Frame(Table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=40,width=700,height=150) #width=860

        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(detail_table,column=("mobileno","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("mobileno",text="Mobile Number")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room Number")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No Of Day")

        self.room_table["show"]="headings"

        self.room_table.column("mobileno",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    #add data
    #=================add data table===============
    def add_data(self):
        if self.var_mobileno.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_mobileno.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room booked successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)


    # =====================Fetch Data in Table===================
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from room")
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

        self.var_mobileno.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])


    #updateFunction===================================================
    def update(self):
        if self.var_mobileno.get()=="":
            messagebox.showerror("Error","Please enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,availableroom=%s,meal=%s,no_of_days=%s where mobileno=%s",(
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_mobileno.get()))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been Updated Successfully",parent=self.root)


    #detelet Function
    def Delete(self):

        Delete=messagebox.askyesno("Hotel Management System", "Do You want delete this customer",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
            my_cursor=conn.cursor()
            query="delete from room where mobileno=%s"
            value=(self.var_mobileno.get(),)
            my_cursor.execute(query,value)
        else:

            if not Delete:

                return

        
        conn.commit()
        self.fetch_data()
        conn.close() 

    def reset(self): 
        self.var_mobileno.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")  
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("") 
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
 

    #=====================All Data Fetch===================

    def Fetch_contact(self):
        if self.var_mobileno.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_mobileno.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=420,y=55,width=295,height=190)

                lblName=Label(showDataframe,text="Name:",font=("courier",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("courier new",12,"bold"))
                lbl.place(x=110,y=0)

            #=====================================Gender===================================
                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_mobileno.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("courier",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl=Label(showDataframe,text=row,font=("courier new",12,"bold"))
                lbl.place(x=125,y=30)

            #=====================================Mobile===================================
                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
                my_cursor=conn.cursor()

                query=("select Mobile from customer where Mobile=%s")
                value=(self.var_mobileno.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Mobile No.:",font=("courier",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl=Label(showDataframe,text=row,font=("courier new",12,"bold"))
                lbl.place(x=125,y=60)

            #=====================================Nationality===================================
                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
                my_cursor=conn.cursor()

                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_mobileno.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("courier",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl=Label(showDataframe,text=row,font=("courier new",12,"bold"))
                lbl.place(x=125,y=90)

          #================================Address===================================
                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
                my_cursor=conn.cursor()

                query=("select Address from customer where Mobile=%s")
                value=(self.var_mobileno.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Address:",font=("courier",12,"bold"))
                lblNationality.place(x=0,y=120)

                lbl=Label(showDataframe,text=row,font=("courier new",12,"bold"))
                lbl.place(x=125,y=120)


    #============Search===============
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================Total Bill===================================
    def total(self):
      inDate=self.var_checkin.get()
      outDate=self.var_checkout.get()
      inDate=datetime.strptime(inDate,"%d/%m/%Y")
      outDate=datetime.strptime(outDate,"%d/%m/%Y")
      self.var_noofdays.set(abs(outDate-inDate).days)

      if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Standard"):
        q1=float(100)
        q2=float(1000)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Deluxe"):
        q1=float(100)
        q2=float(1500)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Premium"):
        q1=float(100)
        q2=float(2000)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Standard"):
        q1=float(350)
        q2=float(1000)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Deluxe"):
        q1=float(350)
        q2=float(1500)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Premium"):
        q1=float(350)
        q2=float(2000)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Standard"):
        q1=float(500)
        q2=float(1000)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Deluxe"):
        q1=float(500)
        q2=float(1500)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Premium"):
        q1=float(500)
        q2=float(2000)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3*q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)


            
if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()




    