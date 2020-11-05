

import tkinter
from tkinter import *
import shutil
import os
from datetime import datetime
import sqlite3

conn = sqlite3.connect('BrowseDB.db')   #creates a database by changing the within the database will be saved in the location of the ".py" file. 

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtbrowse( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileType TEXT \
        )")

col_fileType = ('CopyrightNotice.txt','New Text Document 1.txt','ThirdPartyNotices.txt')

with conn:
    cur = conn.cursor()
    for x in col_fileType:
        if x.endswith(".txt"):
            cur.execute("INSERT INTO tbl_txtbrowse(col_fileType) VALUES(?)",(x,))
    conn.commit()
conn.close()

conn = sqlite3.connect('BrowseDB.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_txtbrowse")
    results = cur.fetchall()
    print(results)
conn.close()

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format (700, 400))
        self.master.title('Check Files ')
        self.master.config(bg='lightgray')


        self.varBrowse = StringVar()
        self.varBrowse1 = StringVar()

        self.lblBrowse = Button(self.master,text='Browse... ',font=("Helvetica", 12), fg='Black', bg='lightgray')
        self.lblBrowse.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblBrowse1 = Button(self.master,text='Browse... ',font=("Helvetica", 12), fg='Black', bg='lightgray')
        self.lblBrowse1.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='',font=("Helvetica", 16), fg='white', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtBrowse = Entry(self.master, text=self.varBrowse, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtBrowse1 = Entry(self.master, text=self.varBrowse1, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse1.grid(row=1,column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Check for files...", width=15, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=0, padx=(30,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=2, padx=(30,90), pady=(30,0), sticky=NE)

    def src_directory(self): #we don't want to name it askdirectory, as that exists in tkinter
       src = tkFileDialog.askdirectory(self.txtBrowse) #this creates a variable to which the user's selection will be stored
       self.txtBrowse.Insert(0, src)

    def src_directory1(self): #we don't want to name it askdirectory, as that exists in tkinter
       src = tkFileDialog.askdirectory(self.txtBrowse1) #this creates a variable to which the user's selection will be stored
       self.txtBrowse1.Insert(0, src)
                                                      
    def submit(self):
       path = self.txtBrowse.get()
       path2 = self.txtBrowse1.get()
       dir_list = os.listdir(path)
       mod_time = os.stat('*.txt').st_mtime
       print(datetime.fromtimestamp(mod_time))
       
       
       print(os.path.join(path, "*.txt"))
       print("Files and directories in '", path, "' :")

       print(dir_list)

      
           

    def cancel(self):
        self.master.destroy()
            



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
