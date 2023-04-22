from tkinter import *
import random
import pandas as pd 
import openpyxl
import os


#create_password
def create():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    sp_char = "@#$&_-()=%*:/!?+."

    str = lower + upper + numbers + sp_char
   
    password = "".join(random.sample(str,8))
    return password

#save_data_in_excel
def save(plat,email,psw):
    data = {"Platform":[plat],"Email":[email],"Password":[psw]}
    df = pd.DataFrame(data,columns=["Platform","Email","Password"])
    
    if not os.path.isfile("password.xlsx"):
        
        df.to_excel('password.xlsx',index=False,header=True)
    else:
        existing_df = pd.read_excel("password.xlsx")
        new_df = pd.concat([existing_df,df],ignore_index=True)
        new_df.to_excel("password.xlsx",index=False)

        
   
    
    print("successful",os.getcwd())




class psw_mnger(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack(expand=YES,fill=BOTH)
        self.master.title('Password Manager')
        master.geometry("500x200")


        #platform_label
        Label(self,relief=SUNKEN,font='20',text='Platform',width=10,height=1).grid(row=0,column=0,padx=10,pady=10)

        #platform_name_entry
        self.platform_name = StringVar()
        Entry(self,justify=CENTER,relief=SUNKEN,font='20',textvariable=self.platform_name,width=40).grid(row=0,column=2)

        #email_label
        Label(self,relief=SUNKEN,font='20',text='Email',width=10).grid(row=1,column=0,padx=10,pady=10)

        #email_entry
        self.email = StringVar()
        Entry(self,justify=CENTER,relief=SUNKEN,font='20',textvariable=self.email,width=40).grid(row=1,column=2)

        #password_label
        Label(self,relief=SUNKEN,font='20',text='Password',width=10).grid(row=2,column=0,padx=10,pady=10)

        #password_entry
        self.password = StringVar()
        Entry(self,justify=CENTER,relief=SUNKEN,font='20',textvariable=self.password,width=40).grid(row=2,column=2)

        #Load_button
        load_btn = Button(master,text='Load',font='20',command=None,width=10,height=1)
        load_btn.pack(side=LEFT,padx=10)
        

        #create_button
        create_btn = Button(master,text='Create',font='20',command=lambda :self.password.set(create()),width=10,height=1)
        create_btn.pack(side=LEFT,padx=75)

        #save_button
        save_btn = Button(master,text='Save',font='20',width=10,height=1,command=lambda :save(self.platform_name.get(),self.email.get(),self.password.get()))
        save_btn.pack(side=LEFT)
        

          

if __name__ =='__main__':
    root = Tk()
    view = psw_mnger(root)
    view.pack()
    view.mainloop()