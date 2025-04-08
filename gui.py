import tkinter as tk
from tkinter import messagebox, filedialog

from courseContext import courseContext
from filesystemBuilder import fileSystemBuilder
from workingDirectory import FileSystemDir


class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("University Folder Structure Builder")

        self.home_directory = tk.StringVar()
        self.years = tk.IntVar(value=3)
        self.modules = tk.IntVar(value=4)
        self.weeks = tk.IntVar(value=10)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Choose Base Directory:").grid(row=0, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.home_directory, width=40).grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_directory).grid(row=0, column=2)

        tk.Label(self.root, text="Years:").grid(row=1, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.years).grid(row=1, column=1)

        tk.Label(self.root, text="Modules per Year:").grid(row=2, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.modules).grid(row=2, column=1)

        tk.Label(self.root, text="Weeks per Module:").grid(row=3, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.weeks).grid(row=3, column=1)

        tk.Button(self.root, text="Create Structure", command=self.create_structure).grid(row=4, column=1, pady=10)

    def browse_directory(self):
        path = filedialog.askdirectory()
        if path:
            self.home_directory.set(path)

    def create_structure(self):
        if not self.home_directory.get():
            messagebox.showerror("Error", "Please select a base directory.")
            return

        try:
            working_dir = FileSystemDir()
            course = courseContext(self.years.get(), self.modules.get(), self.weeks.get())
            fileSystemBuilder(working_dir, course)
            messagebox.showinfo("Success", "Folder structure created successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")
