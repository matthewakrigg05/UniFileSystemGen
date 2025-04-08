import unittest
import os
from pathlib import Path
from unittest.mock import MagicMock
from filesystemBuilder import fileSystemBuilder


class TestFilesystemBuilder(unittest.TestCase):

    def setUp(self):
        # Set up the mock directory and course info
        self.mock_dir = MagicMock()
        self.mock_dir.homeDirectory = "C:\\Test"

        self.mock_course = MagicMock()
        self.mock_course.numOfYears = 2
        self.mock_course.modulesPerYear = 3
        self.mock_course.weeksPerModule = 5

    def test_build_filesystem(self):
        builder = fileSystemBuilder(self.mock_dir, self.mock_course)

        # Test the creation of the University directory
        self.assertTrue(Path(os.path.join(self.mock_dir.homeDirectory, "University")).exists())

        # Test creation of Year directories
        for i in range(self.mock_course.numOfYears):
            self.assertTrue(Path(os.path.join(self.mock_dir.homeDirectory, "University", f"Year {i + 1}")).exists())

        # Test creation of Module directories within Year directories
        for year in range(self.mock_course.numOfYears):
            for module in range(self.mock_course.modulesPerYear):
                for week in range(self.mock_course.weeksPerModule):
                    self.assertTrue(Path(os.path.join(self.mock_dir.homeDirectory, "University", f"Year {year + 1}",
                                                      f"Module {module + 1}", f"Week {week + 1}")).exists())

        # Test creation of Other and Clubs & Societies directories
        self.assertTrue(Path(os.path.join(self.mock_dir.homeDirectory, "University", "Other")).exists())
        self.assertTrue(Path(os.path.join(self.mock_dir.homeDirectory, "University", "Clubs & Societies")).exists())

    def tearDown(self):
        # Clean up the created directories
        dirPath = os.path.join(self.mock_dir.homeDirectory, "University")
        for root, dirs, files in os.walk(dirPath, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

        os.rmdir(dirPath)


if __name__ == "__main__":
    unittest.main()
