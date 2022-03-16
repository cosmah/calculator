def calculate():
    firstNum = int(input("enter the first number: "))
    operator = input("Whats the operator? ")
    secondNum = int(input("enter the second number: "))

    if operator == '+':
        print('{}+{} '.format(firstNum, secondNum))
        print(firstNum + secondNum)
    elif operator == '-':
        print('{}-{} '.format(firstNum, secondNum))
        print(firstNum - secondNum)
    elif operator == '*':
        print('{}*{} '.format(firstNum, secondNum))
        print(firstNum * secondNum)
    elif operator == '/':
        print('{}/{} '.format(firstNum, secondNum))
        print(firstNum / secondNum)
    else:
        print('syntax error')


calculate()
