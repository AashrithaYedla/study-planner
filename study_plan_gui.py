import tkinter as tk
import study_planner

root = tk.Tk()
root.title("Smart Study Planner")
root.geometry("400x400")

tasks = []

tk.Label(root, text="Subject").pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

tk.Label(root, text="Study Time (hours)").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Label(root, text="Deadline").pack()
deadline_entry = tk.Entry(root)
deadline_entry.pack()

def add_task():
    subject = subject_entry.get()
    time = time_entry.get()
    deadline = deadline_entry.get()

    task = f"{subject} - {time} hours - Deadline: {deadline}"
    tasks.append(task)

    listbox.insert(tk.END, task)

def delete_task():
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        study_planner.delete_task(index)
        listbox.delete(index)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

root.mainloop()