import tkinter as tk
from tkinter import messagebox

from courseContext import courseContext
from filesystemBuilder import fileSystemBuilder
from workingDirectory import FileSystemDir


class FileSystemGUI:
    workingDir = FileSystemDir()

    def __init__(self, root):
        self.root = root
        self.root.title("University Folder Structure Builder")

        self.years = tk.IntVar(value=3)
        self.modules = tk.IntVar(value=4)
        self.weeks = tk.IntVar(value=10)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Years:").grid(row=1, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.years).grid(row=1, column=1)

        tk.Label(self.root, text="Modules per Year:").grid(row=2, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.modules).grid(row=2, column=1)

        tk.Label(self.root, text="Weeks per Module:").grid(row=3, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.weeks).grid(row=3, column=1)

        tk.Button(self.root, text="Create Structure", command=self.create_structure).grid(row=4, column=1, pady=10)

    def create_structure(self):
        try:
            course = courseContext(self.years.get(), self.modules.get(), self.weeks.get())
            fileSystemBuilder(self.workingDir, course)
            self.showSuccessMessage()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

    def showSuccessMessage(self):
        messagebox.showinfo("Success", f"Folder structure created successfully. Check {self.workingDir.homeDirectory}!")
        self.root.quit()