class courseContext:
    numOfYears = 0
    modulesPerYear = 0
    modulesPerSemester = 0
    weeksPerModule = 0

    def __init__(self):
        self.gatherInfo()

    def gatherInfo(self):
        self.numOfYears = int(input("How many years are you attending university? "))
        self.modulesPerYear = int(input("How many modules in each year? "))
        self.weeksPerModule = int(input("Approximately how many weeks do you spend on each module? (For default 10, "
                                        "press Enter)"))
