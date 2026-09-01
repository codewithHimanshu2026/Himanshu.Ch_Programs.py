import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Digital clock")
root.geometry("500x250")
root.resizable(False,False)

title=tk.Label(root,text="Digital clock",font=("Arial",12,"bold"),bg="#20E720",relief="groove",borderwidth=10)
title.place(x=170,y=10)

time_label=tk.Label(root,font=("Arial",15,"bold"),bg="#DB09F7",fg="#F0E5F0",relief="groove",borderwidth=8)
time_label.place(x=190,y=85)

date_label=tk.Label(root,font=("Arial",15,"bold"),bg="#DB09F7",fg="#F0E5F0",relief="groove",borderwidth=8)
date_label.place(x=140,y=150)

def update():
    current_time=strftime("%I:%M:%S: %p")
    current_date=strftime("%A: %d: %B: %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000,update)

update()

root.mainloop()
