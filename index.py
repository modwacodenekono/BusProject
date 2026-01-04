print('bus app')


def buyTickets():
    print('buy tickets')


def adminLogIn():
    adminLogInInput1 = int(input('Wellcome to Admin Log In\nPlease enter your Username\n>>>'))
    adminLogInInput2 = int(input('Now please enter your Password\n>>>'))

    if adminLogInInput1 == 123456 and adminLogInInput2 == 123456:
        print('You have successfully logged in as an admin')
    else:
        print('Incorrect Username or Password')


def startMenu():
    # Menu system

    endStartMenuLoop = True

    while True:
        try:
            menuInput = int(input('Wellcome to Bus Ticket App\n1. To buy tickets enter 1\n2. To log in as an admin press 2\n0. To exit enter 0\n>>>'))

            # Alternative to if
            match menuInput:
                case 1:
                    endStartMenuLoop = False
                    buyTickets()
                case 2:
                    endStartMenuLoop = False
                    adminLogIn()
                case 0:
                    exit()
                case _:
                    print('Please enter a correct number. Valid numbers are 1, 2 and 0\n')

        # Expecting a user to enter a letter
        except ValueError:
            print('Please enter a valid input. A valid input is a number\n')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

