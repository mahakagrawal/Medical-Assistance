from tkinter import *
import sqlite3 as s
import requests as r
import bs4
from tkinter import messagebox
try:
     client=s.connect("F://std.db")
     cu=client.cursor()
     cu.execute("create table register(name varchar(50),email varchar(80),phone int,password varchar(20),confirmpassword varchar(20))")
except:
     pass
def fun():
    scr=Tk()
    scr.title('Login')
    scr.geometry('1300x700')
    l=Label(scr,text='Username',bg='Black',fg='Red',font=('Time',38,'bold'))
    l1=Label(scr,text='Password',bg='Black',fg='Red',font=('Time',38,'bold'))
    e=Entry(scr,font=('default',38),bg='Yellow',fg='Blue')
    e1=Entry(scr,font=('default',38),bg='Yellow',fg='Blue')
    b=Button(scr,text=' Submit ',font=('default',32),bg='Green',fg='White')
    b1=Button(scr,text='Register',font=('default' ,32),bg='Red',fg='White')
    l2=Label(scr,text='USER LOGIN',fg='Black',font=('Arial Black',48,'bold'))
    b.place(x=400,y=490)
    b1.place(x=700,y=490)
    e1.place(x=550,y=320)
    l1.place(x=250,y=320)
    l.place(x=250,y=220)
    l2.place(x=430,y=70)
    e.place(x=550,y=220)
    e1.config(show='*')
    def Register():
        scr.destroy()
        scr1=Tk()
        scr1.title('Register')
        scr1.geometry('1300x700')
        a=Label(scr1,text='User Name',fg='black',font=('Time',24,'bold'))
        a1=Label(scr1,text='Email ID',fg='black',font=('Time',24,'bold'))
        a2=Label(scr1,text='Contactno.',fg='black',font=('Time',24,'bold'))
        a3=Label(scr1,text='Password',fg='black',font=('Time',24,'bold'))
        a4=Label(scr1,text='Confirm P.',fg='black',font=('Time',24,'bold'))
        en=Entry(scr1,font=('default',24),fg='blue',bd=5)
        en1=Entry(scr1,font=('default',24),fg='blue',bd=5)
        en2=Entry(scr1,font=('default',24),fg='blue',bd=5)
        en3=Entry(scr1,font=('default',24),fg='blue',bd=5)
        en4=Entry(scr1,font=('default',24),fg='blue',bd=5)
        bu=Button(scr1,text=' Login ',font=('default',32),bg='Green',fg='White')
        a5=Label(scr1,text='REGISTER',fg='Red',font=('Arial Black',32,'bold','underline'))
        a5.place(x=500,y=20)
        a.place(x=300,y=130)
        a1.place(x=300,y=230)
        a2.place(x=300,y=330)
        a3.place(x=300,y=430)
        a4.place(x=300,y=530)
        en.place(x=600,y=130)
        en1.place(x=600,y=230)
        en2.place(x=600,y=330)
        en3.place(x=600,y=430)
        en4.place(x=600,y=530)
        bu.place(x=500,y=600)
        def submitdb():
               if en3.get()==en4.get():
                    cu.execute("insert into register values(%r,%r,%d,%r,%r)"%(en.get(),en1.get(),int(en2.get()),en3.get(),en4.get()))
                    client.commit()
                    submit()
               else:
                    messagebox.showinfo('Error','password does not match')
        def submit():
            scr1.destroy()
            fun()
        bu.config(command=submitdb)
    def login():
        cu.execute("select count(*) from register where Name=%r and Password=%r"%(e.get(),e1.get()))
        a=cu.fetchall()
        if a[0][0]==1:
            messagebox.showinfo('Successful','Login Sucessfull')
            def main():
                global m
                scr.destroy()
                scr2=Tk()
                scr2.title('Medical Assistance')
                scr2.geometry('1300x700')
                l1=Label(scr2,text='Enter name of medicine',fg='black',font=('Time',24,'bold',))
                l=Label(scr2,text='Main Page',fg='red',font=('Time',38,'bold','underline'))
                e1=Entry(scr2,font=('default',24),fg='blue',bd=5)
                l.place(x=500,y=100)
                l1.place(x=270,y=200)
                e1.place(x=720,y=200)
                m=Message(scr2)
                def scrap():
                    lst=[]
                    dt=r.request('get','https://www.1mg.com/search/all?name=%s'%(e1.get()))
                    s=bs4.BeautifulSoup(dt.text,'html.parser')
                    for i in s.findAll('div'):
                        if i.get('class'):
                            if len([x for x in i.get('class') if 'style__container__' in x])>0:
                                if i.find('a'):
                                    x=i.find('a')
                                    try:
                    
                                        dts=r.request('get','https://www.1mg.com'+x.get('href'))
                                        s1=bs4.BeautifulSoup(dts.text,'html.parser')
                                        for j in s1.findAll('div'):
                                            if j.get('class'):
                                                if len([x for x in j.get('class') if '_product-description' in x])>0:
                                    
                                                    try:
                                                        lst.append(j.text)    
                                                    except:
                                                        pass
                                        
                                                elif  len([x for x in j.get('class') if 'DrugOverview__container' in x])>0:
                                    
                                                    try:
                                                        lst.append(j.text)
                                                    except:
                                                        pass
                                    except:
                                        pass

                    global data                        
                    data=iter(lst)
                    m.config(text=next(data),bg='red',fg='white',font=('times',12,'bold'))
    
                b=Button(scr2,text='Search',font=('times',20,'bold'),bg='green',fg='white',command=scrap)
                m.pack(side=BOTTOM)
                b.place(x=470,y=300)
                def nxt():
                    global data,m
                    try:
                        m.config(text=next(data),bg='red',fg='white',font=('times',12,'bold'))
                    except:
                        m.config(text='Finish Information',bg='yellow',font=('times',12,'bold'))
                b1=Button(scr2,text='Next',font=('times',20,'bold'),bg='Cyan',fg='black',command=nxt)
                b1.place(x=670,y=300)
            main()    
        else: 
            messagebox.showinfo('Error','invalid username and password')       
    b1.config(command=Register)
    b.config(command=login)
fun()
