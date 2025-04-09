from pathlib import Path


class FSBuilder:
    homeDir = None
    weeks = None

    def __init__(self, targetDir, weeks):
        self.home_dir = Path(targetDir.homeDirectory) / "University"
        self.weeks = weeks