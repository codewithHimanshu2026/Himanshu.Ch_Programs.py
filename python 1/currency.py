import tkinter as tk

from tkinter import ttk, messagebox
root = tk.Tk()
#root.state('zoomed')
def convert():
    try:
        amount=float(entry_amount.get())
        from_currency=combo_from.get()
        to_currency=combo_to.get()

        rate={

            "INR":1.00,
            "USD":83.50,
            "AUD":54.80,
            "EUR":90.20,
            "JPY":0.56,
            "CAD":61.10,
            "AED":22.70,
            "SGD":62.00

        }

        if(from_currency==to_currency):
            l5_result.config(text=f"{amount}")
        else:
            amount_in_INR=amount*rate[from_currency]
            result=amount_in_INR/rate[to_currency]
            l5_result.config(text=f"{result:.2f} {to_currency}")


    except:
        messagebox.showerror("Error","Please enter a valid amount")

root.title("Currency converter.")

root.geometry("500x400")
root.resizable(False,False)

l1_title = tk.Label(root,text="currency convertor",font=("times of roman",20),background="#07DAFA",fg="#112233",borderwidth=10)
l1_title.place(x=120,y=20)
#l1_title.pack()

l2_amount=tk.Label(root,text="Enter amount",font=("Times of roman",12,"bold"),background="#00d3ef",fg="#100B0B",borderwidth=5)
l2_amount.place(x=50,y=100)

entry_amount=tk.Entry(root,font=("Times of roman",12,"bold"),width=15,border=2,relief="groove",justify="right",background="#D5D5DC")
entry_amount.place(x=180,y=100)

currency=["INR","USD","AUD","EUR","JPY","CAD","AED","SGD"]

lb_from=tk.Label(root,text="from",font="Arial",background="#00d3ef",fg="#071313",borderwidth=5)
lb_from.place(x=30,y=150)


combo_from=ttk.Combobox(root,values=currency,font=("arial",12,"bold"),state="readonly",width=10)
combo_from.place(x=100,y=150)
combo_from.set("INR")

#2

lb_to=tk.Label(root,text="to",font="Arial",background="#00d3ef",fg="#050909",borderwidth=5)
lb_to.place(x=250,y=150)


combo_to=ttk.Combobox(root,values=currency,font=("arial",12,"bold"),state="readonly",width=10)
combo_to.place(x=300,y=150)
combo_to.set("INR")

button_convert=tk.Button(root,text="convert",command=convert)
button_convert.place(x=200,y=250)

l5_result=tk.Label(root,text="",font="Arial",background="#0617F8",fg="#D4E4E4")
l5_result.place(x=120,y=300)


root.mainloop()