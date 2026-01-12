# BusTicketPythonProject
App which allows you to purchase bus tickets

At first the user should be greeted. After that he will be asked the purpose of the visit. It's ether to buy tickets, leave or login as an admin. 

1. User will be given a choice of categories. This will look like: "1. Group Tickets." When the category is chosen, the user will be given top-up options. At each stage the last option will be "description of all categories." When a top-up option is chosen, the user will be able to see the price time range and other details. After that the user will be able to purchase the ticket, and information about time, ticket type and user himself will be stored in a different csv file. User will be brought back to the beginning of p1

2. User will be asked to enter login and password. If they are incorrect user will have to do it again. They are checked by a class function to get the variable from the class. Now admin can change prices of the tickets. At all points a logout option should be available


--------------------------------------------------------------
--------------------------------------------------------------
--------------------------------------------------------------


##Use case diagrams

┌─────────────────────────────────────┐
│               User                  │
├─────────────────────────────────────┤
│ - categoryList: List[str]           │
│ - categoryDescriptionList: List[str]│
├─────────────────────────────────────┤
│ + getCategoryList(): List[str]      │
│ + getCategoryDescriptionList():     │
│   List[str]                         │
│ + loadData(): void                  │
└─────────────────────────────────────┘


┌─────────────────────────────────────┐
│               Admin                 │
├─────────────────────────────────────┤
│ + adminRestriction: bool = True     │
│ - adminUsername: int                │
│ - adminPassword: int                │
├─────────────────────────────────────┤
│ + __init__(username: int,           │
│   password: int): void              │
│ + getAdminUsername(): int           │
│ + getAdminPassword(): int           │
│ + adminLogIn(username: int,         │
│   password: int): void              │
│ + change_product_price(             │
│   category_name: str,               │
│   topup_name: str,                  │
│   new_price_pence: int): bool       │
│ + changePrice(): void               │
└─────────────────────────────────────┘

##Modules used

csv, datetime, os

I created admin as a separate class

##References

Lecture presentation

https://docs.python.org/3/library/csv.html

https://www.w3schools.com/python/python_file_open.asp

https://docs.python.org/3/library/exceptions.html

https://www.w3schools.com/python/python_try_except.asp

https://www.w3schools.com/python/python_string_formatting.asp

https://www.reddit.com/r/learnpython/comments/1hrd60d/pc_clock_connection_with_python/

https://docs.python.org/3/library/datetime.html

https://www.w3schools.com/python/python_file_write.asp

https://docs.python.org/3/library/functions.html#open

https://www.geeksforgeeks.org/python/python-os-path-exists-method/


