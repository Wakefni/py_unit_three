# Nicholas Wakefield
# Last modifed: 10/16/23
# The purpouse of this program is to calculate the area of a rectangular
# prism using user input to get the hight, width, and depth.
def printInstructions():
    '''
    This prints instructions for the user
    :return: N/A
    '''
    print("This program computes the surface area of a rectangular prism")
    print("Please insert the hight, width, and depth of the solid")
def getUserWidth():
    '''
    This gets the parameter width from the user
    :return: width of prism as a float
    '''
    width = input("Please enter the width: ")
    return float(width)
def getUserHight():
    '''
    This gets the parameter hight from the user
    :return: hight of prism as a float
    '''
    hight = input("Please enter the hight: ")
    return float(hight)
def getUserDepth():
    '''
    This gets the parameter depth from the user
    :return: depth of prism as a float
    '''
    depth = input("Please enter the depth: ")
    return float(depth)


def calculateRectangle(side1, side2):
    '''
    This calculates the area of a rectangle for ease of calculating surface area
    :param side1: one side of a rectangle
    :param side2: the other side of a rectangle
    :return: area of a rectangle
    '''
    area = side1 * side2
    return area
def calculateSurfaceArea(hight, width, depth):
    '''
    Calculates the total surface area of a rectangular prism
    :param hight: hight of the prism
    :param width: width of the prism
    :param depth: depth of the prism
    :return: total surface area of the rectangular prism
    '''
    topAndBottom = calculateRectangle(depth, width)
    leftAndRightSide = calculateRectangle(hight, depth)
    frontAndBack = calculateRectangle(hight,width)
    totalArea = topAndBottom + leftAndRightSide + frontAndBack + topAndBottom + leftAndRightSide + frontAndBack
    return totalArea
def printResult(totalArea):
    '''
    Prints the result to the user
    :param totalArea: the total surface area of the prism
    :return: N/A
    '''
    print("The surface area is:",totalArea)
def main():
    printInstructions()
    width = getUserWidth()
    hight = getUserHight()
    depth = getUserDepth()
    calculateRectangle(hight, width)
    trueTotalArea = calculateSurfaceArea(hight, width, depth)
    printResult(trueTotalArea)
main()