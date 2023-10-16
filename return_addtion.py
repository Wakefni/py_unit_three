def getNumberOne():
    '''
    :return: returns the first number
    '''
    falseNum1 = input("What is your first number?: ")
    num1 = float(falseNum1)
    return num1

def getNumberTwo():
    '''
    :return: returns the second number
    '''
    falseNum2 = input("What is your second number?: ")
    num2 = float(falseNum2)
    return num2
def addThemTogether(num1, num2):
    '''
    :param num1: The first number to be added
    :param num2: The second number to be added
    :return: The solution to the equation
    '''
    solution = num1 + num2
    return solution

def main():
    x = getNumberOne()
    y = getNumberTwo()
    print(addThemTogether(x,y))
main()