#Write a program which accept radius of circle and prints area of circle
import math
def CalculateAreaOfCircle(radius):
    return math.pi * radius * radius    
def main(): 
    print("Enter radius of the circle:")
    radius = float(input())
    area = CalculateAreaOfCircle(radius)
    print("Area of circle is: {area}")
if __name__ == "__main__":
    main()