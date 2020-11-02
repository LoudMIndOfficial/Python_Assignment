
import tkinter
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format (625, 200))
        self.master.title('Web Generation Page! ')
        self.master.config(bg='Gray')


        self.varFName = StringVar()

        self.lblFName = Label(self.master,text='Insert Body Text Here: ',font=("Helvetica", 16), fg='white', bg='gray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='',font=("Helvetica", 16), fg='white', bg='gray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightgray')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))
        


        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1, padx=(30,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1, padx=(30,90), pady=(30,0), sticky=NE)

        

        #write-html.py
    def submit(self):
        f = open("Amazing_Summer_Deals.html", "w")


        customText = self.txtFName.get()
        message ="""<html>\
        <head></head>\
        <body> <h1>This IS MY TEXT. <br> THIS IS YOUR TEXT:"+customText+"</h1></body>\
        </html>"""
       
       

        f.write(message)
        f.close()

        webbrowser.open_new_tab("Amazing_Summer_Deals.html")

    def cancel(self):
        self.master.destroy()
            


        
            
                             
        
















if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
