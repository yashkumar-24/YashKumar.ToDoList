import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        
        self.task_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="To-Do List", font=("Helvetica", 16)).pack(pady=10)

        self.task_entry = tk.Entry(self.root, textvariable=self.task_var, font=("Helvetica", 12))
        self.task_entry.pack(fill=tk.X, padx=20, pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task, font=("Helvetica", 12))
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, font=("Helvetica", 12))
        self.delete_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
            self.save_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            new_task = self.task_var.get()
            if new_task:
                self.tasks[selected_index] = new_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, new_task)
                self.save_tasks()
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.tasks[selected_index]
            self.task_listbox.delete(selected_index)
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.read().splitlines()
                self.tasks = tasks
                for task in tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
