import tkinter as tk

def add():
    n1 = int(entry1.get())
    n2 = int(entry2.get())
    result.config(text="sum="+str(n1+n2))

def sub():
    n1 = int(entry1.get())
    n2 = int(entry2.get())
    result.config(text="sub="+str(n1-n2))

window = tk.Tk()
window.title("Tkinter Program Window.")
window.geometry("300x200")

tk.Label(window,text="First Number.").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window,text="second Number.").pack()
entry2 = tk.Entry(window)
entry2.pack()

button_frame = tk.Frame(window)
button_frame.pack()

tk.Button(window,text="add",command=add).pack()
tk.Button(window,text="sub",command=sub).pack()

result=tk.Label(window,text="")
result.pack()

window.mainloop()

