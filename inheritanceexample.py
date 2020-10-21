class User:
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account_number = 0

class Employee(User):
    base_pay = 11.00
    department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True
