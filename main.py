from tkinter import *
from tkinter.font import Font
main = Tk()
main.title("Bitwise Calculator by Group 21")
main.geometry("750x600+250+70")

a = IntVar()
b = IntVar()
c = IntVar()

myfont = Font(size=8, family="Rockwell")

def work():
    global num1
    global num2
    global res
    num1 = a.get()
    num2 = b.get()
    opt1 = c.get()
    if (opt1 == 1):
        res = int(num1 & num2)
        Label(frame, text=res, relief=SUNKEN, font=myfont).place(x=290, y=400)
    elif (opt1 == 2):
        res = int(num1 | num2)
        Label(frame, text=res, relief=SUNKEN, font=myfont).place(x=290, y=400)
    elif (opt1 == 3):
        res = int(not num1)
        Label(frame, text=res, relief=SUNKEN, font=myfont).place(x=290, y=400)
    elif (opt1 == 4):
        res = int(num1 ^ num2)
        Label(frame, text=res, relief=SUNKEN, font=myfont).place(x=290, y=400)

def new():
    ez = Toplevel()
    ez.title("Explanation")
    ez.geometry("600x600+300+80")

    global lol1
    lol1 = PhotoImage(file="")
    Label(ez, image=lol1, relief=SUNKEN).pack()

    fram = Frame(ez, background="ORANGE",borderwidth=25,relief=SUNKEN)
    fram.place(height=600, width=650, x=50, y=70)

    Label(fram, text="Number 1", relief=SUNKEN, font=myfont).place(x=100, y=50)
    Label(fram, text=num1, relief=SUNKEN, font=myfont).place(x=170, y=50)

    Label(fram, text="Number 2", relief=SUNKEN,
          font=myfont).place(x=100, y=100)
    Label(fram, text=num2, relief=SUNKEN, font=myfont).place(x=170, y=100)

    bin1 = f'{num1:04b}'
    bin2 = f'{num2:04b}'

    Label(fram, text="In Binary", relief=SUNKEN,
          font=myfont).place(x=380, y=50)
    Label(fram, text=bin1, relief=SUNKEN, font=myfont).place(x=450, y=50)

    Label(fram, text="In Binary", relief=SUNKEN,
          font=myfont).place(x=380, y=100)
    Label(fram, text=bin2, relief=SUNKEN, font=myfont).place(x=450, y=100)

    bin3 = f'{res:04b}'

    Label(fram, text=bin3, relief=SUNKEN, font=myfont).place(x=450, y=140)
    Label(fram, text="Decimal Result", relief=SUNKEN,
          font=myfont).place(x=240, y=250)

    Label(fram, text=res, relief=SUNKEN, font=myfont).place(x=340, y=250)
    ez.mainloop()

lol = PhotoImage(file="")
Label(main, image=lol, relief=SUNKEN).pack()
frame = Frame(main, bg="#7CCD7C", borderwidth=25, relief=SUNKEN)
frame.place(height=600, width=800, x=25, y=45)

Label(frame, text="Number 1", relief=SUNKEN, font=myfont).place(x=50, y=50)
Entry(frame, textvariable=a, relief=SUNKEN, font=myfont).place(x=110, y=50)

Label(frame, text="Number 2", relief=SUNKEN, font=myfont).place(x=500, y=50)
Entry(frame, textvariable=b, relief=SUNKEN, font=myfont).place(x=560, y=50)

Radiobutton(frame, text="AND", value=1, variable=c,
            relief=SUNKEN, font=myfont).place(x=220, y=150)
Radiobutton(frame, text="OR",    value=2, variable=c,
            relief=SUNKEN, font=myfont).place(x=450, y=150)
Radiobutton(frame, text="NOT", value=3, variable=c,
            relief=SUNKEN, font=myfont).place(x=220, y=220)
Radiobutton(frame, text="XOR", value=4, variable=c,
            relief=SUNKEN, font=myfont).place(x=450, y=220)

Button(frame, text="RESULT", command=work,
       relief=SUNKEN, font=myfont).place(x=270, y=370)
Button(frame, text="EXPLANATION", relief=SUNKEN,
       command=new, font=myfont).place(x=390, y=370)

main.mainloop()
