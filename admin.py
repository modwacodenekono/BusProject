# Admin class is encapsulated to ensure safety and attributes are returned through getters
class Admin:
    #atribute which checks if the user has entered the correct username and password
    adminRestriction = True

    def __init__(self, username, password):
        self.adminUsername = username
        self.adminPassword = password

    def getAdminUsername(self):
        return self.adminUsername

    def getAdminPassword(self):
        return self.adminPassword

    # Checks username and password to remove admin restriction
    def adminLogIn(self, username, password):
        if username == self.getAdminUsername() and password == self.getAdminPassword():
            print('You have successfully logged in as an admin')
            self.adminRestriction = False
        else:
            print('Incorrect Username or Password')

    def changePrice(self):
        if self.adminRestriction:
            print('You are not authorised to change prices')
            exit()
        # Open a file in a writing form to change the price of any object
        else:
            # with open('C:/Users/user/PycharmProjects/BusTicketPythonProject/busTicket.txt', 'r+') as file:
            print('Price has been changed')
            exit()


admin = Admin(123456, 654321)
while True:
    adminLogInInput1 = int(input('Wellcome to Admin Log In\nPlease enter your Username\n>>>'))
    adminLogInInput2 = int(input('Now please enter your Password\n>>>'))

    admin.adminLogIn(adminLogInInput1, adminLogInInput2)