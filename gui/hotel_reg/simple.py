"""
Mehmonxona registratsiya tizimini ishlab chiqing, bunda uning ismi, yoshi, qayerdan
ekanligi va necha kun qolishligi  qancha pul to'lash kerak ekanligini
ro'yxatga oling, ma'lumotlarni csv faylga saqlab boring.
"""

import csv
import tkinter as tk
import os
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar
from hotel_class import HotelGuest
from datetime import datetime
from tkcalendar import DateEntry

window = tk.Tk()
window.title('<<Welcome to P10 hotel(PDP)>>')
window.geometry('500x500')

tourists_info = []


def read_csv_file():
    with open('tourists.csv') as file:
        csv_reader = csv.DictReader(file)
        result = [row for row in csv_reader]
        messagebox.showinfo("All Information", f"{result}")


# Get price func
def ged_price():
    price_of_per_day = 100
    price = dos_entry.get()
    result = int(price) * price_of_per_day
    messagebox.showinfo("Price", f'{result}$')


def add():
    tourist = HotelGuest(
        full_name_entry.get(),
        age_entry.get(),
        where_entry.get(),
        dos_entry.get(),
        datetime.now()
    )
    tourists_info.append(tourist.get_attrs(as_dict=True))
    messagebox.showinfo('Information', 'The data has been added successfully')


def save():
    with open('tourists.csv', 'a', newline='\n') as file:
        header = ['Fullname', 'DOB', 'Where', 'Date of stay', 'DOJ']
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize('tourists.csv') == 0:
            csv_writer.writeheader()

        csv_writer.writerows(tourists_info)
        messagebox.showinfo('Information', 'Saved successfully')


def clear():
    full_name_entry.delete(0, END)
    age_entry.delete(0, END)
    where_entry.delete(0, END)
    dos_entry.delete(0, END)


# Full name label and entry
full_name_label = tk.Label(window, text='Full Name : ', padx=20, pady=10)
full_name_label.place(x=80, y=95)
full_name_entry = tk.Entry(window, width=30, borderwidth=3)
full_name_entry.place(x=200, y=100)

# Age label and entry
age_label = tk.Label(window, text='Age : ', padx=20, pady=10)
age_label.place(x=80, y=125)
age_entry = tk.Entry(window, width=30, borderwidth=3)
age_entry.place(x=200, y=130)

# Where are you from label and entry
where_label = tk.Label(window, text='Your country : ', padx=20, pady=10)
where_label.place(x=80, y=160)
where_entry = tk.Entry(window, width=30, borderwidth=3)
where_entry.place(x=200, y=165)

# Date of stay label and entry
dos_label = tk.Label(window, text='Date of stay : ', padx=20, pady=10)
dos_label.place(x=80, y=195)
dos_entry = tk.Entry(window, width=30, borderwidth=3)
dos_entry.place(x=200, y=200)

# Save button
save_button = Button(window, text='Save', padx=20, pady=10, command=save)
save_button.place(x=90, y=240)

# Add button
add_button = Button(window, text='Add', padx=20, pady=10, command=add)
add_button.place(x=190, y=240)

# Clear button
clear_button = Button(window, text='Clear', padx=20, pady=10, command=clear)
clear_button.place(x=280, y=240)

# Exit button
exit_button = Button(window, text='Exit', padx=20, pady=10, command=window.quit)
exit_button.place(x=390, y=240)

# All info button
all_info = Button(window, text='Show All Information', padx=40, pady=10, command=read_csv_file)
all_info.place(x=90, y=300)

# get price button
price_button = Button(window, text='Get price', padx=78, pady=10, command=ged_price)
price_button.place(x=90, y=360)

if __name__ == '__main__':
    window.mainloop()
