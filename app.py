from  tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as tkFont
import time
#----------------------------------------
root=Tk()

root['bg'] = '#fafafa'
root.title('ToDoList')
root.geometry('750x400')
root.resizable(width=False, height=False)

canvas = Canvas(root,height=750, width=300)
canvas.grid()

frame = Frame(root,bg = "#cfe2f4")
frame.place(relwidth=1, relheight=1)

fontWindow = tkFont.Font(family="Arial", size=10, weight="bold", slant="italic")
#----------------------------------------

def clock():
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S", named_tuple)
    time_n['text'] = '{}'.format(time_string)



def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteTask():
    lb.delete(ANCHOR)

#-----------------------------------------
btn = Button(frame, text='clock',bg="#E0FFFF", command=clock)
btn.grid(row=1, column=0)
#------------------------------------------
img = Image.open("1200px-Sunflower_Taleghan.jpg")
img = img.resize((200, 230))
test = ImageTk.PhotoImage(img)
photo = Label(frame,text="photo: ",  image = test)
photo.grid(row=2, column=2,padx=5)


#--------------------------------------------
time_n = Label(frame,text="A good plan executed at lightning speed today is much better than a perfect plan for tomorrow. ",
               wraplength=200, justify="center",bg="#4169E1", fg="#fff7e0",font="Arial 16", width=21, height=10)
time_n.grid(row=2, column=1,padx=5)

some_text = Label(frame,text="Add task for a day ", bg="#cfe2f4", fg="#0d5a9f",font="Arial 15", width=15, height=3)
some_text.grid(row=4, column=1,columnspan=2,padx=5)

#---------------------------------------
lb = Listbox(frame,bg="#4169E1", fg="#fff7e0",font="Arial 14",width=20, height=10, justify=LEFT)
lb.grid(row=2, column=3,padx=5)

task_list = [
    'write cod',
    'read documentation',
]

#------------------------------------------
for item in task_list:
    lb.insert(END, item)

my_entry = Entry(frame)
my_entry.grid(row=3, column=3,  pady=5)
#----------------------------------------------

addTask_btn = Button(
    frame,
    text='Add Task',
    bg='#c5f776',
    font="Arial 10",
    command=newTask
)
addTask_btn.grid(row=4, column=3, pady=2)

delTask_btn = Button(
    frame,
    text='Delete Task',
    bg='#ff8b61',

    command=deleteTask
)
delTask_btn.grid(row=5, column=3, pady=2)

root.mainloop()





