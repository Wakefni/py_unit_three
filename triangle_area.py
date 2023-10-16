# Nicholas Wakefield
# Calculate area of triangle
import math
def triangleArea(sideA,sideB,sideC):
    s = (sideA+sideB+sideC)/2
    area = math.sqrt(s*(s-sideA)*(s-sideB)*(s-sideC))
    print(area)

def main():
    sideA = input("How big is side A: ")
    sideB = input("How big is side B: ")
    sideC = input("How big is side C: ")
    triangleArea(float(sideA),float(sideB),float(sideC))
main()