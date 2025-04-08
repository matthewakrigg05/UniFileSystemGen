class courseContext:
    numOfYears = 0
    modulesPerYear = 0
    modulesPerSemester = 0

    def __init__(self):
        self.gatherInfo()

    def gatherInfo(self):
        self.numOfYears = input("How many years are you attending university? ")
        self.modulesPerYear = input("How many modules in each year?")