import json
import tkinter as tk
from tkinter import ttk, messagebox
from currency_convert import convert
from requests_and_response import get_requests
from datetime import datetime


def read_json_file():
    with open('currency_short_and_long_name.json') as f:
        names = json.load(f)
        return names


lst_of_long_names = list(read_json_file())


def refresh_data():
    date = datetime.today()
    date = date.strftime('%Y/%m/%d %H:%M:%S')
    with open('update_data.txt', 'w') as f:
        f.write(date)
    get_requests()


def currency_convert():
    # print('convert is work')
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    try:
        int(from_balance_list_box.get())
    except Exception as e:
        pass
    else:
        if from_currency not in lst_of_long_names:
            messagebox.showwarning('are you good', 'enter from currency')
        elif to_currency not in lst_of_long_names:
            messagebox.showwarning('are you good', 'enter to currency')

        else:
            balance = int(from_balance_list_box.get())
            data = read_json_file()
            from_currency = data.get(from_currency)
            to_currency = data.get(to_currency)
            convert_balance = convert(to_currency, from_currency, balance)
            convert_balance_label = tk.Label(window, text='Result balance', width=15, height=1)
            convert_balance_label.place(x=250, y=110)
            convert_balance_list_box = tk.Label(window, text=f'{convert_balance}', width=20, height=1)
            convert_balance_list_box.place(x=250, y=140)


# Create window
window = tk.Tk()
window.title('Currency Converter')
window.geometry('500x300')

with open('update_data.txt') as f:
    data = f.read()
    refresh_data_label = tk.Label(window, text=f'last update date : {data}', padx=10, pady=1)
    refresh_data_label.place(x=160, y=240)

# To currency name
to_currency_label = tk.Label(window, text='From currency')
to_currency_label.place(x=60, y=50)

# From currency
from_currency_label = tk.Label(window, text='To currency')
from_currency_label.place(x=260, y=50)
# from_currency_label.bind('<KeyRelease>', search_by_key)

# Combobox of currency names which is from currency
to_currency_combobox = ttk.Combobox(window, values=lst_of_long_names)
to_currency_combobox.place(x=60, y=80)
# to_currency_combobox.bind('<KeyRelease>', search_by_key)

# Combobox of currency names which is to currency
from_currency_combobox = ttk.Combobox(window, values=lst_of_long_names)
from_currency_combobox.place(x=260, y=80)

# To and From currency search
to_currency_combobox.set('Search')
from_currency_combobox.set('Search')

# Balance entry and label
from_balance_list_box = tk.Entry(window, width=20)
from_balance_list_box.place(x=60, y=135)
from_balance_list_box_label = tk.Label(window, text='Enter balance', padx=10, pady=1)
from_balance_list_box_label.place(x=52, y=110)

# Convert button
converter_button = tk.Button(window, text='Convert', padx=10, pady=1, command=currency_convert)
converter_button.place(x=160, y=200)

# Refresh data
refresh_button = tk.Button(window, text='Refresh data', padx=10, pady=1, command=refresh_data)
refresh_button.place(x=260, y=200)

window.mainloop()
