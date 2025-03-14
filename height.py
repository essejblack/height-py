from tkinter import Tk,Button,Label,DoubleVar,Entry

window = Tk()
window.title("Feet To Meter Conversion App")
window.configure(background="#d9d9d9")
window.geometry("300x300")
window.resizable(False,False)


ft_lbl = Label(window,text="Feet",bg="purple",width=14,fg="white")
ft_lbl.grid(column=0,row=0,padx=10,pady=10)

ft_value = DoubleVar()
ft_entry = Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0,padx=10,pady=10)
ft_entry.delete(0,"end")

mt_lbl = Label(window,text="Meter",bg="purple",width=14,fg="white")
mt_lbl.grid(column=0,row=1,padx=10,pady=10)

mt_value = DoubleVar()
mt_entry = Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1,padx=10,pady=10)
mt_entry.delete(0,"end")

convert_btn = Button(window,text="Convert",bg="green",width=14,fg="white")
convert_btn.grid(column=0,row=2,padx=10,pady=10)


window.mainloop()