class Officer():

    officerType = ""
    secretary = ""
    absoc_representative = ""
    historian = ""
    webmaster = ""

    def is_current_member(self):
        pass
    def is_current_officer(self):
        pass

    def createOfficer(self, officerType):
        self.officerType=officerType
    def displayOfficer(self):
        return self.officerType
