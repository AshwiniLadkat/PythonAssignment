#Write a program which accept length and width of rectangle and prints area 
def CalculateAreaOfRectangle(length, width):
    return length * width
def main(): 
    print("Enter length of the rectangle:")
    length = int(input())
    print("Enter width of the rectangle:")  
    width = int(input())
    area = CalculateAreaOfRectangle(length, width)
    print("Area of rectangle is: {area}")
if __name__ == "__main__":
    main()