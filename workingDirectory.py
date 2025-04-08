import os
import platform
import sys


class FileSystemDir:
    homeDirectory = None
    operatingSystem = None

    def __init__(self):
        self.operatingSystem = platform.system()  # Looking for: Windows, Darwin or Linux
        self.confirmOS()

        self.findHomeDirectory()  # build filesystem in home dir so it is easy to find for the user!

    def confirmOS(self):
        userOS = self.operatingSystem
        validOS = ['Windows', 'Darwin', 'Linux']

        if userOS not in validOS:
            print("Oh no, this application won't function correctly for your operating system. :(")
            sys.exit()

        print(f"Welcome {userOS} user!")

    def findHomeDirectory(self):
        self.homeDirectory = os.path.expanduser('~')
        print(f"Working in {self.homeDirectory}")
