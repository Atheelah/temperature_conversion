import tkinter as tk
from tkinter import messagebox, INSERT

window = tk.Tk()
window.geometry("550x350")
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

#buttons for Celcius and Fahrenheit
button1= tk.Button(window, text="Activate Celcius to Fahrenheit", fg='black', border=4) #still add command
button1.place(x=40, y=200)
button2= tk.Button(window, text="Activate Fahrenheit to Celcius", fg='black', border=4)
button2.place(x=300, y=200)

#conversion button
btnConv = tk.Button(window, text="Calculate Conversion", border=4) #still add a command
btnConv.place(x=0, y=310)

#clear and exit button
btnclear = tk.Button(window, text="Clear", border=4) #still add command
btnclear.place(x=435, y=300)
btnexit = tk.Button(window, text="Exit Program", border=4) #still add command
btnexit.place(x=435, y=335)


window.mainloop()
