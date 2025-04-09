import platform
import sys


class FileSystemDir:
    directoryLocation = None

    def __init__(self, path):
        self.confirmOS()
        self.directoryLocation = path

    @staticmethod
    def confirmOS():
        userOS = platform.system()  # Looking for: Windows, Darwin or Linux
        validOS = ['Windows', 'Darwin', 'Linux']

        if userOS not in validOS:
            sys.exit()
