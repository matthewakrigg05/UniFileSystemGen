from pathlib import Path
import workingDirectory
import courseContext


class fileSystemBuilder:
    def __init__(self, working_dir: workingDirectory.FileSystemDir, course: courseContext.courseContext):
        self.home_dir = Path(working_dir.homeDirectory) / "University"
        self.course_info = course
        self.weeks = course.weeksPerModule or 10

        self.buildFileSystem()

    def buildFileSystem(self):
        # Create base university directory
        self.home_dir.mkdir(parents=True, exist_ok=True)

        # Create year/module/week structure - painful to look at though, i know
        for year in range(1, self.course_info.numOfYears + 1):
            year_path = self.home_dir / f"Year {year}"
            year_path.mkdir(exist_ok=True)

            for module in range(1, self.course_info.modulesPerYear + 1):
                module_path = year_path / f"Module {module}"
                module_path.mkdir(exist_ok=True)

                for week in range(1, self.weeks + 1):
                    (module_path / f"Week {week}").mkdir(exist_ok=True)

        # Create other top-level folders
        for extra_folder in ["Other", "Clubs & Societies"]:
            (self.home_dir / extra_folder).mkdir(exist_ok=True)
