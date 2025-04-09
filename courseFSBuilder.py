from FSBuilder import FSBuilder


class FullFileSystemBuilder(FSBuilder):
    courseInformation = None

    def __init__(self, targetDir, course, weeks=10):
        super().__init__(targetDir, weeks)

        self.courseInformation = course
        self.buildFullFileSystem()

    def buildFullFileSystem(self):
        # Create base university directory
        self.targetDir.mkdir(parents=True, exist_ok=True)

        # Create year/module/week structure - painful to look at though, i know
        for year in range(1, self.courseInformation.numOfYears + 1):
            year_path = self.targetDir / f"Year {year}"
            year_path.mkdir(exist_ok=True)

            for module in range(1, self.courseInformation.modulesPerYear + 1):
                module_path = year_path / f"Module {module}"
                module_path.mkdir(exist_ok=True)

                # Add module subfolders
                for subfolder in ["Coursework", "Notes", "Exam Prep"]:
                    (module_path / subfolder).mkdir(exist_ok=True)

                for week in range(1, self.weeks + 1):
                    (module_path / f"Week {week}").mkdir(exist_ok=True)

        # Create other top-level folders
        for extra_folder in ["Other", "Clubs & Societies"]:
            (self.targetDir / extra_folder).mkdir(exist_ok=True)

