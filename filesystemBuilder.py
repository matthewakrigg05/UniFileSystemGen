from pathlib import Path


class fileSystemBuilder:
    homeDir = None
    weeks = None

    def __init__(self, working_dir, course=None, yearNumber=None, modules=None, weeks=10):

        self.home_dir = Path(working_dir.homeDirectory) / "University"
        self.weeks = weeks

        if course:  # full course mode
            self.course_info = course
            self.buildFullFileSystem()
        elif yearNumber and modules:  # single year mode
            self.year_number = yearNumber
            self.modules = modules
            self.buildSingleYearStructure()
        else:
            raise ValueError("Insufficient arguments provided to initialize FileSystemBuilder.")

    def buildFullFileSystem(self):
        # Create base university directory
        self.home_dir.mkdir(parents=True, exist_ok=True)

        # Create year/module/week structure - painful to look at though, i know
        for year in range(1, self.course_info.numOfYears + 1):
            year_path = self.home_dir / f"Year {year}"
            year_path.mkdir(exist_ok=True)

            for module in range(1, self.course_info.modulesPerYear + 1):
                module_path = year_path / f"Module {module}"
                module_path.mkdir(exist_ok=True)

                # Add module subfolders
                for subfolder in ["Coursework", "Notes", "Exam Prep"]:
                    (module_path / subfolder).mkdir(exist_ok=True)

                for week in range(1, self.weeks + 1):
                    (module_path / f"Week {week}").mkdir(exist_ok=True)

        # Create other top-level folders
        for extra_folder in ["Other", "Clubs & Societies"]:
            (self.home_dir / extra_folder).mkdir(exist_ok=True)

    def buildSingleYearStructure(self):
        yearPath = self.home_dir / f"Year {self.year_number}"
        yearPath.mkdir(parents=True, exist_ok=True)

        for module_name in self.modules:
            module_path = yearPath / module_name
            module_path.mkdir(exist_ok=True)

            for sub in ["Coursework", "Notes", "Exam Prep"]:
                (module_path / sub).mkdir(exist_ok=True)

            for week in range(1, self.weeks + 1):
                (module_path / f"Week {week}").mkdir(exist_ok=True)