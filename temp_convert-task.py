from tkinter import*
#Basiclly the format you use when using tkinter.
root =Tk()
root. title("TEMPERATURE CONVERTOR")
root.geometry("700x500+300+300")
#set window color
root.configure(bg='white')

#Border1.
labelframe1 = Frame(root)
labelframe1.pack()

#Border2.
labelframe2 = Frame(root)
labelframe2.pack()

#Variables.
num_1 = IntVar
num_2 = IntVar

#The title of the first border.
labelframe1=LabelFrame(root, text="Degrees Celcuis",padx="40", pady="40", background="light blue")
labelframe1.pack(fill="both")
labelframe1.place(x =100, y = 10)
Cel_entry=Entry(labelframe1, state="disable")
Cel_entry.pack()

#The title of the second border.
labelframe2=LabelFrame(root, text="Degrees Faranheit",padx="40", pady="40", background="light blue")
labelframe2.pack(fill="both")
labelframe2.place(x = 350, y = 10)
Far_entry=Entry(labelframe2, state="disable")
Far_entry.pack()

def active_cel():
    Cel_entry.configure(state="normal",)

cel_convert_btn=Button(root,text="Activate-Celcuis to Faranheit", command=active_cel, background="lightblue")
cel_convert_btn.pack()
cel_convert_btn.place(x = 120, y = 150)
def convert():
    if Cel_entry:
        num1= float(Cel_entry.get())
        num2= (num1*9/5)+32
        answer.insert(0, float(num2))

def convert1():
    if Far_entry:
        num2= float(Far_entry.get())
        num1= (num2 -32)*5/9
        answer.insert(0, float(num1))

def active_cel():
    Far_entry.configure(state="normal")

f_convert_btn=Button(root,text="Activate-Faranheit to Celcuis", command=active_cel, background="lightblue")
f_convert_btn.pack()
f_convert_btn.place(x = 380, y = 150)

#To calculate the num in first frame.
cal_btn=Button(root,text="Calculate Conversion", command=convert, background="darkgrey")
cal_btn.pack(side=LEFT)
cal_btn.place(x = 50, y = 230)

#To calculate the num in second frame
cal_btn1=Button(root,text="Calculate Conversion", command=convert1, background="darkgrey")
cal_btn1.pack(side=LEFT)
cal_btn1.place(x = 50, y = 270)

#Where the answer displays
answer=Entry(root,text="", background="dark grey")
answer.pack()
answer.place(x = 280, y = 230)

#The function to clear everything.
def clear_all_num():
    Cel_entry.delete(0,END)
    Far_entry.delete(0,END)
    answer.delete(0,END)
#The clear button.
clear_btn=Button(text="Clear", command=clear_all_num, background="red")
clear_btn.pack(side=RIGHT)
clear_btn.place(x = 500, y = 350)

#The function to make the exit button work.
def exit_program():
    root.destroy()

#The exit button.
exit_btn=Button(text="Exit" ,command=exit_program, background="red")
exit_btn.pack(side=RIGHT)
exit_btn.place(x = 500, y = 400)

#Have to end with this so that everything in between this is displayed.
root.mainloop()


