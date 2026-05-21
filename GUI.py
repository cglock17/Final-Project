tasks = []
import tkinter as tk

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        print("No task entered")

def complete_task():
    selected = task_listbox.curselection()

    if selected:
        index = selected[0]

        task = "✔" + tasks[index]
        task_listbox.delete(index)
        task_listbox.insert(index, task)


def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]

    task_listbox.delete(index)
    tasks.pop(index)










root = tk.Tk()
root.title("Task Manager")
root.geometry("400x500")
root.configure(bg="#f0f0f0")
add_button = tk.Button(root, text="Add", command=add_task)
# Title
title_label = tk.Label(
    root,
    text="Task Manager",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0"
)
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

task_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 12)
)
task_entry.pack(side=tk.LEFT, padx=5)


add_button = tk.Button(input_frame, text="Add", width= 10, command=add_task)





add_button.pack(side=tk.LEFT)

# Listbox (task display)
task_listbox = tk.Listbox(
    root,
    width=40,
    height=15,
    font=("Arial", 12)
)
task_listbox.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

complete_button = tk.Button(
    button_frame,
    text="Complete",
    width=12,
    command=complete_task
)
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=12,
    command=delete_task
)
delete_button.pack(side=tk.LEFT, padx=5)

root.mainloop()

