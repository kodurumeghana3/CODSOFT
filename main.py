from tkinter import *
from tkinter import messagebox

tasks = []

def add_task():
    new_task = task_box.get()
    if new_task == "":
        messagebox.showerror("Error", "Please type a task")
    else:
        tasks.append(new_task)
        show_tasks()
        task_box.delete(0, END)

def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        tasks.pop(selected_task)
        show_tasks()
    except:
        messagebox.showerror("Error", "Please select a task to delete")

def show_tasks():
    task_list.delete(0, END)
    for i, t in enumerate(tasks, start=1):
        task_list.insert(END, f"{i}. {t}")

# Main window
win = Tk()
win.title("ToDo App")
win.geometry("300x350")
win.config(bg="lightgreen")

# Input area
Label(win, text="Enter Task:", bg="lightgreen").pack(pady=5)
task_box = Entry(win, width=30)
task_box.pack(pady=5)

# Buttons
add_btn = Button(win, text="Add Task", bg="red", fg="white", command=add_task)
add_btn.pack(pady=5)

# Listbox to show tasks
task_list = Listbox(win, width=40, height=10)
task_list.pack(pady=10)

delete_btn = Button(win, text="Delete Task", bg="red", fg="white", command=delete_task)
delete_btn.pack(pady=5)

exit_btn = Button(win, text="Exit", bg="red", fg="white", command=win.quit)
exit_btn.pack(pady=5)

win.mainloop()