import tkinter as tk
from tkinter import messagebox, filedialog
from pathlib import Path


# --- Mock Classes for Integration ---
class FileSystemDir:
    def __init__(self, home_directory):
        self.homeDirectory = home_directory


class CourseContext:
    def __init__(self, num_of_years, modules_per_year, weeks_per_module):
        self.numOfYears = num_of_years
        self.modulesPerYear = modules_per_year
        self.weeksPerModule = weeks_per_module


# --- FileSystemBuilder ---
class FileSystemBuilder:
    def __init__(self, working_dir: FileSystemDir, course: CourseContext):
        self.home_dir = Path(working_dir.homeDirectory) / "University"
        self.course_info = course
        self.weeks = course.weeksPerModule or 10

        self.build_file_system()

    def build_file_system(self):
        self.home_dir.mkdir(parents=True, exist_ok=True)

        for year in range(1, self.course_info.numOfYears + 1):
            year_path = self.home_dir / f"Year {year}"
            year_path.mkdir(exist_ok=True)

            for module in range(1, self.course_info.modulesPerYear + 1):
                module_path = year_path / f"Module {module}"
                module_path.mkdir(exist_ok=True)

                for subfolder in ["Coursework", "Notes", "Exam Prep"]:
                    (module_path / subfolder).mkdir(exist_ok=True)

                for week in range(1, self.weeks + 1):
                    (module_path / f"Week {week}").mkdir(exist_ok=True)

        for extra_folder in ["Other", "Clubs & Societies"]:
            (self.home_dir / extra_folder).mkdir(exist_ok=True)


# --- Tkinter GUI ---
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

    def create_structure(self):
        if not self.home_directory.get():
            messagebox.showerror("Error", "Please select a base directory.")
            return

        university_path = Path(self.home_directory.get()) / "University"
        if university_path.exists():
            messagebox.showerror("Directory Exists", f"A 'University' folder already exists at:\n{university_path}\n\n")
            return

        try:
            working_dir = FileSystemDir(self.home_directory.get())
            course = CourseContext(self.years.get(), self.modules.get(), self.weeks.get())
            builder = FileSystemBuilder(working_dir, course)
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
            self.home_directory.set(path)
