from tkinter import *
rc = '#FE0808'
bc = '#0831FE'
gc = '#53AD00'
yc = '#FDC701'

root=Tk()
cc = 'None'
def red():
    root.configure(bg=rc)
    l1.config(text="hello")
def blue():
    root.configure(bg=bc)
def green():
    root.configure(bg=gc)
def yellow():
    root.configure(bg=yc)




root.geometry('300x130+200+200')
rb1 = Button(root,text='Vermelho',width=20, height=3,command=red).grid(column=0,row=0)
bb1 = Button(root,text='Azul',width=20, height=3,command=blue).grid(column=0,row=1)
gb1 = Button(root,text='Verde',width=20, height=3,command=green).grid(column=1,row=0)
yb1 = Button(root,text='Amarelo',width=20, height=3,command=yellow).grid(column=1,row=1)
text = tk.StringVar()
text.set("Hello World!")
label = tk.Label(gui, textvariable=text).grid(column=0,row=2)
label.pack(pady=20)

#l1 = Label(root,text=cc).grid(column=0,row=2)



root.mainloop()
