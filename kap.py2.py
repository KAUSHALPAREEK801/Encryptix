import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Initialize list to store tasks
        self.tasks = []

        # Create UI Elements
        self.task_label = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
        self.task_label.pack(pady=10)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append(task)
            self.update_task_listbox()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Update Task", "Please select a task to update.")
            return
        task_index = selected_task_index[0]
        updated_task = simpledialog.askstring("Update Task", "Update the task:", initialvalue=self.tasks[task_index])
        if updated_task:
            self.tasks[task_index] = updated_task
            self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")
            return
        task_index = selected_task_index[0]
        del self.tasks[task_index]
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Create the main window
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
