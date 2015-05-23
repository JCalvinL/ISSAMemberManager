class Officer():
    
    first_name = ""
    last_name = ""
    officerType = ""
    #Officer positions are: secretary, absoc representative, historian, and webmaster
    board_year = ""
    org_email = ""
    elected = ""

    def is_current_officer(self):
        pass

    def __str__(self):
        return self.first_name + " " + self.last_name

    def createOfficer(self):
        if(self == current) and (self == elected):
            return self.officerType