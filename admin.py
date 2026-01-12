class Admin:
    adminUsername = 123456
    adminPassword = 654321

    def getAdminUsername(self):
        return self.adminUsername

    def getAdminPassword(self):
        return self.adminPassword

    def adminLogIn(self):
        adminLogInInput1 = int(input('Wellcome to Admin Log In\nPlease enter your Username\n>>>'))
        adminLogInInput2 = int(input('Now please enter your Password\n>>>'))

        if adminLogInInput1 == self.getAdminUsername() and adminLogInInput2 == self.getAdminPassword():
            print('You have successfully logged in as an admin')
        else:
            print('Incorrect Username or Password')