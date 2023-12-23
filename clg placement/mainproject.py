from tkinter import *
from sqlite3 import *
from tkinter import ttk
import re
root = Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
size=str(w)+'x'+str(h)
root.geometry(size)
root.title("Government polytechnic mumbai")
def main():
    root.geometry(size)
    header = Frame(root)
    content = Frame(root, bg='#f5f5f5')
    
    
    root.columnconfigure(0, weight=1) # 100% 

    root.rowconfigure(0, weight=2) # 10%
    root.rowconfigure(1, weight=6) # 80%
    

    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')
    canvas1=Canvas(header, width=1350, height=600,bg='turquoise2')
    canvas1.place(x=0,y=0)
    #photo=PhotoImage(file=r"logo.png")
    #canvas1.create_image(130,70,image=photo) 

    h1 = Label(canvas1,text="Government Polytechnic Mumbai",bg='turquoise2',fg="white",font=("Times new roman",25,"bold"),width=40).place(x=300, y=20)
    h2=Label(canvas1,text="Maharashtra Government Autonomus institute",bg='turquoise2',fg="white",font=("Times new roman",15,"bold"),width=65).place(x=300,y=70)
    h3=Label(canvas1,text="शासकीय तंत्रनिकेतन मुंबई",bg='turquoise2',fg="white",font=("Times new roman",20,"bold"),width=40).place(x=370,y=100)
    h4=Label(canvas1,text="महाराष्ट्र शासनाची स्वायत्त संस्था",bg='turquoise2',fg="white",font=("Times new roman",15,"bold"),width=65).place(x=300,y=140)
    
    l1=Label(content,text="Training and Placement cell",bg="#f5f5f5",fg="brown",font=("Times new roman",20,"bold"),width=20).place(x=7,y=35)

    training="""The Placement Cell plays a crucial role in locating job opportunities for Under Graduates and Post Graduates passing out from the"""
    training1="""college by keeping in touch with reputed firms and industrial establishments. The Placement Cell operates round the year to facilitate"""
    training2="""contacts between companies and graduates. The number of students placed through the campus interviews is continuously rising. On"""
    training3="""invitation, many reputed industries visit the institute to conduct interviews."""

    training4="""We have been successful in maintaining our high placement statistics over the years and the fact that our students bear the recession"""
    training5="""record breaking placements itself is a testimony to our quality. Our ingenious alumnae have set new standards in the corporate world """
    training6="""through their blues with estimable contributions and it is my firm conviction that we will continue that legacy inthe years to come."""

    training7="""The Placement Cell organizes career guidance programmes for all the students starting from first year. The cell arranges training"""
    training8=""" programmes like Mock Interviews, Group Discussions, Communication Skills Workshop etc and it also organizes Public Sector"""
    training9="""Exam Training for students who are interested to join Government Sectors. It also invites HR Managers from different """
    training10="""industries to conduct training programmes for final year students."""

    training11="""TATA CONSULTANCY SERVICES has accredited our college in the year 2011, from which they are visiting our college every year for"""
    training12="""conducting Placement Training programmes and Campus Interviews"""
    
    l2=Label(content,text=training,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=90)
    l2=Label(content,text=training1,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=115)
    l2=Label(content,text=training2,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=140)
    l2=Label(content,text=training3,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=165)

    l2=Label(content,text=training4,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=205)
    l2=Label(content,text=training5,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=230)
    l2=Label(content,text=training6,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=255)

    l2=Label(content,text=training7,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=295)
    l2=Label(content,text=training8,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=320)
    l2=Label(content,text=training9,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=345)
    l2=Label(content,text=training10,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=370)

    """l2=Label(content,text=training11,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=360)
    l2=Label(content,text=training12,bg="#f5f5f5",font=("Times new roman",16)).place(x=10,y=385)"""
    ###buttons
    #b1=Button(content,text="Register a student",font=("Bookman Old Style",10,"bold"),activebackground="turquoise2",activeforeground="black",bg="white",padx=20,pady=10,command=signup).place(x=1145,y=105)
    #b2=Button(content,text="Log in as a TPO",font=("Bookman Old Style",10,"bold"),activebackground="turquoise2",activeforeground="black",bg="white",padx=30,pady=10,command=TPO).place(x=1145,y=160)
    #b3=Button(content,text="Admin login",font=("Bookman Old Style",10,"bold"),activebackground="turquoise2",activeforeground="black",bg="white",padx=43,pady=10,command=Admin).place(x=1145,y=215)
    #b4=Button(content,text="Show all",font=("Bookman Old Style",10,"bold"),activebackground="#3D8FA5",activeforeground="white",bg="white",padx=55,pady=10,command=showall).place(x=1145,y=210)
    #show all should be in campus(admin login)
    #b4=Button(content,text="Selected students",font=("Bookman Old Style",10,"bold"),activebackground="turquoise2",activeforeground="black",bg="white",padx=25,pady=10,command=selected).place(x=1145,y=270)
    #b5=Button(content,text="Company Details",font=("Bookman Old Style",10,"bold"),activebackground="turquoise2",activeforeground="black",bg="white",padx=27,pady=10,command=company_details).place(x=1145,y=325)
    #b6=Button(content,text="Student Sign in",font=("Bookman Old Style",10,"bold"),activebackground="turquoise2",activeforeground="black",bg="white",padx=27,pady=10,command=login_student).place(x=1145,y=380)
    b6=Button(content,text="home",font=("Bookman Old Style",10,"bold"),activebackground="turquoise2",activeforeground="black",bg="white",padx=27,pady=10,command=HOME).place(x=1145,y=380)
    root.mainloop()

    root.mainloop()    
#for home page
def student_section():
    root.geometry('1350x700')
    root.title("Government polytechnic mumbai")
    canvass = Canvas(root,width=1350, height=700)
    canvass.place(x=0,y=0)

    p1=PhotoImage(file="")
    canvass.create_image(0,0,image=p1) 
    canvas1234 = Canvas(canvass,width=700, height=450)
    canvas1234.place(x=300,y=130)
    canvas1234.create_rectangle(5,5,700,450,width=5,outline="black")
    l2=Button(canvas1234,text="Student Section",fg="Dark Blue",font=("Georgia",22,"bold"),height=1,width=34,bg="white")
    l2.place(x=10,y=10)
    
    photo12=PhotoImage(file=r"Slogo.PNG")
    canvas1234.create_image(40,10,image=photo12)
    
    canvas1234.create_rectangle(70,120,310,400,width=2,outline="black")
    canvas1234.create_rectangle(400,120,640,400,width=2,outline="black")
    bb1=Button(canvas1234,text=" Student Login  ",fg="Dark Blue",command=login_student,font=("Georgia",14,"bold"),width=17,bg="white")
    bb1.place(x=74,y=355)
    bb2=Button(canvas1234,text="Student Registeration",fg="Dark Blue",command=signup,font=("Georgia",14,"bold"),bg="white")
    bb2.place(x=402  ,y=355)

    photo12=PhotoImage(file=r"Slogin.PNG")
    canvas1234.create_image(190,250,image=photo12)

    #canvas1234.create_rectangle(74,120,315,400,width=2,outline="black")
    photo123=PhotoImage(file=r"Sreg.PNG")
    canvas1234.create_image(515,250,image=photo123)
    b4=Button(canvas1234,text="Back",font=("Bookman Old Style",10,"bold"),activeforeground="black",bg="white",padx=30,pady=7,command=HOME)
    b4.place(x=310,y=400)
    mainloop()

def HOME():
    root.geometry('1350x700')
    root.title("Government polytechnic mumbai")
    canvass = Canvas(root,width=1350, height=700)
    canvass.place(x=0,y=0)


    p1=PhotoImage(file="background2.png")
    canvass.create_image(0,0,image=p1) 

    canvas123 = Canvas(canvass,width=1110, height=450)
    canvas123.place(x=100,y=150)
    canvas123.create_rectangle(5,5,1110,450,width=5,outline="black",fill="WHITE")


    l2=Button(canvas123,text="GOVERNMENT POLYTECHNIC MUMBAI",fg="Brown",font=("Georgia",18,"bold"),bg="white",width=40)
    l2.place(x=250,y=10)
    canvas123.create_line(0,70,1110,70,width=2)
    photo=PhotoImage(file=r"RR.PNG")
    canvas123.create_image(120,250,image=photo) 
    b1=Button(canvas123,text="Student",font=("Georgia",12,"bold"),activebackground="#3D8FA5",activeforeground="white",bg="white",padx=40,pady=4,command=student_section).place(x=40,y=350)

    phot=PhotoImage(file=r"Register.PNG")
    canvas123.create_image(330,250,image=phot)
    b2=Button(canvas123,text="TPO Login",font=("Georgia",12,"bold"),activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,command=TPO).place(x=230,y=350)

    pho=PhotoImage(file=r"admin.PNG")
    canvas123.create_image(540,250,image=pho)
    b3=Button(canvas123,text="Admin Login",font=("Georgia",12,"bold"),activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,command=Admin).place(x=440,y=350)


    ph=PhotoImage(file=r"selected_students.PNG")
    canvas123.create_image(770,250,image=ph)
    b4=Button(canvas123,text="Selected Students",font=("Georgia",12,"bold"),height=1,width=10,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,command=selected).place(x=670,y=350)

    p=PhotoImage(file=r"company_details.PNG")
    canvas123.create_image(995,250,image=p)
    b5=Button(canvas123,text="Company Details",font=("Georgia",12,"bold"),height=1,width=10,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,command=company_details).place(x=880,y=350)

    b=Button(canvas123,text="Back",command=main,font=("Georgia",13,"bold"),bg="white",fg="black",padx=40,pady=4).place(x=470,y=400)
    mainloop()


#for 1st button register a student
def signup():
    root.geometry("1350x700")
    root.resizable(0,0)
    img1=PhotoImage(file="background.png")
    canvas = Canvas(root, width=w-15, height=h-40,bg="blue")
    canvas.place(x=0,y=0)
    a=Label(canvas,image=img1).place(x=10,y=10)
    def table():       
        db=connect("student_register.db")
        f=db.cursor()
        f.execute("""Create table if not exists 'signup'(Name text,Enroll_no TEXT,dob TEXT,Gender TEXT,Mobile_no INT,
                        Mobile_no_optional INT,Mail TEXT,Address TEXT,Dept_name TEXT,Year INT,Per_1st REAL,Per_2nd REAL,
                        Per_3rd REAL,per_10th REAL,pass_yr_10th INT,per_12th REAL,pass_yr_12th INT,s1 TEXT,s1m INT,
                        s2 TEXT,s2m INT,s3 TEXT,s3m INT,s4 TEXT,s4m INT,s5 TEXT,s5m INT,Project_details TEXT)""")
        f.execute("insert into 'signup' values('{}','{}','{}','{}',{},{},'{}','{}','{}',{},{},{},{},{},{},{},{},'{}',{},'{}',{},'{}',{},'{}',{},'{}',{},'{}')".format(n1.get(),en.get(),dob.get(),g.get(),mob.get(),mob1.get(),mail.get(),add.get(),dep.get(),yr.get(),fy.get(),sy.get(),ty.get(),sc.get(),scy.get(),hsc.get(),hscy.get(),s1.get(),s1m.get(),s2.get(),s2m.get(),s3.get(),s3m.get(),s4.get(),s4m.get(),s5.get(),s5m.get(),p.get()))
        db.commit()
        db.close()

    n1=StringVar()
    en=StringVar()
    dob=StringVar()
    g=StringVar()
    mob=IntVar()
    mob1=IntVar()
    mail=StringVar()
    add=StringVar()
    dep=StringVar()
    yr=IntVar()
    fy=IntVar()
    sy=IntVar()
    ty=IntVar()
    sc=IntVar()
    scy=IntVar()
    hsc=IntVar()
    hscy=IntVar()
    s1=StringVar()
    s1m=IntVar()
    s2=StringVar()
    s2m=IntVar()
    s3=StringVar()
    s3m=IntVar()
    s4=StringVar()
    s4m=IntVar()
    s5=StringVar()
    s5m=IntVar()
    p=StringVar()

   


    def form1():
        root.geometry(size)


   
        canvas1 = Canvas(root, width=870, height=700,bg="white")
        canvas1.place(x=220,y=20)

        

        Label1=Label(canvas1,text="Student Registration Form",fg="brown",bg="white",font=("Georgia",20,"bold"),width=30)
        Label1.place(x=140,y=30)

       
        Label2=Label(canvas1,text="Name:",bg="white",font=("Bold",12))
        Label2.place(x=40,y=100)

       
        e2=Entry(canvas1,textvariable=n1,width=60,font=(12))
        e2.place(x=130,y=100)
   


        Label3=Label(canvas1,text="Enrollment No:",bg="white",font=("Bold",12))
        Label3.place(x=40,y=140)
        e2=Entry(canvas1,textvariable=en,font=(12))
        e2.place(x=150,y=140)

        Labelp=Label(canvas1,text="Personal Details:",bg="white",font=("Bold",16))
        Labelp.place(x=40,y=180)

        Label4=Label(canvas1,text="DOB:",bg="white",font=("Bold",12))
        Label4.place(x=40,y=220)
        e3=Entry(canvas1,textvariable=dob,font=(12),width=14)
        e3.place(x=100,y=220)


        Label4=Label(canvas1,text="Gender:",bg="white",font=("Bold",12))
        Label4.place(x=40,y=260)
        Radiobutton(canvas1,text="Male",value='Male',variable=g,font=(12),bg="white").place(x=120,y=260)
        Radiobutton(canvas1,text="Female",value='Female',variable=g,bg="white",font=(12)).place(x=200,y=260)
       

        Label7=Label(canvas1,text="Mobile Number:",bg="white",font=("Bold",12))
        Label7.place(x=40,y=300)
        e4=Entry(canvas1,textvariable=mob,font=(12))
        e4.place(x=165,y=300)
     
       
        Label71=Label(canvas1,text="Alternate Mobile No:",bg="white",font=("Bold",12))
        Label71.place(x=335,y=300)
        e41=Entry(canvas1,textvariable=mob1,font=(12))
        e41.place(x=490,y=300)
       

        Label8=Label(canvas1,text="Email ID:",bg="white",font=("Bold",12))
        Label8.place(x=40,y=340)
        e5=Entry(canvas1,textvariable=mail,width=60,font=(12))
        e5.place(x=125,y=340)
       
       
        Label9=Label(canvas1,text="Address:",bg="white",font=("Bold",12))
        Label9.place(x=40,y=380)
        e6=Entry(canvas1,textvariable=add,font=(12))
        e6.place(x=125,y=380)

        Labelp1=Label(canvas1,text="Educational Details:",bg="white",font=("Bold",16))
        Labelp1.place(x=40,y=430)
       
        Label5=Label(canvas1,text="Department Name:",bg="white",font=("Bold",12))
        Label5.place(x=40,y=470)
        l1=["Information Technology","Computer Engineering","Civil Engineering","Mechanical Engineering","Electronics Engineering","Electrical Engineering","Rubber Technology","Leather Technology","Instrumentation Engineering","Science and Humanities"]
        o=OptionMenu(canvas1,dep,*l1)
        o.config(width=20)
        dep.set("Select Dept:")
        o.place(x=180,y=470)

        Label11=Label(canvas1,text="Passing Year:",bg="white",font=("Bold",12))
        Label11.place(x=40,y=510)
        e8=Entry(canvas1,textvariable=yr,font=(12))
        e8.place(x=160,y=510)
       

       
        Label12=Label(canvas1,text="FY percentage:",bg="white",font=("Bold",12))
        Label12.place(x=40,y=540)
        e9=Entry(canvas1,textvariable=fy,font=(12))
        e9.place(x=160,y=540)

     
        Label13=Label(canvas1,text="SY percentage:",bg="white",font=("Bold",12))
        Label13.place(x=40,y=580)
        e10=Entry(canvas1,textvariable=sy,font=(12))
        e10.place(x=160,y=580)

       
        Label14=Label(canvas1,text="TY percentage:",bg="white",font=("Bold",12))
        Label14.place(x=40,y=620)
        e11=Entry(canvas1,textvariable=ty,font=(12))
        e11.place(x=160,y=620)

       
        
        def ch():
            if n1.get()=="":
                Label2=Label(canvas1,text="Please enter the name",bg="white",fg="red",font=("Bold",12))
                Label2.place(x=650,y=100)
            else:
                n1.get()

            if en.get()=="" and len(en.get())!=9:
                Label2=Label(canvas1,text="Enrollment no is empty",bg="white",fg="red",font=("Bold",12))
                Label2.place(x=500,y=140)
            else:
                en.get()
           
            if (re.match(r'\d{1,2}-\d{1,2}-\d{4}',dob.get())):
                dob.get()
        
            else:
                Label4=Label(canvas1,text="enter valid date",bg="white",fg="red",font=("Bold",12))
                Label4.place(x=500,y=220)
            if g.get()=="":
                Label4=Label(canvas1,text="Select the gender",bg="white",fg="red",font=("Bold",12))
                Label4.place(x=500,y=260)
            else:
                g.get()
           
            mobb=str(mob.get())
               
               
            if (re.match(r'0\d7|8|9\d{9}',mobb)):
                mob.get()
       
            else:
                Label7=Label(canvas1,text="Mobile no is wrong",bg="white",fg="red",font=("Bold",12))
                Label7.place(x=600,y=300)

            mobb1=str(mob1.get())
            if (re.match(r'\d7|8|9\d{9}',mobb1)):
                mob1.get()
            else:
                Label7=Label(canvas1,text="Mobile no is wrong",bg="white",fg="red",font=("Bold",12))
                Label7.place(x=600,y=300)
            if (re.match(r'\w+[.-]?\w+[@]\w+[.]\w+',mail.get())):
                mail.get()
       
            else:
                Label8=Label(canvas1,text="Mail id is wrong",bg="white",fg="red",font=("Bold",12))
                Label8.place(x=650,y=340)
            if add.get()=="":
                Label9=Label(canvas1,text="Address field is empty",bg="white",fg="red",font=("Bold",12))
                Label9.place(x=500,y=380)
            else:
                add.get()

            if yr.get()<2010 or yr.get()>2017:
                Label15=Label(canvas1,text="Enter valid year",bg="white",fg="red",font=("Bold",12))
                Label15.place(x=500,y=510)
            else:
                yr.get()
           
           
            if fy.get()<10 or fy.get()>99:
                Label12=Label(canvas1,text="Enter valid percentage",bg="white",fg="red",font=("Bold",12))
                Label12.place(x=500,y=540)
            else:
                fy.get()
           
               
            if sy.get()<10 or sy.get()>99:
                Label12=Label(canvas1,text="Enter valid percentage",bg="white",fg="red",font=("Bold",12))
                Label12.place(x=500,y=580)
            else:
                sy.get()
       

            if ty.get()<10 or ty.get()>99:
                Label12=Label(canvas1,text="Enter valid percentage",bg="white",fg="red",font=("Bold",12))
                Label12.place(x=500,y=620)
            else:
                ty.get()
                form2()
           
            """sy1=str(sy.get())
            if (re.match(r'\d\d\.\d\d',sy1)):
                sy.get()
                form2()
            else:
                Label12=Label(canvas1,text="enter valid percentage",fg="red",font=("Bold",12))
                Label12.place(x=500,y=580)

            ty1=str(ty.get())
            if (re.match(r'\d\d.\d\d',ty1)):
                ty.get()
                form2()
            else:
                Label12=Label(canvas1,text="Enter valid percentage",fg="red",font=("Bold",12))
                Label12.place(x=500,y=620)"""
        b=Button(canvas1,text="Next",command=ch,bg="white",padx=40,pady=4,border=3).place(x=160,y=650)
        b1=Button(canvas1,text="Back",command=student_section,bg="white",padx=40,pady=4,border=3).place(x=290,y=650)
    def form2():
        root.geometry(size)


   
        canvas2 = Canvas(root, width=870, height=700,bg="white")
        canvas2.place(x=220,y=20)
   
       
        Label15=Label(canvas2,text="10th percentage:",bg="white",font=("Bold",12))
        Label15.place(x=40,y=100)
        e111=Entry(canvas2,textvariable=sc,font=(12))
        e111.place(x=175,y=100)
       
        Label15=Label(canvas2,text="10th passing year:",bg="white",font=("Bold",12))
        Label15.place(x=40,y=140)
        e111=Entry(canvas2,textvariable=scy,font=(12))
        e111.place(x=185,y=140)

        Label15=Label(canvas2,text="12th percentage(if applicable):",bg="white",font=("Bold",12))
        Label15.place(x=40,y=180)
        e111=Entry(canvas2,textvariable=hsc,font=(12))
        e111.place(x=260,y=180)
       
        Label15=Label(canvas2,text="12th passing year(if applicable):",bg="white",font=("Bold",12))
        Label15.place(x=40,y=220)
        e111=Entry(canvas2,textvariable=hscy,font=(12))
        e111.place(x=270,y=220)

        if  dep.get()=="Information Technology":
            l1=["python","java","cpp","c","html",".net"]
        elif dep.get()=="Computer Engineering":
            l1=["abc","def","ghi"]
        elif  dep.get()=="Civil Engineering":
            l1=[]
        elif dep.get()=="Mechanical Engineering":
            l1=[]
        elif dep.get()=="Electronics Engineering":
            l1=[]
        elif dep.get()=="Electrical Engineering":
            l1=[]
        elif dep.get()=="Rubber Technology":
            l1=[]
        elif dep.get()=="Leather Technology":
            l1=[]
        elif dep.get()=="Instrumentation Engineering":
            l1=[]
        elif dep.get()=="Science and Humanities":
            l1=[]
           
        Labelp2=Label(canvas2,text="Intrested subjects:",bg="white",font=("Bold",16))
        Labelp2.place(x=40,y=260)

        Labelp3=Label(canvas2,text="Subjects:",bg="white",font=("Bold",12))
        Labelp3.place(x=85,y=300)
        Labelp4=Label(canvas2,text="Marks",bg="white",font=("Bold",12))
        Labelp4.place(x=300,y=300)
       
        Label15=Label(canvas2,text="1:",bg="white",font=("Bold",12))
        Label15.place(x=40,y=340)
        o=OptionMenu(canvas2,s1,*l1)
        o.config(width=20)
        s1.set("Select skills:")
        o.place(x=60,y=340)
        e12m=Entry(canvas2,textvariable=s1m,font=(12))
        e12m.place(x=250,y=340)
        s1m.get()
       
        Label16=Label(canvas2,text="2:",bg="white",font=("Bold",12))
        Label16.place(x=40,y=380)
        o=OptionMenu(canvas2,s2,*l1)
        o.config(width=20)
        s1.set("Select skills:")
        o.place(x=60,y=380)
        e13m=Entry(canvas2,textvariable=s2m,font=(12))
        e13m.place(x=250,y=380)
        s2m.get()
       
        Label17=Label(canvas2,text="3:",bg="white",font=("Bold",12))
        Label17.place(x=40,y=420)
        o=OptionMenu(canvas2,s3,*l1)
        o.config(width=20)
        s1.set("Select skills:")
        o.place(x=60,y=420)
        s3.get()
        e14m=Entry(canvas2,textvariable=s3m,font=(12))
        e14m.place(x=250,y=420)
        s3m.get()
       
        Label18=Label(canvas2,text="4:",bg="white",font=("Bold",12))
        Label18.place(x=40,y=460)
        o=OptionMenu(canvas2,s4,*l1)
        o.config(width=20)
        s1.set("Select skills:")
        o.place(x=60,y=460)
        s4.get()
        e15m=Entry(canvas2,textvariable=s4m,font=(12))
        e15m.place(x=250,y=460)
        s4m.get()
       
        Label19=Label(canvas2,text="5:",bg="white",font=("Bold",12))
        Label19.place(x=40,y=500)
        o=OptionMenu(canvas2,s5,*l1)
        o.config(width=20)
        s1.set("Select skills:")
        o.place(x=60,y=500)
        s5.get()
        e16m=Entry(canvas2,textvariable=s5m,font=(12))
        e16m.place(x=250,y=500)
        s5m.get()
       
        Label20=Label(canvas2,text="Projects",bg="white",font=("Bold",12))
        Label20.place(x=40,y=540)
        e17=Entry(canvas2,textvariable=p,font=(12),width=90)
        e17.place(x=160,y=540)
        def table2():
            sc1=str(sc.get())
            if (re.match(r'/d/d./d/d',sc1)):
                sc.get()
                form2()
            else:
                Label12=Label(canvas2,text="enter valid percentage",fg="red",font=("Bold",12))
                Label12.place(x=500,y=100)
               
           
            if scy.get()<2010 or scy.get()>2017:
                Label15=Label(canvas2,text="enter valid year",fg="red",font=("Bold",12))
                Label15.place(x=500,y=140)
            else:
                scy.get()
            hsc1=str(hsc.get())
            if (re.match(r'/d/d./d/d',hsc1)):
                hsc.get()
                form2()
            else:
                Label12=Label(canvas2,text="enter valid percentage",fg="red",font=("Bold",12))
                Label12.place(x=500,y=180)
               
           
            if hscy.get()<2010 or hscy.get()>2017:
                Label15=Label(canvas2,text="enter valid year",fg="red",font=("Bold",12))
                Label15.place(x=500,y=220)
            else:
                hscy.get()
            if s1.get() or s2.get()=="":
                 Label15=Label(canvas2,text="minimum 2 subjects with marks are required.",fg="red",font=("Bold",12))
                 Label15.place(x=500,y=340)
            else:
                s1.get()
                s2.get()
            if s2m.get()<35 or s2m.get()>100 or s1m.get()<35 or s1m.get()>100:
                 Label15=Label(canvas2,text="marks are out of range.",fg="red",font=("Bold",12))
                 Label15.place(x=500,y=380)
            else:
                s1m.get()
                s2m.get()
               
            if p.get()=="":
                Label2=Label(canvas2,text="fill the project details.",fg="red",font=("Bold",12))
                Label2.place(x=500,y=540)
            else:
                p.get()
                table()

       
        b4=Button(canvas2,text="Back",command=form1,bg="white",padx=40,pady=4,border=3).place(x=160,y=600)
        b2=Button(canvas2,text="Submit",command=table2,bg="white",padx=40,pady=4,border=3).place(x=290,y=600)
           
    form1()
    root.mainloop()
    

    
#for 2nd button tpo cordinator
def TPO():
    def check():
        global a,d,r,rec
        a=connect('student_register.db')
        d=a.cursor()
        d.execute("select login from logindata where login='{}'".format(ac.get()))
        r=d.fetchall()
        if not r:
            Label(canvas2,text="User id is Not Present",fg="red",bg="white",font=("Arial Rounded MT Bold",12),width=30).place(x=500,y=300)
        else:
            d.execute("select * from logindata where login='{}'".format(ac.get()))
            rec=d.fetchall()
            for row in rec:
                a=str(pa.get())
                if(row[1]==a and row[0]==ac.get()):
                    dept1()
                else:
                    Label(canvas2,text="Wrong Password!!!!",fg="red",font=("Arial Rounded MT Bold",12),width=30).place(x=400,y=340)
    def test():
        global c
        a=pa.get()
        c=len(str(a))
        if(c<=5):
            Label(canvas2,text="Password :",bg="white",font=("Georgia",13,"bold")).place(x=235,y=340)
            check()
        else:
            Label(canvas2,text="Wrong password:",bg="white",font= ("bold",13),fg="red2").place(x=400,y=340)
#IF
    def IF():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Information Technology'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="white",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()
        
#ET
    def ET():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Electrical Technology'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="#fff9fe",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()
#COE
    def COE():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Computer Engineering'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="#fff9fe",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()
        
#LT
    def LT():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Leather Technology'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="#fff9fe",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()

        
#EE
    def EE():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Electronic Engineering'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="#fff9fe",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()

        #ME
    def ME():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Mechanical Engineering'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="#fff9fe",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()

#CE
    def CE():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Civil Engineering'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="#fff9fe",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()

#RT
    def RT():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Rubber Technology'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="#fff9fe",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()

#IT
    def IT():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Instrumentation Technology'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="#fff9fe",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()

#SH
    def SH():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        def search():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
            result=cur.fetchall()
            if not result:
                l1=Label(canvas1,text="student is not present",fg="red",bg="white").place(x=150,y=270)
            else:
                cur.execute("select * from 'signup' where Enroll_no='{}'".format(no.get()))
                ab=cur.fetchall()
                for row in ab:
                    if (row[1]==no.get() and row[8]=='Science and Humanities'):
                        l1=Label(canvas1,text="student is present......",fg="red",bg="white").place(x=150,y=270)
                        cur.execute("""UPDATE 'signup' SET
                                    verification='yes'
                                    WHERE verification=1
                                    """)
                        ab=cur.fetchall()
                        con.commit()
                        

        canvas4 = Canvas(root, width=w-15, height=h-50,bg="blue").place(x=0,y=0)
        img1=PhotoImage(file="background.png")
        a=Label(canvas4,image=img1).place(x=10,y=10)
        canvas1=Canvas(canvas4,width=400,height=350)
        canvas1.place(x=500,y=150)
        canvas1.create_rectangle(0,0,400,350,width=9,outline="green",fill="WHITE")
        a=Label(canvas1,text="Verification of student:",fg="brown",bg="white",font=("Georgia",18,"bold"),width=20).place(x=55,y=30)
        no=StringVar()
        l1=Label(canvas1,text="Enrollment No:",fg="blue",bg="white",font=("Georgia",16,"bold"))
        l1.place(x=30,y=120)
        Entry(canvas1,textvariable=no,width=25).place(x=220,y=125)
        btn1=Button(canvas1,text="verify",bg="#fff9fe",padx=35,pady=3,border=3,command=search).place(x=200,y=200)
        b1=Button(canvas1,text="Back",bg="#fff9fe",padx=35,pady=3,border=3,command=dept1).place(x=85,y=200)
        mainloop()

#select your department
    def dept1():
        canvas2 = Canvas(root, width=850, height=550)
        canvas2.place(x=250,y=100)

        canvas2.create_rectangle(0,0,850,550,width=5,outline="Turquoise2",fill="WHITE")
        b4=Button(canvas2,text="Back",command=TPO,bg="#fff9fe",padx=40,pady=8,border=3).place(x=50,y=460)
        l1 = Label(canvas2,text="SELECT  YOUR  DEPARTMENT:",font=("Georgia",25,"bold"),fg="brown",bg="white").place(x=150,y=30)

        b=Button(canvas2,text="Information Technology",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=IF,padx=20,pady=10).place(x=50,y=150)
        b=Button(canvas2,text="Electrical Technology",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=ET,padx=20,pady=10).place(x=330,y=150)
        b=Button(canvas2,text="Computer Engineering",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=COE,padx=20,pady=10).place(x=585,y=150)
        b=Button(canvas2,text="Leather Technology",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=LT,padx=35,pady=12).place(x=50,y=240)
        b=Button(canvas2,text="Electronic Engineering",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=EE,padx=20,pady=10).place(x=320,y=240)
        b=Button(canvas2,text="Mechanical Engineering",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=ME,padx=20,pady=12).place(x=585,y=240)
        b=Button(canvas2,text="Civil Engineering",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=CE,padx=40,pady=10).place(x=50,y=330)
        b=Button(canvas2,text="Rubber Technology",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=RT,padx=35,pady=10).place(x=320,y=330)
        b=Button(canvas2,text="Instrumentation Technology",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=IT,padx=10,pady=10).place(x=580,y=330)
        b=Button(canvas2,text="Science and humanities",font=("Constantia",12,"bold"),activebackground="turquoise2",activeforeground="black",bg="#afeeee",command=SH,padx=20,pady=10).place(x=320,y=420)

        
    root.geometry(size)
    root.resizable(0,0)
    img1=PhotoImage(file="background.png")
    canvas = Canvas(root, width=w-15,height=h-40)
    canvas.place(x=0,y=0)
    a=Label(canvas,image=img1).place(x=10,y=10)
    canvas2 = Canvas(root, width=800, height=550)
    canvas2.place(x=250,y=100)
    
    canvas2.create_rectangle(0,0,800,550,width=9,outline="black",fill="WHITE")
    
    l2=Label(canvas2,text="TPO SECTION",bg="white",fg="Brown",font=("Georgia",25,"bold"),width=20)
    l2.place(x=195,y=50)
    photo=PhotoImage(file=r"login.png")
    canvas2.create_image(410,170,image=photo)

    l2=Label(canvas2,text="Please enter User ID and Password to continue in TPO co-login:",bg="white",font=("MV Boli",13))
    l2.place(x=160,y=260)
    l2=Label(canvas2,text="Login    :",bg="white",font=("Georgia",13,"bold")).place(x=245,y=300)
    ac=StringVar()
    Entry(canvas2,textvariable=ac).place(x=360,y=300)

    l2=Label(canvas2,text="Password :",bg="white",font=("Georgia",13,"bold")).place(x=245,y=340)
    pa=StringVar()
    Entry(canvas2,textvariable=pa,show="*").place(x=360,y=340)


    b=Button(canvas2,text="Submit",font=("Times new roman",11,"bold"),padx=30,pady=3,border=3,bg="white",activebackground="#3D8FA5",activeforeground="brown",command=test).place(x=450,y=400)
    b1=Button(canvas2,text=" Back ",font=("Times new roman",11,"bold"),padx=30,pady=3,border=3,bg="white",activebackground="#3D8FA5",activeforeground="brown",command=HOME).place(x=250,y=400)



    mainloop()
    
#for showing database of verified students
#for all verified students
def showallv():
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        b1=Button(root1,text="Back").place(x=1,y=0)
        b1=Button(root1,text="Next").place(x=40,y=0)
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students if infirmation technology
def IFV():
    
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
   
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Information Technology'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students of electrical technology
def ETV():
    
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Electrical Technology'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students of computer engineering
def COEV():
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Computer Engineering'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students of leather technology
def LTV():
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Leather Technology'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students of electronics engineering
def EEV():
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Electronics Engineering'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students of computer engineering
def MEV():
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Mechanical Engineering'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students of computer engineering
def CEV():
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Civil Engineering'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students of computer engineering
def RTV():
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Rubber Technology'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students of instrumentation technology
def ITV():
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Instrumentation Technology'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for verified students of science and humanities
def SHV():
    root1 = Tk()
    root1.title("DETAILS")
    root1.geometry(size)
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)

    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup where verification='yes' and Dept_name='Science and humanities'")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for 3rd button Admin login
def Admin():
    def campus():
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        root.resizable(0,0)
        img1=PhotoImage(file="background.png")
        canvas = Canvas(root, width=w-15, height=h-40,bg="blue")
        canvas.place(x=0,y=0)
        a=Label(canvas,image=img1).place(x=10,y=10)
        def table():
            db1=connect("student_register.db")
            f=db1.cursor()
            f.execute("Create table if not exists 'campus'(C_Name text,Address text,year int,branch text,n_job text,ssc text,hsc text,iti text,diploma_holder text,location text,t_f_d int,t_f_m int,t_f_y int,t_t_d int,t_t_m int,t_t_y int,last_d int,last_m int,last_y int,ssc_per int,hsc_per int,trd_per int,cs1 text,cs1m int,cs2 text,cs2m int,cs3 text,cs3m int,cs4 text,cs4m int,cs5 text,cs5m int,details text)")
            f.execute("insert into 'campus' values('{}','{}',{},'{}','{}','{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},'{}',{},'{}',{},'{}',{},'{}',{},'{}')".format(n.get(),n1.get(),c1.get(),d1.get(),w1.get(),c2.get(),c3.get(),c4.get(),c5.get(),d2.get(),w2.get(),w3.get(),w4.get(),w5.get(),w6.get(),w7.get(),w8.get(),w9.get(),w10.get(),sc.get(),hsc.get(),trd.get(),cs1.get(),cs1m.get(),cs2.get(),cs2m.get(),cs3.get(),cs3m.get(),cs4.get(),cs4m.get(),cs5.get(),cs5m.get(),de.get()))
            db1.commit()
            db1.close()
        n=StringVar()
        n1=StringVar()
        c1=IntVar()
        d1=StringVar()
        w1=StringVar()
        c2=StringVar()
        c3=StringVar()
        c4=StringVar()
        c5=StringVar()
        d2=StringVar()
        w2=IntVar()
        w3=IntVar()
        w4=IntVar()
        w5=IntVar()
        w6=IntVar()
        w7=IntVar()
        w8=IntVar()
        w9=IntVar()
        w10=IntVar()
        sc=IntVar()
        hsc=IntVar()
        trd=IntVar()
        cs1=StringVar()
        cs1m=IntVar()
        cs2=StringVar()
        cs2m=IntVar()
        cs3=StringVar()
        cs3m=IntVar()
        cs4=StringVar()
        cs4m=IntVar()
        cs5=StringVar()
        cs5m=IntVar()
        de=StringVar()
     

        def abc():
            canvas1 = Canvas(canvas, width=800, height=700,bg="white")
            canvas1.place(x=275,y=10)
            h=Label(canvas1,text="COMPANY",font=("Dubai",25,"bold"),bg="white",fg="brown")
            h.place(x=300,y=5)
            
            l1=Label(canvas1,text="Company Name :",font=("bold",12),bg="white")
            l1.place(x=10,y=60)
            e1=Entry(canvas1,textvariable=n,width=35)
            e1.place(x=140,y=60)
            n.get()


            l2=Label(canvas1,text="Address :",font=("bold",12),bg="white")
            l2.place(x=10,y=100)
            e2=Entry(canvas1,textvariable=n1,width=35)
            e2.place(x=140,y=100)
            n1.get()


            l4=Label(canvas1,text="Placement Year :",font=("bold",12),bg="white")
            l4.place(x=10,y=140)

            r1=Radiobutton(canvas1,text="1st Year",variable=c1,value=1,font=("bold",10),bg="white")
            r1.place(x=145,y=160)

            r2=Radiobutton(canvas1,text="2nd Year",variable=c1,value=2,font=("bold",10),bg="white")
            r2.place(x=145,y=180)

            r3=Radiobutton(canvas1,text="3rd Year",variable=c1,value=3,font=("bold",10),bg="white")
            r3.place(x=145,y=200)
            c1.get()


            Label(canvas1, text="Branch :",font=("bold",12),bg="white").place(x=10,y=240)
            ch =["Information Technology","Computer Engineering","Civil Engineering",
                      "Mechanical Engineering","Electronics Engineering","Electrical Engineering"
                      ,"Rubber Technology","Leather Technology","Instrumentation Engineering",
                      "Science and Humanities"]
            o1 = OptionMenu(canvas1,d1,*ch)
            o1.place(x=140,y=240)
            d1.set("select dept:")

            Label(canvas1, text="Nature of Job :",font=("bold",12),bg="white").place(x=10,y=280)
            Entry(canvas1,textvariable=w1,width=35).place(x=140,y=280)
            w1.get()

            Label(canvas1, text="Eligibility Criteria :",font=("bold",12),bg="white").place(x=10,y=320)
            
            Checkbutton(canvas1,text="SSC",variable=c2,font=("bold",10),bg="white").place(x=140,y=340)
            c2.get()
            Checkbutton(canvas1,text="HSC",variable=c3,font=("bold",10),bg="white").place(x=140,y=360)
            c3.get()
            Checkbutton(canvas1,text="ITI",variable=c4,font=("bold",10),bg="white").place(x=140,y=380)
            c4.get()
            Checkbutton(canvas1,text="Diploma Holder Average",variable=c5,font=("bold",10),bg="white").place(x=140,y=400)
            c5.get()

            d2 = StringVar(canvas1)
            Label(canvas1, text="Location of work",font=("bold",12),bg="white").place(x=10,y=440)
            choice ={"Mumbai","Thane","Pune",
                      "Delhi","Banglore","Gujrat"
                      ,"Chennai","Madras","Ahamdabad",
                      "Surat"}
            d2.set('Mumbai') # set the default option
            o2 = OptionMenu(canvas1,d2,*choice)
            o2.place(x=150,y=440)


            Label(canvas1, text="Training Period :  From ",font=("bold",12),bg="white").place(x=10,y=480)
            s1=Spinbox(canvas1,from_=1,to=31,textvariable=w2,width=10).place(x=190,y=480)
            w2.get()
            s1=Spinbox(canvas1,from_=1,to=12,textvariable=w3,width=10).place(x=290,y=480)
            w3.get()
            s1=Spinbox(canvas1,from_=2019,to=2040,textvariable=w4,width=10).place(x=390,y=480)
            w4.get()


            Label(canvas1, text="To:",font=("bold",12),bg="white").place(x=480,y=480)
            s1=Spinbox(canvas1,from_=1,to=31,textvariable=w5,width=10).place(x=510,y=480)
            w5.get()
            s1=Spinbox(canvas1,from_=1,to=12,textvariable=w6,width=10).place(x=610,y=480)
            w6.get()
            s1=Spinbox(canvas1,from_=2019,to=2040,textvariable=w7,width=10).place(x=710,y=480)
            w7.get()

            Label(canvas1, text="Last Date of Application :",font=("bold",12),bg="white").place(x=10,y=520)
            s1=Spinbox(canvas1,from_=1,to=31,textvariable=w8,width=10).place(x=190,y=520)
            w8.get()
            s1=Spinbox(canvas1,from_=1,to=12,textvariable=w9,width=10).place(x=290,y=520)
            w9.get()
            s1=Spinbox(canvas1,from_=2019,to=2040,textvariable=w10,width=10).place(x=390,y=520)
            w10.get()
            def am():
                if n.get()=="":
                    Label1=Label(canvas1,text="Empty Field",fg="red",font=("Bold",12),bg="white")
                    Label1.place(x=400,y=60)
                else:
                    n.get()
                if n1.get()=="":
                    Label2=Label(canvas1,text="Empty Field",fg="red",font=("Bold",12),bg="white")
                    Label2.place(x=400,y=100)
                else:
                    n1.get()


                if (c1.get()==0):
                    Label3=Label(canvas1,text="Select your year",fg="red",font=("Bold",12),bg="white")
                    Label3.place(x=400,y=180)

                if w1.get()=="":
                    Label4=Label(canvas1,text="Empty Field",fg="red",font=("Bold",12),bg="white")
                    Label4.place(x=400,y=280)
                else:
                    w1.get()
                    abc1()
            b3=Button(canvas1,text="Next",command=am,bg="white").place(x=270,y=600)
            b3=Button(canvas1,text="Back",command=dept1).place(x=220,y=600)
            
        def abc1():
            root.geometry("800x700")
            canvas = Canvas(root, width=800, height=700,bg="white")
            canvas.place(x=0,y=0)
            

            Label15=Label(root,text="10th percentage:",font=("Bold",12),bg="white")
            Label15.place(x=40,y=100)
            e111=Entry(root,textvariable=sc,font=(12))
            e111.place(x=175,y=100)
            sc.get()

            Label15=Label(root,text="12th percentage(if applicable):",font=("Bold",12),bg="white")
            Label15.place(x=40,y=150)
            e111=Entry(root,textvariable=hsc,font=(12))
            e111.place(x=260,y=150)
            hsc.get()

            Label3rd=Label(root,text="3rd year percentage :",font=("Bold",12),bg="white")
            Label3rd.place(x=40,y=200)
            e113=Entry(root,textvariable=trd,font=(12))
            e113.place(x=260,y=200)
            trd.get()
            if d1.get()=="Information Technology":
                ch=["python","java","cpp","c","html",".net"]
            elif d1.get()=="Computer Engineering":
                ch=["abc","def","ghi"]
            elif  d1.get()=="Civil Engineering":
                ch=["abc","def","ghi"]
            elif d1.get()=="Mechanical Engineering":
                ch=["abc","def","ghi"]
            elif d1.get()=="Electronics Engineering":
                ch=["abc","def","ghi"]
            elif d1.get()=="Electrical Engineering":
                ch=["abc","def","ghi"]
            elif d1.get()=="Rubber Technology":
                ch=["abc","def","ghi"]
            elif d1.get()=="Leather Technology":
                ch=["abc","def","ghi"]
            elif d1.get()=="Instrumentation Engineering":
                ch=["abc","def","ghi"]
            elif d1.get()=="Science and Humanities":
                ch=["abc","def","ghi"]
            
            Labelp2=Label(root,text="Intrested Subjects:",font=("Bold",14),bg="white")
            Labelp2.place(x=40,y=260)

            Labelp3=Label(root,text="Subjects:",font=("Bold",12),bg="white")
            Labelp3.place(x=85,y=300)
            Labelp4=Label(root,text="Marks:",font=("Bold",12),bg="white")
            Labelp4.place(x=300,y=300)
            Label15=Label(root,text="1:",font=("Bold",12),bg="white")
            Label15.place(x=40,y=340) 
            o=OptionMenu(root,cs1,*ch)
            o.config(width=20)
            cs1.set("Select skills:")
            o.place(x=60,y=340)
            e12m=Entry(root,textvariable=cs1m,font=(12))
            e12m.place(x=250,y=340)
            cs1m.get() 
            Label16=Label(root,text="2:",font=("Bold",12),bg="white")
            Label16.place(x=40,y=380)
            o=OptionMenu(root,cs2,*ch)
            o.config(width=20)
            cs2.set("Select skills:")
            o.place(x=60,y=380)
            e13m=Entry(root,textvariable=cs2m,font=(12))
            e13m.place(x=250,y=380)
            cs2m.get()
            
            Label17=Label(root,text="3:",font=("Bold",12),bg="white")
            Label17.place(x=40,y=420)
            o=OptionMenu(root,cs3,*ch)
            o.config(width=20)
            cs3.set("Select skills:")
            o.place(x=60,y=420)
            cs3.get()
            e14m=Entry(root,textvariable=cs3m,font=(12))
            e14m.place(x=250,y=420)
            cs3m.get()
            
            Label18=Label(root,text="4:",font=("Bold",12),bg="white")
            Label18.place(x=40,y=460)
            o=OptionMenu(root,cs4,*ch)
            o.config(width=20)
            cs4.set("Select skills:")
            o.place(x=60,y=460)
            cs4.get()
            e15m=Entry(root,textvariable=cs4m,font=(12))
            e15m.place(x=250,y=460)
            cs4m.get()
            
            Label19=Label(root,text="5:",font=("Bold",12),bg="white")
            Label19.place(x=40,y=500)
            o=OptionMenu(root,cs5,*ch)
            o.config(width=20)
            cs5.set("Select skills:")
            o.place(x=60,y=500)
            cs5.get()
            e16m=Entry(root,textvariable=cs5m,font=(12))
            e16m.place(x=250,y=500)
            cs5m.get()
            
            Label20=Label(root,text="Details:",font=("Bold",12),bg="white")
            Label20.place(x=40,y=540)
            e17=Entry(root,textvariable=de,width=100,bd=5,font=(12))
            e17.place(x=160,y=540)

            b3=Button(root,text="Submit",command=table).place(x=200,y=580)
            b3=Button(root,text="Back",command=abc).place(x=300,y=580)
        abc()
        mainloop()
        
    def check():
        global a,d,r,rec
        a=connect('student_register.db')
        d=a.cursor()
        d.execute("select Login from adminlogin where Login='{}'".format(ac.get()))
        r=d.fetchall()
        if not r:
            Label(canvas2,text="User id is Not Present",bg="white",fg="red",font=("Arial Rounded MT Bold",12),width=30).place(x=400,y=300)
        else:
            d.execute("select * from adminlogin where Login='{}'".format(ac.get()))
            rec=d.fetchall()
            for row in rec:
                a=str(pa.get())
                if(row[1]==a and row[0]==ac.get()):
                    dept1()
                else:
                    Label(canvas2,text="Wrong Password!!!!",bg="white",fg="red",font=("Arial Rounded MT Bold",12),width=30).place(x=400,y=340) 
    def test():
        global c
        a=pa.get()
        c=len(str(a))
        if(c<=5 and c>=0):
            Label(canvas2,text="Password :",bg="white",font=("Georgia",13,"bold")).place(x=245,y=340)
            check()
        else:
            Label(canvas2,text="Wrong password:",font= ("bold",13),fg="red2").place(x=400,y=340)
    def dept1():
        w=root.winfo_screenwidth()
        h=root.winfo_screenheight()
        size=str(w)+'x'+str(h)
        root.geometry(size)
        root.title("Government polytechnic mumbai")
        
        canvas = Canvas(root,width=w-15, height=h-14)
        canvas.place(x=0,y=0)
        #canvas.create_rectangle(0,0,1350,700,width=5,outline="Black",fill="WHITE")

        img1=PhotoImage(file=r"background5.png")
        aa=Label(canvas,image=img1).place(x=10,y=10)

        canvas1 = Canvas(canvas,width=1100,height=550,bg="white")
        canvas1.place(x=120,y=100)
        

        l1 = Button(canvas1,text="ADMIN SECTION",font=("Times new roman",28,"bold"),fg="black",bg="white").place(x=370,y=10)
        canvas1.create_line(10,85,1100,85,width=2)
        

        photo=PhotoImage(file=r"addcamp.PNG")
        canvas1.create_image(150,250,image=photo)
        b=Button(canvas1,text="Add Campus Details",command=campus,font=("Georgia",13,"bold"),bg="white",fg="black",padx=40,pady=4).place(x=10,y=400)


        photo1=PhotoImage(file=r"Slogo.PNG")
        canvas1.create_image(425,250,image=photo1) 
        b=Button(canvas1,text="TPO Ragisteration",command=register_tpo,font=("Georgia",13,"bold"),bg="white",fg="black",padx=40,pady=4).place(x=300,y=400)


        photo2=PhotoImage(file=r"deptlist.PNG")
        canvas1.create_image(700,250,image=photo2) 
        b=Button(canvas1,text="Department List",font=("Georgia",13,"bold"),bg="white",fg="black",padx=40,pady=4,command=alldep).place(x=580,y=400)


        photo3=PhotoImage(file=r"RR.PNG")
        canvas1.create_image(925,250,image=photo3) 
        b=Button(canvas1,text="All Student",command=showall,font=("Georgia",13,"bold"),bg="white",fg="black",padx=40,pady=4).place(x=850,y=400)

        b=Button(canvas1,text="Back",command=HOME,font=("Georgia",13,"bold"),bg="white",fg="black",padx=40,pady=4).place(x=500,y=500)

        mainloop()


    def alldep():
        canvas2 = Canvas(root,width=w-15, height=h-40)
        canvas2.place(x=0,y=0)
        canvas2.create_rectangle(0,0,1350,700,width=5,outline="Black")
        

        l1 = Button(canvas2,text="SELECT YOUR DEPARTMENT",font=("Georgia",25,"bold"),bg="white",fg="Dark Blue").place(x=400,y=10)
        canvas2.create_line(0,90,1350,90,width=2)



        canvas3 = Canvas(root,width=50, height=50)
        canvas3.place(x=42,y=120)
        b=Button(canvas2,text="        Information Technology",font=("Georgia",17,"bold"),command=IFV,height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=40,y=120)

        #photo123=PhotoImage(file=r"Logo.PNG")
        #canvas3.create_image(1,1,image=photo123) 

        canvas4 = Canvas(root,width=50, height=50)
        canvas4.place(x=42,y=240)
        
        b=Button(canvas2,text="        Computer Engineering",command=COEV,font=("Georgia",17,"bold"),height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=40,y=240)

        canvas5 = Canvas(root,width=50, height=50)
        canvas5.place(x=42,y=360)
        b=Button(canvas2,text="        Leather Technology",command=LTV,font=("Georgia",17,"bold"),height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=40,y=360)

        canvas6 = Canvas(root,width=50, height=50)
        canvas6.place(x=502,y=120)
        b=Button(canvas2,text="        Electronic Engineering",command=EEV,font=("Georgia",17,"bold"),height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=500,y=120)

        canvas7 = Canvas(root,width=50, height=50)
        canvas7.place(x=502,y=240)
        b=Button(canvas2,text="        Mechanical Engineering",command=MEV,font=("Georgia",17,"bold"),height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=500,y=240)

        canvas8 = Canvas(root,width=50, height=50)
        canvas8.place(x=502,y=360)
        b=Button(canvas2,text="        Civil Engineering",command=CEV,font=("Georgia",17,"bold"),height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=500,y=360)


        canvas9 = Canvas(root,width=50, height=50)
        canvas9.place(x=502,y=480)
        b=Button(canvas2,text="        Rubber Technology",command=RTV,font=("Georgia",17,"bold"),height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=500,y=480)

        canvas10 = Canvas(root,width=50, height=50)
        canvas10.place(x=942,y=120)
        b=Button(canvas2,text="        Instrument Technology",command=ITV,font=("Georgia",17,"bold"),height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=940,y=120)

        canvas11 = Canvas(root,width=50, height=50)
        canvas11.place(x=942,y=240)
        b=Button(canvas2,text="        Science and Huminities",command=SHV,font=("Georgia",17,"bold"),height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=940,y=240)

        canvas12 = Canvas(root,width=50, height=50)
        canvas12.place(x=942,y=360)
        b=Button(canvas2,text="        Electrical Engineering",command=EEV,font=("Georgia",17,"bold"),height=1,width=17,activebackground="#3D8FA5",activeforeground="brown",bg="white",padx=40,pady=4,border=3).place(x=940,y=360)

        b11=Button(canvas2,text="Show Verified",command=showallv,font=("Georgia",13,"bold"),bg="white",fg="black",height=1,width=10,padx=40,pady=4,border=3).place(x=800,y=580)
        b12=Button(canvas2,text="Back",font=("Georgia",13,"bold"),activebackground="#3D8FA5",height=1,width=10,activeforeground="brown",bg="white",padx=40,pady=4,border=3,command=dept1).place(x=350,y=580)

   

    def register_tpo():
        def table():
            dbt=connect("student_register.db")
            ft=dbt.cursor()
            ft.execute("Create table if not exists 'logindata'(login text,password text)")
            ft.execute("insert into 'logindata' values('{}','{}')".format(ac.get(),pa.get()))
            dbt.commit()
            dbt.close()
        ac=StringVar()
        pa1=StringVar()
        pa=StringVar()

        root.geometry(size)
    
        img1=PhotoImage(file="background.png")
        canvas = Canvas(root, width=1350, height=700)
        canvas.place(x=0,y=0)
        a=Label(canvas,image=img1).place(x=10,y=10)
        canvas2 = Canvas(canvas,width=800, height=550)
        canvas2.place(x=300,y=100)
        
        canvas2.create_rectangle(0,0,800,550,width=9,outline="black",fill="WHITE")
        
        
        l2=Label(canvas2,text="Registering New TPO",bg="white",fg="brown",font=("Georgia",25,"bold"),width=20)
        l2.place(x=195,y=50)
        

        l2=Label(canvas2,text="Username   :",bg="white",font= ("Georgia",13,"bold"))
        l2.place(x=235,y=300)
        Entry(canvas2,textvariable=ac).place(x=430,y=300)
        ac.get()

        l2=Label(canvas2,text="Password :",bg="white",font=("Georgia",13,"bold"))
        l2.place(x=235,y=340)
        Entry(canvas2,textvariable=pa1,show="*").place(x=430,y=340)
        pa1.get()
            

        l2=Label(canvas2,text="Re-enter Password :",bg="white",font=("Georgia",13,"bold"))
        l2.place(x=235,y=380)
        Entry(canvas2,textvariable=pa,show="*").place(x=430,y=380)
        pa.get()
        def check():
            if pa1.get()=="" or pa1.get()!=pa.get(): 
                l2=Label(canvas2,text="Re enter the password",bg="white",fg="red",font=("Arial Rounded MT Bold",12),width=20)
                l2.place(x=500,y=340)         
            else: 
                pa.get()
                table()          

        b=Button(canvas2,text="Submit",font=("Times new roman",11,"bold"),padx=30,pady=3,border=3,bg="white",activebackground="#3D8FA5",activeforeground="brown",command=check).place(x=450,y=440)
        b1=Button(canvas2,text=" Back ",font=("Times new roman",11,"bold"),padx=30,pady=3,border=3,bg="white",activebackground="#3D8FA5",activeforeground="brown",command=dept1).place(x=250,y=440)
        mainloop()
        
    root.geometry("1350x700")
    root.resizable(0,0)
    img1=PhotoImage(file="background.png")
    canvas = Canvas(root, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    a=Label(canvas,image=img1).place(x=10,y=10)
    canvas2 = Canvas(root, width=800, height=550)
    canvas2.place(x=300,y=100)
    
    canvas2.create_rectangle(0,0,800,550,width=9,outline="black",fill="WHITE")
    
    l2=Label(canvas2,text="ADMIN SECTION",bg="white",fg="Brown",font=("Georgia",25,"bold"),width=20)
    l2.place(x=195,y=50)
    photo=PhotoImage(file=r"login.png")
    canvas2.create_image(410,170,image=photo)

    l2=Label(canvas2,text="Please enter User ID and Password to continue in Admin section:",bg="white",font=("MV Boli",13))
    l2.place(x=160,y=260)
    l2=Label(canvas2,text="Login    :",bg="white",font=("Georgia",13,"bold")).place(x=245,y=300)
    ac=StringVar()
    Entry(canvas2,textvariable=ac).place(x=360,y=300)

    l2=Label(canvas2,text="Password :",bg="white",font=("Georgia",13,"bold")).place(x=245,y=340)
    pa=StringVar()
    Entry(canvas2,textvariable=pa,show="*").place(x=360,y=340)

    b=Button(canvas2,text="Submit",font=("Times new roman",11,"bold"),padx=30,pady=3,border=3,bg="white",activebackground="#3D8FA5",activeforeground="brown",command=test).place(x=450,y=400)
    b1=Button(canvas2,text=" Back ",font=("Times new roman",11,"bold"),padx=30,pady=3,border=3,bg="white",activebackground="#3D8FA5",activeforeground="brown",command=HOME).place(x=250,y=400)


    mainloop()
#for 4th button selected students
def selected():
    def selected1():
        root1=Tk()
        root1.geometry(size)
        root1.resizable(0,0)
        root1.title()
        canvas1=Canvas(root1,width=w-15,height=h-40)
        canvas1.place(x=0,y=0)
        def table1():
            db_1=connect("student_register.db")
            f1_1=db_1.cursor()

            f1_1.execute("select Name,Enroll_no,Dept_name from 'signup' where select1='selected'")
            rows=f1_1.fetchall()
            for row in rows:
                student_table.insert("",END,values=row)
                db_1.commit()
            db_1.close()
        def show2():
            scroll_x=Scrollbar(root1,orient=HORIZONTAL)
            scroll_y=Scrollbar(root1,orient=VERTICAL)
            global student_table
            student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","Dept_name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=student_table.xview)
            scroll_y.config(command=student_table.yview)
            student_table.heading("Name",text="Name")
            student_table.heading("Enroll_no",text="Enroll_no")
            student_table.heading("Dept_name",text="Dept_name")
            student_table['show']="headings"
            student_table.column("Name",width=250)
            student_table.column("Enroll_no",width=120)
            student_table.column("Dept_name",width=150)
            student_table.pack(fill=BOTH,expand=1)
            table1()
        show2()
        

    
    def search():
        
        con=connect('student_register.db')
        cur=con.cursor()
        cur.execute("select * from 'campus' where C_Name='{}'".format(name.get()))
        re=cur.fetchall()
        if not re:
            l1=Label(canvass11,text="company is not available",fg="red",font=("Arial Rounded MT Bold",12),width=30).place(x=180,y=280)
        else:
            for i in re:
                if(i[0]==name.get()):
                    l1=Label(canvass11,text="company is available......",fg="red",font=("Arial Rounded MT Bold",12)).place(x=180,y=280)
                    db=connect("student_register.db")
                    cur=db.cursor()       
                    b=cur.execute("select s1,s2,s3,s4,s5,per_10th from signup where per_10th>65")
                    r1=b.fetchall()
                    for rows1 in r1:
                        a=cur.execute("select cs1,cs2,cs3,cs4,cs5 from campus where C_Name='{}'".format(name.get()))
                        r=a.fetchone()
                        print(r)
                        print(rows1)

                        res=[ele1 for ele1 in rows1
                             for ele2 in r if ele1==ele2]
                        print("output:"+str(res))
                        length=len(res)
                        print("count",length)

                        if length>=3:
                            cc=cur.execute("""UPDATE 'signup' SET select1="selected" WHERE select1=0 and per_10th>65 """)
                            db.commit()
                            selected1()                                                
    root.title("gpm")
    root.geometry(size)
    img1=PhotoImage(file="background5.png")
    canvasss1 = Canvas(root, width=w-15, height=h-50,bg="white")
    canvasss1.place(x=0,y=0)
    a=Label(canvasss1,image=img1).place(x=15,y=10)
    #canvasss1.create_rectangle(5,5,1350,700,width=5,outline="black")

    name=StringVar(root)

    #p11=PhotoImage(file=r"C2.PNG")
    canvass11 = Canvas(canvasss1,width=600, height=300,bg="white")
    canvass11.place(x=400,y=200)

    #pd=Label(canvass11,image=p11).place(x=0,y=0)

    l2=Label(canvass11,text="To know about the Selected student kindly enter the Company name ",bg="white",font=("MV Boli",13))
    l2.place(x=20,y=100)
    l1=Label(canvass11,text="Company Name :",bg="White",font= ("Georgia",13,"bold"))
    l1.place(x=60,y=170)
    Entry(canvass11,textvariable=name,width=50,border=3).place(x=250,y=170)
    btn=Button(canvass11,text="Back",font=("Georgia",11,"bold"),command=main,bg="white",padx=30,pady=3,border=3).place(x=150,y=230)
    btn1=Button(canvass11,text="Search",font=("Georgia",11,"bold"),command=search,bg="white",padx=30,pady=3,border=3).place(x=320,y=230)
    mainloop()


#for 5th button show all
def showall():
    root1 = Tk()
    root1.geometry(size)
    root1.title("DETAILS")
    canvas = Canvas(root1, width=w-15, height=h-40)
    canvas.place(x=0,y=0)
    def table1():
        db_1=connect("student_register.db")
        f1_1=db_1.cursor()
        f1_1.execute("select * from signup")
        rows=f1_1.fetchall()
        for row in rows:
            student_table.insert("",END,values=row)
            db_1.commit()
        db_1.close()
    def show2():
        scroll_x=Scrollbar(root1,orient=HORIZONTAL)
        scroll_y=Scrollbar(root1,orient=VERTICAL)
        global student_table
        student_table=ttk.Treeview(root1,columns=("Name","Enroll_no","dob","Gender","Mobile_no","Mobile_no_opt.","Mail","Address","Dept_name",
                                                 "Year","Per_1st","Per_2nd","Per_3rd","per_10th","pass_yr_10th","per_12th","pass_yr_12th",
                                                 "s1","s1m","s2","s2m","s3","s3m","s4","s4m","s5","s5m","Project_details","verification"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("Name",text="Name")
        student_table.heading("Enroll_no",text="Enroll_no")
        student_table.heading("dob",text="dob")
        student_table.heading("Gender",text="Gender")
        student_table.heading("Mobile_no",text="Mobile_no")
        student_table.heading("Mobile_no_opt.",text="Mobile_no_opt.")
        student_table.heading("Mail",text="Mail")
        student_table.heading("Address",text="Address")
        student_table.heading("Dept_name",text="Dept_name")
        student_table.heading("Year",text="Year")
        student_table.heading("Per_1st",text="Per_1st")
        student_table.heading("Per_2nd",text="Per_2nd")
        student_table.heading("Per_3rd",text="Per_3rd")
        student_table.heading("per_10th",text="Per_10th")
        student_table.heading("pass_yr_10th",text="pass_yr_10th")
        student_table.heading("per_12th",text="Per_12th")
        student_table.heading("pass_yr_12th",text="pass_yr_12th")
        student_table.heading("s1",text="s1")
        student_table.heading("s1m",text="s1m")
        student_table.heading("s2",text="s2")
        student_table.heading("s2m",text="s2m")
        student_table.heading("s3",text="s3")
        student_table.heading("s3m",text="s3m")
        student_table.heading("s4",text="s4")
        student_table.heading("s4m",text="s4m")
        student_table.heading("s5",text="s5")
        student_table.heading("s5m",text="s5m")
        student_table.heading("Project_details",text="Project_details")
        student_table.heading("verification",text="verification")
        student_table['show']="headings"
        student_table.column("Name",width=250)
        student_table.column("Enroll_no",width=120)
        student_table.column("dob",width=100)
        student_table.column("Gender",width=100)
        student_table.column("Mobile_no",width=150)
        student_table.column("Mobile_no_opt.",width=150)
        student_table.column("Mail",width=180)
        student_table.column("Address",width=250)
        student_table.column("Dept_name",width=150)
        student_table.column("Year",width=70)
        student_table.column("Per_1st",width=70)
        student_table.column("Per_2nd",width=70)
        student_table.column("Per_3rd",width=70)
        student_table.column("per_10th",width=100)
        student_table.column("pass_yr_10th",width=100)
        student_table.column("per_12th",width=100)
        student_table.column("pass_yr_12th",width=100)
        student_table.column("s1",width=100)
        student_table.column("s1m",width=70)
        student_table.column("s2",width=100)
        student_table.column("s2m",width=70)
        student_table.column("s3",width=100)
        student_table.column("s3m",width=70)
        student_table.column("s4",width=100)
        student_table.column("s4m",width=70)
        student_table.column("s5",width=100)
        student_table.column("s5m",width=70)
        student_table.column("Project_details",width=250)
        student_table.column("verification",width=70)
        student_table.pack(fill=BOTH,expand=1)
        table1()
    show2()
#for 5th button company details
def company_details():
        root1 = Tk()
        root1.geometry(size)
        root1.title("COMPANY DETAILS")
        root1.geometry("1350x700")
        canvas = Canvas(root1, width=w-15, height=h-40)
        canvas.place(x=0,y=0)
        def table1():
            db_1=connect("student_register.db")
            f1_1=db_1.cursor()
            
            f1_1.execute("select C_Name,Address,branch,details from 'campus'")
            rows=f1_1.fetchall()
            for row in rows:
                student_table.insert("",END,values=row)
                db_1.commit()
            db_1.close()
        def show2():
            scroll_x=Scrollbar(root1,orient=HORIZONTAL)
            scroll_y=Scrollbar(root1,orient=VERTICAL)
            global student_table
            student_table=ttk.Treeview(root1,columns=("C_Name","Address","branch","details"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=student_table.xview)
            scroll_y.config(command=student_table.yview)
            student_table.heading("C_Name",text="C_Name")
            student_table.heading("Address",text="Address")
            student_table.heading("branch",text="branch")
            student_table.heading("details",text="details")
            student_table['show']="headings"
            student_table.column("C_Name",width=250)
            student_table.column("Address",width=120)
            student_table.column("branch",width=150)
            student_table.column("details",width=150)
            student_table.pack(fill=BOTH,expand=1)
            table1()
        show2()
#for 6th button log in as a student
def login_student():
    
    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()
    size=str(w)+'x'+str(h)
    root.geometry(size)
    root.title("Government polytechnic mumbai")
    img1=PhotoImage(file="background.png")
    canvas = Canvas(root, width=1350, height=800,bg="blue")
    canvas.place(x=0,y=0)
    a=Label(canvas,image=img1).place(x=10,y=10)
    n1=StringVar()
    dob=StringVar()
    g=StringVar()
    mob=IntVar()
    mob1=IntVar()
    mail=StringVar()
    add=StringVar()
    dep=StringVar()
    yr=IntVar()
    fy=IntVar()
    sy=IntVar()
    ty=IntVar()
    sc=IntVar()
    scy=IntVar()
    hsc=IntVar()
    hscy=IntVar()
    s1=StringVar()
    s1m=IntVar()
    s2=StringVar()
    s2m=IntVar()
    s3=StringVar()
    s3m=IntVar()
    s4=StringVar()
    s4m=IntVar()
    s5=StringVar()
    s5m=IntVar()
    p=StringVar()
    pass1=StringVar()
    pass2=StringVar()
    def signup_view(en1):
        global en
        en=en1
        print("hi",en)
        root.geometry(size)
        img1=PhotoImage(file="background.png")
        canvas = Canvas(root, width=w-15, height=h-50,bg="blue")
        canvas.place(x=0,y=0)
        a=Label(canvas,image=img1).place(x=10,y=10)
        def table():       
            db=connect("student_register.db")
            f=db.cursor()
            f.execute("""Create table if not exists 'signup'(Name text,Enroll_no TEXT,dob TEXT,Gender TEXT,Mobile_no INT,
                            Mobile_no_optional INT,Mail TEXT,Address TEXT,Dept_name TEXT,Year INT,Per_1st REAL,Per_2nd REAL,
                            Per_3rd REAL,per_10th REAL,pass_yr_10th INT,per_12th REAL,pass_yr_12th INT,s1 TEXT,s1m INT,
                            s2 TEXT,s2m INT,s3 TEXT,s3m INT,s4 TEXT,s4m INT,s5 TEXT,s5m INT,Project_details TEXT,password TEXT)""")
            f.execute("insert into 'signup' values('{}','{}','{}','{}',{},{},'{}','{}','{}',{},{},{},{},{},{},{},{},'{}',{},'{}',{},'{}',{},'{}',{},'{}',{},'{}','{}')".format(n1.get(),en.get(),dob.get(),g.get(),mob.get(),mob1.get(),mail.get(),add.get(),dep.get(),yr.get(),fy.get(),sy.get(),ty.get(),sc.get(),scy.get(),hsc.get(),hscy.get(),s1.get(),s1m.get(),s2.get(),s2m.get(),s3.get(),s3m.get(),s4.get(),s4m.get(),s5.get(),s5m.get(),p.get(),pass1.get()))
            db.commit()
            db.close()

        def form1():
            global en1
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(en)) 
            result=cur.fetchall()
            root.geometry(size)
            canvas1 = Canvas(root, width=870, height=700,bg="white")
            canvas1.place(x=220,y=20)

            Label1=Label(canvas1,text="Student Registration Form",fg="brown",bg="white",font=("Georgia",20,"bold"),width=30)
            Label1.place(x=140,y=30)

           
            Label2=Label(canvas1,text="Name:",bg="white",font=("Bold",12))
            Label2.place(x=40,y=100)


           
            e2=Entry(canvas1,textvariable=n1,width=60,font=(12))
            e2.insert(0,result[0][0])
            e2.place(x=130,y=100)
       


            Label3=Label(canvas1,text="Enrollment No:",bg="white",font=("Bold",12))
            Label3.place(x=40,y=140)
            e2=Entry(canvas1,textvariable=en,font=(12))
            e2.insert(0,result[0][1])
            e2.place(x=150,y=140)
            

            Labelp=Label(canvas1,text="Personal Details:",bg="white",font=("Bold",16))
            Labelp.place(x=40,y=180)

            Label4=Label(canvas1,text="DOB:",bg="white",font=("Bold",12))
            Label4.place(x=40,y=220)
            e3=Entry(canvas1,textvariable=dob,font=(12),width=14)
            e3.insert(0,result[0][2])
            e3.place(x=100,y=220)


            Label4=Label(canvas1,text="Gender:",bg="white",font=("Bold",12))
            Label4.place(x=40,y=260)

            r1=Radiobutton(canvas1,text="Male",value='Male',variable=g,font=(12),bg="white")
            r1.place(x=120,y=260)
            r2=Radiobutton(canvas1,text="Female",value='Female',variable=g,bg="white",font=(12))
            r2.place(x=200,y=260)
            if result[0][3]=="male":
                r1.select()
            else:
                r2.select()
            
           

            Label7=Label(canvas1,text="Mobile Number:",bg="white",font=("Bold",12))
            Label7.place(x=40,y=300)
            e4=Entry(canvas1,textvariable=mob,font=(12))
            e4.insert(0,result[0][4])
            e4.place(x=165,y=300)
         
           
            Label71=Label(canvas1,text="Alternate Mobile No:",bg="white",font=("Bold",12))
            Label71.place(x=335,y=300)
            e41=Entry(canvas1,textvariable=mob1,font=(12))
            e41.insert(0,result[0][5])
            e41.place(x=490,y=300)
           

            Label8=Label(canvas1,text="Email ID:",bg="white",font=("Bold",12))
            Label8.place(x=40,y=340)
            e5=Entry(canvas1,textvariable=mail,width=60,font=(12))
            e5.insert(0,result[0][6])
            e5.place(x=125,y=340)
           
           
            Label9=Label(canvas1,text="Address:",bg="white",font=("Bold",12))
            Label9.place(x=40,y=380)
            e6=Entry(canvas1,textvariable=add,font=(12))
            e6.insert(0,result[0][7])
            
            e6.place(x=125,y=380)

            Labelp1=Label(canvas1,text="Educational Details:",bg="white",font=("Bold",16))
            Labelp1.place(x=40,y=430)
           
            Label5=Label(canvas1,text="Department Name:",bg="white",font=("Bold",12))
            Label5.place(x=40,y=470)
            l1=["Information Technology","Computer Engineering","Civil Engineering","Mechanical Engineering","Electronics Engineering","Electrical Engineering","Rubber Technology","Leather Technology","Instrumentation Engineering","Science and Humanities"]
            o=OptionMenu(canvas1,dep,*l1)
            o.config(width=20)
            dep.set("Select Dept:")
            o.place(x=180,y=470)
            dep.set(result[0][8])

            Label11=Label(canvas1,text="Passing Year:",bg="white",font=("Bold",12))
            Label11.place(x=40,y=510)
            e8=Entry(canvas1,textvariable=yr,font=(12))
            e8.insert(0,result[0][9])
            e8.place(x=160,y=510)
           

           
            Label12=Label(canvas1,text="FY percentage:",bg="white",font=("Bold",12))
            Label12.place(x=40,y=540)
            e9=Entry(canvas1,textvariable=fy,font=(12))
            e9.insert(0,result[0][10])
            e9.place(x=160,y=540)

         
            Label13=Label(canvas1,text="SY percentage:",bg="white",font=("Bold",12))
            Label13.place(x=40,y=580)
            e10=Entry(canvas1,textvariable=sy,font=(12))
            e10.insert(0,result[0][11])
            e10.place(x=160,y=580)

           
            Label14=Label(canvas1,text="TY percentage:",bg="white",font=("Bold",12))
            Label14.place(x=40,y=620)
            e11=Entry(canvas1,textvariable=ty,font=(12))
            e11.insert(0,result[0][12])
            e11.place(x=160,y=620)
            
            

               
            """def ch():
                if n1.get()=="":
                    Label2=Label(canvas1,text="Please enter the name",bg="white",fg="red",font=("Bold",12))
                    Label2.place(x=650,y=100)
                else:
                    n1.get()

                if en.get()=="" and len(en.get())!=9:
                    Label2=Label(canvas1,text="Enrollment no is empty",bg="white",fg="red",font=("Bold",12))
                    Label2.place(x=500,y=140)
                else:
                    en.get()
               
                if (re.match(r'\d{1,2}-\d{1,2}-\d{4}',dob.get())):
                    dob.get()
            
                else:
                    Label4=Label(canvas1,text="enter valid date",bg="white",fg="red",font=("Bold",12))
                    Label4.place(x=500,y=220)
                if g.get()=="":
                    Label4=Label(canvas1,text="Select the gender",bg="white",fg="red",font=("Bold",12))
                    Label4.place(x=500,y=260)
                else:
                    g.get()
               
                mobb=str(mob.get())
                   
                   
                if (re.match(r'0\d7|8|9\d{9}',mobb)):
                    mob.get()
           
                else:
                    Label7=Label(canvas1,text="Mobile no is wrong",bg="white",fg="red",font=("Bold",12))
                    Label7.place(x=600,y=300)

                mobb1=str(mob1.get())
                if (re.match(r'\d7|8|9\d{9}',mobb1)):
                    mob1.get()
                else:
                    Label7=Label(canvas1,text="Mobile no is wrong",bg="white",fg="red",font=("Bold",12))
                    Label7.place(x=600,y=300)
                if (re.match(r'\w+[.-]?\w+[@]\w+[.]\w+',mail.get())):
                    mail.get()
           
                else:
                    Label8=Label(canvas1,text="Mail id is wrong",bg="white",fg="red",font=("Bold",12))
                    Label8.place(x=650,y=340)
                if add.get()=="":
                    Label9=Label(canvas1,text="Address field is empty",bg="white",fg="red",font=("Bold",12))
                    Label9.place(x=500,y=380)
                else:
                    add.get()

                if yr.get()<2010 or yr.get()>2017:
                    Label15=Label(canvas1,text="Enter valid year",bg="white",fg="red",font=("Bold",12))
                    Label15.place(x=500,y=510)
                else:
                    yr.get()
               
               
                if fy.get()<10 or fy.get()>99:
                    Label12=Label(canvas1,text="Enter valid percentage",bg="white",fg="red",font=("Bold",12))
                    Label12.place(x=500,y=540)
                else:
                    fy.get()
               
                   
                if sy.get()<10 or sy.get()>99:
                    Label12=Label(canvas1,text="Enter valid percentage",bg="white",fg="red",font=("Bold",12))
                    Label12.place(x=500,y=580)
                else:
                    sy.get()
           

                if ty.get()<10 or ty.get()>99:
                    Label12=Label(canvas1,text="Enter valid percentage",bg="white",fg="red",font=("Bold",12))
                    Label12.place(x=500,y=620)
                else:
                    ty.get()
                    form2()
               
                sy1=str(sy.get())
                if (re.match(r'\d\d\.\d\d',sy1)):
                    sy.get()
                    form2()
                else:
                    Label12=Label(canvas1,text="enter valid percentage",fg="red",font=("Bold",12))
                    Label12.place(x=500,y=580)

                ty1=str(ty.get())
                if (re.match(r'\d\d.\d\d',ty1)):
                    ty.get()
                    form2()
                else:
                    Label12=Label(canvas1,text="Enter valid percentage",fg="red",font=("Bold",12))
                    Label12.place(x=500,y=620)"""
            b=Button(canvas1,text="Next",command=form2,bg="white",padx=40,pady=4,border=3).place(x=160,y=650)
        def form2():
            con=connect('student_register.db')
            cur=con.cursor()
            cur.execute("select * from 'signup' where Enroll_no='{}'".format(en))
            result=cur.fetchall()
            root.geometry(size)

       
            canvas2 = Canvas(root, width=870, height=750,bg="white")
            canvas2.place(x=220,y=20)
       
           
            Label15=Label(canvas2,text="10th percentage:",bg="white",font=("Bold",12))
            Label15.place(x=40,y=100)
            e111=Entry(canvas2,textvariable=sc,font=(12))
            e111.insert(0,result[0][13])
            e111.place(x=175,y=100)
           
            Label15=Label(canvas2,text="10th passing year:",bg="white",font=("Bold",12))
            Label15.place(x=40,y=140)
            e111=Entry(canvas2,textvariable=scy,font=(12))
            e111.insert(0,result[0][14])
            e111.place(x=185,y=140)

            Label15=Label(canvas2,text="12th percentage(if applicable):",bg="white",font=("Bold",12))
            Label15.place(x=40,y=180)
            e111=Entry(canvas2,textvariable=hsc,font=(12))
            e111.insert(0,str(result[0][15]))
            e111.place(x=260,y=180)
           
            Label15=Label(canvas2,text="12th passing year(if applicable):",bg="white",font=("Bold",12))
            Label15.place(x=40,y=220)
            e111=Entry(canvas2,textvariable=hscy,font=(12))
            e111.insert(0,str(result[0][16]))
            e111.place(x=270,y=220)

            if  dep.get()=="Information Technology":
                l1=["python","java","cpp","c","html",".net"]
            elif dep.get()=="Computer Engineering":
                l1=["abc","def","ghi"]
            elif  dep.get()=="Civil Engineering":
                l1=[]
            elif dep.get()=="Mechanical Engineering":
                l1=[]
            elif dep.get()=="Electronics Engineering":
                l1=[]
            elif dep.get()=="Electrical Engineering":
                l1=[]
            elif dep.get()=="Rubber Technology":
                l1=[]
            elif dep.get()=="Leather Technology":
                l1=[]
            elif dep.get()=="Instrumentation Engineering":
                l1=[]
            elif dep.get()=="Science and Humanities":
                l1=[]
               
            Labelp2=Label(canvas2,text="Intrested subjects:",bg="white",font=("Bold",16))
            Labelp2.place(x=40,y=260)

            Labelp3=Label(canvas2,text="Subjects:",bg="white",font=("Bold",12))
            Labelp3.place(x=85,y=300)
            Labelp4=Label(canvas2,text="Marks",bg="white",font=("Bold",12))
            Labelp4.place(x=300,y=300)
           
            Label15=Label(canvas2,text="1:",bg="white",font=("Bold",12))
            Label15.place(x=40,y=340)
            o=OptionMenu(canvas2,s1,*l1)
            o.config(width=20)
            s1.set("Select skills:")
            o.place(x=60,y=340)
            e12m=Entry(canvas2,textvariable=s1m,font=(12))
            e12m.place(x=250,y=340)
            e12m.insert(0,result[0][18])
            s1m.get()
           
            Label16=Label(canvas2,text="2:",bg="white",font=("Bold",12))
            Label16.place(x=40,y=380)
            o=OptionMenu(canvas2,s2,*l1)
            o.config(width=20)
            s1.set("Select skills:")
            o.place(x=60,y=380)
            e13m=Entry(canvas2,textvariable=s2m,font=(12))
            e13m.place(x=250,y=380)
            e13m.insert(0,result[0][20])
            s2m.get()
           
            Label17=Label(canvas2,text="3:",bg="white",font=("Bold",12))
            Label17.place(x=40,y=420)
            o=OptionMenu(canvas2,s3,*l1)
            o.config(width=20)
            s1.set("Select skills:")
            o.place(x=60,y=420)
            s3.get()
            e14m=Entry(canvas2,textvariable=s3m,font=(12))
            e14m.place(x=250,y=420)
            e14m.insert(0,result[0][22])
            s3m.get()
           
            Label18=Label(canvas2,text="4:",bg="white",font=("Bold",12))
            Label18.place(x=40,y=460)
            o=OptionMenu(canvas2,s4,*l1)
            o.config(width=20)
            s1.set("Select skills:")
            o.place(x=60,y=460)
            s4.get()
            e15m=Entry(canvas2,textvariable=s4m,font=(12))
            e15m.place(x=250,y=460)
            e15m.insert(0,result[0][24])
            s4m.get()
           
            Label19=Label(canvas2,text="5:",bg="white",font=("Bold",12))
            Label19.place(x=40,y=500)
            o=OptionMenu(canvas2,s5,*l1)
            o.config(width=20)
            s1.set("Select skills:")
            o.place(x=60,y=500)
            s5.get()
            e16m=Entry(canvas2,textvariable=s5m,font=(12))
            e16m.place(x=250,y=500)
            e16m.insert(0,result[0][26])
            s5m.get()
           
            Label20=Label(canvas2,text="Projects",bg="white",font=("Bold",12))
            Label20.place(x=40,y=540)
            e17=Entry(canvas2,textvariable=p,font=(12),width=90)
            e17.insert(0,result[0][27])
            e17.place(x=160,y=540)

            Label20=Label(canvas2,text="Password:",bg="white",font=("Bold",12))
            Label20.place(x=40,y=580)
            e17=Entry(canvas2,textvariable=pass1,font=(12))
            e17.place(x=180,y=580)

            Label20=Label(canvas2,text="confrim Password:",bg="white",font=("Bold",12))
            Label20.place(x=40,y=620)
            e17=Entry(canvas2,textvariable=pass2,font=(12))
            e17.place(x=180,y=620)
          
            def table2():
                sc1=str(sc.get())
                if (re.match(r'/d/d./d/d',sc1)):
                    sc.get()
                    form2()
                else:
                    Label12=Label(canvas2,text="enter valid percentage",fg="red",font=("Bold",12))
                    Label12.place(x=500,y=100)
                   
               
                if scy.get()<2010 or scy.get()>2017:
                    Label15=Label(canvas2,text="enter valid year",fg="red",font=("Bold",12))
                    Label15.place(x=500,y=140)
                else:
                    scy.get()
                hsc1=str(hsc.get())
                if (re.match(r'/d/d./d/d',hsc1)):
                    hsc.get()
                    form2()
                else:
                    Label12=Label(canvas2,text="enter valid percentage",fg="red",font=("Bold",12))
                    Label12.place(x=500,y=180)
                   
               
                if hscy.get()<2010 or hscy.get()>2017:
                    Label15=Label(canvas2,text="enter valid year",fg="red",font=("Bold",12))
                    Label15.place(x=500,y=220)
                else:
                    hscy.get()
                if s1.get() or s2.get()=="":
                     Label15=Label(canvas2,text="minimum 2 subjects with marks are required.",fg="red",font=("Bold",12))
                     Label15.place(x=500,y=340)
                else:
                    s1.get()
                    s2.get()
                if s2m.get()<35 or s2m.get()>100 or s1m.get()<35 or s1m.get()>100:
                     Label15=Label(canvas2,text="marks are out of range.",fg="red",font=("Bold",12))
                     Label15.place(x=500,y=380)
                else:
                    s1m.get()
                    s2m.get()
                   
                if p.get()=="":
                    Label2=Label(canvas2,text="fill the project details.",fg="red",font=("Bold",12))
                    Label2.place(x=500,y=540)
                else:
                    p.get()
                if pass1.get()!=pass2.get():
                    l2=Label(canvas2,text="Re enter the password",fg="red",font=("Arial Rounded MT Bold",12),width=20)
                    l2.place(x=400,y=620)         
                else: 
                    pass1.get()
                    table()

               
        form1()
        mainloop()
    def student_login():
        def check():
            global a,d,r,rec
            a=connect('student_register.db')
            d=a.cursor()
            d.execute("select Enroll_no from signup where Enroll_no='{}'".format(en.get()))
            r=d.fetchall()
            if not r:
                Label(canvas2,text="student  is Not Present",fg="red",bg="white",font=("Arial Rounded MT Bold",12),width=30).place(x=500,y=300)
            else:
                d.execute("select * from signup where Enroll_no='{}'".format(en.get()))
                rec=d.fetchall()
                for row in rec:
                    a=str(p.get())
                    if(row[30]==a and row[1]==en.get()):
                        signup_view(en.get())
                    else:
                        Label(canvas2,text="Wrong Password!!!!",fg="red",font=("Arial Rounded MT Bold",12),width=30).place(x=400,y=340)
        def test():
            global c
            a=p.get()
            c=len(str(a))
            print(a,c)
            if(c>5):
                Label(canvas2,text="Password :",bg="white",font=("Georgia",13,"bold")).place(x=235,y=340)
                check()
            else:
                Label(canvas2,text="Wrong password:",bg="white",font= ("bold",13),fg="red2").place(x=400,y=340)
            
        root.geometry("1350x700")
        img1=PhotoImage(file="background.png")
        canvas = Canvas(root, width=1350, height=700)
        canvas.place(x=0,y=0)
        a=Label(canvas,image=img1).place(x=10,y=10)
        canvas2 = Canvas(root, width=800, height=550)
        canvas2.place(x=250,y=100)
        
        canvas2.create_rectangle(0,0,800,550,width=9,outline="black",fill="WHITE")
        
        l2=Label(canvas2,text="STUDENT LOGIN",bg="white",fg="Brown",font=("Georgia",25,"bold"),width=20)
        l2.place(x=195,y=50)
        photo=PhotoImage(file=r"login.png")
        canvas2.create_image(410,170,image=photo)

        l2=Label(canvas2,text="Please enter User ID and Password to continue in student login:",bg="white",font=("MV Boli",13))
        l2.place(x=160,y=260)
        l2=Label(canvas2,text="Login    :",bg="white",font=("Georgia",13,"bold")).place(x=245,y=300)
        en=StringVar()
        Entry(canvas2,textvariable=en).place(x=360,y=300)

        l2=Label(canvas2,text="Password :",bg="white",font=("Georgia",13,"bold")).place(x=245,y=340)
        p=StringVar()
        Entry(canvas2,textvariable=p,show="*").place(x=360,y=340)


        b=Button(canvas2,text="Submit",font=("Times new roman",11,"bold"),padx=30,pady=3,border=3,bg="white",activebackground="#3D8FA5",activeforeground="brown",command=test).place(x=450,y=400)
        b=Button(canvas2,text="Back",font=("Times new roman",11,"bold"),padx=30,pady=3,border=3,bg="white",activebackground="#3D8FA5",activeforeground="brown",command=student_section).place(x=300,y=400)
        mainloop()
    student_login()

    
main()

