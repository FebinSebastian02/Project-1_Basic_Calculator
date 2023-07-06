#Functions are defined
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

print("!!!Welcome to Arithmetic machine!!!")

#While loop is used to repeat the arithmetic operations until the user quits the program
while True: #Used to repeat a block of code continously. A logic must be given to break this loop
#Possible arithmetic operations are displayed to the user
    print("\nThe following operations can be performed")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Quit")

#Choice of arithmetic operation is asked to the user and respective functions are called depending upon choice
    choice = int(input("\nEnter 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division, 0 for quitting the program..."))
    if choice == 1:
        # Inputs are taken from the user
        num1 = int(input("Enter a number..."))
        num2 = int(input("Enter a number..."))
        result = add(num1, num2)
        print("The sum of {} and {} is {}".format(num1, num2, result))
    elif choice == 2:
        # Inputs are taken from the user
        num1 = int(input("Enter a number..."))
        num2 = int(input("Enter a number..."))
        result = sub(num1, num2)
        print("The difference of {} and {} is {}".format(num1, num2, result))
    elif choice == 3:
        # Inputs are taken from the user
        num1 = int(input("Enter a number..."))
        num2 = int(input("Enter a number..."))
        result = mul(num1, num2)
        print("The product of {} and {} is {}".format(num1, num2, result))
    elif choice == 4:
        # Inputs are taken from the user
        num1 = int(input("Enter a number..."))
        num2 = int(input("Enter a number..."))
        result = div(num1, num2)
        print("The result is {}".format(result))
    elif choice == 0:
        print("Bye, See you soon!!!")
        quit()  #It's an inbuilt function used to quit the program
    else:
        print("Invalid choice entered. Please enter a valid choice")
