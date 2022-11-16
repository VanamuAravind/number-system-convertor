from tkinter import*


root=Tk()
root.geometry("1500x900")
root.configure(bg="#41B3A3")
root.title("NUMBER SYSTEM CONVERTOR")

#backend....  only solution interface is included

def decide():
    frominput=fromset.get()
    
    if(frominput=="Octal"):
        octaltobinary()
    else:
        hextobinary()

def octaltobinary():
    tooutput=toset.get()
    
    num=fromentry.get()
    lst=[]
    ans=[]                                  #holds binary number 
    for i in num:
        lst.append(i)

    for i in lst:                                   #octal to binary
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    if(int(i)==4*k + 2*l + m):
                        ans.append(str(k))
                        ans.append(str(l))
                        ans.append(str(m))
                        break

    dec=list(reversed(ans))         #binary to decimal
    count=0
    power=0
    for i in dec:
        count=count+int(i)*(2**power)
        power=power+1
                                #count=final decimal number


    ctr=0
    for i in ans:
        ctr=ctr+1

    extra=ctr%4

    hans=list(reversed(ans))

    if(extra!=0):
        for i in range(4-extra):
            hans.append(0)

    hdans=list(reversed(hans))          #holds binary number with extra zero's


                        #program to convert binary to hexadecimal
    lst=hdans
    ptr=0
    j=0
    k=0
    sumlst=[]
    mainlst=[]
    for i in lst:
        ptr=ptr+1

    n=int(ptr/4)
    for i in range(n):
        j=j+4
        dosum=0
        power=3
        for i in range(k,j):
            dosum=dosum+(int(lst[i])*(2**power))
            power=power-1
        sumlst.append(dosum)
        k=k+4 

    for i in sumlst:
        if(i>9):
            if(i==10):
                mainlst.append('A')
            if(i==11):
                mainlst.append('B')
            if(i==12):
                mainlst.append('C')
            if(i==13):
                mainlst.append('D')
            if(i==14):
                mainlst.append('E')
            if(i==15):
                mainlst.append('F')
        else:
            mainlst.append(str(i))
            
    if(tooutput=="Binary"):
        x1=140
        label1=Label(root,text="Answer = "+''.join(ans))
        label1.place(x=x1,y=450)
        label1.configure(width=38,bg="#C38D9E",fg="white",font=("Times New Roman",18,"bold"))
        octalsol()
    if(tooutput=="Decimal"):
        x1=140
        label1=Label(root,text="Answer = "+str(count))
        label1.place(x=x1,y=450)
        label1.configure(width=38,bg="#C38D9E",fg="white",font=("Times New Roman",18,"bold"))
        octalsol()
    if(tooutput=="Hexadecimal"):
        x1=140
        label1=Label(root,text="Answer = "+''.join(mainlst))
        label1.place(x=x1,y=450)
        label1.configure(width=38,bg="#C38D9E",fg="white",font=("Times New Roman",18,"bold"))
        octalsol()


def hextobinary():
    num=fromentry.get()
    hexbin=[]
    for i in num:
        if(i=='A' or i=='B' or i=='C' or i=='D' or i=='E' or i=='F'):
            if(i=='A'):
                hexbin.append("1010")
            if(i=='B'):
                hexbin.append("1011")
            if(i=='C'):
                hexbin.append("1100")
            if(i=='D'):
                hexbin.append("1101")
            if(i=='E'):
                hexbin.append("1110")
            if(i=='F'):
                hexbin.append("1111")
        else:
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        for n in range(2):
                            if(k*8+l*4+m*2+n==int(i)):
                                s=str(k)+str(l)+str(m)+str(n)
                                hexbin.append(s)
    x1=140
    label1=Label(root,text="Answer = "+''.join(hexbin))
    label1.place(x=x1,y=450)
    label1.configure(width=38,bg="#C38D9E",fg="white",font=("Times New Roman",18,"bold"))




def octalsol():
    choice=toset.get()
    if(choice=="Binary"):
        num=fromentry.get()
        y1=200
        q="Given octal number is "+num
        l=Label(root,text=q)
        l.place(x=900,y=y1)
        l.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        lm=Label(root,text="to convert from octal to binary number,")
        y1=y1+40
        lm.place(x=900,y=y1)
        lm.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        ln=Label(root,text="we need to convert each digit into a binary number")
        y1=y1+40
        ln.place(x=900,y=y1)
        ln.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        lst=[]
        ans=[]                                  #holds binary number 
        for i in num:
            lst.append(i)
        y1=y1+40
        for i in lst:                                   #octal to binary
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        if(int(i)==4*k + 2*l + m):
                            ans.append(str(k))
                            ans.append(str(l))
                            ans.append(str(m))
                            sen="we can write "+str(i)+" as "+str(k)+str(l)+str(m)
                            sen1=str(i)+"->"+str(k)+str(l)+str(m)
                            l1=Label(root,text=sen)
                            l2=Label(root,text=sen1)
                            l1.place(x=900,y=y1)
                            l1.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
                            l2.place(x=900,y=y1+40)
                            l2.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
                            y1=y1+80
                            break
        l3=Label(root,text="so the final answer will be,")
        l3.place(x=900,y=y1)
        l3.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        l4=Label(root,text="Answer = "+''.join(ans))
        l4.place(x=900,y=y1+40)
        l4.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))

    if(choice=="Decimal"):
        num=fromentry.get()
        y1=200
        txt="to convert "+str(num)+" to decimal,"
        l1=Label(root,text=txt)
        l2=Label(root,text="we need to convert this number first into binary.")
        l1.place(x=900,y=y1)
        y1=y1+40
        l2.place(x=900,y=y1)
        l1.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        l2.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        lst=[]
        ans=[]                                  #holds binary number 
        for i in num:
            lst.append(i)

        for i in lst:                                   #octal to binary
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        if(int(i)==4*k + 2*l + m):
                            ans.append(str(k))
                            ans.append(str(l))
                            ans.append(str(m))
                            break
        txt1=str(num)+"->"+''.join(ans)
        l3=Label(root,text=txt1)
        y1=y1+40
        l3.place(x=900,y=y1)
        l3.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))

        l4=Label(root,text="to convert this binary to decimal,")
        y1=y1+40
        l4.place(x=900,y=y1)
        l4.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))

        l5=Label(root,text="we need to multiply each digit from right to left by 2 power i,")
        y1=y1+40
        l5.place(x=900,y=y1)
        l5.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))


        l6=Label(root,text="where i=0 and for every term i must increase by 1 .")
        y1=y1+40
        l6.place(x=900,y=y1)
        l6.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        tot=0
        for i in ans:
            tot=tot+1
        powr=tot-1
        y1=y1+40
        x1=900
        for i in ans:
            l7=Label(root,text="("+str(i)+"*"+"2^"+str(powr)+")")
            l7.place(x=x1,y=y1)
            l7.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
            powr=powr-1
            x1=x1+88
            
        l8=Label(root,text="we need to add all the terms after solving.")
        y1=y1+40
        l8.place(x=900,y=y1)
        l8.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))

        
        
        dec=list(reversed(ans))         #binary to decimal
        count=0
        power=0
        for i in dec:
            count=count+int(i)*(2**power)
            power=power+1
            
        l9=Label(root,text="final answer = "+str(count))
        y1=y1+40
        l9.place(x=900,y=y1)
        l9.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))

    if(choice=="Hexadecimal"):
        num=fromentry.get()
        y1=200
        txt="to convert "+str(num)+" to Hexadecimal,"
        l1=Label(root,text=txt)
        l2=Label(root,text="we need to convert this number first into binary.")
        l1.place(x=900,y=y1)
        y1=y1+40
        l2.place(x=900,y=y1)
        l1.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        l2.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        lst=[]
        ans=[]                                  #holds binary number 
        for i in num:
            lst.append(i)

        for i in lst:                                   #octal to binary
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        if(int(i)==4*k + 2*l + m):
                            ans.append(str(k))
                            ans.append(str(l))
                            ans.append(str(m))
                            break
        txt1=str(num)+"->"+''.join(ans)
        l3=Label(root,text=txt1)
        y1=y1+40
        l3.place(x=900,y=y1)
        l3.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))


        ctr=0
        for i in ans:
            ctr=ctr+1

        extra=ctr%4

        hans=list(reversed(ans))

        if(extra!=0):
            for i in range(4-extra):
                hans.append(0)

        hdans=list(reversed(hans))
        
        l4=Label(root,text="to convert from binary to hexadecimal,")
        l5=Label(root,text="the number of digits must be a multiple of 4")
        l6=Label(root,text="because we need to divide the number into parts of 4 digits")
        y1=y1+40
        l4.place(x=900,y=y1)
        l4.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        y1=y1+40
        l5.place(x=900,y=y1)
        l5.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        y1=y1+40
        l6.place(x=900,y=y1)
        l6.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))

        c=0
        x1=900
        y1=y1+40
        for i in hdans:
            c=c+1
            l7=Label(root,text=str(i))
            l7.place(x=x1,y=y1)
            l7.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
            
            if(c%4==0 and c<ctr+extra):
                x1=x1+20
                l8=Label(root,text=" | ")
                l8.place(x=x1,y=y1)
                l8.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
                
            x1=x1+20
        l9=Label(root,text="now we need to add the following terms")
        y1=y1+40
        l9.place(x=900,y=y1)
        l9.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))


        

        
        lst=hdans
        ptr=0
        j=0
        k=0
        sumlst=[]
        mainlst=[]
        for i in lst:
            ptr=ptr+1

        n=int(ptr/4)
        for i in range(n):
            j=j+4
            dosum=0
            power=3
            y1=y1+40
            x1=900
            for h in range(k,j):
                dosum=dosum+(int(lst[h])*(2**power))
                l10=Label(root,text="("+str(lst[h])+"*2^"+str(power)+")")
                l10.place(x=x1,y=y1)
                l10.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
                x1=x1+88
                
                power=power-1

                
            sumlst.append(dosum)
            l13=Label(root,text="=     "+str(dosum))
            l13.place(x=x1+88,y=y1)
            l13.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
            k=k+4

        l11=Label(root,text="we know that A=10,B=11,C=12,D=13,E=14,F=15")
        y1=y1+40
        l11.place(x=900,y=y1)
        l11.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))

        l12=Label(root,text="after substituting and merging all the terms we get,")
        y1=y1+40
        l12.place(x=900,y=y1)
        l12.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))
        

        for i in sumlst:
            if(i>9):
                if(i==10):
                    mainlst.append('A')
                if(i==11):
                    mainlst.append('B')
                if(i==12):
                    mainlst.append('C')
                if(i==13):
                    mainlst.append('D')
                if(i==14):
                    mainlst.append('E')
                if(i==15):
                    mainlst.append('F')
            else:
                mainlst.append(str(i))

        l14=Label(root,text="answer  =  "+''.join(mainlst))
        y1=y1+40
        l14.place(x=900,y=y1)
        l14.configure(bg="#41B3A3",fg="white",font=("Times New Roman",18,"bold"))

        
            
        








#interface

main_heading=Label(root,text="NUMBER SYSTEM CONVERTOR")
main_heading.configure(bg="#41B3A3",fg="#2F2FA2",font=("Georgia",24,"bold"))
main_heading.place(x=550,y=50)


fromset=StringVar()
fromset.set("select")
from_select=OptionMenu(root,fromset,"Octal","Hexadecimal")
from_select.place(x=160,y=200)
from_select.configure(width=20)
from_select["highlightthickness"]=0
from_select.configure(bg="#E8A87C",fg="white",font=("Garamond",14,"normal"))
from_select["menu"].configure(bg="#E8A87C",fg="white",font=("Garamond",14,"normal"))


fromlist=["Binary","Decimal","Hexadecimal"]
toset=StringVar()
toset.set("select")
to_select=OptionMenu(root,toset,*fromlist)
to_select.place(x=440,y=200)
to_select.configure(width=20)
to_select["highlightthickness"]=0
to_select.configure(bg="#E8A87C",fg="white",font=("Garamond",14,"normal"))
to_select["menu"].configure(bg="#E8A87C",fg="white",font=("Garamond",14,"normal"))


fromentry=Entry(root,width=20)
fromentry.place(x=160,y=250)
fromentry.configure(width=42,bg="#C38D9E",fg="white",font=("Times New Roman",18,"bold"))




submitb=Button(root,text="calculate")
submitb.place(x=320,y=350)
submitb.configure(width=20)
submitb.configure(bg="#E27D60",fg="white",font=("Times New Roman",16,"normal"),command=decide)



note=Label(root,text="NOTE :- my module contains...")
note.place(x=50,y=500)
note.configure(bg="#41B3A3",fg="red",font=("Courier New",12,"normal"))

note1=Label(root,text="1) Octal -> Binary")
note1.place(x=50,y=530)
note1.configure(bg="#41B3A3",fg="red",font=("Courier New",12,"normal"))

note2=Label(root,text="2) Octal -> Decimal")
note2.place(x=50,y=560)
note2.configure(bg="#41B3A3",fg="red",font=("Courier New",12,"normal"))

note3=Label(root,text="3) Octal -> Hexadecimal")
note3.place(x=50,y=590)
note3.configure(bg="#41B3A3",fg="red",font=("Courier New",12,"normal"))

note4=Label(root,text="4) Hexadecimal -> Binary")
note4.place(x=50,y=620)
note4.configure(bg="#41B3A3",fg="red",font=("Courier New",12,"normal"))







root.mainloop()
