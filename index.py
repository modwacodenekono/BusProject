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
        if 0 > categoryChoiceInput or categoryChoiceInput > len(categoryList):
            print('Invalid choice')

        else:
            terminateLoop = False
            print('You have chosen ' + categoryList[categoryChoiceInput])
            confirmChoice('category', categoryChoiceInput + 1)



# This function allows confirming choice or going back. It also works for two different parts of the program, which saves space
def confirmChoice(choice, userInput):
    terminateLoop = True
    # error handling
    confirmChoiceInput = int(input('1. To find out more or\n2. To choose this category or\n0. To move back\n>>>'))

    if choice == 'category':
        x = 1

    # while terminateLoop:
    #     match confirmChoiceInput:
    #         case 1:
    #             print(categoryDescriptionList[userInput - 1])
    #             terminateLoop = False
    #             #add choice!
    #         case 2:
    #             print('You have chosen to move on with this category')
    #             terminateLoop = False
    #             chooseTopUp(userInput)
    #         case 0:
    #             chooseCategory()
    #         case _:
    #             print('Invalid choice')

    while terminateLoop:
        match confirmChoiceInput:
            case 1:
                print(categoryDescriptionList[userInput - 1])
                terminateLoop = False
                #add choice!
            case 2:
                print('You have chosen to move on with this category')
                terminateLoop = False
                chooseTopUp(userInput)
            case 0:
                chooseCategory()
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
    #            2025-08-31T23:00:00+00:00 2026-07-31T22:59:00+00:00

    for data in topUpList:
        print(str(i) + '.', str(data[0]))
        i += 1

    while terminateLoop:
        topUpChoiceInput = int(input('To find out more or buy a ticket please enter the number.\n>>>'))
        topUpInputNumber = topUpChoiceInput - 1
        if 0 > topUpChoiceInput - 1 or topUpChoiceInput > len(topUpList):
            print('Invalid choice')

        else:
            terminateLoop = False
            print('You have chosen ' + topUpList[topUpInputNumber - 1][0])
            confirmChoice('topUp', topUpInputNumber)


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

