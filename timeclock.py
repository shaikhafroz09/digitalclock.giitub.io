import time
from tkinter import *

root=Tk()
root.title('Digital Clock')
root.geometry('400x300')
root.config(bg='gray')

def clock():
    hour= time.strftime('%H')
    minute=time.strftime('%M')
    second=time.strftime('%S')

    my_label.config(text=hour + ':' + minute + ':' + second)
    my_label.after(1000,clock)

my_label=Label(root,text="",font=('Helvetica',48),fg='red',bg='black')
my_label.pack(pady=30)

clock()
root.mainloop()