import tkinter as tk

window = tk.Tk()

window.title('P10 registration')
window.geometry('600x700')
# text = tk.Label(window, text='hello pdp')
# text.place(x=100, y=100)



# label.place(x=100, y=20)
name_entry = tk.Entry(window, width=20)



# name_entry.place(x=190, y=20)
name_entry.grid(row=2, column=3)

if __name__ == '__main__':
    window.mainloop()
