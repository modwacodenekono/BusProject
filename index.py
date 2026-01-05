import csv

print('bus app')





# except FileNotFoundError:
#    print(f"File is not found")

# def buyTickets():




def chooseCategory():
    i = 1
    terminateLoop = True

    for data in categoryList:
        print(str(i) + '.', str(data))
        i += 1
    for data in categoryDescriptionList:
        print(str(i) + '.', str(data))
        i += 1

    #error handling
    while terminateLoop:
        categoryChoiceInput = int(input('To find out more or buy a ticket please enter the number.\n>>>'))
        if 0 <= categoryChoiceInput - 1 <= len(categoryList):
            terminateLoop = False
            print('You have chosen ' + categoryList[categoryChoiceInput - 1])


        else:
            print('Invalid choice')

def confirmChoice():
    # error handling
    confirmChoiceInput = int(input('1. To find out more or\n2. To choose this category or\n0. To exit\n>>>'))

    while terminateLoop:
        categoryChoice = int(input('To find out more or buy a ticket please enter the number.\n>>>'))
        if 0 <= categoryChoice - 1 <= len(categoryList):
            terminateLoop = False
            print('You have chosen ' + categoryList[categoryChoice - 1])


        else:
            print('Invalid choice')

        match confirmChoiceInput:
            case 1:
                print('You have chosen to move on with this category')



            case 2:
                print('You have chosen to buy a ticket')
            case 0:
                chooseCategory()


with open('mobile_products.csv', 'r') as file:
    csvFile = csv.DictReader(file)
    global categoryList
    global categoryDescriptionList
    categoryList = []
    categoryDescriptionList = []
    # global categoryObjectList
    code = 0


    for lines in csvFile:
        if lines['category_title'] not in categoryList:
            categoryList.append(lines['category_title'])
            categoryDescriptionList.append(lines['category_description'])
            # thisCat = category(code, lines['category_title'], lines['category_description'])
            # categoryObjectList.append(thisCat)
            # code += 1

    chooseCategory()
# buyTickets()

