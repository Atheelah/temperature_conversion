import tkinter as tk
from tkinter import messagebox, INSERT

window = tk.Tk()
window.geometry("550x400")
window.config(bg='pink')
window.resizable(height=False, width=False)
window.title("Temperature Converter")

#Celcius and Fahrenheit frame
label1_FC = tk.LabelFrame(window, text="Celcius to Fahrenheit")
label1_FC.place(x=50, y=60, height=120, width=210)
label2_CF = tk.LabelFrame(window, text="Fahrenheit to Celcuis")
label2_CF.place(x=300, y=60, height=120, width=210)


#Entry boxes
celcius_entry = tk.Entry(label1_FC, bg="beige", fg="black")
celcius_entry.place(x=40, y=40, width=100)
fahrenheit_entry = tk.Entry(label2_CF, bg='beige', fg='black')
fahrenheit_entry.place(x=40, y=40, width=100)

#Conversion Box
converbox = tk.Entry(window, state="readonly")
converbox.place(x=170, y=300, height=50, width=200)

#CELCIUS BUTTON AND FUNCTION
def activate1():
    celcius_entry.config(state = "normal")
    fahrenheit_entry.config(state = "readonly")
button1= tk.Button(window, text="Activate Celcius to Fahrenheit", fg='black', border=4, bg="grey", command = activate1)
button1.place(x=40, y=200)

#FAHRENHEIT BUTTON AND FUNCTION
def activate2():
    fahrenheit_entry.config(state = "normal")
    celcius_entry.config(state = "readonly")
button2= tk.Button(window, text="Activate Fahrenheit to Celcius", fg='black', border=4, bg="grey", command = activate2)
button2.place(x=300, y=200)

#EXIT BUTTON AND FUNCTION
def exiting():

    message = messagebox.askquestion("Exit Application", "Are you sure you want to exit?", icon = "warning")
    if message == 'yes':
        window.destroy()
    else:
        tk.messagebox.showinfo('Return', 'Returning to the application screen')

btnexit = tk.Button(window, text="Exit Program", border=4, bg="grey", command = exiting)
btnexit.place(x=435, y=335)


#Clear button & function
def clear():
    celcius_entry.delete(0,tk.END)
    fahrenheit_entry.delete(0, tk.END)
    converbox.delete(0,tk.END)

btnclear = tk.Button(window, text="Clear", border=4, bg="grey", command = clear) #still add command
btnclear.place(x=435, y=300)

#CONVERSION BUTTON AND FUNCTION
def conversion():
    if celcius_entry['state'] == "normal" :
        try:
            fahrenheit_entry.delete(0,tk.END)
            converbox.delete(0,tk.END)
            convert1 = float(celcius_entry.get())*1.8 + 32
            converbox.config(state = 'normal')
            converbox.insert(INSERT, str(round(convert1,1)))
        except ValueError:

          messagebox.showinfo("Error", "Incorrect value entered, Please enter valid input")
          celcius_entry.delete(0, tk.END)
    elif fahrenheit_entry['state'] == "normal":
        try:

           celcius_entry.delete(0, tk.END)
           converbox.delete (0, tk.END)
           convert2 = ((float(fahrenheit_entry.get())) - 32) * (5 / 9)
           converbox.config(state="normal")
           converbox.insert(INSERT, str(round(convert2,1)))
        except ValueError:
           messagebox.showinfo("Error", "Incorrect value entered, Please enter valid input")
           fahrenheit_entry.delete(0, tk.END)

btnConv = tk.Button(window, text="Calculate Conversion", border=4, bg='grey', command = conversion) #still add a command
btnConv.place(x=0, y=310)

window.mainloop()
