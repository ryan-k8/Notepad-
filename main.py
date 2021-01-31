from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.font import Font
from tkinter.messagebox import showerror
from tkinter import messagebox

root = Tk()
root.title('Simple Notepad by Ryan')
root.minsize(width=500, height=300)
root.resizable(width=True, height=True)
root.iconbitmap(r"notepad.ico")


def save():
    try:
        with open('note.txt', 'w') as file:
            text = textBox.get("1.0", "end-1c")
            file.write(text)
    except IOError as error:
        showerror(error)


def client_exit():
    exit()


def open_file():
    fname = askopenfilename(filetypes=(("Text files", "*.txt"),
                                       ("HTML files", "*.html;*.htm"),
                                       ("All files", "*.*")))
    with open(fname, 'r') as file:
        textBox.insert(INSERT, file.read())
        textBox.pack()


menu = Menu(root)
root.config(menu=menu)

file = Menu(menu, tearoff=0)
file.add_command(label="Open file", command=open_file)
file.add_command(label="Exit", command=client_exit)
menu.add_cascade(label="File", menu=file)

def about_notepad():
    messagebox.showinfo("Notepad"," NotePad Developed By Ryan in Tkinter GUI (^_^) from tut")


file = Menu(menu, tearoff=0)
menu.add_cascade(label="Help",menu=file)
file.add_command(label="About",command=about_notepad)
fnt = Font(family="Helvetica", size=16)

textBox = Text(root, font=fnt)
textBox.pack()

button = Button(root, height=1, width=10, text="Save", command=save, background='blue')
button.pack()

root.mainloop()
