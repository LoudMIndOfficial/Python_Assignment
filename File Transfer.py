

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
        self.master.geometry('{}x{}'.format (500, 300))
        self.master.title('File Transfer ')
        self.master.config(bg='Orange')


        self.varFName = StringVar()
      
        self.lblFName = Label(self.master,text='Daily File Check: ',font=("Helvetica", 16), fg='white', bg='Orange')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='',font=("Helvetica", 16), fg='white', bg='Orange')
        self.lblDisplay.grid(row=4, column=1, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightgray')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Browse Files", width=10, height=2, command=self.browse)
        self.btnSubmit.grid(row=2,column=1, padx=(30,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1, padx=(30,90), pady=(30,0), sticky=NE)

    def browse(self):
          l = "/Users/Jerem/Desktop/FolderA/"
          for text in l:
                if(text == ".txt"):
                      break;
          else:
                  print(letter)


                  fn = self.varFName.get()
                  self.lbl.Display.config(text='{}'.())

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
