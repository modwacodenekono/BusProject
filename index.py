import csv

# except FileNotFoundError:
#    print(f"File is not found")

# def openFile():



# The user is able to pick one category and each category is only shown once
def chooseCategory():
    i = 1
    terminateLoop = True

    # Going through csv
    for data in categoryList:
        print(str(i) + '.', str(data))
        i += 1

    # error handling!
    # Validating user input and calling next function
    while terminateLoop:
        categoryChoiceInput = int(input('To find out more or choose a category please enter the number.\n>>>')) - 1
        if 0 > categoryChoiceInput or categoryChoiceInput > len(categoryList):# maybe - 1!
            print('Invalid choice')

        else:
            terminateLoop = False
            print('You have chosen ' + categoryList[categoryChoiceInput])
            confirmChoice('category', categoryChoiceInput)



# This function allows confirming choice or going back. It also works for two different parts of the program, which saves space
def confirmChoice(choice, userInput, topUpList = None):
    terminateLoop = True
    # error handling
    confirmChoiceInput = int(input('1. To find out more or\n2. To choose this category or\n0. To move back\n>>>'))

    if choice == 'category':

        while terminateLoop:
            match confirmChoiceInput:
                case 1:
                    print(categoryDescriptionList[userInput])
                    terminateLoop = False
                    # add choice!
                case 2:
                    terminateLoop = False
                    chooseTopUp(userInput)
                case 0:
                    chooseCategory()
                case _:
                    print('Invalid choice')

    else:
        print(topUpList[userInput][3])
        if topUpList[userInput][3] == '':
            topUpOutputPhrase = 'from 2025-08-31T23:00:00+00:00 to 2026-07-31T22:59:00+00:00'
        else:
            topUpOutputPhrase = 'for ' + topUpList[userInput][4]
            if topUpList[userInput][4] == 1:
                topUpOutputPhrase += topUpList[userInput][3][:-1]
            else:
                topUpOutputPhrase += ' ' + topUpList[userInput][3]

            topUpOutputPhrase += 'providing you with ' + topUpList[userInput][5] + ' ticket'

            if topUpList[userInput][5] != 1:
                topUpOutputPhrase += 's'

        if topUpList[userInput][7] == '1':
            topUpOutputPhrase2 = '.'
        else:
            topUpOutputPhrase2 = ' and for a group of ' + topUpList[userInput][7] + ' people.'

        while terminateLoop:
            match confirmChoiceInput:
                case 1:
                    print(topUpList[userInput][1], 'That costs £' , int(int(topUpList[userInput][2]) / 100), 'and lasts', topUpOutputPhrase + '. This ticket is designed for', topUpList[userInput][6] + topUpOutputPhrase2)
                    terminateLoop = False
                    #add choice!
                case 2:
                    terminateLoop = False
                    chooseTopUp(userInput)# finish function!
                case 0:
                    chooseTopUp()
                case _:
                    print('Invalid choice')



# Lets you choose top-up and describes different features of it
def chooseTopUp(categoryChoiceInput):
    #order of variables, use of functions,
    topUpList = []
    terminateLoop = True
    i = 1

    with open('mobile_products.csv', 'r') as file1:
        csvFile1 = csv.DictReader(file1)
        for line in csvFile1:
            if line['category_title'] == categoryList[categoryChoiceInput]:
                topUpList.append([line['topup_title'], line['topup_description'], line['topup_price_in_pence'], line['topup_entitlement_unit'], line['topup_entitlement_value'], line['topup_entitlement_quantity'], line['topup_passenger_class_name'], line['topup_passenger_class_quantity']])


    for data in topUpList:
        print(str(i) + '.', str(data[0]))
        i += 1

    while terminateLoop:
        topUpChoiceInput = int(input('To find out more or buy a ticket please enter the number.\n>>>'))
        topUpInputNumber = topUpChoiceInput - 1 # ???????????
        if 0 > topUpChoiceInput - 1 or topUpChoiceInput > len(topUpList):
            print('Invalid choice')

        else:
            terminateLoop = False
            print('You have chosen ' + topUpList[topUpInputNumber - 1][0])
            confirmChoice('topUp', topUpInputNumber, topUpList)


print('===>>> BUS APP <<<===')

#going through csv
with open('mobile_products.csv', 'r') as file:
    csvFile = csv.DictReader(file)
    categoryList = []
    categoryDescriptionList = []
    # categoryObjectList
    # code = 0


    for lines in csvFile:
        if lines['category_title'] not in categoryList:
            categoryList.append(lines['category_title'])
            categoryDescriptionList.append(lines['category_description'])
            # thisCat = category(code, lines['category_title'], lines['category_description'])
            # categoryObjectList.append(thisCat)
            # code += 1

    chooseCategory()
# buyTickets()

