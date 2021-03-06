from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile, askopenfilename
import os
import datetime

file_name = NONE
path = 'C:/Notes/'

root = Tk()
root.title('Notes')
root.geometry('600x300')

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label='File', menu=file_menu)

root.config(menu=menu_bar)

text = Text(root, width=600, height=300)
text.insert(INSERT, "Hi, I am Note, clear this note or File->New")
text.pack()

try:
    directory = 'Notes'
    os.chdir('C:/')
    os.mkdir(directory)
except:
    #os.chdir(path)
    pass

def save():
    summary = text.get('1.0', END)
    d = datetime.date.today()
    summary = summary[:15].rstrip() + str(d.year) + ' ' + str(d.month) + ' ' + str(d.day)
    data = text.get('1.0', END)
    file = open(f"C:/Notes/{summary}.txt", "w")
    file.write(data)
    file.close()
    messagebox.showinfo('Save', 'File saved, path: C:/Notes/')

def open_file():
    global file_name
    inp = askopenfile(mode='r', initialdir='C:/Notes/')
    if inp is not NONE:
        file_name = inp.name
        text.delete('1.0', END)
        data = inp.read()
        text.insert('1.0', data)

def save_as():
    out = asksaveasfile(mode='w', filetypes=[('Word', '.docx'), ('Word 97–2003', '.doc'),
                                             ('txt', '.txt'), ('Web', '.html')], initialdir='C:/Notes/')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror('Error', 'File was not saved')

def new_file():
    global file_name
    file_name = 'No Name'
    text.delete('1.0', END)

def browseFiles():
    filename = askopenfilename(initialdir = 'C:/Notes/', title = "Select a File",
                                filetypes = (("Text files",
                                "*.txt*"), ("all files", "*.*")))

file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save as...', command=save_as)
file_menu.add_command(label='Save', command=save)
file_menu.add_command(label='Browse', command=browseFiles)

root.mainloop()
