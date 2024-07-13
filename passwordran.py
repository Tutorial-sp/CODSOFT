import random
import string
from tkinter import * 

password=""
def getpass():

        global password
        length=textbox.get()
        psd=string.ascii_letters

        psd+=string.digits

        psd+=string.punctuation

        for i in range (int(length)):
             password+=random.choice(psd)
        label2.config(text=f"newly generated password is: {password}")     
        
#code for gui

obj=Tk()

obj.configure(bg="lightblue")
space=Label(obj,bg="lightblue")
space.pack(pady=20)
obj.geometry("270x280")
label = Label(obj, text="Enter length of password:")
label.pack(pady=10)

textbox = Entry(obj, width=20)
textbox.pack(pady=10)

submit=Button(obj,text="get password ",command=getpass)
submit.pack(pady=10)

label2 = Label(obj, text="new password is:")
label2.pack(pady=10)


obj.title("password generator")
obj.mainloop()


