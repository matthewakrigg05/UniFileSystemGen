import tkinter as tk
from tkinter import messagebox, filedialog
from utils import workingDirectory, courseContext
from FSBuilders import courseFSBuilder, yearFSBuilder


# --- Tkinter GUI ---
class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("University Folder Structure Builder")

        self.option = tk.StringVar(value='multiple')
        self.directoryLocation = tk.StringVar()
        self.years = tk.IntVar(value=3)
        self.modules = tk.IntVar(value=4)
        self.weeks = tk.IntVar(value=10)

        self.year_label = tk.Label(root, text="Number of Years:")
        self.module_label = tk.Label(self.root, text="Modules per Year:")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Choose System Builder:").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(self.root, text='Multiple Years', variable=self.option, value='multiple',
                       command=self.on_selection_change).grid(row=1, column=0)
        tk.Radiobutton(self.root, text='Add Year To Existing Folder', variable=self.option, value='single',
                       command=self.on_selection_change).grid(row=1, column=1)

        tk.Label(self.root, text="Choose Base Directory:").grid(row=2, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.directoryLocation, width=40).grid(row=2, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_directory).grid(row=2, column=2)

        self.year_label.grid(row=3, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.years).grid(row=3, column=1)

        self.module_label.grid(row=4, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.modules).grid(row=4, column=1)

        tk.Label(self.root, text="Weeks per Module:").grid(row=5, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.weeks).grid(row=5, column=1)

        tk.Button(self.root, text="Build!", command=self.create_structure).grid(row=6, column=1, pady=10)

    def create_structure(self):
        self.validate_inputs()

        try:
            working_dir = workingDirectory.FileSystemDir(self.directoryLocation.get())
            course = courseContext.courseContext(self.years.get(), self.modules.get(), self.weeks.get())

            if self.option.get() == 'multiple':
                courseFSBuilder.FullFileSystemBuilder(working_dir, course)
                self.root.quit()

            else:
                yearFSBuilder.YearFileSystemBuilder(working_dir, course)
                self.root.quit()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

    def browse_directory(self):
        path = filedialog.askdirectory()
        if path:
            self.directoryLocation.set(path)

    def validate_inputs(self):
        if not self.directoryLocation.get():
            messagebox.showerror("Error", "Please select a base directory.")
            return

    def on_selection_change(self):
        if self.option.get() == 'multiple':
            self.year_label.config(text="Number of Years:")
            self.module_label.config(text="Modules per Year")
        else:
            self.year_label.config(text="Year to Add:")
            self.module_label.config(text="Modules in the Year")
