import tkinter as tk
from gui import FileSystemGUI


if __name__ == '__main__':
    root = tk.Tk()
    app = FileSystemGUI(root)
    root.mainloop()
