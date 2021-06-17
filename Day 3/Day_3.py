from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Employees Details")
window.geometry('500x400')
window.configure(background = "blue");

Firstname = Label(window ,text = "First Name").grid(row = 5,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 6,column = 0)
Gender =Label(window ,text = "Gender").grid(row = 7,column = 0)
var = IntVar()
Radiobutton(window, text="Male",padx = 18, variable=var, value=1,).grid(row = 7,column = 1)
Radiobutton(window, text="Female",padx = 18, variable=var, value=2).grid(row = 7,column = 2)
Email = Label(window ,text = "Email Id").grid(row = 8,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 9,column = 0)
Address = Label(window ,text = "Address").grid(row = 10,column = 0)
City = Label(window ,text = "City").grid(row = 11,column = 0)
State= Label(window ,text = "State").grid(row = 12,column = 0)
Country = Label(window ,text = "Country").grid(row = 13,column = 0)
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(window,c, *list1)
droplist.config(width=22)
c.set('SELECT YOUR COUNTRY')
droplist.grid(row = 13,column = 1)
label_12 = Label(window, text="Programming").grid(row = 14,column = 0)
var1 = IntVar()
Checkbutton(window, text="Java", variable=var1).grid(row = 14,column = 1)
var2 = IntVar()
Checkbutton(window, text="Python", variable=var2).grid(row = 14,column = 2)

Firstname1 = Entry(window).grid(row = 5,column = 1)
Lastname1 = Entry(window).grid(row = 6,column = 1)
Email1 = Entry(window).grid(row = 8,column = 1)
Mobile1 = Entry(window).grid(row = 9,column = 1)
Adderss1=Entry(window).grid(row = 10,column = 1)
city1=Entry(window).grid(row = 11,column = 1)
state1=Entry(window).grid(row = 12,column = 1)


#fubction declaration
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=30,column=1)
window.mainloop()
