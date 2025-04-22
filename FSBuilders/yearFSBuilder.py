from tkinter import messagebox

from FSBuilders.FSBuilder import FSBuilder


class YearFileSystemBuilder(FSBuilder):
    def __init__(self, targetDir, course):
        super().__init__(targetDir, course)

        self.year_number = course.years
        self.modules = course.modules
        self.buildSingleYearStructure()

    def buildSingleYearStructure(self):
        year_path = self.targetDir / f"Year {self.year_number}"
        year_path.mkdir(parents=True, exist_ok=True)

        for module in range(1, self.course.modules + 1):
            module_path = year_path / f"Module {module}"
            module_path.mkdir(exist_ok=True)

            for sub in ["Coursework", "Notes", "Exam Prep"]:
                (module_path / sub).mkdir(exist_ok=True)

            for week in range(1, self.course.weeks + 1):
                week_path = (module_path / f"Week {week}")
                week_path.mkdir(exist_ok=True)

                for subfolder in ['Lectures', 'Seminar', 'Reading Material', 'Exercises and Practice',
                                  'Notes']:
                    (week_path / subfolder).mkdir(exist_ok=True)

        messagebox.showinfo("Success",f"Folder structure created successfully at:\n\n{year_path}\n\nYou will be redirected there now!")

        self.open_location(year_path)
