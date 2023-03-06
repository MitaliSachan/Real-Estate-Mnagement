import tkinter as tk
from tkinter.ttk import*
from tkinter import scrolledtext
from tkinter import messagebox
import mysql.connector as mys
import pyttsx3
import getpass

a=mys.connect(host='localhost',user='root',passwd='mitali@2003')
cursor=a.cursor()
cursor.execute('create database if not exists real_estate')
cursor.execute('use real_estate')
cursor.execute("create table if not exists budget"
            "("
            "BUD_TYPE char(1) primary key,"
            "PRI_RANGE char(20))")
cursor.execute("create table if not exists customers"
            "("
            "cust_name char(25),"
            "phone bigint(11))")
cursor.execute("create table if not exists owners"
            "("
            "USR_PASSWD char(20) primary key,"
            "O_NAME char(30),"
            "AGE int(3),"
            "CONT bigint(11),"
            "LOC varchar(70),"
            "HOU_TYP varchar(11),"
            "FLOOR int(2) NOT NULL,"
            "LAND_TYPE varchar(15),"
            "FACING char(15),"
            "FURN varchar(15),"
            "AREA_COV varchar(17),"
            "AVAB char(15),"
            "FOR_ char(7),"
            "BUD_TYPE char(1))")

'''query0="insert into budget (BUD_TYPE, PRI_RANGE) VALUES (%s, %s)"
val=[
    ('A','ABOVE 10 CRORE'),
    ('B','5-10 CRORE'),
    ('C','1-5 CRORE'),
    ('D','75 LAKHS-1 CRORE'),
    ('E','50-75 LAKHS'),
    ('F','34-50 LAKHS'),
    ('G','20-34 LAKHS'),
    ('H','1-20 LAKHS'),
    ('I','70000-90000'),
    ('J','55000-70000'),
    ('K','30000-55000'),
    ('L','10000-30000'),
    ('M','6000-10000'),
    ('N','2000-6000')
    ]
cursor.executemany(query0, val)
a.commit()'''
if a.is_connected():
    print('yes')
    
def speak(audio):
    s.say(audio)
    s.connect(topic =audio, cb = callable)
    s.runAndWait()

def wanna_buy():
    global root
    
    root.title("PURCHASE")
    root.geometry("650x650")
    a = tk.PhotoImage(file ="C:\\Users\\hp\\OneDrive\\Desktop\\mitali\\wp5.png")
    b = Label(root, image=a)
    b.place(x=0, y=0,relwidth=1, relheight=1)
    def clearTextInput():
        z1.delete(first=0,last=100)
        z2.delete(first=0,last=100)
        z3.delete(first=0,last=100)
        z4.delete(first=0,last=100)
        z5.delete(first=0,last=100)
        combo.delete(first=0,last=100)
        combo.current(0)
        combo1.delete(first=0,last=100)
        combo1.current(0)
        combo2.delete(first=0,last=100)
        combo2.current(0)
        combo3.delete(first=0,last=100)
        combo3.current(0)
    Label(root,text=' **FILL THE DETAILS IN CAPITAL LETTERS ONLY  ',relief='raised').grid(column=1,row=0,padx=81,pady=17)
    a1=Label(root,text=" NAME : ",relief='sunken',font='Times 10 bold ')
    a1.place(x=30,y=102)
    z1=Entry(root,textvariable=nam,width=20)
    z1.place(x=177,y=102)
    a2=Label(root,text=' PHONE NO. : ',relief='sunken',font='Times 10 bold ')
    a2.place(x=30,y=138)
    z2=Entry(root,textvariable=cont,width=20)
    z2.place(x=177,y=138)
    l1=Label(root,text=" LOCATION :",relief='sunken',font='Times 10 bold ')
    l1.place(x=30,y=174)
    z3=Entry(root,textvariable=loc,width=23)
    z3.place(x=177,y=174)
    l2=Label(root,text=" HOUSE TYPE : ",relief='sunken',font='Times 10 bold ')
    l2.place(x=30,y=210)
    combo=Combobox(root,textvariable=hou_typ,font="Times 10 ")
    combo['values']=("1BHK","2BHK","3BHK","4BHK","5BHK",">5BHK")
    combo.place(x=177,y=210)
    combo.current(0)
    l3=Label(root,text=" FLOOR : ",relief='sunken',font='Times 10 bold ')
    l3.place(x=30,y=246)
    z4=Entry(root,textvariable=floor,width=20)
    z4.place(x=177,y=246)
    l4=Label(root,text=" LAND TYPE : ",relief='sunken',font='Times 10 bold ')
    l4.place(x=30,y=282)
    combo1=Combobox(root,textvariable=lan_typ,font="Times 10 ")
    combo1['values']=("RESIDENTIAL","COMMERCIAL","OTHERS")
    combo1.place(x=177,y=282)
    combo1.current(0)
    l5=Label(root,text=" FACING : ",relief='sunken',font='Times 10 bold ')
    l5.place(x=30,y=318)
    combo2=Combobox(root,textvariable=face,font="Times 10 ")
    combo2['values']=("EAST","WEST","NORTH","SOUTH","NORTH-EAST","SOUTH-EAST","NORTH-WEST","SOUTH-WEST")
    combo2.place(x=177,y=318)
    combo2.current(0)
    l6=Label(root,text=" FURNISHED : ",relief='sunken',font='Times 10 bold ')
    l6.place(x=30,y=354)
    combo3=Combobox(root,textvariable=furn,font="Times 10 ")
    combo3['values']=("FURNISHED","SEMI-FURNISHED","UNFURNISHED")
    combo3.place(x=177,y=354)
    combo3.current(0)
    l7=Label(root,text=" BUDGET TYPE : ",relief='sunken',font='Times 10 bold ')
    l7.place(x=30,y=390)
    z5=Entry(root,textvariable=bud,width=17)
    z5.place(x=177,y=390)
    Button(root,text='QUIT',command= quit ).place(x=40,y=476)
    Button(root,text='  VIEW RESULT  ',command= viewresult1 ).place(x=314,y=476)
    Button(root,text='BACK',command= back ).place(x=177,y=476)
    Button(root,text='CLEAR',command=clearTextInput).place(x=451,y=476)
    X=scrolledtext.ScrolledText(root,wrap=tk.WORD,width=18,height=11,font=('Times New Roman',12))
    X.place(x=399,y=102)
    X.insert(tk.INSERT,
             """\
BUDGET
TYPE  ~  PRICE        |
-----------------------
A    ->  ABOVE 10 Cr 
B    ->  5-10 Cr
C    ->  1-5 Cr      
D    ->  75 L - 1 Cr 
E    ->  50-75 L     
F    ->  34-50 L
G    ->  20-34 L
H    ->  1-20 L      
I    ->  90000-70000
J    ->  70000-55000 
K    ->  55000-30000
L    ->  30000-10000 
M    ->  10000-6000  
N    ->  6000-2000   
------------------------""")
    X.configure(state='disabled')
    speak('for better response fill your details in capital letters only')
    
    root.mainloop()
    
def wanna_sell():
    global root
    speak('for better response fill your details in capital letters only')
    root.title("SELL")
    root.geometry("650x650")
    tabcontrol1=Notebook(root)
    tab1=tk.Frame(tabcontrol1,relief='sunken',bg='olive')
    tabcontrol1.add(tab1,text='NEW PROFILE')
    tab2=tk.Frame(tabcontrol1,relief='sunken',bg='olive')
    tabcontrol1.add(tab2,text='UPDATE PROFILE')
    tabcontrol1.grid(column=0,row=0,ipadx=600,ipady=550,sticky='S')
    Label(tab2,text=' **FILL THE DETAILS IN CAPITAL LETTERS ONLY  ',relief='raised').grid(column=1,row=0,padx=81,pady=17)
    Label(tab2,text=' *YOU CAN ONLY UPDATE YOUR CONTACT NO. AND AVAILABILITY*  ',relief='raised').grid(column=1,row=1,padx=81)
    def clearTextInput():
        
        y1.delete(first=0,last=100)
        z0.delete(first=0,last=100)
        z1.delete(first=0,last=100)
        z2.delete(first=0,last=100)
        z3.delete(first=0,last=100)
        z4.delete(first=0,last=100)
        z5.delete(first=0,last=100)
        z6.delete(first=0,last=100)
        z7.delete(first=0,last=100)
        comb.delete(first=0,last=100)
        comb.current(0)
        combo.delete(first=0,last=100)
        combo.current(0)
        combo1.delete(first=0,last=100)
        combo1.current(0)
        combo2.delete(first=0,last=100)
        combo2.current(0)
        combo3.delete(first=0,last=100)
        combo3.current(0)
        combo4.delete(first=0,last=100)
        combo4.current(0)
    def check() :
        if num.get() == 1 :
            z0.configure(show = "")
            y1.configure(show="")
        elif num.get() == 0 :
            z0.configure(show = "*")
            y1.configure(show="*")    
    a0=Label(tab2,text="USER PASSWD:",relief='sunken',font='Times 10 bold ')
    a0.place(x=80,y=120)
    z0=Entry(tab2,textvariable=idd,width=20,show='*')
    z0.place(x=240,y=120)
    button1 = Checkbutton(tab2,command=check,onvalue=1,offvalue=0,variable=num)
    button1.place(x =390, y = 120)
    a1=Label(tab2,text=" NAME : ",relief='sunken',font='Times 10 bold ')
    a1.place(x=80,y=176)
    z1=Entry(tab2,textvariable=nam,width=20)
    z1.place(x=240,y=176)
    a2=Label(tab2,text=' PHONE NO. : ',relief='sunken',font='Times 10 bold ')
    a2.place(x=80,y=232)
    z2=Entry(tab2,textvariable=cont,width=20)
    z2.place(x=240,y=232)
    a3=Label(tab2,text=' AVAILABILITY : ',relief='sunken',font='Times 10 bold ')
    a3.place(x=80,y=288)
    comb=Combobox(tab2,width=14,textvariable=ava,font="Times 10 ")
    comb['values']=("AVAILABLE","OCCUPIED")
    comb.place(x=240,y=288)
    comb.current(0)
    tk.Button(tab2,text='  QUIT!  ',command= quit,fg='maroon',width=12 ,borderwidth=5,highlightthickness=5,font=' bold').place(x=111,y=396)
    tk.Button(tab2,text='  UPDATE   ',command= update,fg='blue',width=12 ,borderwidth=5,highlightthickness=5,font=' bold').place(x=430,y=396)
    tk.Button(tab2,text='   DELETE   ',command= delete ,fg='red',width=12 ,borderwidth=5,highlightthickness=5,font=' bold').place(x=156,y=508)
    tk.Button(tab2,text='   CLEAR    ',command=clearTextInput,fg='green',width=12,borderwidth=5,highlightthickness=5,font=' bold ').place(x=372,y=508)

    Label(tab1,text=' **FILL THE DETAILS IN CAPITAL LETTERS ONLY  ',relief='raised').grid(column=1,row=0,padx=121,pady=17)
    b0=Label(tab1,text=" USER PASSWD : ",relief='sunken',font='Times 10 bold ')
    b0.place(x=30,y=390)
    y1=Entry(tab1,textvariable=idd,width=20,show='*')
    y1.place(x=177,y=390)
    button = Checkbutton(tab1,command=check,onvalue=1,offvalue=0,variable=num)
    button.place(x =315, y = 390)
    a1=Label(tab1,text=" NAME : ",relief='sunken',font='Times 10 bold ')
    a1.place(x=30,y=66)
    z1=Entry(tab1,textvariable=nam,width=20)
    z1.place(x=177,y=66)
    a2=Label(tab1,text=' PHONE NO. : ',relief='sunken',font='Times 10 bold ')
    a2.place(x=30,y=102)
    z2=Entry(tab1,textvariable=cont,width=20)
    z2.place(x=177,y=102)
    l1=Label(tab1,text=" LOCATION :",relief='sunken',font='Times 10 bold ')
    l1.place(x=30,y=138)
    z3=Entry(tab1,textvariable=loc,width=23)
    z3.place(x=177,y=138)
    l2=Label(tab1,text=" HOUSE TYPE : ",relief='sunken',font='Times 10 bold ')
    l2.place(x=30,y=174)
    combo=Combobox(tab1,textvariable=hou_typ,font="Times 10 ")
    combo['values']=("1BHK","2BHK","3BHK","4BHK","5BHK",">5BHK")
    combo.place(x=177,y=174)
    combo.current(0)
    l3=Label(tab1,text=" FLOOR : ",relief='sunken',font='Times 10 bold ')
    l3.place(x=30,y=210)
    z4=Entry(tab1,textvariable=floor,width=20)
    z4.place(x=177,y=210)
    l4=Label(tab1,text=" LAND TYPE : ",relief='sunken',font='Times 10 bold ')
    l4.place(x=30,y=246)
    combo1=Combobox(tab1,textvariable=lan_typ,font="Times 10 ")
    combo1['values']=("RESIDENTIAL","COMMERCIAL","OTHERS")
    combo1.place(x=177,y=246)
    combo1.current(0)
    l5=Label(tab1,text=" FACING : ",relief='sunken',font='Times 10 bold ')
    l5.place(x=30,y=282)
    combo2=Combobox(tab1,textvariable=face,font="Times 10 ")
    combo2['values']=("EAST","WEST","NORTH","SOUTH","NORTH-EAST","SOUTH-EAST","NORTH-WEST","SOUTH-WEST")
    combo2.place(x=177,y=282)
    combo2.current(0)
    l6=Label(tab1,text=" FURNISHED : ",relief='sunken',font='Times 10 bold ')
    l6.place(x=30,y=318)
    combo3=Combobox(tab1,textvariable=furn,font="Times 10 ")
    combo3['values']=("FURNISHED","SEMI-FURNISHED","UNFURNISHED")
    combo3.place(x=177,y=318)
    combo3.current(0)
    l7=Label(tab1,text=" BUDGET TYPE : ",relief='sunken',font='Times 10 bold ')
    l7.place(x=30,y=354)
    z5=Entry(tab1,textvariable=bud,width=17)
    z5.place(x=177,y=354)
    l8=Label(tab1,text=" AREA COVD.: ",relief='sunken',font='Times 10 bold ')
    l8.place(x=362,y=390)
    z6=Entry(tab1,textvariable=area,width=17)
    z6.place(x=494,y=390)
    l9=Label(tab1,text=" AVAILABILITY: ",relief='sunken',font='Times 10 bold ')
    l9.place(x=30,y=426)
    combo4=Combobox(tab1,width=14,textvariable=ava,font="Times 10 ")
    combo4['values']=("AVAILABLE","OCCUPIED")
    combo4.place(x=177,y=426)
    combo4.current(0)
    l10=Label(tab1,text=" AGE: ",relief='sunken',font='Times 10 bold ')
    l10.place(x=362,y=426)
    z7=Entry(tab1,textvariable=age,width=17)
    z7.place(x=494,y=426)
    tk.Button(tab1,text='  QUIT!   ',command= quit,fg='maroon',width=12 ,borderwidth=5,highlightthickness=5,font=' bold' ).place(x=40,y=535)
    tk.Button(tab1,text='  SUBMIT  ',command= submit2,fg='dark blue',width=12 ,borderwidth=5,highlightthickness=5,font=' bold' ).place(x=182,y=535)
    tk.Button(tab1,text='   CLEAR   ',command=clearTextInput,fg='dark green',width=12,borderwidth=5,highlightthickness=5,font='bold').place(x=324,y=535) 
    X=scrolledtext.ScrolledText(tab1,wrap=tk.WORD,width=18,height=11,font=('Times New Roman',12))
    X.place(x=399,y=66)
    X.insert(tk.INSERT,
             """\
BUDGET
TYPE  ~  PRICE        |
-----------------------
A    ->  ABOVE 10 Cr 
B    ->  5-10 Cr
C    ->  1-5 Cr      
D    ->  75 L - 1 Cr 
E    ->  50-75 L     
F    ->  34-50 L
G    ->  20-34 L
H    ->  1-20 L      
I    ->  90000-70000
J    ->  70000-55000 
K    ->  55000-30000
L    ->  30000-10000 
M    ->  10000-6000  
N    ->  6000-2000   
------------------------""")
    X.configure(state='disabled')

    root.mainloop()

def torent():
    global root
    speak('for better response fill your details in capital letters only')
    root.title("SELL")
    root.geometry("650x650")
    tabcontrol1=Notebook(root)
    tab1=tk.Frame(tabcontrol1,relief='sunken',bg='olive')
    tabcontrol1.add(tab1,text='NEW PROFILE')
    tab2=tk.Frame(tabcontrol1,relief='sunken',bg='olive')
    tabcontrol1.add(tab2,text='UPDATE PROFILE')
    tabcontrol1.grid(column=0,row=0,ipadx=600,ipady=550,sticky='S')
    Label(tab2,text=' **FILL THE DETAILS IN CAPITAL LETTERS ONLY  ',relief='raised').grid(column=1,row=0,padx=81,pady=17)
    Label(tab2,text=' *YOU CAN ONLY UPDATE YOUR CONTACT NO. AND AVAILABILITY*  ',relief='raised').grid(column=1,row=1,padx=81)
    def clearTextInput():
        
        y1.delete(first=0,last=100)
        z0.delete(first=0,last=100)
        z1.delete(first=0,last=100)
        z2.delete(first=0,last=100)
        z3.delete(first=0,last=100)
        z4.delete(first=0,last=100)
        z5.delete(first=0,last=100)
        z6.delete(first=0,last=100)
        z7.delete(first=0,last=100)
        comb.delete(first=0,last=100)
        comb.current(0)
        combo.delete(first=0,last=100)
        combo.current(0)
        combo1.delete(first=0,last=100)
        combo1.current(0)
        combo2.delete(first=0,last=100)
        combo2.current(0)
        combo3.delete(first=0,last=100)
        combo3.current(0)
        combo4.delete(first=0,last=100)
        combo4.current(0)
    def check() :
        if num.get() == 1 :
            z0.configure(show = "")
            y1.configure(show="")
        elif num.get() == 0 :
            z0.configure(show = "*")
            y1.configure(show="*")    
    a0=Label(tab2,text="USER PASSWD:",relief='sunken',font='Times 10 bold ')
    a0.place(x=80,y=120)
    z0=Entry(tab2,textvariable=idd,width=20,show='*')
    z0.place(x=240,y=120)
    button1 = Checkbutton(tab2,command=check,onvalue=1,offvalue=0,variable=num)
    button1.place(x =380, y = 120)
    a1=Label(tab2,text=" NAME : ",relief='sunken',font='Times 10 bold ')
    a1.place(x=80,y=176)
    z1=Entry(tab2,textvariable=nam,width=20)
    z1.place(x=240,y=176)
    a2=Label(tab2,text=' PHONE NO. : ',relief='sunken',font='Times 10 bold ')
    a2.place(x=80,y=232)
    z2=Entry(tab2,textvariable=cont,width=20)
    z2.place(x=240,y=232)
    a3=Label(tab2,text=' AVAILABILITY : ',relief='sunken',font='Times 10 bold ')
    a3.place(x=80,y=288)
    comb=Combobox(tab2,width=14,textvariable=ava,font="Times 10 ")
    comb['values']=("AVAILABLE","OCCUPIED")
    comb.place(x=240,y=288)
    comb.current(0)
    tk.Button(tab2,text='  QUIT!  ',command= quit,fg='maroon',width=12 ,borderwidth=5,highlightthickness=5,font=' bold').place(x=111,y=396)
    tk.Button(tab2,text='  UPDATE   ',command= update,fg='blue',width=12 ,borderwidth=5,highlightthickness=5,font=' bold').place(x=430,y=396)
    tk.Button(tab2,text='   DELETE   ',command= delete ,fg='red',width=12 ,borderwidth=5,highlightthickness=5,font=' bold').place(x=156,y=508)
    tk.Button(tab2,text='   CLEAR    ',command=clearTextInput,fg='green',width=12,borderwidth=5,highlightthickness=5,font=' bold ').place(x=372,y=508)

    Label(tab1,text=' **FILL THE DETAILS IN CAPITAL LETTERS ONLY  ',relief='raised').grid(column=1,row=0,padx=121,pady=17)
    b0=Label(tab1,text=" USER PASSWD : ",relief='sunken',font='Times 10 bold ')
    b0.place(x=30,y=390)
    y1=Entry(tab1,textvariable=idd,width=20,show='*')
    y1.place(x=177,y=390)
    button = Checkbutton(tab1,command=check,onvalue=1,offvalue=0,variable=num)
    button.place(x =315, y = 390)
    a1=Label(tab1,text=" NAME : ",relief='sunken',font='Times 10 bold ')
    a1.place(x=30,y=66)
    z1=Entry(tab1,textvariable=nam,width=20)
    z1.place(x=177,y=66)
    a2=Label(tab1,text=' PHONE NO. : ',relief='sunken',font='Times 10 bold ')
    a2.place(x=30,y=102)
    z2=Entry(tab1,textvariable=cont,width=20)
    z2.place(x=177,y=102)
    l1=Label(tab1,text=" LOCATION :",relief='sunken',font='Times 10 bold ')
    l1.place(x=30,y=138)
    z3=Entry(tab1,textvariable=loc,width=23)
    z3.place(x=177,y=138)
    l2=Label(tab1,text=" HOUSE TYPE : ",relief='sunken',font='Times 10 bold ')
    l2.place(x=30,y=174)
    combo=Combobox(tab1,textvariable=hou_typ,font="Times 10 ")
    combo['values']=("1BHK","2BHK","3BHK","4BHK","5BHK",">5BHK")
    combo.place(x=177,y=174)
    combo.current(0)
    l3=Label(tab1,text=" FLOOR : ",relief='sunken',font='Times 10 bold ')
    l3.place(x=30,y=210)
    z4=Entry(tab1,textvariable=floor,width=20)
    z4.place(x=177,y=210)
    l4=Label(tab1,text=" LAND TYPE : ",relief='sunken',font='Times 10 bold ')
    l4.place(x=30,y=246)
    combo1=Combobox(tab1,textvariable=lan_typ,font="Times 10 ")
    combo1['values']=("RESIDENTIAL","COMMERCIAL","OTHERS")
    combo1.place(x=177,y=246)
    combo1.current(0)
    l5=Label(tab1,text=" FACING : ",relief='sunken',font='Times 10 bold ')
    l5.place(x=30,y=282)
    combo2=Combobox(tab1,textvariable=face,font="Times 10 ")
    combo2['values']=("EAST","WEST","NORTH","SOUTH","NORTH-EAST","SOUTH-EAST","NORTH-WEST","SOUTH-WEST")
    combo2.place(x=177,y=282)
    combo2.current(0)
    l6=Label(tab1,text=" FURNISHED : ",relief='sunken',font='Times 10 bold ')
    l6.place(x=30,y=318)
    combo3=Combobox(tab1,textvariable=furn,font="Times 10 ")
    combo3['values']=("FURNISHED","SEMI-FURNISHED","UNFURNISHED")
    combo3.place(x=177,y=318)
    combo3.current(0)
    l7=Label(tab1,text=" BUDGET TYPE : ",relief='sunken',font='Times 10 bold ')
    l7.place(x=30,y=354)
    z5=Entry(tab1,textvariable=bud,width=17)
    z5.place(x=177,y=354)
    l8=Label(tab1,text=" AREA COVD.: ",relief='sunken',font='Times 10 bold ')
    l8.place(x=362,y=390)
    z6=Entry(tab1,textvariable=area,width=17)
    z6.place(x=494,y=390)
    l9=Label(tab1,text=" AVAILABILITY: ",relief='sunken',font='Times 10 bold ')
    l9.place(x=30,y=426)
    combo4=Combobox(tab1,width=14,textvariable=ava,font="Times 10 ")
    combo4['values']=("AVAILABLE","OCCUPIED")
    combo4.place(x=177,y=426)
    combo4.current(0)
    l10=Label(tab1,text=" AGE: ",relief='sunken',font='Times 10 bold ')
    l10.place(x=362,y=426)
    z7=Entry(tab1,textvariable=age,width=17)
    z7.place(x=494,y=426)
    tk.Button(tab1,text='  QUIT!   ',command= quit,fg='maroon',width=12 ,borderwidth=5,highlightthickness=5,font=' bold' ).place(x=40,y=535)
    tk.Button(tab1,text='  SUBMIT  ',command= submit2,fg='dark blue',width=12 ,borderwidth=5,highlightthickness=5,font=' bold' ).place(x=182,y=535)
    tk.Button(tab1,text='   CLEAR   ',command=clearTextInput,fg='dark green',width=12,borderwidth=5,highlightthickness=5,font='bold').place(x=324,y=535) 
    X=scrolledtext.ScrolledText(tab1,wrap=tk.WORD,width=18,height=11,font=('Times New Roman',12))
    X.place(x=399,y=66)
    X.insert(tk.INSERT,
             """\
BUDGET
TYPE  ~  PRICE        |
-----------------------
A    ->  ABOVE 10 Cr 
B    ->  5-10 Cr
C    ->  1-5 Cr      
D    ->  75 L - 1 Cr 
E    ->  50-75 L     
F    ->  34-50 L
G    ->  20-34 L
H    ->  1-20 L      
I    ->  90000-70000
J    ->  70000-55000 
K    ->  55000-30000
L    ->  30000-10000 
M    ->  10000-6000  
N    ->  6000-2000   
------------------------""")
    X.configure(state='disabled')

    root.mainloop()


def forrent():
    global root
    
    root.title("PURCHASE")
    root.geometry("650x650")
    a = tk.PhotoImage(file ="C:\\Users\\hp\\OneDrive\\Desktop\\mitali\\wp5.png")
    b = Label(root, image=a)
    b.place(x=0, y=0,relwidth=1, relheight=1)
    def clearTextInput():
        z1.delete(first=0,last=100)
        z2.delete(first=0,last=100)
        z3.delete(first=0,last=100)
        z4.delete(first=0,last=100)
        z5.delete(first=0,last=100)
        combo.delete(first=0,last=100)
        combo.current(0)
        combo1.delete(first=0,last=100)
        combo1.current(0)
        combo2.delete(first=0,last=100)
        combo2.current(0)
        combo3.delete(first=0,last=100)
        combo3.current(0)
    Label(root,text=' **FILL THE DETAILS IN CAPITAL LETTERS ONLY  ',relief='raised').grid(column=1,row=0,padx=81,pady=17)
    a1=Label(root,text=" NAME : ",relief='sunken',font='Times 10 bold ')
    a1.place(x=30,y=102)
    z1=Entry(root,textvariable=nam,width=20)
    z1.place(x=177,y=102)
    a2=Label(root,text=' PHONE NO. : ',relief='sunken',font='Times 10 bold ')
    a2.place(x=30,y=138)
    z2=Entry(root,textvariable=cont,width=20)
    z2.place(x=177,y=138)
    l1=Label(root,text=" LOCATION :",relief='sunken',font='Times 10 bold ')
    l1.place(x=30,y=174)
    z3=Entry(root,textvariable=loc,width=23)
    z3.place(x=177,y=174)
    l2=Label(root,text=" HOUSE TYPE : ",relief='sunken',font='Times 10 bold ')
    l2.place(x=30,y=210)
    combo=Combobox(root,textvariable=hou_typ,font="Times 10 ")
    combo['values']=("1BHK","2BHK","3BHK","4BHK","5BHK",">5BHK")
    combo.place(x=177,y=210)
    combo.current(0)
    l3=Label(root,text=" FLOOR : ",relief='sunken',font='Times 10 bold ')
    l3.place(x=30,y=246)
    z4=Entry(root,textvariable=floor,width=20)
    z4.place(x=177,y=246)
    l4=Label(root,text=" LAND TYPE : ",relief='sunken',font='Times 10 bold ')
    l4.place(x=30,y=282)
    combo1=Combobox(root,textvariable=lan_typ,font="Times 10 ")
    combo1['values']=("RESIDENTIAL","COMMERCIAL","OTHERS")
    combo1.place(x=177,y=282)
    combo1.current(0)
    l5=Label(root,text=" FACING : ",relief='sunken',font='Times 10 bold ')
    l5.place(x=30,y=318)
    combo2=Combobox(root,textvariable=face,font="Times 10 ")
    combo2['values']=("EAST","WEST","NORTH","SOUTH","NORTH-EAST","SOUTH-EAST","NORTH-WEST","SOUTH-WEST")
    combo2.place(x=177,y=318)
    combo2.current(0)
    l6=Label(root,text=" FURNISHED : ",relief='sunken',font='Times 10 bold ')
    l6.place(x=30,y=354)
    combo3=Combobox(root,textvariable=furn,font="Times 10 ")
    combo3['values']=("FURNISHED","SEMI-FURNISHED","UNFURNISHED")
    combo3.place(x=177,y=354)
    combo3.current(0)
    l7=Label(root,text=" BUDGET TYPE : ",relief='sunken',font='Times 10 bold ')
    l7.place(x=30,y=390)
    z5=Entry(root,textvariable=bud,width=17)
    z5.place(x=177,y=390)
    Button(root,text='QUIT',command= quit ).place(x=40,y=476)
    Button(root,text='  VIEW RESULT  ',command= viewresult1 ).place(x=314,y=476)
    Button(root,text='BACK',command= back ).place(x=177,y=476)
    Button(root,text='CLEAR',command=clearTextInput).place(x=451,y=476)
    X=scrolledtext.ScrolledText(root,wrap=tk.WORD,width=18,height=11,font=('Times New Roman',12))
    X.place(x=399,y=102)
    X.insert(tk.INSERT,
             """\
BUDGET
TYPE  ~  PRICE        |
-----------------------
A    ->  ABOVE 10 Cr 
B    ->  5-10 Cr
C    ->  1-5 Cr      
D    ->  75 L - 1 Cr 
E    ->  50-75 L     
F    ->  34-50 L
G    ->  20-34 L
H    ->  1-20 L      
I    ->  90000-70000
J    ->  70000-55000 
K    ->  55000-30000
L    ->  30000-10000 
M    ->  10000-6000  
N    ->  6000-2000   
------------------------""")
    X.configure(state='disabled')
    speak('for better response fill your details in capital letters only')
    
    root.mainloop()

def quit(): 
    root.destroy()

def back():
    
    root.title("NIVAS REAL ESTATE")
    root.geometry("560x470")
    filename = tk.PhotoImage(file ="C:\\Users\\hp\\OneDrive\\Desktop\\mitali\\wpp.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0,relwidth=1, relheight=1)
    Label(root,text='Get your dream home with NIVAS...',font='Times 16 bold italic',relief='raised').grid(column=1,row=0,padx=81,pady=24)
    Button(root,text='PURCHASE',command= wanna_buy ).grid(column=1,row=1,pady=21,padx=81,ipadx=12,ipady=7,sticky='S')
    Button(root,text='SELL',command= wanna_sell ).grid(column=1,row=2,pady=21,padx=81,ipadx=12,ipady=7,sticky='S')
    Button(root,text='TO RENT',command= torent).grid(column=1,row=3,pady=21,padx=81,ipadx=12,ipady=7,sticky='S')
    Button(root,text='FOR RENT',command= forrent ).grid(column=1,row=4,pady=21,padx=81,ipadx=12,ipady=7,sticky='S')        
    root.mainloop()

def viewresult1():
   
    global root
    p1=loc.get()
    p2=hou_typ.get()
    p3=lan_typ.get()
    p4=face.get()
    p5=furn.get()
    p6=bud.get()
    p9=floor.get()
    p7=nam.get()
    p8=cont.get()
    query2="insert into customers (cust_name,phone) values('{}',{})".format(p7,p8)
    cursor.execute(query2)
    a.commit()
    query1="select O_NAME,LOC,AREA_COV,AVAB from OWNERS where loc like %s  and for_=%s and floor='%s' and hou_typ= %s and land_type=%s and facing=%s and furn=%s and bud_type=%s "
    cursor.execute(query1,('%'+p1+'%','SELL',p9,p2,p3,p4,p5,p6))
    data=cursor.fetchall()
    print("................................................................................................................")
    print(" OWNER NAME                  LOCATION                    AREA COVERED           AVAILABILITY        ")
    print("................................................................................................................")
    for r in data:
        print( r[0],"     ",r[1],"       ", r[2],"        ",r[3])

def viewresult2():
   
    global root
    p1=loc.get()
    p2=hou_typ.get()
    p3=lan_typ.get()
    p4=face.get()
    p5=furn.get()
    p6=bud.get()
    p9=floor.get()
    p7=nam.get()
    p8=cont.get()
    query2="insert into customers (cust_name,phone) values('{}',{})".format(p7,p8)
    cursor.execute(query2)
    a.commit()
    query1="select O_NAME,LOC,AREA_COV,AVAB ,BUD_TYPE from OWNERS where loc like %s  and for_=%s and floor='%s' and hou_typ= %s and land_type=%s and facing=%s and furn=%s and bud_type=%s "
    cursor.execute(query1,('%'+p1+'%','RENT',p9,p2,p3,p4,p5,p6))
    data=cursor.fetchall()
    print("........................................................................................................................................")
    print(" OWNER NAME                  LOCATION                     AREA COVERED               AVAILABILITY           BUDGET TYPE    ")
    print("........................................................................................................................................")
    for r in data:
        print( r[0],"     ",r[1],"           ", r[2],"             ",r[3],"           " ,r[4])


#.........................................INSERTION.....................................

def submit1():
    global root
    p1=loc.get()
    p2=hou_typ.get()
    p3=lan_typ.get()
    p4=face.get()
    p5=furn.get()
    p6=bud.get()
    p9=floor.get()
    p7=nam.get()
    p8=cont.get()
    p10=idd.get()
    p12=area.get()
    p13=ava.get()
    p11=age.get()
    
    if p8!=0 and p10!=' ':
        query="insert into owners(usr_passwd,o_name,age,cont,loc,hou_typ,floor,land_type,facing,furn,area_cov,avab,for_,bud_type)values('{}','{}',{},{},'{}','{}',{},'{}','{}','{}','{}','{}','{}','{}')".format(p10,p7,p11,p8,p1,p2,p9,p3,p4,p5,p12,p13,'RENT',p6)
        cursor.execute(query)
        a.commit()
        messagebox.showinfo("INFO","YOUR DETAILS HAVE BEEN SUBMITTED SUCCESSFULLY..." )
    else:
        messagebox.showwarning("WARNING","PLEASE FILL YOUR DETAILS CORRECTLY")
def submit2():
    global root
    p1=loc.get()
    p2=hou_typ.get()
    p3=lan_typ.get()
    p4=face.get()
    p5=furn.get()
    p6=bud.get()
    p9=floor.get()
    p7=nam.get()
    p8=cont.get()
    p10=idd.get()
    p12=area.get()
    p13=ava.get()
    p11=age.get()
    
    if p8!=0 and p10!=' ':
        query="insert into owners(usr_passwd,o_name,age,cont,loc,hou_typ,floor,land_type,facing,furn,area_cov,avab,for_,bud_type)values('{}','{}',{},{},'{}','{}',{},'{}','{}','{}','{}','{}','{}','{}')".format(p10,p7,p11,p8,p1,p2,p9,p3,p4,p5,p12,p13,'SELL',p6)
        cursor.execute(query)
        a.commit()
        messagebox.showinfo("INFO","YOUR DETAILS HAVE BEEN SUBMITTED SUCCESSFULLY..." )
    else:
        messagebox.showwarning("WARNING","PLEASE FILL YOUR DETAILS CORRECTLY")

#.....................................UPDATION........................................
    
def update():
    p7=ava.get()
    p8=cont.get()
    p10=idd.get()
    query0="select * from owners where usr_passwd='{}'".format(p10)
    cursor.execute(query0)
    data=cursor.fetchall()
    if len(data)==0:
        messagebox.showerror("ERROR","NO DATA FOUND...")
    else:
        query="update owners set avab = '{}' where usr_passwd='{}' ".format(p7,p10)
        cursor.execute(query)
        query1="update owners set cont = '{}' where usr_passwd='{}' ".format(p8,p10)
        cursor.execute(query1)
        a.commit( )
        messagebox.showinfo("INFO","YOUR DETAILS HAVE BEEN UPDATED SUCCESSFULLY...")

        
#.....................................DELETION.......................................
    
def delete():
    p10=idd.get()
    p8=cont.get()
    query0="select * from owners where usr_passwd='{}' and cont='{}'".format(p10,p8)
    cursor.execute(query0)
    data=cursor.fetchall()
    if len(data)==0:
        messagebox.showerror("ERROR","NO DATA FOUND...")
    else:
        query="delete from owners where usr_passwd='{}' and cont='{}'".format(p10,p8)
        cursor.execute(query)
        a.commit( )
        messagebox.showinfo("INFO","YOUR PROFILE HAS BEEN DELETED ...")


root=tk.Tk()
root.title("NIVAS REAL ESTATE")
root.geometry("560x470")
s=pyttsx3.init()
voices=s.getProperty('voices')
s.setProperty('voice',voices[1].id)
speak('welcome to my project')
filename = tk.PhotoImage(file ="C:\\Users\\hp\\OneDrive\\Desktop\\mitali\\wpp.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0,relwidth=1, relheight=1)
Label(root,text='Get your dream home with NIVAS...',font='Times 16 bold italic',relief='raised').grid(column=1,row=0,padx=81,pady=24)
hou_typ=tk.StringVar()
lan_typ=tk.StringVar()
face=tk.StringVar()
furn=tk.StringVar()
bud=tk.StringVar()
nam=tk.StringVar()
cont=tk.IntVar()
floor=tk.IntVar()
idd=tk.StringVar()
loc=tk.StringVar()
area=tk.StringVar()
ava=tk.StringVar()
age=tk.IntVar()
num=tk.IntVar()
Button(root,text='PURCHASE',command= wanna_buy ).grid(column=1,row=1,pady=21,padx=81,ipadx=12,ipady=7,sticky='S')
Button(root,text='SELL',command= wanna_sell ).grid(column=1,row=2,pady=21,padx=81,ipadx=12,ipady=7,sticky='S')
Button(root,text='TO RENT',command= torent).grid(column=1,row=3,pady=21,padx=81,ipadx=12,ipady=7,sticky='S')
Button(root,text='FOR RENT',command= forrent ).grid(column=1,row=4,pady=21,padx=81,ipadx=12,ipady=7,sticky='S')        

root.mainloop()
