from pathlib import Path
from FSBuilder import FSBuilder


class YearFileSystemBuilder(FSBuilder):

    def __init__(self, targetDir, yearNumber, modules, weeks):
        super().__init__(targetDir, weeks)

        self.year_number = yearNumber
        self.modules = modules
        self.buildSingleYearStructure()

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