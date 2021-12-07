from tkinter import *
from PIL import ImageTk,Image
from tkinter import Text, Tk
from tkinter import filedialog

root = Tk()
root.title("Wage Calculator")
root.geometry("830x500")
root.configure(bg="#222222")

img = PhotoImage(file="images/tiledbackground_intense3.png")
label = Label(root,image=img)
label.place(x=0, y=0)




def wage_calculator():
    hourly_rate = rate.get('1.0', END)
    hours_worked = hours.get('1.0', END)

    rate_calc = float(hourly_rate)
    hours_calc = float(hours_worked)
    if hours_calc <= 40:
        weekly = rate_calc * hours_calc

        yearly = weekly * 52

        monthly = yearly / 12

        overtime_hours = None
        overtime_rate = None
        overtime_pay = None
        
    if hours_calc > 40:
        overtime_hours = hours_calc - 40
        overtime_rate = (rate_calc / 2) + rate_calc
        overtime_pay = overtime_hours * overtime_rate
        
        weekly = (rate_calc * 40) + overtime_pay 
        yearly = weekly * 52
        monthly = yearly / 12 
##    msg0 = "Base hours: " + str(hours_calc - overtime_hours) + "Overtime hours: " + str(overtime_hours) + 
    msg1 = "Hourly rate: " + str(hourly_rate) + "\nHours worked: " + str(hours_worked) + "\nWeekly wage before taxes: " + str(weekly) + "\nMonthly wage before taxes: " + str(monthly) + "\nYearly wage before taxes: " + str(yearly)
    msg2 = "\n" + "-"*30 + "\nOvertime calculations\n Hours of overtime: " + str(overtime_hours) + "\n Overtime rate: " + str(overtime_rate) + "\n Overtime pay: " + str(overtime_pay)
    main_msg = msg1 + msg2
    mainfield.delete('1.0', END)
    mainfield.insert('1.0', main_msg)
    rate.delete('1.0', END)
    rate.insert('1.0', "Hourly Rate")
    hours.delete('1.0', END)
    hours.insert('1.0', "Hours Worked")
    
def max_income():
    
    max_yearly = gross.get('1.0', END)
    try:
        monthly = float(max_yearly) / 12

        weekly = float(max_yearly) / 52

        hourly = float(weekly) / 40
    except:
        pass



    msg1 = "Gross yearly: " + str(max_yearly) + "\nMax montly income: " + str(monthly) + "\nMax weekly income: " + str(weekly) + "\nMax hourly income (40 hour week): " + str(hourly)
    mainfield.delete('1.0', END)
    mainfield.insert('1.0', msg1)
    gross.delete('1.0', END)
    gross.insert('1.0', "Max Yearly")


rate = Text(root,  bg='#333333', fg='#aedbf0', width=13, height=1, borderwidth=1, highlightthickness=1)
rate.config(highlightbackground ='#000000', highlightcolor='#111111')
rate.insert(END, "Hourly Rate")
def callback_rate(event):
    rate.delete("1.0", END)
    return None
rate.bind("<Button-1>", callback_rate)
rate.grid(row=2, rowspan=1, column=1, columnspan=2, padx=20, pady=5)

hours = Text(root,  bg='#333333', fg='#aedbf0', width=13, height=1, borderwidth=1, highlightthickness=1)
hours.config(highlightbackground ='#000000', highlightcolor='#111111')
hours.insert(END, "Hours Worked")
def callback_hours(event):
    hours.delete("1.0", END)
    return None
hours.bind("<Button-1>", callback_hours)
hours.grid(row=3, rowspan=1, column=1, columnspan=2, padx=20, pady=5)

mainfield = Text(root,  bg='#222222', fg='#aedbf0', width=60, height=20, borderwidth=1, highlightthickness=1)
mainfield.grid(row=2, rowspan=2, column=3, columnspan=4, padx=20, pady=5)
mainfield.config(highlightbackground ='#000000', highlightcolor='#111111')
mainfield.insert(END, "Left fields: Calculate your wage based on hours and rate.\nRight field: Breakdown of income by gross yearly income.")
         
gross = Text(root,  bg='#333333', fg='#aedbf0', width=13, height=1, borderwidth=1, highlightthickness=1)
gross.config(highlightbackground ='#000000', highlightcolor='#111111')
gross.insert(END, "Max Yearly")
def callback_gross(event):
    gross.delete("1.0", END)
    return None
gross.bind("<Button-1>", callback_gross)
gross.grid(row=2, rowspan=1, column=7, columnspan=3, padx=10, pady=5)

button_1 = Button(root, bg='#222222', fg='#E2FCFF', activebackground='#333333', activeforeground='#3F7EB3', text="Calculate Wage", padx=30, pady=20, command=lambda: wage_calculator())
button_2 = Button(root, bg='#222222', fg='#E2FCFF', activebackground='#333333', activeforeground='#3F7EB3', text="Calculate Max", padx=30, pady=20, command=lambda: max_income())
button_1.grid(row=4, column=1)
button_2.grid(row=4, column=7)

root.mainloop()
