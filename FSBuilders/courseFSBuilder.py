from pathlib import Path
from tkinter import messagebox

from FSBuilders.FSBuilder import FSBuilder


class FullFileSystemBuilder(FSBuilder):
    def __init__(self, targetDir, course):
        super().__init__(targetDir, course)
        self.buildFullFileSystem()

    def buildFullFileSystem(self):
        university_path = Path(self.targetDir) / "University"
        if university_path.exists():
            messagebox.showerror("Directory Exists", f"A 'University' folder already exists at:\n{university_path}\n\n")
            return

        # Create base university directory
        uni_dir = self.targetDir / "University"
        uni_dir.mkdir(parents=True, exist_ok=True)

        # Create year/module/week structure - painful to look at though, i know
        for year in range(1, self.course.years + 1):
            year_path = uni_dir / f"Year {year}"
            year_path.mkdir(exist_ok=True)

            for module in range(1, self.course.modules + 1):
                module_path = year_path / f"Module {module}"
                module_path.mkdir(exist_ok=True)

                # Add module subfolders
                for subfolder in ["Coursework", "Notes", "Exam Prep"]:
                    (module_path / subfolder).mkdir(exist_ok=True)

                for week in range(1, self.course.weeks + 1):
                    (module_path / f"Week {week}").mkdir(exist_ok=True)

        # Create other top-level folders
        for extra_folder in ["Other", "Clubs & Societies"]:
            (uni_dir / extra_folder).mkdir(exist_ok=True)

        messagebox.showinfo("Success",f"Folder structure created successfully at:\n\n{uni_dir}")
