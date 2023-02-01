import csv
import tkinter as tk
import os
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar
from student_class import Student
from datetime import datetime
from tkcalendar import DateEntry

window = tk.Tk()
window.title('p10')
window.geometry('500x500')

students = []


def read_csv_file():
    with open('students.csv') as file:
        csc_reader = csv.DictReader(file)
        result = [row for row in csc_reader]
        messagebox.showinfo("All Information" , f'{result}')

def add():
    student = Student(
        full_name_entry.get(),
        email_entry.get(),
        dob_entry.get(),
        gender.get(),
        phone_entry.get(),
        course_entry.get(),
        datetime.now()
    )
    students.append(student.get_attrs(as_dict=True))
    messagebox.showinfo('Information', 'The data has been added successfully')


def save():
    with open('students.csv', 'a', newline='\n') as file:
        header = ['Fullname', 'Email', 'DOB', 'Gender', 'Phone', 'Course', 'DOJ']
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize('students.csv') == 0:
            csv_writer.writeheader()
        print(students)
        csv_writer.writerows(students)
        messagebox.showinfo('Information', 'Saved successfully')


def clear():
    full_name_entry.delete(0, END)
    email_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    course_entry.delete(0, END)


# Full name label and entry
full_name_label = tk.Label(window, text='Full Name : ', padx=20, pady=10)
full_name_label.place(x=100, y=95)
full_name_entry = tk.Entry(window, width=30, borderwidth=3)
full_name_entry.place(x=200, y=100)

# Email label and entry
email_label = tk.Label(window, text='Email : ', padx=20, pady=10)
email_label.place(x=100, y=130)
email_entry = tk.Entry(window, width=30, borderwidth=3)
email_entry.place(x=200, y=135)

# DOB label and entry
dob_label = tk.Label(window, text='DOB : ', padx=20, pady=10)
dob_label.place(x=100, y=165)
dob_entry = DateEntry(window)
dob_entry.place(x=200, y=170)

# Gender
gender = StringVar()
GENDER_TYPES = {'m': 'Male', 'f': 'Female'}
gender_label = tk.Label(window, text='Gender : ', padx=20, pady=10)
gender_label.place(x=100, y=200)
male_radio_button_entry = tk.Radiobutton(
    window, text=GENDER_TYPES.get('m'), value='Male', variable=gender
)
male_radio_button_entry.place(x=190, y=210)

female_radio_button_entry = tk.Radiobutton(
    window, text=GENDER_TYPES.get('f'), value='Female', variable=gender
)
female_radio_button_entry.place(x=270, y=210)

# Phone label and entry
phone_label = tk.Label(window, text='Phone : ', padx=20, pady=10)
phone_label.place(x=100, y=245)
phone_entry = tk.Entry(window, width=30, borderwidth=3)
phone_entry.place(x=200, y=245)

# Course label and entry
course_label = tk.Label(window, text='Course : ', padx=20, pady=10)
course_label.place(x=100, y=280)
course_entry = tk.Entry(window, width=30, borderwidth=3)
course_entry.place(x=200, y=280)

# Save button
save_button = Button(window, text='Save', padx=20, pady=10, command=save)
save_button.place(x=110, y=330)

# Add button
add_button = Button(window, text='Add', padx=20, pady=10, command=add)
add_button.place(x=200, y=330)

# Clear button
clear_button = Button(window, text='Clear', padx=20, pady=10, command=clear)
clear_button.place(x=290, y=330)

# Exit button
exit_button = Button(window, text='Exit', padx=20, pady=10, command=window.quit)
exit_button.place(x=380, y=330)

all_info_button = Button(window, text='Show All Information', padx=40, pady=10,command=read_csv_file)
all_info_button.place(x=170, y=380)

if __name__ == '__main__':
    window.mainloop()
