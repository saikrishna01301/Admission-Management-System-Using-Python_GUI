from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import itertools

#================================================================================================================
#======================================DATABASE CONNECTION=======================================================

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Kittu@01301",database="ams")  

# create cursor to execute the sql commands/queries
mycurs=mydb.cursor()

# creating the ams(addmission management system) database
# mycurs.execute("create database ams")

# createing the signup table in ams database
# mycurs.execute("create table table1(name varchar(225),age int)")
# mycurs.execute("create table s_signup (name varchar(255),email varchar(255),phone varchar(255),username varchar(255),password varchar(255))")
# mycurs.execute("create table files(email varchar(255),adhar longblob,tenth longblob,twelfth longblob,tc longblob,photo longblob,income longblob)")

#to fetch all the records in s_signup table
#mycurs.execute("select*from form")
#signup_result=mycurs.fetchall()
#for i in signup_result:
#    print(i)

# creating the table for addmission form

#mycurs.execute("create table form(s_name varchar(255),dob varchar(255),s_phone varchar(255),gender varchar(255),email varchar(255),f_name varchar(255),m_name varchar(255),f_occu varchar(255),m_occu varchar(255),f_phone varchar(255),m_phone varchar(255),country varchar(255),state varchar(255),religion varchar(255),pincode varchar(255),address varchar(255),course varchar(255))")

#===========================================================================================================================
#============================================================================================================================


def main():
    root=Tk()
    obj1=window1(root)
    root.mainloop()
    
class window1():
    

    def login_into(self):
        
        user_name=self.u_lgn.get()
        user_password=self.psd.get()

        #=====================sql used to login=================================
        # it is to fetch the whole records of username attribute
        mycurs.execute("select username from s_signup")
        username_result=mycurs.fetchall()
    
        # it is to fetch the whole records of password attribute
        mycurs.execute("select password from s_signup")
        password_result=mycurs.fetchall()

        if not user_name:
            messagebox.askretrycancel("Error","Please Check the Username")
        elif not user_password:
            messagebox.askretrycancel("Error","Please Check the Password")
        elif (user_name not in itertools.chain(*username_result)) :
            messagebox.askretrycancel("Error","invalid usernmae")
        elif (user_password not in itertools.chain(*password_result)) :
            messagebox.askretrycancel("Error","invalid Password")
        else:
            self.user_entry.delete(0,"end")
            self.pass_entry.delete(0,"end")
            self.show_adm()
        
        
    def exit_fun(self):
        self.root.quit()

        
    def __init__(self,root):
        self.root=root
        root.title("Lovely Professional University")      #interface name
        root.geometry("850x700+250+10")                   #interface size
        root.resizable(False,False)                       #interface resize
        root.iconbitmap(r'myicon1.ico')                   #interface icon
        root.configure(bg="orange")           #interface bg

        
        #====================================================================
        title_label=Label(self.root,text="Lovely Professional University",bg="orange",fg="#fff",font=("times new roman",40),relief=GROOVE)
        title_label.place(x=0,y=0,relwidth=1)

        #user & pass icons
        self.user_icon=PhotoImage(file='username.png')
        self.pass_icon=PhotoImage(file='password.png')
        self.exit_icon=PhotoImage(file='quit.png')
      
       
        self.login_frame=Frame(self.root,bg="white")
        self.login_frame.place(x=200,y=150,height=450,width=450)
        
        #login label
        self.lbl_frame=Label(self.login_frame,text="Login Here",bg="white",fg="#228B22",font=("times new roman",30))
        self.lbl_frame.place(x=60,y=40)

        #user & pass label
        lbl_user=Label(self.login_frame,text="Username",image=self.user_icon,compound=LEFT,bg="#fff",font=("Goudy old style",18))
        lbl_user.place(x=60,y=120)
        lbl_pass=Label(self.login_frame,text="Password",image=self.pass_icon,compound=LEFT,bg="#fff",font=("Goudy old style",18))
        lbl_pass.place(x=61,y=215)

        #user & pass entry and set focus
        def l_focus1(event):
            self.pass_entry.focus_set()
        
        self.u_lgn=StringVar()
        self.psd=StringVar()

        self.user_entry=Entry(self.login_frame,textvariable=self.u_lgn,font=("times new roman",15),bg="lightgrey")
        self.user_entry.place(x=65,y=168,width=320,height=35)
        self.pass_entry=Entry(self.login_frame,textvariable=self.psd,font=("times new roman",15),bg="lightgrey",show="*")
        self.pass_entry.place(x=65,y=255,width=320,height=35)
        
        # bind method of widget is used for 
        # the binding the function with the events 
  
        # whenever the enter key is pressed 
        # then call the focus functions  
        self.user_entry.bind("<Return>",l_focus1) 

        #forget,sign up & login btnss
        #login-exit
        login_exit=Button(self.login_frame,image=self.exit_icon,bg="#fff",bd=0,activebackground="#fff",command=self.exit_fun)
        login_exit.place(x=420,y=5)

        forget_btn=Button(self.login_frame,text="forget password ?",bg="#fff",bd=0,activebackground="#fff",cursor="hand2",font=("times new roman",15),command=self.show_forget)
        forget_btn.place(x=60,y=305)

        l_text=Label(self.login_frame,text="Don't have an account?",bg="#fff",fg="Dimgrey",font=("times new roman",15),activebackground="#fff")
        l_text.place(x=62,y=345)

        staff_login=Button(self.login_frame,text="Staff login ",bg="#fff",bd=0,activebackground="#fff",cursor="hand2",font=("times new roman",15),command=self.staff_win)
        staff_login.place(x=60,y=380)

        sign_up_btn=Button(self.login_frame,text="signUp",bg="#fff",bd=0,activebackground="#fff",cursor="hand2",font=("times new roman",15),command=self.show_signup)
        sign_up_btn.place(x=250,y=342)

        self.login_btn=Button(self.root,text="Login",bg="#228B22",bd=0,fg="#fff",activebackground="#228B22",activeforeground="#fff",cursor="hand2",font=("times new roman",20),command=self.login_into)
        self.login_btn.place(x=330,y=575,width=180,height=50)


    
    def show_signup(self):
        self.newwindow=Toplevel(self.root)
        self.obj1=window2(self.newwindow)
        
    def show_adm(self):
        self.newwindow=Toplevel(self.root)
        self.obj1=window3(self.newwindow)

    def show_forget(self):
        self.for_pass_window=Toplevel(self.root)
        self.obj1=window6(self.for_pass_window) 

    def staff_win(self):
        self.staff_window=Toplevel(self.root)
        self.obj1=window7(self.staff_window)
            


#=============================================signup window =====================================================
#==================================================================================================================
class window2():

    # it is to fetch the whole records of username attribute
    def chk_username(self):
        mycurs.execute("select username from s_signup")
        self.username_result=mycurs.fetchall()

    # this method is saved when we press signup button
    def signup_savedata(self):
        mycurs.execute("insert into s_signup values(%s,%s,%s,%s,%s)",( self.a,self.b,self.c,self.d,self.e ))
        mydb.commit()

    # this method is to check the details are valid or invalid
    def create_fun(self):
        self.a=self.fname.get()
        self.b=self.email.get()
        self.c=self.pno.get()
        self.d=self.user.get()
        self.e=self.pwd.get()

        chk_email="@gmail.com"
        #chk_phone=("1,2,3,4,5,6,7,8,9,0")
        # it is to fetch the whole records of username attribute
        mycurs.execute("select username from s_signup")
        username_result=mycurs.fetchall()
        
        if not self.a:
            messagebox.showerror("Error","Every detail is required,PLEASE AGAIN SIGNUP")
        elif not self.b:
            messagebox.showerror("Error","Every detail is required,PLEASE AGAIN SIGNUP")
        elif(chk_email not in self.b):
            messagebox.showerror("Error","Invalid Email")
        elif not self.c:
            messagebox.showerror("Error","Every detail is required,PLEASE AGAIN SIGNUP")
        #elif self.c not in chk_phone:
            #messagebox.showerror("Error","Invalid Phone Number")
        elif not self.d:
            messagebox.showerror("Error","Every detail is required,PLEASE AGAIN SIGNUP")
        elif not self.e:
            messagebox.showerror("Error","Every detail is required,PLEASE AGAIN SIGNUP")
        elif (self.d in itertools.chain(*username_result)) :
            messagebox.showerror("Error","Username is already exist")
        else:
            self.f_entry.delete(0,"end")
            self.email_entry.delete(0,"end")
            self.phn_entry.delete(0,"end")
            self.user_entry.delete(0,"end")
            self.p_entry.delete(0,"end")
            self.signup_savedata()
            messagebox.showinfo("Account Created","Your Account Created Successfully,please login")

    # mani signup constructor 
    def __init__(self,root):
        self.root=root
        self.title=root.title("LPU Addmission Management System")      #interface name
        self.geometry=root.geometry("1350x720+0+0")                    #interface size
        self.resize=root.resizable(False,False)                        #interface resize
        self.icon=root.iconbitmap(r'myicon1.ico')                      #interface icon
        self.config=root.configure(bg="orange")                        #interface bg

        title_label=Label(self.root,text="Lovely Professional University",bg="orange",fg="#fff",font=("times new roman",40),relief=GROOVE)
        title_label.place(x=0,y=0,relwidth=1)

        #creatin signup focus functions
        def s_focus1(event):
            self.email_entry.focus_set()
        def s_focus2(event):
            self.phn_entry.focus_set()
        def s_focus3(event):
            self.user_entry.focus_set()
        def s_focus4(event):
            self.p_entry.focus_set()
        def s_focus5(event):
            self.create_btn.focus_set()
        
        
        

        #creating sing_up frame
        self.signup_frame=Frame(self.root,bg="#fff")
        self.signup_frame.place(x=420,y=120,height=480,width=520)

       
        #singup labels
        lbl_frame=Label(self.signup_frame,text="SignUp Here",bg="white",fg="#228B22",font=("times new roman",30))
        lbl_frame.place(x=40,y=20)

        sign_name=Label(self.signup_frame,text="Name",bg="#fff",font=("Goudy old style",18))
        sign_name.place(x=40,y=105)

        sign_email=Label(self.signup_frame,text="Email",bg="#fff",font=("Goudy old style",18))
        sign_email.place(x=40,y=170)

        sign_phone=Label(self.signup_frame,text="Phone",bg="#fff",font=("Goudy old style",18))
        sign_phone.place(x=40,y=230)

        sign_u_name=Label(self.signup_frame,text="User Name",bg="#fff",font=("Goudy old style",18))
        sign_u_name.place(x=40,y=290)

        sign_pass=Label(self.signup_frame,text="Password",bg="#fff",font=("Goudy old style",18))
        sign_pass.place(x=40,y=350)



        #signup entry boxes
        self.fname=StringVar()
        self.email=StringVar()
        self.pno=StringVar()
        self.user=StringVar()
        self.pwd=StringVar()

        self.f_entry=Entry(self.signup_frame,textvariable=self.fname,font=("times new roman",15),bg="lightgrey")
        self.f_entry.place(x=180,y=105,width=320,height=35) 

        self.email_entry=Entry(self.signup_frame,textvariable=self.email,font=("times new roman",15),bg="lightgrey")
        self.email_entry.place(x=180,y=170,width=320,height=35)

        self.phn_entry=Entry(self.signup_frame,textvariable=self.pno,font=("times new roman",15),bg="lightgrey")
        self.phn_entry.place(x=180,y=230,width=320,height=35)

        self.user_entry=Entry(self.signup_frame,textvariable=self.user,font=("times new roman",15),bg="lightgrey")
        self.user_entry.place(x=180,y=290,width=320,height=35)

        self.p_entry=Entry(self.signup_frame,textvariable=self.pwd,font=("times new roman",15),bg="lightgrey",show="*")
        self.p_entry.place(x=180,y=350,width=320,height=35)

        self.f_entry.bind("<Return>",s_focus1)
        self.email_entry.bind("<Return>",s_focus2)
        self.phn_entry.bind("<Return>",s_focus3)
        self.user_entry.bind("<Return>",s_focus4)
        self.p_entry.bind("<Return>",s_focus5)
        
        #signup buttons
        #l_btn=Button(self.signup_frame,text="Login in",bg="#fff",bd=0,activebackground="#fff",cursor="hand1",font=("times new roman",15))
        #l_btn.place(x=195,y=408)
        
        self.create_btn=Button(self.root,text="Create",bg="#228B22",bd=0,fg="#fff",activebackground="#228B22"
                        ,activeforeground="#fff",cursor="hand2",font=("times new roman",20),command=self.create_fun)
        self.create_btn.place(x=580,y=570,width=200,height=50)


class window3:
    def adm_form(self):
        e1=self.get_fname.get()+self.get_lname.get()
        e2=self.get_dob_dd.get()+self.get_dob_mm.get()+self.get_dob_yy.get()
        e3=self.get_s_phone_c.get()+self.get_s_phone.get()
        e4=self.get_gender.get()
        e5=self.get_email.get()
        e6=self.get_f_name.get()
        e7=self.get_m_name.get()
        e8=self.get_f_occ.get()
        e9=self.get_m_occ.get()
        e10=self.get_f_pho_c.get()+self.get_f_pho_e.get()
        e11=self.get_m_pho_c.get()+self.get_m_pho_e.get()
        e12=self.get_country.get()
        e13=self.get_state.get()
        e14=self.get_religion.get()
        e15=self.get_pincode.get()
        e16=self.get_course.get()
        e17=self.add_entry.get(1.0,END)

        chk_email="@gmail.com"

        if not e1:
            messagebox.showerror("Error","Every detail is required")
        elif not e2:
            messagebox.showerror("Error","Every detail is required")
        elif not self.get_dob_dd.get():
            messagebox.showerror("Error","Every detail is required")
        elif not self.get_dob_mm.get():
            messagebox.showerror("Error","Every detail is required")
        elif not self.get_dob_yy.get():
            messagebox.showerror("Error","Every detail is required")
        elif not e3:
            messagebox.showerror("Error","Every detail is required")
        elif not e4:
            messagebox.showerror("Error","Every detail is required")
        elif not e5:
            messagebox.showerror("Error","Every detail is required")
        elif(chk_email not in e5):
            messagebox.showerror("Error","Invalid Email")
        elif not e6:
            messagebox.showerror("Error","Every detail is required")
        elif not e7:
            messagebox.showerror("Error","Every detail is required")
        elif not e8:
            messagebox.showerror("Error","Every detail is required")
        elif not e9:
            messagebox.showerror("Error","Every detail is required")
        elif not e10:
            messagebox.showerror("Error","Every detail is required")
        elif not e11:
            messagebox.showerror("Error","Every detail is required")
        elif not e12:
            messagebox.showerror("Error","Every detail is required")
        elif not e13:
            messagebox.showerror("Error","Every detail is required")
        elif not e14:
            messagebox.showerror("Error","Every detail is required")
        elif not e15:
            messagebox.showerror("Error","Every detail is required")
        elif not e16:
            messagebox.showerror("Error","Every detail is required")
        elif not e17:
            messagebox.showerror("Error","Every detail is required")
        else:
            mycurs.execute("insert into form values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17))  
            mydb.commit()
            messagebox.showinfo("saved","Your details saved successfully.....")
            self.show_window4()
            # it clears the older entries 
            self.fn_entry.delete(0,"end")
            self.ln_entry.delete(0,"end")
            self.dob_dd.delete(0,"end")
            self.dob_mm.delete(0,"end")
            self.dob_yy.delete(0,"end")
            self.phone_entry.delete(0,"end")
            self.gender_cb.delete(0,"end")
            self.email_entry.delete(0,"end")
            self.f_entry.delete(0,"end")
            self.mn_entry.delete(0,"end")
            self.f_occ_cb.delete(0,"end")
            self.m_occ_cb.delete(0,"end")
            self.f_phone_entry.delete(0,"end")
            self.m_phone_entry.delete(0,"end")
            self.c_entry.delete(0,"end")
            self.s_entry.delete(0,"end")
            self.rel_cb.delete(0,"end")
            self.pin_entry.delete(0,"end")
            self.add_entry.delete(1.0,"end")
            self.course_cb.delete(0,"end")


    def __init__(self,root):
        #======================textvariables of entry and combo boxes====================
        self.get_fname=StringVar()
        self.get_lname=StringVar()
        self.get_dob_dd=StringVar()
        self.get_dob_mm=StringVar()
        self.get_dob_yy=StringVar()
        self.get_s_phone_c=StringVar()
        self.get_s_phone=StringVar()
        self.get_gender=StringVar()
        self.get_email=StringVar()
        self.get_f_name=StringVar()
        self.get_m_name=StringVar()
        self.get_f_occ=StringVar()
        self.get_m_occ=StringVar()
        self.get_f_pho_c=StringVar()
        self.get_f_pho_e=StringVar()
        self.get_m_pho_c=StringVar()
        self.get_m_pho_e=StringVar()
        self.get_country=StringVar()
        self.get_state=StringVar()
        self.get_religion=StringVar()
        self.get_pincode=StringVar()
        #self.get_address=StringVar()
        self.get_course=StringVar()
        #=================================================================


        #==================binding functions==============================
        def l_focus1(event):
            self.ln_entry.focus_set()
        def l_focus2(event):
            self.dob_dd.focus_set()
        def l_focus3(event):
            self.dob_mm.focus_set()
        def l_focus4(event):
            self.dob_yy.focus_set()
        def l_focus5(event):
            self.pho_code.focus_set()
        def l_focus6(event):
            self.phone_entry.focus_set()
        def l_focus7(event):
            self.gender_cb.focus_set()
        def l_focus8(event):
            self.email_entry.focus_set()
        def l_focus9(event):
            self.f_entry.focus_set()
        def l_focus10(event):
            self.mn_entry.focus_set()
        def l_focus11(event):
            self.f_occ_cb.focus_set()
        def l_focus12(event):
            self.m_occ_cb.focus_set()
        def l_focus13(event):
            self.f_pho_code.focus_set()
        def l_focus14(event):
            self.f_phone_entry.focus_set()
        def l_focus15(event):
            self.m_pho_code.focus_set()
        def l_focus16(event):
            self.m_phone_entry.focus_set()  
        def l_focus17(event):
            self.c_entry.focus_set()
        def l_focus18(event):
            self.s_entry.focus_set()
        def l_focus19(event):
            self.rel_cb.focus_set()
        def l_focus20(event):
            self.pin_entry.focus_set()
        def l_focus21(event):
            self.add_entry.focus_set()
        def l_focus22(event):
            self.course_cb.focus_set()
        #=======================================================================================


        #=======================================================================================
        self.root=root
        self.title=root.title("LPU Addmission Management System")      #interface name
        self.geometry=root.geometry("1350x720+0+0")                    #interface size
        self.resize=root.resizable(False,False)                       #interface resize
        self.icon=root.iconbitmap(r'myicon1.ico')                      #interface icon
        #self.config=root.configure(bg="orange")                        #interface bg


        #=======creating top frame==================
        lbl_f1=LabelFrame(root)
        lbl_f1.place(x=10,y=10,width=1330,height=80)
        
        lbl_text=Label(lbl_f1,text="Admission Management System",font=("times new roman",40),fg="#228B22",bg="#fff")
        lbl_text.pack(fill="both",expand="true")
        #===========================================


        #=======creating bottom frame================
        lbl_f2=LabelFrame(root,)
        lbl_f2.place(x=10,y=105,width=1330,height=600)
        #=============================================

        
        #========================student details================================
        #first name label and entry box
        self.first_name=Label(lbl_f2,text="First Name",font=("times new roman",15))
        self.first_name.place(x=70,y=10)

        self.fn_entry=Entry(lbl_f2,width=34,font=("times new roman",15),textvariable=self.get_fname)  
        self.fn_entry.place(x=270,y=10)

        #last name label and entry box
        self.last_name=Label(lbl_f2,text="Last Name",font=("times new roman",15))
        self.last_name.place(x=690,y=10)

        self.ln_entry=Entry(lbl_f2,width=34,font=("times new roman",15),textvariable=self.get_lname)  
        self.ln_entry.place(x=890,y=10)

        #dob entry and comboboxes
        self.std_dob=Label(lbl_f2,text="DOB(dd/mm/yy)",font=("times new roman",15))
        self.std_dob.place(x=70,y=50)

        self.dob_dd=ttk.Combobox(lbl_f2,font=("times new roman",12),width=10,textvariable=self.get_dob_dd)
        self.dob_dd['value']=('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15'
                            ,'16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
        self.dob_dd.current(0)
        self.dob_dd.place(x=270,y=50)

        self.dob_mm=ttk.Combobox(lbl_f2,font=("times new roman",12),width=10,textvariable=self.get_dob_mm)
        self.dob_mm['value']=('01','02','03','04','05','06','07','08','09','10','11','12')
        self.dob_mm.current(2)
        self.dob_mm.place(x=390,y=50)

        self.dob_yy=ttk.Combobox(lbl_f2,font=("times new roman",12),width=10,textvariable=self.get_dob_yy)
        self.dob_yy['value']=('2020','2019','2018','2017','2016','2015','2014','2013','2012','2010','2009','2008'
                        ,'2006','2005','2004','2003','2002','2001','2000','1999','1998','1997','1996','1995')
        self.dob_yy.current(17)
        self.dob_yy.place(x=510,y=50)

        #phone label,combobox,entry
        self.phone=Label(lbl_f2,text="Phone",font=("times new roman",15))
        self.phone.place(x=690,y=50)

        self.pho_code=ttk.Combobox(lbl_f2,font=("times new roman",12),width=5,textvariable=self.get_s_phone_c)
        self.pho_code['value']=('+91','+1','+27','+41','+44','+82','+86','+94','+850','+880','+971','+977')
        self.pho_code.current(0)
        self.pho_code.place(x=890,y=50)

        self.phone_entry=Entry(lbl_f2,width=26,font=("times new roman",15),textvariable=self.get_s_phone)  
        self.phone_entry.place(x=970,y=50)

        #gender entry and combobox
        self.std_gender=Label(lbl_f2,text="Gender",font=("times new roman",15))
        self.std_gender.place(x=70,y=90)

        self.gender_cb=ttk.Combobox(lbl_f2,state="readonly",font=("times new roman",12),width=40,textvariable=self.get_gender)
        self.gender_cb['value']=('','Male','Female','Other')
        self.gender_cb.current(0)
        self.gender_cb.place(x=270,y=90)
        
        #email label and entry
        self.std_email=Label(lbl_f2,text="Email",font=("times new roman",15))
        self.std_email.place(x=690,y=90)

        self.email_entry=Entry(lbl_f2,width=34,font=("times new roman",15),textvariable=self.get_email)  
        self.email_entry.place(x=890,y=90)

        #country label and entry
        self.country=Label(lbl_f2,text="Country",font=("times new roman",15))
        self.country.place(x=70,y=290)

        self.c_entry=Entry(lbl_f2,width=34,font=("times new roman",15),textvariable=self.get_country)
        self.c_entry.place(x=270,y=290)

        #state label and entry
        self.state=Label(lbl_f2,text="State",font=("times new roman",15))
        self.state.place(x=690,y=290)

        self.s_entry=Entry(lbl_f2,width=34,font=("times new roman",15),textvariable=self.get_state)  
        self.s_entry.place(x=890,y=290)

        #religion label,combobox
        self.religion=Label(lbl_f2,text="Religion",font=("times new roman",15))
        self.religion.place(x=70,y=340)

        self.rel_cb=ttk.Combobox(lbl_f2,font=("times new roman",12),width=40,textvariable=self.get_religion)
        self.rel_cb['value']=('','Hindu','Muslim','Christian','Other')
        self.rel_cb.current(0)
        self.rel_cb.place(x=270,y=340)

        #pincode label and entry 
        self.pincode=Label(lbl_f2,text="Pincode",font=("times new roman",15))
        self.pincode.place(x=690,y=340)

        self.pin_entry=Entry(lbl_f2,width=34,font=("times new roman",15),textvariable=self.get_pincode)  
        self.pin_entry.place(x=890,y=340)

        #address label and text box
        self.address=Label(lbl_f2,text="Address",font=("times new roman",15))
        self.address.place(x=70,y=390)        

        self.add_entry=Text(lbl_f2,width=34,height=5,font=("times new roman",15))  
        self.add_entry.place(x=270,y=390)

        #course lablel and combobox
        self.course_lbl=Label(lbl_f2,text="Course",font=("times new roman",15))
        self.course_lbl.place(x=690,y=390)

        self.course_cb=ttk.Combobox(lbl_f2,state="readonly",font=("times new roman",12),width=40,textvariable=self.get_course)
        self.course_cb['values']=('',"Engineering Diploma course","Marine field related Diploma course","Diploma in Fire and safety technology"
                        ,"Diploma in Hotel Management","Diploma in animation and multimedia"
                        ,"Electronics and Communication Engineering (ECE)","Mechanical Engineering (ME)","Biotechnology (BT)"
                        ,"Computer Science and Engineering (CSE)","ME-Mechatronics","Food Technology"
                        ,"Robotics and Automation","Information Technology (IT)","Automobile Engineering (AE)"
                        ,"Biomedical Engineering (BE)","Electrical Engineering (EE)","Aerospace Engineering"
                        ,"Chemical Engineering (CHE)","Electrical and Electronics Engineering (EEE)","Civil Engineering (CE)"
                        ,"B.Sc. (Hons.) Agriculture","SciencesInterior and Furniture Design","Political Science","Zoology"
                        ,"Product and Industrial Design","Geography","Physics","Fashion Design","English and Foreign Languages"
                        ,"Chemistry","Multimedia and Animation","Mathematics","Journalism and Film Production","Law","Performing ArtsFine Arts"
                        ,"MBA","MBA with Talentedge","MBA (Hons.)","MBA (Hospital and Healthcare Management)","MBA (Tourism and Hospitality)"
                        ,"MBA (International Business)","MBA (Business Analytics) with WileyNXT","MBA (Financial Markets) with NSE Academy"
                        ,"MBA (Supply Chain & Logistics) with Safeducate")
        self.course_cb.current(0)
        self.course_cb.place(x=890,y=390)
        #==============================student details ended===============================
    



        #==============================father details=======================================
        #father name label and entry

        self.father_name=Label(lbl_f2,text="Father Name",font=("times new roman",15))
        self.father_name.place(x=70,y=140)

        self.f_entry=Entry(lbl_f2,width=34,font=("times new roman",15),textvariable=self.get_f_name)  
        self.f_entry.place(x=270,y=140)

        #father ocupation label,combobox
        self.father_occ=Label(lbl_f2,text="Father Occupation",font=("times new roman",15))
        self.father_occ.place(x=70,y=190) 

        self.f_occ_cb=ttk.Combobox(lbl_f2,state="readonly",font=("times new roman",12),width=40,textvariable=self.get_f_occ)
        self.f_occ_cb['value']=('','Government Job','Businessman','Private Job','Other')
        self.f_occ_cb.current(0)
        self.f_occ_cb.place(x=270,y=190)

        #father phone,combobox,entry
        self.father_phone=Label(lbl_f2,text="Father Phone",font=("times new roman",15))
        self.father_phone.place(x=70,y=240)

        self.f_pho_code=ttk.Combobox(lbl_f2,font=("times new roman",12),width=5,textvariable=self.get_f_pho_c)
        self.f_pho_code['value']=('+91','+1','+27','+41','+44','+82','+86','+94','+850','+880','+971','+977')
        self.f_pho_code.current(0)
        self.f_pho_code.place(x=270,y=240)

        self.f_phone_entry=Entry(lbl_f2,width=26,font=("times new roman",15),textvariable=self.get_f_pho_e)  
        self.f_phone_entry.place(x=350,y=240)
        #==========================father details ended=================================================



        #==========================mother details=====================================================
        #mother name label
        self.mother_name=Label(lbl_f2,text="Mother Name",font=("times new roman",15))
        self.mother_name.place(x=690,y=140)

        self.mn_entry=Entry(lbl_f2,width=34,font=("times new roman",15),textvariable=self.get_m_name)  
        self.mn_entry.place(x=890,y=140)

        #mother occupation label,combobox
        self.mother_occ=Label(lbl_f2,text="Mother Occupation",font=("times new roman",15))
        self.mother_occ.place(x=690,y=190) 

        self.m_occ_cb=ttk.Combobox(lbl_f2,state="readonly",font=("times new roman",12),width=40,textvariable=self.get_m_occ)
        self.m_occ_cb['value']=('','Government Job','House-Wife','Private Job','Other')
        self.m_occ_cb.current(0)
        self.m_occ_cb.place(x=890,y=190)

        #mother phone label,combobox,entry
        self.mother_phone=Label(lbl_f2,text="Mother Phone",font=("times new roman",15))
        self.mother_phone.place(x=690,y=240)

        self.m_pho_code=ttk.Combobox(lbl_f2,font=("times new roman",12),width=5,textvariable=self.get_m_pho_c)
        self.m_pho_code['value']=('+91','+1','+27','+41','+44','+82','+86','+94','+850','+880','+971','+977')
        self.m_pho_code.current(0)
        self.m_pho_code.place(x=890,y=240)

        self.m_phone_entry=Entry(lbl_f2,width=26,font=("times new roman",15),textvariable=self.get_m_pho_e)  
        self.m_phone_entry.place(x=970,y=240)        
        #===========================mother details ended================================================


        #==========================event and binding of widgets=========================================
        self.fn_entry.bind("<Return>",l_focus1)
        self.ln_entry.bind("<Return>",l_focus2)
        self.dob_dd.bind("<Return>",l_focus3)
        self.dob_mm.bind("<Return>",l_focus4)
        self.dob_yy.bind("<Return>",l_focus5)
        self.pho_code.bind("<Return>",l_focus6)
        self.phone_entry.bind("<Return>",l_focus7)
        self.gender_cb.bind("<Return>",l_focus8)
        self.email_entry.bind("<Return>",l_focus9)
        self.f_entry.bind("<Return>",l_focus10)
        self.mn_entry.bind("<Return>",l_focus11)
        self.f_occ_cb.bind("<Return>",l_focus12)
        self.m_occ_cb.bind("<Return>",l_focus13)
        self.f_pho_code.bind("<Return>",l_focus14)
        self.f_phone_entry.bind("<Return>",l_focus15)
        self.m_pho_code.bind("<Return>",l_focus16)
        self.m_phone_entry.bind("<Return>",l_focus17)
        self.c_entry.bind("<Return>",l_focus18)
        self.s_entry.bind("<Return>",l_focus19)
        self.rel_cb.bind("<Return>",l_focus20)
        self.pin_entry.bind("<Return>",l_focus21)
        self.add_entry.bind("<Return>",l_focus22)
        #==============================================================================================


        #===========================save and next buttons===============================================

        #save button 
        save_btn=Button(lbl_f2,text="Save",font=("times new roman",16),cursor="hand2",fg="#fff",bg="#228822"
                ,activebackground="#228B22",activeforeground="#fff",command=self.adm_form)
        save_btn.place(x=570,y=540,width=150)

        #next button 
        #next_btn=Button(lbl_f2,text="Next >>",font=("times new roman",16),cursor="hand2",fg="#fff",bg="#228822"
                #,activebackground="#228B22",activeforeground="#fff",command=self.show_window4)
        #next_btn.place(x=690,y=540,width=150)

    def show_window4(self):
        self.nextwindow=Toplevel(self.root)
        self.obj2=window4(self.nextwindow)




class window4():
    def dialog1(self):
        self.filename1=filedialog.askopenfilename(initialdir="/",title="Select file",filetype=(("jpg type","*.jpg"),("png type","*.png")
                                                        ,("All types","*.*")) )
    def dialog2(self):
        self.filename2=filedialog.askopenfilename(initialdir="/",title="Select file",filetype=(("jpg type","*.jpg"),("png type","*.png")
                                                        ,("All types","*.*")) )
    def dialog3(self):
        self.filename3=filedialog.askopenfilename(initialdir="/",title="Select file",filetype=(("jpg type","*.jpg"),("png type","*.png")
                                                        ,("All types","*.*")) )
    def dialog4(self):
        self.filename4=filedialog.askopenfilename(initialdir="/",title="Select file",filetype=(("jpg type","*.jpg"),("png type","*.png")
                                                        ,("All types","*.*")) )
    def dialog5(self):
        self.filename5=filedialog.askopenfilename(initialdir="/",title="Select file",filetype=(("jpg type","*.jpg"),("png type","*.png")
                                                        ,("All types","*.*")) )
    def dialog6(self):
        self.filename6=filedialog.askopenfilename(initialdir="/",title="Select file",filetype=(("jpg type","*.jpg"),("png type","*.png")
                                                        ,("All types","*.*")) )
    #==========================================================================================================================
    #==========================================================================================================================
    def files_table(self):
        messagebox.askokcancel("","Upload all files otherwise it not you to next step")
        f=("insert into files values(%s,%s,%s,%s,%s,%s,%s)")
        f_get=(self.e_get.get(),self.filename1,self.filename2,self.filename3,self.filename4,self.filename5,self.filename6)   
        mycurs.execute(f,f_get)
        mydb.commit()
        messagebox.showinfo("saved","Your files saved successfully")
        self.e_entry.delete(0,"end")
        self.show_window5()
    #==========================================================================================================================
    #==========================================================================================================================
    def __init__(self,root):
        self.root=root
        self.title=root.title("LPU Admission Management System")      #interface name
        self.geometry=root.geometry("1350x720+0+0")                    #interface size
        self.resize=root.resizable(False,False)                       #interface resize
        self.icon=root.iconbitmap(r'myicon1.ico')                      #interface icon
        self.upload_icon=PhotoImage(file='upload.png')

        lbl_f3=LabelFrame(root,text="Upload Your Forms",font=("times new roman",15),fg="#228B22")
        lbl_f3.place(x=20,y=20,width=1310,height=680)

        #adhar card label and image button 
        email_lbl=Label(lbl_f3,text="Enter Email",font=("times new roman",15))
        email_lbl.place(x=400,y=15)
        
        self.e_get=StringVar()

        self.e_entry=Entry(lbl_f3,width=26,font=("times new roman",15),textvariable=self.e_get)  
        self.e_entry.place(x=700,y=15)        

        self.lbl_adhar=Label(lbl_f3,text="Upload Adhar Card",font=("times new roman",15))
        self.lbl_adhar.place(x=400,y=70)
        self.adhar_upload_btn=Button(lbl_f3,image=self.upload_icon,relief=RIDGE,cursor="hand2",command=self.dialog1)
        self.adhar_upload_btn.place(x=800,y=70)

        # 10th memo label and image buttton
        self.lbl_ten_m=Label(lbl_f3,text="Upload 10th Memo",font=("times new roman",15))
        self.lbl_ten_m.place(x=400,y=160)
        self.upload_10_btn=Button(lbl_f3,image=self.upload_icon,relief=RIDGE,cursor="hand2",command=self.dialog2)
        self.upload_10_btn.place(x=800,y=160)

        # 12th memo label and image buttton
        self.lbl_in_m=Label(lbl_f3,text="Upload 12th Memo",font=("times new roman",15))
        self.lbl_in_m.place(x=400,y=250)
        self.upload_12_btn=Button(lbl_f3,image=self.upload_icon,relief=RIDGE,cursor="hand2",command=self.dialog3)
        self.upload_12_btn.place(x=800,y=250)

        # tc memo label and image buttton
        self.lbl_tc_m=Label(lbl_f3,text="Upload Transfer Certificate",font=("times new roman",15))
        self.lbl_tc_m.place(x=400,y=340)
        self.tc_upload_btn=Button(lbl_f3,image=self.upload_icon,relief=RIDGE,cursor="hand2",command=self.dialog4)
        self.tc_upload_btn.place(x=800,y=340)

        #photos label and image buttton
        self.lbl_photos=Label(lbl_f3,text="Upload Photo",font=("times new roman",15))
        self.lbl_photos.place(x=400,y=430)
        self.pts_upload_btn=Button(lbl_f3,image=self.upload_icon,relief=RIDGE,cursor="hand2",command=self.dialog5)
        self.pts_upload_btn.place(x=800,y=430)

        #income c label and image buttton
        self.lbl_income=Label(lbl_f3,text="Upload Income Certificate",font=("times new roman",15))
        self.lbl_income.place(x=400,y=520)
        self.in_upload_btn=Button(lbl_f3,image=self.upload_icon,relief=RIDGE,cursor="hand2",command=self.dialog6)
        self.in_upload_btn.place(x=800,y=520)

        #save and next button
        #save button 
        save_btn=Button(lbl_f3,text="Save",font=("times new roman",16),cursor="hand2",fg="#fff",bg="#228822"
                        ,activebackground="#228B22",activeforeground="#fff",relief=RIDGE,command=self.files_table)
        save_btn.place(x=505,y=600,width=150)

        #next button 
        #next_btn=Button(lbl_f3,text="Next >>",font=("times new roman",16),cursor="hand2",fg="#fff",bg="#228822"
        #                ,activebackground="#228B22",activeforeground="#fff",relief=RIDGE,command=self.show_window5)
        #next_btn.place(x=690,y=600,width=150)


    def show_window5(self):
        self.nextwindow5=Toplevel(self.root)
        self.obj3=window5(self.nextwindow5)


class window5():
    def credit(self):
        if not self.cno_get.get():
            messagebox.showerror("ERROR","Please check your details")
        elif not self.cname_get.get():
            messagebox.showerror("ERROR","Please check your details")
        elif not self.m_get.get():
            messagebox.showerror("ERROR","Please check your details")
        elif self.m_get.get()=="Select Month":
            messagebox.showerror("ERROR","Please check your details")
        elif self.yr_get.get()=="Select Year":
            messagebox.showerror("ERROR","Please check your details") 
        elif not self.yr_get.get():
            messagebox.showerror("ERROR","Please check your details")
        elif not self.cvv_get.get():
            messagebox.showerror("ERROR","Please check your details")
        else:
            messagebox.showinfo("Success","Your Payment successfully completed")
            messagebox.showinfo("Success","Please check your EMAIL for admission details")
            self.cn_entry.delete(0,"end")
            self.cname_entry.delete(0,"end")
            self.cvv_entry.delete(0,"end")
            self.en.delete(0,"end")
    
    def net_b(self):
        if not self.id_get.get():
            messagebox.showerror("ERROR","Please enter your transaction ID")
        else:
            messagebox.showinfo("Success","Your Payment successfully completed")
            messagebox.showinfo("Success","Please check your EMAIL for admission details")
            self.cn_entry.delete(0,"end")
            self.cname_entry.delete(0,"end")
            self.cvv_entry.delete(0,"end")
            self.en.delete(0,"end")
    def __init__(self,root):
        self.root=root
        self.title=root.title("LPU Admission Management System")      #interface name
        self.geometry=root.geometry("1350x720+0+0")                    #interface size
        self.resize=root.resizable(False,False)                       #interface resize
        self.icon=root.iconbitmap(r'myicon1.ico')                      #interface icon
        self.qr_photo=PhotoImage(file='qr.png')
        
        # outer frame of window5
        lbl_f5=LabelFrame(self.root,text="Payment",font=("times new roman",15),fg="#228B22")
        lbl_f5.place(x=20,y=20,width=1310,height=680)
        
        # top level frame in outer frame
        lbl_f6=LabelFrame(lbl_f5)
        lbl_f6.place(x=20,y=20,width=1260,height=150)

        txt=Label(lbl_f6,text="The Admission fee for a student is 10,000 rupees",font=("times new roman",16))
        txt.place(x=30,y=20)

        txt2=Label(lbl_f6,text="semester fee all Groups is 90,000 rupees only and scholarship is applicable only for those who written JEE Mains"
                                ,font=("times new roman",16))
        txt2.place(x=30,y=60)

        txt3=Label(lbl_f6,text="Exam fee for each semester is 5,000 rupees",font=("times new roman",16))
        txt3.place(x=30,y=100)
        #==================================================================================================

        #==========================C/D card payment frame==================================================
        #credit and debit payment frame
        lbl_f7=LabelFrame(lbl_f5,text="Debit/Credit Card",font=("times new roman",13),fg="#228B22")
        lbl_f7.place(x=20,y=200,width=620,height=420)
        
        #card no label and entry
        card_no=Label(lbl_f7,text="Card Number :",font=("times new roman",16))
        card_no.place(x=40,y=30)

        self.cno_get=StringVar()
        self.cn_entry=Entry(lbl_f7,textvariable=self.cno_get,font=("times new roman",15),width=30)
        self.cn_entry.place(x=250,y=30)
        
        #cname label and entry box
        card_name=Label(lbl_f7,text="Name On Card :",font=("times new roman",16))
        card_name.place(x=40,y=100)

        self.cname_get=StringVar()
        self.cname_entry=Entry(lbl_f7,textvariable=self.cname_get,font=("times new roman",15),width=30)
        self.cname_entry.place(x=250,y=100)

        #card label and expiry comboboxes
        card_dates=Label(lbl_f7,text="Card Expiry :",font=("times new roman",16))
        card_dates.place(x=40,y=170)

        self.m_get=StringVar()
        exp_m=ttk.Combobox(lbl_f7,textvariable=self.m_get,font=("times new roman",15),width=12,state="readonly")
        exp_m['value']=('Select Month','01','02','03','04','05','06','07','08','09','10','11','12')
        exp_m.current(0)
        exp_m.place(x=250,y=170)
        
        self.yr_get=StringVar()
        exp_yr=ttk.Combobox(lbl_f7,textvariable=self.yr_get,font=("times new roman",15),width=12,state="readonly")
        exp_yr['value']=('Select Year','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2031'
                        ,'2032','2033','2034','2035')
        exp_yr.current(0)
        exp_yr.place(x=410,y=170)

        # card cvv label and entry
        card_cvv=Label(lbl_f7,text="Card CVV :",font=("times new roman",16))
        card_cvv.place(x=40,y=240)
        
        self.cvv_get=StringVar()
        self.cvv_entry=Entry(lbl_f7,textvariable=self.cvv_get,font=("times new roman",15),width=15)
        self.cvv_entry.place(x=250,y=240)

        # payment button
        pay_btn=Button(lbl_f7,text="PAY NOW",font=("times new roman",16),cursor="hand2",fg="#fff",bg="#228822"
                        ,activebackground="#228B22",activeforeground="#fff",relief=RIDGE,command=self.credit)
        pay_btn.place(x=250,y=320,width=150)
        #================================d/c card payment ended================================================


        #========================netbanking frame=============================================================
        #net banking payment frame
        lbl_f8=LabelFrame(lbl_f5,text="Net Banking/UPI",font=("times new roman",13),fg="#228B22")
        lbl_f8.place(x=660,y=200,width=620,height=420)
        
        qr_img=Label(lbl_f8,image=self.qr_photo)
        qr_img.pack(pady=40)

        lb=Label(lbl_f8,text="Enter Transaction ID",font=(" ",15))
        lb.place(x=220,y=270)

        self.id_get=StringVar()
        self.en=Entry(lbl_f8,width=30,textvariable=self.id_get,font=(" ",13))
        self.en.place(x=180,y=310)

        btn=Button(lbl_f8,text="submit",font=("times new roman",16),cursor="hand2",fg="#fff",bg="#228822"
                        ,activebackground="#228B22",activeforeground="#fff",relief=RIDGE,command=self.net_b)
        btn.place(x=260,y=350,height=30,width=100)




#=================================it is for forget password==================================================
#=================================================================================================
class window6():
    #=============================================================================================
    #==========================forget sql queries=================================================
    def database(self):
        self.u=self.for_user.get()
        self.p=self.for_pass.get()

        if not self.u:
            messagebox.showerror("Error","Please check the username")
        elif not self.p:
            messagebox.showerror("Error","Please check the Password")
        else:
            mycurs.execute("update s_signup set password=%s where username=%s",(self.p,self.u))
            mydb.commit()

            messagebox.showinfo("","Password Successfully Updated")

    #==============================================================================================
    # =============================================================================================
        
    def __init__(self,root):
        self.root=root
        self.root.title("Lovely Professional University")      
        self.root.geometry("850x700+250+10")                 
        self.root.resizable(False,False)                     
        self.root.iconbitmap(r'myicon1.ico')                 
        self.root.configure(bg="orange")                     

        #====================================================================
        title_label=Label(self.root,text="Lovely Professional University",bg="orange",fg="#fff",font=("times new roman",30),relief=GROOVE)
        title_label.place(x=0,y=0,relwidth=1)

        # creating forget frame
        for_frame=Frame(self.root,bg="white")
        for_frame.place(x=200,y=160,height=440,width=450)

        #forget password label
        self.lbl_frame=Label(for_frame,text="Forget Password",bg="white",fg="#228B22",font=("times new roman",30))
        self.lbl_frame.place(x=40,y=20)

        # labels for forget password
        lbl_user=Label(for_frame,text="Username",bg="#fff",font=("Goudy old style",18))
        lbl_user.place(x=40,y=100)
        lbl_pass=Label(for_frame,text="New Password",bg="#fff",font=("Goudy old style",18))
        lbl_pass.place(x=40,y=240)
        
        # entry boxes for forget password
        self.for_user=StringVar()
        self.for_pass=StringVar()

        def p_focus(event):
            pass_entry.focus_set()

        user_entry=Entry(for_frame,font=("times new roman",15),bg="lightgrey",textvariable=self.for_user)
        user_entry.place(x=45,y=170,width=320,height=35)
        user_entry.bind("<Return>",p_focus)

        pass_entry=Entry(for_frame,font=("times new roman",15),textvariable=self.for_pass,bg="lightgrey",show="*")
        pass_entry.place(x=45,y=310,width=320,height=35)

        
        submit_btn=Button(self.root,text="Submit",bg="#228B22",bd=0,fg="#fff",activebackground="#228B22",activeforeground="#fff",cursor="hand2",font=("times new roman",20),command=self.database)
        submit_btn.place(x=330,y=575,width=180,height=50)

class window7():
    def verify_staff(self):
        user=self.staff_u.get()
        pwd=self.staff_p.get()
        if (user=="23626" and pwd=="BhupinderKaur") or (user=="kittu123" and pwd=="01301") :
            self.details_win()
            self.staff_user_entry.delete(0,"end")
            self.staff_pass_entry.delete(0,"end")
        else:
            messagebox.showerror("ERROR","Invalid Username and Password")
    def __init__(self,root):
        self.root=root
        self.root=root
        self.title=root.title("Lovely Professional University")      #interface name
        self.geometry=root.geometry("850x700+250+10")                  #interface size
        self.resize=root.resizable(False,False)                     #interface resize
        self.icon=root.iconbitmap(r'myicon1.ico')                    #interface icon
        self.config=root.configure(bg="orange")                      #interface bg

        
        #====================================================================
        title_label=Label(self.root,text="Lovely Professional University",bg="orange",fg="#fff",font=("times new roman",40),relief=GROOVE)
        title_label.place(x=0,y=0,relwidth=1)

        #user & pass icons
        self.user_icon=PhotoImage(file='username.png')
        self.pass_icon=PhotoImage(file='password.png')
        self.exit_icon=PhotoImage(file='quit.png')
      
       
        staff_login_frame=Frame(self.root,bg="white")
        staff_login_frame.place(x=200,y=150,height=450,width=450)
        
        #login label
        lbl_frame=Label(staff_login_frame,text="Login Here",bg="white",fg="#228B22",font=("times new roman",30))
        lbl_frame.place(x=60,y=40)

        #user & pass label
        lbl_staff_user=Label(staff_login_frame,text="Username",image=self.user_icon,compound=LEFT,bg="#fff",font=("Goudy old style",18))
        lbl_staff_user.place(x=60,y=120)
        lbl_staff_pass=Label(staff_login_frame,text="Password",image=self.pass_icon,compound=LEFT,bg="#fff",font=("Goudy old style",18))
        lbl_staff_pass.place(x=61,y=245)

        #user & pass entry and set focus
        def l_focus1(event):
            self.staff_pass_entry.focus_set()
        
        
        self.staff_u=StringVar()
        self.staff_p=StringVar()
        self.staff_user_entry=Entry(staff_login_frame,textvariable=self.staff_u,font=("times new roman",15),bg="lightgrey")
        self.staff_user_entry.place(x=65,y=188,width=320,height=35)
        self.staff_pass_entry=Entry(staff_login_frame,textvariable=self.staff_p,font=("times new roman",15),bg="lightgrey",show="*")
        self.staff_pass_entry.place(x=65,y=305,width=320,height=35)
        
        # bind method of widget is used  
        self.staff_user_entry.bind("<Return>",l_focus1) 

        #login btns

        self.login_btn=Button(self.root,text="Login",bg="#228B22",bd=0,fg="#fff",activebackground="#228B22"
                    ,activeforeground="#fff",cursor="hand2",font=("times new roman",20),command=self.verify_staff)
        self.login_btn.place(x=330,y=575,width=180,height=50)

    def details_win(self):
        self.details_win=Toplevel(self.root)
        self.obj1=window8(self.details_win)


class window8():
    #======================tree view for details===================================================================
    #==============================================================================================================
    # tree view for to search particular student
    def std_d_treeview(self):
        def insert_std_details(r):
            tree_view=ttk.Treeview(self.top_lbl_frame,column=(1,2,3,4,5,6,7)
                            ,show="headings",height=12)
            tree_view.pack(pady=20)
            tree_view.heading(1,text="NAME",anchor="w")
            tree_view.heading(2,text="DOB",anchor="w")
            tree_view.heading(3,text="GENDER",anchor="w")
            tree_view.heading(4,text="EMAIL",anchor="w")
            tree_view.heading(5,text="PHONE",anchor="w")
            tree_view.heading(6,text="COURSE",anchor="w")
            tree_view.heading(7,text="ADDRESS",anchor="w")
            for i in r:
                tree_view.insert('',"end",values=i)
        
        e=self.get_s_email.get()
        mycurs.execute("select s_name,dob,gender,email,s_phone,course,address from form where email=%s",(e,) )
        r=mycurs.fetchall()
        insert_std_details(r)
    #===============================================================================================================
    #===============================================================================================================
    # tree view for to search details of parents particular student
    def par_treeview(self):
        def std_par_details(r):
            tree_view1=ttk.Treeview(self.top_lbl_frame,column=(1,2,3,4,5,6)
                            ,show="headings",height=12)
            tree_view1.pack(pady=20)
            tree_view1.heading(1,text="F NAME",anchor="w")
            tree_view1.heading(2,text="M NAME",anchor="w")
            tree_view1.heading(3,text="F PHONE",anchor="w")
            tree_view1.heading(4,text="M PHONE",anchor="w")
            tree_view1.heading(5,text="F OCCU",anchor="w")
            tree_view1.heading(6,text="M OCCU",anchor="w")
            for i in r:
                tree_view1.insert('',"end",values=i)
        
        e=self.get_s1_email.get()
        mycurs.execute("select f_name,m_name,f_phone,m_phone,f_occu,m_occu from form where email=%s",(e,) )
        r=mycurs.fetchall()
        std_par_details(r)
    #==============================================================================================================
    #==============================================================================================================
    # tree view for to delete particular student details
    def del_treeview(self):
        def del_std_details(r):
            tree_view2=ttk.Treeview(self.top_lbl_frame,column=(1,2,3,4,5,6,7)
                            ,show="headings",height=12)
            tree_view2.pack(pady=20)
            tree_view2.heading(1,text="NAME",anchor="w")
            tree_view2.heading(2,text="DOB",anchor="w")
            tree_view2.heading(3,text="GENDER",anchor="w")
            tree_view2.heading(4,text="EMAIL",anchor="w")
            tree_view2.heading(5,text="PHONE",anchor="w")
            tree_view2.heading(6,text="COURSE",anchor="w")
            tree_view2.heading(7,text="ADDRESS",anchor="w")
            for i in r:
                tree_view2.insert('',"end",values=i)
        e=self.get_ps_email.get()
        mycurs.execute("delete from form where email=%s",(e,) )
        mydb.commit()
        r=mycurs.fetchall()
        del_std_details(r)
    #================================================================================================================
    #================================================================================================================
    # tree view to fetch all students details
    def fetch_all_treeview(self):
        def fetch_std_details(r):
            tree_view=ttk.Treeview(self.top_lbl_frame,column=(1,2,3,4,5,6,7)
                            ,show="headings",height=12)
            tree_view.pack(pady=20)
            tree_view.heading(1,text="NAME",anchor="w")
            tree_view.heading(2,text="DOB",anchor="w")
            tree_view.heading(3,text="GENDER",anchor="w")
            tree_view.heading(4,text="EMAIL",anchor="w")
            tree_view.heading(5,text="PHONE",anchor="w")
            tree_view.heading(6,text="COURSE",anchor="w")
            tree_view.heading(7,text="ADDRESS",anchor="w")
            for i in r:
                tree_view.insert('',"end",values=i)

        
        mycurs.execute("select s_name,dob,gender,email,s_phone,course,address from form")
        r=mycurs.fetchall()
        fetch_std_details(r)
    #================================================================================================================
    #================================================================================================================
    # tree view to fetch particular student files
    def std_files_treeview(self):
        def std_files_details(r):
            tree_view=ttk.Treeview(self.top_lbl_frame,column=(1,2,3,4,5,6,7)
                            ,show="headings",height=12)
            tree_view.pack(pady=20)
            tree_view.heading(1,text="EMAIL",anchor="w")
            tree_view.heading(2,text="ADHAR",anchor="w")
            tree_view.heading(3,text="10TH MEMO",anchor="w")
            tree_view.heading(4,text="12TH MEMO",anchor="w")
            tree_view.heading(5,text="TC",anchor="w")
            tree_view.heading(6,text="PHOTO",anchor="w")
            tree_view.heading(7,text="INCOME",anchor="w")
            for i in r:
                tree_view.insert('',"end",values=i)

        
        mycurs.execute("select*from files")
        r=mycurs.fetchall()
        std_files_details(r)
    #================================================================================================================
    #================================================================================================================
    # tree view to delete particular student files
    def del_files_treeview(self):
        def del_std_files(r):
            tree_view=ttk.Treeview(self.top_lbl_frame,column=(1,2,3,4,5,6,7)
                            ,show="headings",height=12)
            tree_view.pack(pady=20)
            tree_view.heading(1,text="EMAIL",anchor="w")
            tree_view.heading(2,text="ADHAR",anchor="w")
            tree_view.heading(3,text="10TH MEMO",anchor="w")
            tree_view.heading(4,text="12TH MEMO",anchor="w")
            tree_view.heading(5,text="TC",anchor="w")
            tree_view.heading(6,text="PHOTO",anchor="w")
            tree_view.heading(7,text="INCOME",anchor="w")
            for i in r:
                tree_view.insert('',"end",values=i)

        e=self.get_email.get()
        mycurs.execute("delete from files where email=%s",(e,) )
        mydb.commit()
        r=mycurs.fetchall()
        del_std_files(r)
    def __init__(self,root):
        self.root=root
        self.title=root.title("LPU Addmission Management System")      
        self.geometry=root.geometry("1350x720+0+0")                    
        #self.resize=root.resizable(False,False)                       
        self.icon=root.iconbitmap(r'myicon1.ico')         

        # create  top labelframe
        self.top_lbl_frame=LabelFrame(self.root,text="Display Details",font=("times new roman",15),fg="#228B22")  
        self.top_lbl_frame.place(x=20,y=20,width=1310,height=350)

        
        #======================================================================================================
        #======================================================================================================
        # create  bottom labelframe
        bottom_lbl_frame=LabelFrame(self.root,font=("times new roman",15),fg="#228B22")  
        bottom_lbl_frame.place(x=20,y=400,width=700,height=300)

        #======================================================================================================
        # to search particular student details 
        search=Label(bottom_lbl_frame,text="Search Student Details",font=("times new roman",15))
        search.place(x=20,y=40)

        self.get_s_email=StringVar()
        search_entry=Entry(bottom_lbl_frame,textvariable=self.get_s_email,font=("times new roman",15),bg="#fff")
        search_entry.place(x=270,y=40,width=280,height=30)
        search_entry.insert(0,"Enter student Email")

        search_btn=Button(bottom_lbl_frame,text="search",bg="#228B22",fg="#fff",activebackground="#228B22",activeforeground="#fff"
                        ,cursor="hand2",font=("times new roman",15),relief=RIDGE,command=self.std_d_treeview)
        search_btn.place(x=570,y=40,width=100,height=30)
        #=======================================================================================================
        # to search parent details of particular student
        search=Label(bottom_lbl_frame,text="Search Student parent Details",font=("times new roman",15))
        search.place(x=20,y=120)

        self.get_s1_email=StringVar()
        search_entry=Entry(bottom_lbl_frame,textvariable=self.get_s1_email,font=("times new roman",15),bg="#fff")
        search_entry.place(x=270,y=120,width=280,height=30)
        search_entry.insert(0,"Enter student Email")

        search_btn=Button(bottom_lbl_frame,text="search",bg="#228B22",fg="#fff",activebackground="#228B22",activeforeground="#fff"
                        ,cursor="hand2",font=("times new roman",15),relief=RIDGE,command=self.par_treeview)
        search_btn.place(x=570,y=120,width=100,height=30)
        #========================================================================================================
        # to delete particular student detail
        search=Label(bottom_lbl_frame,text="Delete student Details",font=("times new roman",15))
        search.place(x=20,y=200)

        self.get_ps_email=StringVar()
        search_entry=Entry(bottom_lbl_frame,textvariable=self.get_ps_email,font=("times new roman",15),bg="#fff")
        search_entry.place(x=270,y=200,width=280,height=30)
        search_entry.insert(0,"Enter student Email")

        search_btn=Button(bottom_lbl_frame,text="Delete",bg="#228B22",fg="#fff",activebackground="#228B22",activeforeground="#fff"
                        ,cursor="hand2",font=("times new roman",15),relief=RIDGE,command=self.del_treeview)
        search_btn.place(x=570,y=200,width=100,height=30)



        #==========================================================================================================
        #================================bottom right==============================================================
        # create bottom_right labelframe

        bottom_r_frame=LabelFrame(self.root,font=("times new roman",15),fg="#228B22")  
        bottom_r_frame.place(x=740,y=400,width=590,height=300)
        
        #==========================================================================================================
        # to fetch all details in form table
        search=Label(bottom_r_frame,text="Fetch All Details",font=("times new roman",15))
        search.place(x=60,y=40)

        fetch_btn=Button(bottom_r_frame,text="Fetch",bg="#228B22",fg="#fff",activebackground="#228B22",activeforeground="#fff"
                       ,cursor="hand2",font=("times new roman",15),relief=RIDGE,command=self.fetch_all_treeview)
        fetch_btn.place(x=300,y=40,height=30,width=100)

        #==========================================================================================================
        # to fetch particular student files form table
        search=Label(bottom_r_frame,text="Fetch Particular student Files",font=("times new roman",15))
        search.place(x=60,y=100)

        fetch_btn=Button(bottom_r_frame,text="Fetch",bg="#228B22",fg="#fff",activebackground="#228B22",activeforeground="#fff"
                       ,cursor="hand2",font=("times new roman",15),relief=RIDGE,command=self.std_files_treeview)
        fetch_btn.place(x=300,y=100,height=30,width=100)

        #==========================================================================================================
        # to delete particular student files form table
        search=Label(bottom_r_frame,text="delete student Files",font=("times new roman",15))
        search.place(x=60,y=160)

        self.get_email=StringVar()
        search_entry=Entry(bottom_r_frame,textvariable=self.get_email,font=("times new roman",15),bg="#fff")
        search_entry.place(x=250,y=160,width=280,height=30)
        search_entry.insert(0,"Enter student Email")

        search_btn=Button(bottom_r_frame,text="Fetch",bg="#228B22",fg="#fff",activebackground="#228B22",activeforeground="#fff"
                       ,cursor="hand2",font=("times new roman",15),relief=RIDGE,command=self.del_files_treeview)
        search_btn.place(x=300,y=200,height=30,width=100)

if __name__ == "__main__":
    main()