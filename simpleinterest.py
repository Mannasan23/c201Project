from cProfile import label
from cgitb import text
from tkinter import *

window=Tk()

def calculateInterest():
    amount = int(input_amount.get())
    rate = int(input_rate.get())
    time = int(input_time.get())
    name = input_name.get()

    s_interest = (amount*time*rate)/100
    s_interest = round(s_interest, 1)
    result_label.destroy()
    
    output_msg = Label(result_frame, text = name + ", your Simple Interest is " + str(s_interest), bg = "lightcyan", fg = "black", 
    font = ("Calibri", 12), width = 42)
    output_msg.place(x = 20, y = 40)
    output_msg.pack()


window.title("Simple Interest Calculator")
window.geometry("380x400")
window.configure(bg = "lightcyan")

app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label = Label(window, text = "Name", fg = "black", bg = "lightcyan", font = ("Calibri", 12), bd = 1)
name_label.place(x=20, y=90)

input_name = Entry(window, text = "", bd = 2, width = 22)
input_name.place(x=150, y=92)

result_frame = LabelFrame(window, text="Result", bg = "lightcyan", font = ("Calibri", 12))
result_frame.pack(padx= 20, pady= 20)
result_frame.place(x = 20, y = 300)

result_label=Label(window, text="", bg = "lightcyan", font=("Calibri", 12), width = 33)
result_label.place(x=20, y=20)
result_label.pack()

amount_label = Label(window, text = "Amount (₹)", fg = "black", bg = "lightcyan", font = ("Calibri", 20), bd = 1)
amount_label.place(x = 20, y = 185)

rate_label = Label(window, text = "Rate (%)", fg = "black", bg = "lightcyan", font = ("Calibri", 20), bd = 1)
rate_label.place(x = 20, y = 140)

time_label = Label(window, text = "Time (in years)", fg = "black", bg = "lightcyan", font = ("Calibri", 20), bd = 1)
time_label.place(x = 20, y = 250)

input_amount = Entry(window, text = "", bd = 2, width = 15)
input_amount.place(x = 150, y = 187)

input_rate = Entry(window, text = "", bd = 2, width = 15)
input_rate.place(x = 150, y = 142)

input_time = Entry(window, text = "", bd = 2, width = 15)
input_time.place(x = 150, y = 250)

calculate_button = Button(window, text = "Calculate", fg = "Red", bg = "lightcyan", bd = 4, command = calculateInterest)
calculate_button.place(x = 20, y = 350)


window.mainloop()