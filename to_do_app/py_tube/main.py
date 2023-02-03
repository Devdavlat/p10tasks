import tkinter as tk
import pytube as py


def downloader():
    print("here")
    url = py.YouTube(str(entry.get()))

    video = url.streams.first()
    video.download()



window = tk.Tk()
window.title('P10 youtube downloader')
window.geometry('500x300')
text_label = tk.Label(window, text='you tube video downloader', font='arial 16')
text_label.pack()

link = tk.StringVar()
entry = tk.Entry(window)
entry.pack()

download = tk.Button(window, text='download', command=downloader)
download.pack()

window.mainloop()
