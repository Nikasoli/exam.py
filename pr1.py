from tkinter import *
from tkinter import ttk
import sqlite3
import pandas as pd
#********************************
con=sqlite3.connect('data.db')
pk=con.cursor()
pk.execute('create table if not exists std(name txt , grade integer)')

def save():
    n=name.get()
    g=grade.get()
    ful=[n,g]
    pk.execute('insert into std(name,grade) values(?,?)',ful)
    con.commit()
    clear()
def clear():
    name.delete(0,'end')
    grade.delete(0,'end')
    name.focus()
def export():
    lst1=[]
    lst2=[]
    result1=pk.execute('select name from std ')
    for i in result1:
        lst1.append(*i)
    result2=pk.execute('select grade from std')
    for i in result2:
        lst2.append(*i)
    print(lst1)
    print(lst2)
    lst3=list(zip(lst1,lst2))
    df=pd.DataFrame(lst3)
    print(df)
    df.to_excel('std.xlsx')
    df.to_json('std.json')
    df.to_csv('std.csv')
def search():
    grade.delete(0,'end')
    n=name.get()
    result=pk.execute('select * from std where name=?',(n,))
    result=(list(*result))
    print(result)
    grade.insert(0,result[1])
    result2=pk.execute('select grade from std')
def result():
    lst4=[]
    lst5=[]
    result=pk.execute('select * from std where grade=?',(20,))
    for itm in result:
        lst4.append(list(itm))
    print(lst4)
    for i in lst4:
        lst5.append(i)
        lst5=''.join(i)
    print(lst5)
        

    

    #lst4=[]
    #for i in result:
        #lst4.append(*i)
    #x=max(lst4)
    #y=min(lst4)
    #a=sum(lst4)
    #l=len(lst4)
    #a=a/l
    #resultn=pk.execute('select name from std where grade=?',(x,))
    #resultn=list(*resultn)
    #for i in resultn:
        #resultn=i
    #L3.config(text=f'max={x}  name={resultn}\n  min={y}\n average={a}')
    

win=Tk()
win.config(bg='purple')
win.geometry('500x300+300+500')
win.title('form')
name=Entry(justify='center',font=('tahoma',12),bg='skyblue')
name.place(x=50,y=10,width=200,height=40)
grade=Entry(justify='center',font=('tahoma',12),bg='skyblue')
grade.place(x=50,y=65,width=200,height=40)
bt1=Button(justify='center',font=('tahoma',14),bg='pink',text='save',command=save)
bt1.place(x=50,y=150,width=200,height=40)
bt2=Button(justify='center',font=('tahoma',14),bg='pink',text='search',command=search)
bt2.place(x=50,y=205,width=200,height=40)
bt3=Button(justify='center',font=('tahoma',14),bg='pink',text='export',command=export)
bt3.place(x=50,y=260,width=200,height=40)
#دکمه result برای بالا ترین نمره  و معدل کل کلاس و پایین ترین نمره هست
b4=Button(text='results',font=('tahoma',9),bg='yellow',justify='center',command=result)
b4.place(x=300,y=20,width=60,height=40)
L1=Label(bg='purple',text='نام',justify='center')
L1.place(x=250,y=10,width=25,height=35)
L2=Label(bg='purple',text='معدل',justify='center')
L2.place(x=253,y=65,width=25,height=35)
L3=Label(bg='white',text='...',justify='center')
L3.place(x=300,y=70,width=150,height=200)
mainloop()