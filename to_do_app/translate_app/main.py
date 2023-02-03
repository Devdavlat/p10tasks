import translate as tr
from translate import Translator
import tkinter as tk
from tkinter import messagebox
from lesson_1.p10tasks.to_do_app.translate_app.languages.languages import choices

languages_list = choices

languages = [language[1] for language in languages_list]

"""
from translate import Translator
In [2]: translator= Translator(to_lang="zh")
In [3]: translation = translator.translate("This is a pen.")
"""


# Translater func


# def make_waring(text):


def translate_text():
    text = text_entry.get()
    language_index = list_box.curselection()
    chosen_lan = int(list(languages_list).pop(language_index)[0])
    if len(text) == 0:
        messagebox.showwarning(title='are you brain', text='write text to translate!')
    else:
        language = Translator(to_lang=f'{list(chosen_lan)[0]}')
        res = language.translate(text)

        new_text_entry = tk.Label(window, text=res)
        new_text_entry.place(x=98, y=25)


window = tk.Tk()
window.title('<<P10>> Translate')

# Text entry
text_entry = tk.Entry(window, width=40)
text_entry.pack()

# List box
list_box = tk.Listbox(window, width=10, height=20, )
list_box.pack(side=tk.LEFT)

# Translate button
translate_button = tk.Button(window, text='Translate', width=50, command=translate_text)
translate_button.pack(side=tk.BOTTOM)

for lan in languages:
    list_box.insert(tk.END, lan)

if __name__ == "__main__":
    window.mainloop()
