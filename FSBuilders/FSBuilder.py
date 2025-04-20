from pathlib import Path


class FSBuilder:
    targetDir = None
    course = None

    def __init__(self, targetDir, course):
        self.targetDir = Path(targetDir.directoryLocation)
        self.course = course
