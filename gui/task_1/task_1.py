import tkinter as tk
from tkinter import Button, messagebox
from tkcalendar import DateEntry
from datetime import date


def make_date(date_):
    current_year = int(str(date.today())[1:4])
    # 2 / 1 / 23
    date_ = str(date_).split('/')

    day = int(date_[1])
    month = int(date_[0])
    year = int(int(date_[2]) + 2000 if int(date_[2]) < current_year else int(date_[2]) + 1000)
    return [year, month, day]


def get_age(year, month, day):
    print(month)
    birth_date = date(year, month, day)
    today = date.today()

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


window = tk.Tk()
window.title('Calculation age')
window.geometry('500x500')

dob_label = tk.Label(window, text='DOB : ', padx=20, pady=3)
dob_label.place(x=100, y=100)
dob_entry = DateEntry(window)
dob_entry.place(x=180, y=100)


def get_result():
    date_ = dob_entry.get()
    dob = make_date(date_)
    year = dob[0]
    month = dob[1]
    day = dob[2]
    print(month)
    age = get_age(year, month, day)
    messagebox.showinfo('Information', f'Your age : {age}')


# Age button
age_button = Button(window, text='Result', padx=20, pady=3, command=get_result)
age_button.place(x=140, y=200)

# Exit button
exit_button = Button(window, text="Exit", padx=20, pady=3, command=window.quit)
exit_button.place(x=240, y=200)

if __name__ == '__main__':
    window.mainloop()
