from tkinter import *
import datetime


def press(value):
    
    current = entry.get()
    value = str(value)
    if current == "Error":
        entry.delete(0,END)
        current =""
    if current and current[-1] in "+-*/" and value in "+-*/":
        return
    if value == ".":
        last_part = current.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]
        if "." in last_part:
            return
    entry.delete(0,END)
    entry.insert(0,current + str(value))

def clear_entry():
    current = entry.get()
    if not current:
        return
    parts = current.rstrip("0123456789.")
    entry.delete(0,END)
    entry.insert(0,parts)

def calculate():
    try:
        expression = entry.get()
        result = round(eval(expression),5)
        time = datetime.datetime.now().strftime("%H:%M")
        history.append(f"[{time}] {expression} → {result}")
        
        entry.delete(0,END)
        entry.insert(0,result)
        update_history()
    except:
        entry.delete(0,END)
        entry.insert(0,"Error")
        
def clear_all():
    entry.delete(0,END)

def clear_one():
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,current[:-1])

def toggle_sign():
    current = entry.get()
    if current.startswith("-"):
        entry.delete(0,END)
        entry.insert(0,current[1:])
    else:
        entry.delete(0,END)
        entry.insert(0,"-"+current)

def on_enter_num(e):
    e.widget.configure(bg="#3a3a3a")

def on_leave_num(e):
    e.widget.configure(bg=e.widget.original_bg)

def on_enter_op(e):
    e.widget.configure(bg="#ffad33")

def on_leave_op(e):
    e.widget.configure(bg="#ff9500")

def on_enter_eq(e):
    e.widget.configure(bg="#3399ff")

def on_leave_eq(e):
    e.widget.configure(bg="#0078ff")

def on_enter_sc(e):
    e.widget.configure(bg="#6a6a6a")

def on_leave_sc(e):
    e.widget.configure(bg=e.widget.original_bg)

def on_enter_ac(e):
    e.widget.configure(bg="#ff6b6b")

def on_leave_ac(e):
    e.widget.configure(bg=e.widget.original_bg)

def on_press(e):
    e.widget.configure(relief="sunken",bg="#1f1f1f")

def on_release(e):
    e.widget.configure(relief="raised",bg=e.widget.original_bg)

def key_input(event):
    key = event.char
    keysym = event.keysym
    if key in "0123456789":
        press(key)
    elif key in "+-/*":
        press(key)
    elif key == ".":
        press(key)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "Backspace":
        clear_one()
    elif event.keysym == "Escape":
        clear_all()
def update_history():
    history_box.delete(0,END)
    for item in history[-10:]:
        history_box.insert(END,item)
    for i in range(history_box.size()):
        history_box.itemconfig(i,fg="white")
    if history:
        history_box.itemconfig(END,fg="#00ffcc")
def clear_history():
    history.clear()
    history_box.delete(0,END)

def on_click_history(event):
    selection = history_box.curselection()
    if not selection:
        return
    index = selection[0]
    selected_text = history_box.get(index)
    expression = selected_text.split("=")[0].strip()
    expression = expression.replace("x","*").replace("%","/")
    entry.delete(0,END)
    entry.insert(0,expression)


window = Tk()
window.focus_set()
history = []
window.title("Smart Calculator")
window.configure(padx=10,pady=10)
window.resizable(False,False)
bg="#1e1e1e"
window.configure(bg=bg)
window.update()
# window.geometry("500x450")
window.bind("<Key>",key_input)


for i in range(5):
    window.grid_columnconfigure(i,weight=1)

for i in range(6):
    window.grid_rowconfigure(i,weight=1)

entry = Entry(window,bg="white",fg="black",insertbackground="black",width=20,font=("Arial",28,"bold"),bd=5,relief="flat",justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10,sticky="nsew")


button = Button(window,width=6,height=2,text="/",command=lambda:press("/"),font=("Arial",14),bg="#ff9500",fg="white",activebackground="#ffad33")
button.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")
button.original_bg="#ff9500"
button.bind("<Enter>",on_enter_op)
button.bind("<Leave>",on_leave_op)

button = Button(window,width=6,height=2,text="CE",command=clear_entry,font=("Arial",14),bg="#505050",fg="#dddddd",activebackground="#6a6a6a")
button.grid(row=1,column=1,padx=5,pady=5,sticky="nsew")
button.original_bg="#505050"
button.bind("<Enter>",on_enter_sc)
button.bind("<Leave>",on_leave_sc)


button = Button(window,width=6,height=2,text="C",command=clear_one,font=("Arial",14),bg="#444444",fg="#dddddd",activebackground="#6a6a6a")
button.grid(row=1,column=2,padx=5,pady=5,sticky="nsew")
button.original_bg="#505050"
button.bind("<Enter>",on_enter_sc)
button.bind("<Leave>",on_leave_sc)

button = Button(window,width=6,height=2,text="AC",command=clear_all,font=("Arial",14),bg="#d9534f",fg="#dddddd",activebackground="#ff6b6b")
button.grid(row=1,column=3,padx=5,pady=5,sticky="nsew")
button.original_bg="#d9534f"
button.bind("<Enter>",on_enter_ac)
button.bind("<Leave>",on_leave_ac)

button = Button(window,bg="#2d2d2d",fg="white",activebackground="#555555",width=6,height=2,text="7",command=lambda:press("7"),font=("Arial",14))
button.grid(row=2,column=0,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)


button = Button(window,width=6,height=2,text="8",command=lambda:press("8"),font=("Arial",14),bg="#2d2d2d",fg="white",activebackground="#555555")
button.grid(row=2,column=1,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button = Button(window,width=6,height=2,text="9",command=lambda:press("9"),font=("Arial",14),bg="#2d2d2d",fg="white",activebackground="#555555")
button.grid(row=2,column=2,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button = Button(window,width=6,height=2,text="*",command=lambda:press("*"),font=("Arial",14),bg="#ff9500",fg="white",activebackground="#ffad33")
button.grid(row=2,column=3,padx=5,pady=5,sticky="nsew")
button.original_bg="#ff9500"
button.bind("<Enter>",on_enter_op)
button.bind("<Leave>",on_leave_op)

button = Button(window,width=6,height=2,text="4",command=lambda:press("4"),font=("Arial",14),bg="#2d2d2d",fg="white",activebackground="#555555")
button.grid(row=3,column=0,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button = Button(window,width=6,height=2,text="5",command=lambda:press("5"),font=("Arial",14),bg="#2d2d2d",fg="white",activebackground="#555555")
button.grid(row=3,column=1,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button = Button(window,width=6,height=2,text="6",command=lambda:press("6"),font=("Arial",14),bg="#2d2d2d",fg="white",activebackground="#555555")
button.grid(row=3,column=2,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button = Button(window,width=6,height=2,text="-",command=lambda:press("-"),font=("Arial",14),bg="#ff9500",fg="white",activebackground="#ffad33")
button.grid(row=3,column=3,padx=5,pady=5,sticky="nsew")
button.original_bg="#ff9500"
button.bind("<Enter>",on_enter_op)
button.bind("<Leave>",on_leave_op)

button = Button(window,width=6,height=2,text="1",command=lambda:press("1"),font=("Arial",14),bg="#2d2d2d",fg="white",activebackground="#555555")
button.grid(row=4,column=0,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button = Button(window,width=6,height=2,text="2",command=lambda:press("2"),font=("Arial",14),bg="#2d2d2d",fg="white",activebackground="#555555")
button.grid(row=4,column=1,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button = Button(window,width=6,height=2,text="3",command=lambda:press("3"),font=("Arial",14),bg="#2d2d2d",fg="white",activebackground="#555555")
button.grid(row=4,column=2,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button = Button(window,width=6,height=2,text="+",command=lambda:press("+"),font=("Arial",14),bg="#ff9500",fg="white",activebackground="#ffad33")
button.grid(row=4,column=3,padx=5,pady=5,sticky="nsew")
button.original_bg="#ff9500"
button.bind("<Enter>",on_enter_op)
button.bind("<Leave>",on_leave_op)

button = Button(window,width=6,height=2,text="+/-",command=toggle_sign,font=("Arial",14),bg="#3d5a80",fg="white")
button.grid(row=5,column=0,padx=5,pady=5,sticky="nsew")


button = Button(window,width=6,height=2,text="0",command=lambda:press("0"),font=("Arial",14),bg="#2d2d2d",fg="white",activebackground="#555555")
button.grid(row=5,column=1,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button = Button(window,width=6,height=2,text=".",fg="white",bg="#2d2d2d",command=lambda:press("."),font=("Arial",14))
button.grid(row=5,column=2,padx=5,pady=5,sticky="nsew")
button.original_bg="#2d2d2d"
button.bind("<Enter>",on_enter_num)
button.bind("<Leave>",on_leave_num)

button1 = Button(window,bg="#0078ff",fg="white",width=6,height=2,text="=",command=calculate,font=("Arial",14),activebackground="#3399ff")
button1.grid(row=5,column=3,padx=5,pady=5,sticky="nsew")
button1.original_bg="#0078ff"
button1.bind("<Enter>",on_enter_eq)
button1.bind("<Leave>",on_leave_eq)

history_box = Listbox(window,height=10,width=25,bg="#1e1e1e",fg="white",font=("Consolas",12),bd=0)
history_box.grid(row=0,column=4,rowspan=6,padx=10,pady=10,sticky="nsew")
history_box.bind("<<ListboxSelect>>",on_click_history)
history_box.config(selectbackground="#0078ff")
window.mainloop()