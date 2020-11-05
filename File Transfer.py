

import tkinter   #tkniter is a module for python 
from tkinter import *
import shutil   #a module that moves and copies files for python 
import os       # a module that interacts with the Operating system
from datetime import datetime, timedelta  #this dates odjects 
from tkinter import filedialog



class ParentWindow(Frame):        #tkinter part of the GUI and frame widget and is used to group widgets together
    def __init__ (self, master):          #def equals to a function. __init__  is inheritance / self is the glue for everything to stick together (it binds the attributes together) 
        Frame.__init__ (self)            #everything that is inside this frame inherits the 

        self.master = master           #GUI master window
        self.master.resizable(width=True, height=True)   #this is for if the user can resize the window or not 
        self.master.geometry('{}x{}'.format (700, 400))     #is the actual load size of the new window
        self.master.title('Check Files ')                            #this is the title of the GUI
        self.master.config(bg='lightgray')                         #background color of the window


        self.varBrowse = StringVar()                              #what type of data is entered into the entry field
        self.varBrowse1 = StringVar()                             #same thing as above

        self.lblBrowse = Button(self.master,text='Browse... ',font=("Helvetica", 12), fg='Black', bg='lightgray', command=self.src_directory)    #wording on top of the button
        self.lblBrowse.grid(row=0, column=0, padx=(30,0), pady=(30,0))           #where the button is placed on the grid system and how much padding is around them 

        self.lblBrowse1 = Button(self.master,text='Browse... ',font=("Helvetica", 12), fg='Black', bg='lightgray', command=self.src_directory1) #wording on top of the button
        self.lblBrowse1.grid(row=1, column=0, padx=(30,0), pady=(30,0))   #where the button is placed on the grid system and how much padding is around them 

        self.lblDisplay = Label(self.master,text='',font=("Helvetica", 16), fg='white', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtBrowse = Entry(self.master, text=self.varBrowse, font=("Helvetica", 16), fg='black', bg='white') #entry field color and size and placement 
        self.txtBrowse.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtBrowse1 = Entry(self.master, text=self.varBrowse1, font=("Helvetica", 16), fg='black', bg='white')   #entry field color and size and placement 
        self.txtBrowse1.grid(row=1,column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Check for files...", width=15, height=2, command=self.submit)   #check files for any modifcations in the last 24 hours  
        self.btnSubmit.grid(row=2,column=0, padx=(30,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=self.cancel)        #closes program window
        self.btnCancel.grid(row=2,column=2, padx=(30,90), pady=(30,0), sticky=NE)

    def src_directory(self): #function for the source directory 
       src = filedialog.askdirectory() #this creates a variable to which the user's selection will be stored

       self.txtBrowse.delete(0, END)     #deletes whats there in the entry field
       self.txtBrowse.insert(0, src)         # allows data to be entered

    def src_directory1(self): #function for the source directory 
       src = filedialog.askdirectory() #this creates a variable to which the user's selection will be stored

       self.txtBrowse1.delete(0, END) #deletes whats there in the entry field
       self.txtBrowse1.insert(0, src)        # allows data to be entered
                                                      
    def submit(self):                           #defines the submit function when pushed 
       path = self.txtBrowse.get()           # this is the variable for the first browse button get function
       path2 = self.txtBrowse1.get()         # this is the variable for the first browse button get function
       dir_list = os.listdir(path)                 # first dir_list is the variable for os.listdir which gets all files and directories from PATH,
       for file in dir_list:                          #for loop that is iterating over the dir_list which is the variable for PATH
         absolutepath = os.path.join(path,file)     #this is the absolutepath to the first browse button to choose which folder to use for the files
         mod_time = os.path.getmtime(absolutepath) #this displays when the last modification to the file was
         last24hours_date_time = datetime.now() - timedelta(hours = 24)   #this tells the program how far back to look in this case it is 24 hours 
         modify_time = datetime.fromtimestamp(mod_time)  #compares the modify time with the actual time
         
         if last24hours_date_time <= modify_time: # compares the modify times and sorts the ones that are LESS than 24 hours old
            
            shutil.move(absolutepath,path2)        #this moves the files that are less than 24hrs to the destination folder
           

    def cancel(self):                #Ends the program 
        self.master.destroy()
            



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
