import tkinter as tk
from tkinter import messagebox, filedialog
from pathlib import Path
import courseContext
import workingDirectory
import courseFSBuilder


# --- Tkinter GUI ---
class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("University Folder Structure Builder")

        self.directory_location = tk.StringVar()
        self.years = tk.IntVar(value=3)
        self.modules = tk.IntVar(value=4)
        self.weeks = tk.IntVar(value=10)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Choose Base Directory:").grid(row=0, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.directory_location, width=40).grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_directory).grid(row=0, column=2)

        tk.Label(self.root, text="Years:").grid(row=1, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.years).grid(row=1, column=1)

        tk.Label(self.root, text="Modules per Year:").grid(row=2, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.modules).grid(row=2, column=1)

        tk.Label(self.root, text="Weeks per Module:").grid(row=3, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.weeks).grid(row=3, column=1)

        tk.Button(self.root, text="Create Structure", command=self.create_structure).grid(row=4, column=1, pady=10)

    def create_structure(self):
        if not self.directory_location.get():
            messagebox.showerror("Error", "Please select a base directory.")
            return

        university_path = Path(self.directory_location.get()) / "University"
        if university_path.exists():
            messagebox.showerror("Directory Exists", f"A 'University' folder already exists at:\n{university_path}\n\n")
            return

        try:
            working_dir = workingDirectory.FileSystemDir(self.directory_location.get())
            course = courseContext.courseContext(self.years.get(), self.modules.get(), self.weeks.get())
            builder = filesystemBuilder.fileSystemBuilder(working_dir, course)
            messagebox.showinfo(
                "Success",
                f"Folder structure created successfully at:\n\n{builder.home_dir}"
            )
            self.root.quit()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

    def browse_directory(self):
        path = filedialog.askdirectory()
        if path:
            self.directory_location.set(path)
