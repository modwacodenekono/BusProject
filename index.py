import csv, datetime, os

# You can delete this file to try this program functionality

class User:

    categoryList = []
    categoryDescriptionList = []

    def getCategoryList(self):
        return self.categoryList

    def getCategoryDescriptionList(self):
        return self.categoryDescriptionList

    def loadData(self):
        # Going through csv and saving data into the list
        with open('mobile_products.csv', 'r') as file:
            csvFile = csv.DictReader(file)

            # Saving data into lists
            for lines in csvFile:
                if lines['category_title'] not in user.categoryList:
                    self.categoryList.append(lines['category_title'])
                    self.categoryDescriptionList.append(lines['category_description'])


# while True:
    #     try:
    #
    #     # Expecting a user to enter a letter
    #     except ValueError:
    #         print('Please enter a valid input. A valid input is a number\n')




# The user is able to pick one category and each category is only shown once
def chooseCategory():
    i = 1
    terminateLoop = True
    global categoryChoiceInput

    # Going through csv
    for data in user.getCategoryList():
        print(str(i) + '.', str(data))
        i += 1

    # error handling!
    # Validating user input and calling the next function
    while terminateLoop:
        categoryChoiceInput = int(input('To find out more or choose a category please enter the number.\n>>>')) - 1
        if 0 > categoryChoiceInput or categoryChoiceInput > len(user.getCategoryList()) - 1:
            print('Invalid choice')

        else:
            terminateLoop = False
            print('You have chosen ' + user.getCategoryList()[categoryChoiceInput])
            confirmChoice('category', categoryChoiceInput)



# This function allows confirming choice exploring more information or going back. It also works for two different parts of the program, which saves space
def confirmChoice(choice, userInput, topUpList = None):
    terminateLoop = True

    if choice == 'category':

        while terminateLoop:
            # error handling!
            confirmChoiceInput = int(input('1. To find out more or\n2. To choose this category or\n0. To move back\n>>>'))

            match confirmChoiceInput:
                case 1:
                    print(user.getCategoryDescriptionList()[userInput])

                    confirmChoiceInput2 = int(input('Do you still want to buy this ticket?\n1. Yes\n0. Go back\n>>>'))

                    terminateLoop = False

                    # Another check if after finding out more information, the user still wants to buy a ticket
                    if confirmChoiceInput2 == 1:
                        chooseTopUp()
                    elif confirmChoiceInput2 == 0:
                        chooseCategory()
                    else:
                        print('Invalid choice')

                case 2:
                    chooseTopUp()
                    terminateLoop = False
                case 0:
                    chooseCategory()
                    terminateLoop = False
                case _:
                    print('Invalid choice')

    else:

        # Creating full message considering multiple factors like use of plural and correct appearance of price
        if topUpList[userInput][3] == '':
            topUpOutputPhrase = 'from 2025-08-31T23:00:00+00:00 to 2026-07-31T22:59:00+00:00'
        else:
            topUpOutputPhrase = 'for ' + topUpList[userInput][4]
            if topUpList[userInput][4] == 1:
                topUpOutputPhrase += topUpList[userInput][3][:-1]
            else:
                topUpOutputPhrase += ' ' + topUpList[userInput][3]

            topUpOutputPhrase += ' providing you with ' + topUpList[userInput][5] + ' ticket'

            if topUpList[userInput][5] != 1:
                topUpOutputPhrase += 's'

        if topUpList[userInput][7] == '1':
            topUpOutputPhrase2 = '.'
        else:
            topUpOutputPhrase2 = ' and for a group of ' + topUpList[userInput][7] + ' people.'

        while terminateLoop:
            confirmChoiceInput = int(
                input('1. To find out more or\n2. To choose this category or\n0. To move back\n>>>'))

            match confirmChoiceInput:
                case 1:
                    print(topUpList[userInput][1], 'That costs £' + formatNumber(float(topUpList[userInput][2]) / 100), 'and lasts', topUpOutputPhrase + '. This ticket is designed for', topUpList[userInput][6] + topUpOutputPhrase2)

                    confirmChoiceInput2 = int(input('Do you still want to buy this ticket?\n1. Yes\n0. Go back\n>>>'))

                    terminateLoop = False

                    if confirmChoiceInput2 == 1:
                        payment(topUpList[userInput])
                    elif confirmChoiceInput2 == 0:
                        chooseTopUp()
                    else:
                        print('Invalid choice')

                case 2:
                    payment(topUpList[userInput])
                    terminateLoop = False
                case 0:
                    chooseTopUp()
                    terminateLoop = False
                case _:
                    print('Invalid choice')



# Lets you choose top-up and describes different features of it
def chooseTopUp():
    #order of variables, use of functions!
    topUpList = []
    terminateLoop = True
    i = 1

    with open('mobile_products.csv', 'r') as file1:
        csvFile1 = csv.DictReader(file1)
        for line in csvFile1:
            if line['category_title'] == user.getCategoryList()[categoryChoiceInput]:

                #2d list where each list inside contains all the data about one top-up
                topUpList.append([line['topup_title'], line['topup_description'], line['topup_price_in_pence'], line['topup_entitlement_unit'], line['topup_entitlement_value'], line['topup_entitlement_quantity'], line['topup_passenger_class_name'], line['topup_passenger_class_quantity']])


    for data in topUpList:
        print(str(i) + '.', str(data[0]))
        i += 1

    while terminateLoop:
        topUpChoiceInput = int(input('To find out more or buy a ticket please enter the number.\n>>>')) - 1
        if 0 > topUpChoiceInput or topUpChoiceInput > len(topUpList) - 1:
            print('Invalid choice')

        else:
            terminateLoop = False
            print('You have chosen ' + topUpList[topUpChoiceInput][0])
            confirmChoice('topUp', topUpChoiceInput, topUpList)

# If the price is an integer, it is displayed as such, otherwise it is displayed with two decimal places
def formatNumber(value):
    num = float(value)
    if num == int(num):
        return str(int(num))
    else:
        return f"{num:.2f}"

# Function which saves data about transaction
def payment(data):
    print('Processing...\n\nThank you for your purchase!')

    transaction = {
        'transaction_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'category_title': user.getCategoryList()[categoryChoiceInput],
        'topup_title': data[0],
        'topup_price_in_pence': data[2]
    }

    csv_filename = 'transactions.csv'
    file_exists = os.path.exists(csv_filename)

    # Write to CSV file
    try:
        with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['transaction_time', 'category_title', 'topup_title', 'topup_price_in_pence']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header if file is new
            if not file_exists:
                writer.writeheader()

            # Write transaction data
            writer.writerow(transaction)


    except Exception as e:
        print('Processing...')
        print('Thank you for your purchase!')
        print(f'Warning: Could not save receipt - {str(e)}')

    exit()


print('===>>> BUS APP <<<===\n')

user = User()
user.loadData()

finishLoop = True

while finishLoop:
    starterMenuInput = input('1. Press 1 to buy tickets or\n2. Press 2 to log in as an admin\n0. Press 0 to exit\n>>> ')

    match starterMenuInput:
        case 1:
            finishLoop = False
            chooseCategory()
            continue
        case 2:
            print('You have chosen to log in as an admin\n')
            # admin.admin.logIn() ...
            finishLoop = False
        case 0:
            exit()
        case _:
            print('Invalid choice')
