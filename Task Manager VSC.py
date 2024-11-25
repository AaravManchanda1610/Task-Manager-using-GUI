import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("550x550")
        self.root.config(bg="#f0f0f0")

        self.tasks = []

        # Create the GUI elements
        self.task_listbox = tk.Listbox(root, width=50, height=15, bg="#ffffff", fg="#333333", font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.add_task_button.pack(pady=5)

        self.edit_task_button = tk.Button(root, text="Edit Task", command=self.edit_task, bg="#2196F3", fg="white", font=("Arial", 12))
        self.edit_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(root, text="Mark Task as Completed", command=self.complete_task, bg="#FF9800", fg="white", font=("Arial", 12))
        self.complete_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="#f44336", fg="white", font=("Arial", 12))
        self.remove_task_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append(task)
            self.update_task_list()

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            current_task = self.tasks[selected_index]
            new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_index] = new_task
                self.update_task_list()
        except IndexError:
            messagebox.showwarning("Edit Task", "Please select a task to edit.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_index]
            self.tasks[selected_index] = f"{completed_task} (Completed)"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Mark Task as Completed", "Please select a task to be marked as completed.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Remove Task", "Please select a task to remove.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Add tasks to the listbox

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()