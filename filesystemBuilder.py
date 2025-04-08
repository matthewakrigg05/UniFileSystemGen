import os
import workingDirectory
import courseContext


class filesystemBuilder:
    directory = None
    courseInfo = None  # contains all vars that decide how system is structured

    def __init__(self, workingDir: workingDirectory.FileSystemDir, course: courseContext.courseContext):
        self.directory = workingDir
        self.courseInfo = course

    def buildFileSystem(self):
        os.mkdir(self.directory.homeDirectory + "\\University")
