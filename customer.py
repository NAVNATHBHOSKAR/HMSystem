from optparse import Values
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+225+215")


        #================Variables==================
        self.var_cust_no=StringVar()
        x=random.randint(1,99)
        self.var_cust_no.set(str(x))

        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_address=StringVar()
        self.var_postal_code=StringVar()
        self.var_room_number=StringVar()

        #=================Title======================

        lbl_title=Label(self.root,text="Add Customer Details", font=("times new roman",16,"bold"),bg="white",fg="royalblue",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=35) # width=1295

        #================logo========================

        img2=Image.open(r"C:\Users\navna\Music\Hotel Management System\guest.jpg") #room
        img2=img2.resize((80,80),Image.ANTIALIAS) #100
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=175,y=4,width=75,height=75) #width=50


        #================lebel frame===================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=70,width=380,height=400)#width=400 y=35 height=440


        #===============lables and entries=================
        #cust_ref

        lbl_cust_ref=Label(labelframeleft,text="Customer No:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        txtref=ttk.Entry(labelframeleft,width=25,textvariable=self.var_cust_no,font=("arial",11,"bold"),state="readonly")
        txtref.grid(row=0,column=1)

         #cust_name

        lbl_cust_ref=Label(labelframeleft,text="Customer Name:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0,sticky=W)

        txtname=ttk.Entry(labelframeleft,width=25,textvariable=self.var_cust_name,font=("arial",11,"bold"))
        txtname.grid(row=1,column=1)


         #Gender

        lbl_cust_ref=Label(labelframeleft,text="Gender:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=2,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",11),width=23,state="readonly") #("arial",12,"bold")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)

        #Mobno

        lbl_cust_ref=Label(labelframeleft,text="Mobile:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=3,column=0,sticky=W)

        txtmob=ttk.Entry(labelframeleft,width=25,textvariable=self.var_mobile,font=("arial",11,"bold"))
        txtmob.grid(row=3,column=1)

        #email

        lbl_cust_ref=Label(labelframeleft,text="Email:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=4,column=0,sticky=W)

        txtemail=ttk.Entry(labelframeleft,width=25,textvariable=self.var_email,font=("arial",11,"bold"))
        txtemail.grid(row=4,column=1)

        #natitality

        lbl_cust_ref=Label(labelframeleft,text="Nationality:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=5,column=0,sticky=W)
        combo_nat=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",11),width=23,state="readonly")
        combo_nat["value"]=("India","British","American")
        combo_nat.current(0)
        combo_nat.grid(row=5,column=1)

        #idproof

        lbl_cust_ref=Label(labelframeleft,text="Id Proof Type:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=6,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",11),width=23,state="readonly")
        combo_id["value"]=("Aadhar Card","Driving Licence","Passport")
        combo_id.current(0)
        combo_id.grid(row=6,column=1)

        #roomno

        lbl_cust_ref=Label(labelframeleft,text="Room Number:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=9,column=0,sticky=W)

        txtid=ttk.Entry(labelframeleft,width=25,textvariable=self.var_room_number,font=("arial",11,"bold"))
        txtid.grid(row=9,column=1)

        #address

        lbl_cust_ref=Label(labelframeleft,text="Address:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=7,column=0,sticky=W)

        txtaddress=ttk.Entry(labelframeleft,width=25,textvariable=self.var_address,font=("arial",11,"bold"))
        txtaddress.grid(row=7,column=1)

        #Postcode

        lbl_cust_ref=Label(labelframeleft,text="Postal Code:-",font=("arial",11),padx=2,pady=6)
        lbl_cust_ref.grid(row=8,column=0,sticky=W)

        txtpass=ttk.Entry(labelframeleft,width=25,textvariable=self.var_postal_code,font=("arial",11,"bold"))
        txtpass.grid(row=8,column=1)


        #=====================btn==============================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=345,width=370,height=25) #y=380

        btn_add=Button(btn_frame,text="Login",command=self.add_data,font=("arial",11),bg="royalblue",fg="black",width=9) #,"bold"
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",11),bg="royalblue",fg="black",width=9) #,"bold"
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11),bg="royalblue",fg="black",width=9) #,"bold"
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11),bg="royalblue",fg="black",width=9) #,"bold"
        btn_reset.grid(row=0,column=3,padx=1)

        #btn_reset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="royalblue",fg="black",width=9) 
        #btn_reset.grid(row=0,column=3,padx=1)


        #=================table frame============================

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=390,y=35,width=860,height=490) 
        #labelframeleft.place(x=5,y=35,width=380,height=470)


        labelSearchBy=Label(Table_frame,text="Search By:",bg="lime green",fg="black",font=("arial",10,"bold"))
        labelSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",10,"bold"),width=15,state="readonly")
        combo_search["value"]=("Mobile","CustomerNo")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=15,font=("arial",10,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btn_search=Button(Table_frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="royalblue",fg="black",width=15)
        btn_search.grid(row=0,column=3,padx=1)

        btn_Showall=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="royalblue",fg="black",width=15)
        btn_Showall.grid(row=0,column=4,padx=1)


        #=================show data table===============

        detail_table=Frame(Table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=40,width=730,height=370) #width=860



        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(detail_table,column=("ref","name","gender","mobile","email","nationality","idproof","address","post","roomnumber"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="CustomerNo")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id proof")
        self.Cust_Details_Table.heading("address",text="Address")
        self.Cust_Details_Table.heading("post",text="Postal Code")
        self.Cust_Details_Table.heading("roomnumber",text="Room Number")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("address",width=100)
        self.Cust_Details_Table.column("roomnumber",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #=================add data to database table===============
    def add_data(self):
        if self.var_cust_name.get()=="" or self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter All details",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_cust_no.get(),
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_id_proof.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_postal_code.get(),
                                                                                                self.var_room_number.get()
                                                                                            ))


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]


        self.var_cust_no.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_email.set(row[4]),
        self.var_nationality.set(row[5]),
        self.var_id_proof.set(row[6]),
        self.var_address.set(row[7]),
        self.var_postal_code.set(row[8]),
        self.var_room_number.set(row[9])



    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Gender=%s,Mobile=%s,Email=%s,Nationality=%s,Idprof=%s,Address=%s,Postalcode=%s,Roomnumber=%s where CustomerNo=%s",(
                                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_postal_code.get(),
                                                                                                                                                                self.var_room_number.get(),
                                                                                                                                                                self.var_cust_no.get()
                                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)


    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
            my_cursor=conn.cursor()
            query="delete from customer where CustomerNo=%s"
            value=(self.var_cust_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()



    def reset(self):
        #self.var_cust_no.set(""),
        self.var_cust_name.set(""),
        self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        self.var_id_proof.set(""),
        self.var_room_number.set(""),
        self.var_address.set(""),
        self.var_postal_code.set("")
        x=random.randint(1,99)
        self.var_cust_no.set(str(x))


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="hotel_management_system")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()

