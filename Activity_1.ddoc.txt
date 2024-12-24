
# Act 1 
result = None
while True:  
    numOne = int(input('Enter first number: '))  
    numTwo = int(input('Enter second number: '))
    userOperator = input('Enter your desired operator (+, -, /, *): ')

    if userOperator == '+':
        result = numOne + numTwo
    elif userOperator == '-':
        result = numOne - numTwo
    elif userOperator == '*':
        result = numOne * numTwo
    elif userOperator == '/':
        if numTwo != 0:  
            result = numOne / numTwo
        else:
            print ('Error! Division by zero is not allowed.')
    else:
        print('Entered operator is not in the options')

    print("The result of your input is:" , result)

    # Ask the user if they want to continue
    continueOption = input("Type Y to continue or N to exit: ")
    if continueOption.lower() != 'y':
        print('You have exited the calculator.')
        break
