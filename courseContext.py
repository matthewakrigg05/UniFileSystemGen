class courseContext:
    numOfYears = 0
    modulesPerYear = 0
    modulesPerSemester = 0
    weeksPerModule = 0

    def __init__(self, years, modules, weeks):
        self.numOfYears = years
        self.modulesPerYear= modules
        self.weeksPerModule = weeks
