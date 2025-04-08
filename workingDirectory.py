import os
import platform
import sys


class FileSystemDir:
    path = ''
    operatingSystem = ''

    def __init__(self):
        self.operatingSystem = platform.system()  # Looking for: Windows, Darwin or Linux
        self.confirmOS()

    def confirmOS(self):
        userOS = self.operatingSystem
        validOS = ['Windows', 'Darwin', 'Linux']

        if userOS not in validOS:
            print("Oh no, this application won't function correctly for your operating system. :(")
            sys.exit()

        print(f"Welcome {userOS} user!")
