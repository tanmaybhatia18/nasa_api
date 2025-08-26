import tkinter as tk
def presskey(k):
    if k=='=':
         calculate()
    else:
        entry_var.set(entry_var.get()+str(k))
def calculate():
    try:
        result=str(eval(entry_var.get()))
        entry_var.set(result)
    except Exception:
        entry_var.set('error')
def clear():
    entry_var.set('')
win=tk.Tk()
win.title('calculator')
win.geometry('400x400')
win.resizable(False,False)
entry_var=tk.StringVar()
entry=tk.Entry(win,textvariable=entry_var,font=('Arial',25),bd=10,relief='sunken',justify='right')
entry.pack(fill='both',ipadx=8,ipady=8,padx=10,pady=10)
buttons=[
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']]
for row in buttons:
    frame=tk.Frame(win)
    frame.pack(expand=True,fill='both')
    for btn in row:
            b=tk.Button(frame,text=btn,font=('Arial',18),
command=lambda x=btn: presskey(x))
            b.pack(side='left',expand=True,fill='both')
clear_button=tk.Button(win,text='c',font=('Arial',20),command=clear,bg='white',fg='red')
clear_button.pack(expand=True,fill='both',padx=10,pady=5)
win.mainloop()
