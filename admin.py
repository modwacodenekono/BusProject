import csv, os

# Admin class is encapsulated to ensure safety and attributes are returned through getters
class Admin:
    # Attribute, which checks if the user has entered the correct username and password
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


    def changeProductPrice(self, category_name, topup_name, newPricePence):
        if self.adminRestriction:
            print("Access denied. Please log in first.")
            return False

        csvFilePath = 'mobile_products.csv'
        tempFilePath = 'mobile_products_temp.csv'
        productFound = False
        oldPrice = None

        try:
            # Read the original file and write to temporary file with changes
            with open(csvFilePath, 'r', newline='', encoding='utf-8') as input_file, \
                    open(tempFilePath, 'w', newline='', encoding='utf-8') as output_file:

                reader = csv.DictReader(input_file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    if row['category_title'] == category_name and row['topup_title'] == topup_name:
                        oldPrice = row['topup_price_in_pence']
                        row['topup_price_in_pence'] = str(newPricePence)
                        productFound = True
                        print(f"Found product: {topup_name}")
                        print(f"Old price: {oldPrice} pence")
                        print(f"New price: {newPricePence} pence")

                    writer.writerow(row)




admin = Admin(123456, 654321)
while True:
    try:
        adminLogInInput1 = int(input('Welcome to Admin Log In\nPlease enter your Username\n>>>'))
        adminLogInInput2 = int(input('Now please enter your Password\n>>>'))

        admin.adminLogIn(adminLogInInput1, adminLogInInput2)

        if not admin.adminRestriction:
            while True:
                try:
                    admin_choice = int(input('\nAdmin Menu:\n1. Change Price\n0. Logout\n>>> '))

                    if admin_choice == 1:
                        admin.changePrice()
                    elif admin_choice == 0:
                        admin.adminRestriction = True
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice. Please enter 0 or 1.")

                except ValueError:
                    print("Invalid input. Please enter a number.")
            break

    except ValueError:
        print('Invalid input. Please enter a number.\n')

