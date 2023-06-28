from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")

        #==============1st img==================

        img1=Image.open(r"C:\Users\navna\Music\Hotel Management System\welcome.png") #reception jw welcome.png
        img1=img1.resize((1300,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=130,y=0,width=1300,height=140) #x=130

        #================logo========================

        img2=Image.open(r"C:\Users\navna\Music\Hotel Management System\hotels.jpg")
        img2=img2.resize((220,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=220,height=140)
        

        #=================Title======================

        lbl_title=Label(self.root,text="Mahindra Holidays & Resorts India", font=("times new roman",25,"bold"),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=40)

        #=================main frame==================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=180,width=1550,height=620)

        #======================menu====================
        lbl_menu=Label(main_frame,text="MENU", font=("times new roman",15,"bold"),bg="white",fg="royalblue",bd=4,relief=RIDGE)#fg="royalblue"
        lbl_menu.place(x=0,y=0,width=220)

        #=====================button frame====================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=30,width=220,height=165)#190


        cust_btn=Button(btn_frame,text="Customer",command=self.cust_details,width=22,font=("times new roman",13,"bold"),bg="white",fg="royalblue",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="Room",command=self.roombooking,width=22,font=("times new roman",13,"bold"),bg="white",fg="royalblue",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        detail_btn=Button(btn_frame,text="Details",command=self.details_room,width=22,font=("times new roman",13,"bold"),bg="white",fg="royalblue",bd=0,cursor="hand1")
        detail_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="Report",width=22,font=("times new roman",13,"bold"),bg="white",fg="royalblue",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="Logout",command=self.logout,width=22,font=("times new roman",13,"bold"),bg="white",fg="royalblue",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


        #=================right side image===================

        img3=Image.open(r"C:\Users\navna\Music\Hotel Management System\reception cdac.jpg")#reception cdac
        img3=img3.resize((1310,590),Image.ANTIALIAS)#1310,590
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=220,y=0,width=1310,height=590)#x=225 width=1310,height=590


         #=================down image===================

        img4=Image.open(r"C:\Users\navna\Music\Hotel Management System\hotel room.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=195,width=220,height=180)

        img5=Image.open(r"C:\Users\navna\Music\Hotel Management System\maharashtrian food.jpg") #food 
        img5=img5.resize((230,210),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=360,width=220,height=180)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)


    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

  
    