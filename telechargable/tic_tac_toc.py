from tkinter import *
from random import *
win=Tk()
win.title("morpion")
t=randint(1,2)
run =True
def ver(si):
    global run
    if c1['text']==c2['text']==c3['text']!=''or c4['text']==c5['text']==c6['text']!='' or c7['text']==c8['text']==c9['text']!="" or c1['text']==c4['text']==c7['text']!=""or c2['text']==c5['text']==c8['text']!="" or c3['text']==c6['text']==c9['text']!="" or c1['text']==c5['text']==c9['text']!="" or c3['text']==c5['text']==c7['text']!='':
        res['text']="le joueur {} à gagner".format(si)
        run=False
def un():
    global t
    if c1['text']=='' and run ==True:
        if t==1:
            c1['text']='0'
            ver("0")
            t=2
        else:
            c1['text']="X"
            ver("X")
            t=1
def deux():
    global t
    if c2['text']==''and run ==True:
        if t==1:
            c2['text']='0'
            ver("0")
            t=2
        else:
            c2['text']="X"
            ver("X")
            t=1
def trois():
    global t
    if c3['text']==''and run ==True:
        if t==1:
            c3['text']='0'
            ver("0")
            t=2
        else:
            c3['text']="X"
            ver("X")
            t=1
def quatre():
    global t
    if c4['text']==''and run ==True:
        if t==1:
            c4['text']='0'
            ver("0")
            t=2
        else:
            c4['text']="X"
            ver("X")
            t=1
def cinq():
    global t
    if c5['text']==''and run ==True:
        if t==1:
            c5['text']='0'
            ver("0")
            t=2
        else:
            c5['text']="X"
            ver("X")
            t=1
def six():
    global t
    if c6['text']==''and run ==True:
        if t==1:
            c6['text']='0'
            ver("0")
            t=2
        else:
            c6['text']="X"
            ver("X")
            t=1
def sept():
    global t
    if c7['text']==''and run ==True:
        if t==1:
            c7['text']='0'
            ver("0")
            t=2
        else:
            c7['text']="X"
            ver("0")
            t=1
def huit():
    global t
    if c8['text']==''and run ==True:
        if t==1:
            c8['text']='0'
            ver("0")
            t=2
        else:
            c8['text']="X"
            ver("X")
            t=1
def neuf():
    global t
    if c9['text']==''and run ==True:
        if t==1:
            c9['text']='0'
            ver("0")
            t=2
        else:
            c9['text']="X"
            ver("X")
            t=1
res=Label(text="result:")
c1=Button(width=5,height=2,command=un)
c2=Button(width=5,height=2,command=deux)
c3=Button(width=5,height=2,command=trois)
c4=Button(width=5,height=2,command=quatre)
c5=Button(width=5,height=2,command=cinq)
c6=Button(width=5,height=2,command=six)
c7=Button(width=5,height=2,command=sept)
c8=Button(width=5,height=2,command=huit)
c9=Button(width=5,height=2,command=neuf)
res.place(relx=0.3,rely=0.0)
c1.place(relx=0.1,rely=0.1)
c2.place(relx=0.4,rely=0.1)
c3.place(relx=0.7,rely=0.1)
c4.place(relx=0.1,rely=0.4)
c5.place(relx=0.4,rely=0.4)
c6.place(relx=0.7,rely=0.4)
c7.place(relx=0.1,rely=0.7)
c8.place(relx=0.4,rely=0.7)
c9.place(relx=0.7,rely=0.7)
win.mainloop()