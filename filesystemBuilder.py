import os
from pathlib import Path
import workingDirectory
import courseContext


class filesystemBuilder:
    directory = None
    courseInfo = None  # contains all vars that decide how system is structured

    def __init__(self, workingDir: workingDirectory.FileSystemDir, course: courseContext.courseContext):
        self.directory = workingDir
        self.courseInfo = course

        self.buildFileSystem()

    def buildFileSystem(self):
        file_path = Path(self.directory.homeDirectory + "\\University")

        if not file_path.exists():
            os.mkdir(self.directory.homeDirectory + "\\University")

        for i in range(self.courseInfo.numOfYears):
            if not Path(self.directory.homeDirectory + f"\\University\\Year {i + 1}").exists():
                os.mkdir(self.directory.homeDirectory + f"\\University\\Year {i + 1}")

        for dir in os.listdir(self.directory.homeDirectory + f"\\University"):
            for i in range(self.courseInfo.modulesPerYear):
                if not Path(self.directory.homeDirectory + f"\\University\\{dir}\\Module {i + 1}").exists():
                    os.mkdir(self.directory.homeDirectory + f"\\University\\{dir}\\Module {i + 1}")
