from tkinter import *
import random



#create_password
def create():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    sp_char = "@#$&_-()=%*:/!?+."

    str = lower + upper + numbers + sp_char
    length  = int(input("enter the length of your password! "))
    password = "".join(random.sample(str,8))
    return password

class psw_mnger(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack(expand=YES,fill=BOTH)
        self.master.title('Password Manager')
        master.geometry("850x200")


        #website_label
        Label(self,relief=SUNKEN,font='20',text='Website',width=10,height=1).grid(row=0,column=0,padx=10,pady=10)

        #website_name_entry
        website_name = StringVar()
        Entry(self,relief=SUNKEN,font='20',textvariable=website_name,width=40).grid(row=0,column=2)

        #email_label
        Label(self,relief=SUNKEN,font='20',text='Email',width=10).grid(row=1,column=0,padx=10,pady=10)

        #email_entry
        email = StringVar()
        Entry(self,relief=SUNKEN,font='20',textvariable=email,width=40).grid(row=1,column=2)

        #password_label
        Label(self,relief=SUNKEN,font='20',text='Password',width=10).grid(row=2,column=0,padx=10,pady=10)

        #password_entry
        password = StringVar()
        Entry(self,relief=SUNKEN,font='20',textvariable=password,width=40).grid(row=2,column=2)

        

        #Load_button
        Button(master,text='Load',font='20',command=create,width=10,height=1).pack(side=LEFT,padx=10)

        #create_button
        Button(master,text='Create',font='20',command=create,width=10,height=1).pack(side=LEFT,padx=75)

        #save_button
        Button(master,text='Save',font='20',command=create,width=10,height=1).pack(side=LEFT,padx=10)

          

if __name__ =='__main__':
    root = Tk()
    view = psw_mnger(root)
    view.pack()
    view.mainloop()