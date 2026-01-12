class Admin:
    adminUsername = 123456
    adminPassword = 654321

    def getAdminUsername(self):
        return self.adminUsername

    def getAdminPassword(self):
        return self.adminPassword

    def adminLogIn(self, username, password):
        if username == self.getAdminUsername() and password == self.getAdminPassword():
            print('You have successfully logged in as an admin')
            print(username, password)
        else:
            print('Incorrect Username or Password')
            print(username, password)

admin = Admin()
while True:
    adminLogInInput1 = int(input('Wellcome to Admin Log In\nPlease enter your Username\n>>>'))
    adminLogInInput2 = int(input('Now please enter your Password\n>>>'))

    admin.adminLogIn(adminLogInInput1, adminLogInInput2)