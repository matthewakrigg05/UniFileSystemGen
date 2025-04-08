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

        fileSystemBuilder(self.mock_dir, self.mock_course)

    def test_create_university_directory(self):
        university_dir = os.path.join(self.mock_dir.homeDirectory, "University")
        self.assertTrue(Path(university_dir).exists())

    def test_create_year_directories(self):
        for i in range(self.mock_course.numOfYears):
            year_dir = os.path.join(self.mock_dir.homeDirectory, "University", f"Year {i + 1}")
            self.assertTrue(Path(year_dir).exists())

    def test_create_module_directories(self):
        for year in range(self.mock_course.numOfYears):
            for module in range(self.mock_course.modulesPerYear):
                module_dir = os.path.join(self.mock_dir.homeDirectory, "University", f"Year {year + 1}",
                                          f"Module {module + 1}")
                self.assertTrue(Path(module_dir).exists())

    def test_create_week_directories(self):
        for year in range(self.mock_course.numOfYears):
            for module in range(self.mock_course.modulesPerYear):
                for week in range(self.mock_course.weeksPerModule):
                    week_dir = os.path.join(self.mock_dir.homeDirectory, "University", f"Year {year + 1}",
                                            f"Module {module + 1}", f"Week {week + 1}")
                    self.assertTrue(Path(week_dir).exists())

    def test_create_other_directory(self):
        other_dir = os.path.join(self.mock_dir.homeDirectory, "University", "Other")
        self.assertTrue(Path(other_dir).exists())

    def test_create_clubs_societies_directory(self):
        clubs_dir = os.path.join(self.mock_dir.homeDirectory, "University", "Clubs & Societies")
        self.assertTrue(Path(clubs_dir).exists())

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
