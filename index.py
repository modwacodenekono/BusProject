import csv

print('bus app')





# except FileNotFoundError:
#    print(f"File is not found")

# def openFile():




def chooseCategory():
    i = 1
    terminateLoop = True
    global categoryChoiceInput

    for data in categoryList:
        print(str(i) + '.', str(data))
        i += 1

    #error handling
    while terminateLoop:
        categoryChoiceInput = int(input('To find out more or choose a category please enter the number.\n>>>'))
        if 0 > categoryChoiceInput - 1 or categoryChoiceInput > len(categoryList):
            print('Invalid choice')

        else:
            terminateLoop = False
            print('You have chosen ' + categoryList[categoryChoiceInput - 1])
            confirmChoice('category')

def confirmChoice(choise):
    terminateLoop = True
    # error handling
    confirmChoiceInput = int(input('1. To find out more or\n2. To choose this category or\n0. To move back\n>>>'))

    if choise == 'category':
        x = 1

    while terminateLoop:
        match confirmChoiceInput:
            case 1:
                print(categoryDescriptionList[categoryChoiceInput - 1])
                terminateLoop = False
                #add choise
            case 2:
                print('You have chosen to move on with this category')
                terminateLoop = False
                chooseTouUp()
            case 0:
                chooseCategory()
            case _:
                print('Invalid choice')


def chooseTouUp():
    #order of variables, use of functions,
    topUpList = []
    topUpDescriptionList = []
    topUpPrice = []
    terminateLoop = True
    i = 1

    with open('mobile_products.csv', 'r') as file1:
        csvFile1 = csv.DictReader(file1)
        for line in csvFile1:
            if line['category_title'] == categoryList[categoryChoiceInput - 1]:
                #2d list
                topUpList.append(line['topup_title'])
                topUpDescriptionList.append(line['topup_description'])
                topUpPrice.append(line['topup_price_in_pence'])

    for data in topUpList:
        print(str(i) + '.', str(data))
        i += 1

    while terminateLoop:
        topUpChoiceInput = int(input('To find out more or buy a ticket please enter the number.\n>>>'))
        topUpInputNumber = topUpChoiceInput - 1
        if 0 > topUpChoiceInput - 1 or topUpChoiceInput > len(topUpList):
            print('Invalid choice')

        else:
            terminateLoop = False
            print('You have chosen ' + topUpList[topUpInputNumber - 1])
            confirmChoice('topUp')


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

