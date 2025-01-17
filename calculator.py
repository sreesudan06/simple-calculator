from tkinter import * # import all the components of the Tkinter module into your py script.
import tkinter as tk
root=tk.Tk()
root.title("calculator")
root.geometry("357x420")
root.resizable(False,False)

cal=Label(root,width=35,height=2,text="",font=("arial,30"),bg="light yellow")
cal.pack()

equation=""

def display(value):
    global equation
    equation+=value
    cal.config(text=equation)

def delete():
    global equation
    equation=""
    cal.config(text=equation)    

def evaluate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="ERROR!"
            
        
    cal.config(text=result)
    

# displayig buttons
Button(root,text="(",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("(")).place(x=0,y=50)
Button(root,text=")",width=11,height=4, font=("arial",8,"bold"),command=lambda:display(")")).place(x=90,y=50)
Button(root,text="%",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("%")).place(x=180,y=50)
Button(root,text="/",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("/")).place(x=270,y=50)
Button(root,text="1",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("1")).place(x=0,y=125)
Button(root,text="2",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("2")).place(x=90,y=125)
Button(root,text="3",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("3")).place(x=180,y=125)
Button(root,text="+",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("+")).place(x=270,y=125)
Button(root,text="4",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("4")).place(x=0,y=200)
Button(root,text="5",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("5")).place(x=90,y=200)
Button(root,text="6",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("6")).place(x=180,y=200)
Button(root,text="-",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("-")).place(x=270,y=200)
Button(root,text="7",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("7")).place(x=0,y=275)
Button(root,text="8",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("8")).place(x=90,y=275)
Button(root,text="9",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("9")).place(x=180,y=275)
Button(root,text="x",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("*")).place(x=270,y=275)
Button(root,text="c",width=11,height=4, font=("arial",8,"bold"),bg="light yellow",command=lambda:delete()).place(x=0,y=350)
Button(root,text="0",width=11,height=4, font=("arial",8,"bold"),command=lambda:display("0")).place(x=90,y=350)
Button(root,text=".",width=11,height=4, font=("arial",8,"bold"),command=lambda:display(".")).place(x=180,y=350)
Button(root,text="=",width=11,height=4, font=("arial",8,"bold"),bg="light yellow",command=lambda:evaluate()).place(x=270,y=350)

    
    

#icon
#image_icon=PhotoImage(file="image/calculator.png")
#root.iconphoto(False,image_icon)

root.mainloop()
