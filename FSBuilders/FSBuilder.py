import os.path
from pathlib import Path


class FSBuilder:
    targetDir = None
    course = None

    def __init__(self, targetDir, course):
        self.targetDir = Path(targetDir.directoryLocation)
        self.course = course

    def open_location(self, open_loc):
        path = open_loc
        path = os.path.realpath(path)
        os.startfile(path)
