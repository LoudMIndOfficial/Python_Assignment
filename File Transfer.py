

import tkinter
from tkinter import *
import shutil
import os
import time

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format (700, 400))
        self.master.title('Check Files ')
        self.master.config(bg='lightgray')


        self.varFName = StringVar()
        self.varLName = StringVar()

        self.lblFName = Button(self.master,text='Browse... ',font=("Helvetica", 12), fg='Black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLName = Button(self.master,text='Browse... ',font=("Helvetica", 12), fg='Black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='',font=("Helvetica", 16), fg='white', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='white')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='white')
        self.txtLName.grid(row=1,column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Check for files...", width=15, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=0, padx=(30,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=2, padx=(30,90), pady=(30,0), sticky=NE)

    def askdirectory(self):
          """Returns a selected directoryname."""

    print(tkFileDialog.askdirectory(self.path))

      

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lbl.Display.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()
            
path = '/Users/Jerem/Desktop/FolderA/'
dir_list = os.listdir(path)
print(os.path.join(path, "*.txt"))
print("Files and directories in '", path, "' :")

print(dir_list)



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
