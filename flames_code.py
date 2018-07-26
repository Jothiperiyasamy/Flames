from tkinter import *

def flames_function():
    name1=list(n1.get())
    name2=list(n2.get())
    name22=name2.copy()
    for i in name1:
        if(i in name2):
            
            name2.remove(i)

    for i in name22:
        if(i in name1):
            name1.remove(i)
    
    num=len(name1)+len(name2)
    
    lst=list("flames")
    rep=int(num/6)
    print(rep)
    if(rep>=1):
        rem=num%6
        lst=lst * (rep+rem)
    
    while True:
        a=lst[num-1]
        lst1=lst[num-1:]
        lst1=lst1+lst[:num-1]
        lst=lst1.copy()
        cnt=lst.count(a)
        for i in range(cnt):
                lst.remove(a)
        if(lst.count(lst[0])==len(lst)):
            
            break
        rep=int(num/len(lst))
        if(rep>=1):
            rem=num%len(lst)
            lst=lst * (rep+rem)
    res=lst[0]
    dic={'f':'Friends','l':'Lovers','a':'Affectionate with each other','m':'Marriage','e':'Enemies','s':'Sisters'}
    text.insert(END,(dic[res]))

window=Tk()
window.title("FLAMES")


f=Frame(window, height=300, width=1000)
f.propagate(0)
f.pack()
label1=Label(f,text="Enter His Name")
label1.grid(row=0,column=0)
n1=StringVar()
n2=StringVar()
t1=Entry(f,textvariable=n1)
t1.grid(row=0,column=1,columnspan=2)
label2=Label(f,text="Enter Her Name")
label2.grid(row=1,column=0)
t2=Entry(f,textvariable=n2)
t2.grid(row=1,column=1,columnspan=2)
button=Button(f,text="Find out",command=flames_function)
button.grid(row=2,column=1)
label3=Label(f,text="Your Relationship:")
label3.grid(row=3,column=0)
text=Text(f,height=1,width=10)
text.grid(row=3,column=1)

window.mainloop()
