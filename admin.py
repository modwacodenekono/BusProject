class Admin:
    adminUsername = 123456
    adminPassword = 654321

    def getAdminUsername:
        return adminUsername

    def getAdminPassword:
        return adminPassword

    def adminLogIn():
        adminLogInInput1 = int(input('Wellcome to Admin Log In\nPlease enter your Username\n>>>'))
        adminLogInInput2 = int(input('Now please enter your Password\n>>>'))

        if adminLogInInput1 == 123456 and adminLogInInput2 == 123456:
            print('You have successfully logged in as an admin')
        else:
            print('Incorrect Username or Password')