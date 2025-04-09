from pathlib import Path


class FSBuilder:
    targetDir = None
    weeks = None

    def __init__(self, targetDir, weeks):
        self.targetDir = Path(targetDir.directoryLocation) / "University"
        self.weeks = weeks
