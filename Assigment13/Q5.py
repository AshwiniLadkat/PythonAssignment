#write a program which accept marks and display grade
def display_grade(marks):
    if marks >= 75:
        return "Distinction"    
    elif marks >= 60 and marks < 75:
        return "First Class"
    elif marks >= 50 and marks < 60:
        return "Second class"
    elif marks < 50:
        return "Fail"
    else:
        return "Invalid marks entered"
def main():
    print("Enter marks to display grade:")
    marks = int(input())
    grade = display_grade(marks)
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()