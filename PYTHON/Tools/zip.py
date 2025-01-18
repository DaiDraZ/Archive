import shutil
from tkinter import *
from tkinter import filedialog
import time


master = Tk()

master.title('Zip file')
master.geometry('600x400')

master.minsize(400, 300)
path1 = StringVar()
path2 = StringVar()



def browseFiles1():
    filename = filedialog.askdirectory()
    path1.set(filename)                                      

                                                       
    # Change label contents
    return filename





def zip():
    shutil.make_archive(box1.get(), 'zip',root_dir=box1.get())
    path2.set('PATH ZIP : ' + box1.get() + '.zip')
    print(time.perf_counter())
lb = Label(master,text='ZIP FILE').grid(column=2)


lb1 = Label(master, text='folder path to zip: ').grid(row=1, column=1)
box1 = Entry(master, textvariable=path1)
box1.grid(row=1, column=2, ipadx=100)
btn1 = Button(master, text='browse', command=browseFiles1).grid(row=1, column=3, padx=10)


lb2 = Label(master, textvariable=path2)
path2.set('PATH ZIP : ')
lb2.grid(row=3, column=2)




btn3 = Button(master, text='Zip',command=zip).grid(row=2, column=2)
master.mainloop()
