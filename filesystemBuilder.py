import os

import workingDirectory


class filesystemBuilder:
    directory = None

    def __init__(self, workingDir: workingDirectory.FileSystemDir):
        self.directory = workingDir

    def buildFileSystem(self):
        os.mkdir(self.directory.homeDirectory + "\\University")
