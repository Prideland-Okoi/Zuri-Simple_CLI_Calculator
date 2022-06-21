def welcome():
    print("Welcome to PrideApp")
welcome()

def calculation():
    num1=int(input("Please enter the first number: "))
    operation = input(''' Please type in the math operation you would like to perform
    '+' for addition 
    '-' for subtraction
    '*' for multiplication
    '-' for division
    '%' for modulus
    ''')
    num2=int(input("Please enter the second number: "))


    if operation=='+':
        print('{}+{}='.format(num1, num2))
        print(num1 + num2)
    elif operation=='-':
        print('{}-{}='.format(num1, num2))
        print(num1 - num2)
    elif operation=='*':
        print('{}*{}='.format(num1, num2))
        print(num1 * num2)
    elif operation=='/':
        print('{}/{}='.format(num1, num2))
        print(num1 / num2)
    elif operation=='%':
        print('{}%{}='.format(num1, num2))
        print(num1 % num2)
    else:
        print("You have not typed a valid operator, please run the program again")
    

def again():
    calculate_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO. 
    ''')
    if calculate_again.upper()=='Y':
        calculation()
    elif calculate_again.upper()=='N':
        print("See you later")
    else:
        again()
calculation()
again()