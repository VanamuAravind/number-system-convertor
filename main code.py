from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Number convertor')
root.geometry('1280x720')

#====================variable====================
num=IntVar()
lblbinary=StringVar()
lbldecimal=StringVar()
lblhexa=StringVar()
lbloctal=StringVar()

#===================functions=====================
def convert():
    if num.get()==0:
        messagebox.showerror('Error','You must enter a number to convert')
    else:
        lblbinary.set(str(bin(num.get())))
        lbldecimal.set(str(num.get()))
        lblhexa.set(str(hex(num.get())))
        lbloctal.set(str(oct(num.get())))

def clear():
    num.set(0)
    lblhexa.set('')
    lblbinary.set('')
    lbldecimal.set('')
    lbloctal.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to Exit'):
        root.destroy()


Label(root,text='Coversion System',font=('times new rommon',60,'bold'),bg='lime',fg='red',relief=RIDGE).pack(pady=10)

n=Label(root,text='Enter Number',font='arial 20 bold')
n.place(x=300,y=150)
n_txt=Entry(root,font=('times new rommon',20,'bold'),fg='red',justify=CENTER,relief=GROOVE,textvariable=num)
n_txt.place(x=650,y=160)

b=Label(root,text='Binary',font='arial 20 bold')
b.place(x=300,y=310)
b_txt=Entry(root,font=('times new rommon',20,'bold'),fg='orange',justify=CENTER,relief=GROOVE,textvariable=lblbinary)
b_txt.place(x=650,y=230)

d=Label(root,text='decimal',font='arial 20 bold')
d.place(x=300,y=230)
d_txt=Entry(root,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=lbldecimal)
d_txt.place(x=650,y=300)

h=Label(root,text='Hexa Decimal',font='arial 20 bold')
h.place(x=300,y=470)
h_txt=Entry(root,font=('times new rommon',20,'bold'),fg='pink',justify=CENTER,relief=GROOVE,textvariable=lblhexa)
h_txt.place(x=650,y=380)


o=Label(root,text='Octal',font='arial 20 bold')
o.place(x=300,y=390)
o_txt=Entry(root,font=('times new rommon',20,'bold'),fg='black',justify=CENTER,relief=GROOVE,textvariable=lbloctal)
o_txt.place(x=650,y=460)

btn1=Button(root,text='Converter',font='arial 20 bold',fg='crimson',bg='lime',width=10,relief=GROOVE,bd=10,command=convert)
btn1.place(x=300,y=600)

btn2=Button(root,text='Clear',font='arial 20 bold',fg='crimson',bg='lime',width=10,relief=GROOVE,bd=10,command=clear)
btn2.place(x=600,y=600)

btn3=Button(root,text='Exit',font='arial 20 bold',fg='crimson',bg='lime',width=10,relief=GROOVE,bd=10,command=exit)
btn3.place(x=900,y=600)

root.mainloop()
