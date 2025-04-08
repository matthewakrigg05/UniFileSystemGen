# 📁 University Filesystem Builder

A desktop utility that generates an organized folder structure for university students — structured by academic years, modules, and weeks, with separate folders for coursework, notes, and exam prep.

---

This is a small automation project written in python. The aim of the project is to create a simple application
capable of building a file system for a user - assuming they are a university student. As it stands, 
the application assumes that the user has no university directory at all, and so creates a new one in the
users home directory. This application has yet to be tested on MAC and Linux BUT should work...

Here is a link to my trello board for this project if youd like to see where I am up to:
https://trello.com/b/bO4zqCO7/fsm

---

### Requirements

- **Windows OS**
- Python 3.10+ (only if you're running the `.py` file)
- Or use the `.exe` version (no Python required)

---

### Using the `.exe` File

1. **Download the `.exe`** from the [Releases](https://github.com/matthewakrigg05/UniFileSystemGen/releases) tab.
2. **Run it** — A window will appear.
3. **Enter details**:
   - Number of academic years
   - Number of modules per year
   - Weeks per module *(optional — defaults to 10)*
4. Click **Generate Structure**.
5. You'll see a success message when it’s done!

Your folder structure will look like this:

University/ Year 1/ Module 1/ Week 1/ Week 2/ ... Coursework/ Notes/ Exam Prep/ Module 2/ ... Year 2/ ... Other/ Clubs & Societies/
