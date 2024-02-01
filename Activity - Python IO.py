#Code By: Andur909
#Date Created: 02/01/2024
#Date Finished: 02/01/2024

#Sets Functions for Arithmetic operations
def add(num1, num2):
    total = num1 + num2
    return total

def sub(num1, num2):
    total = num1 - num2
    return total

def divide(num1, num2):
    total = num1 / num2
    return total

def mult(num1, num2):
    total = num1 * num2
    return total

def mod(num1, num2):
    total = num1 % num2
    return total

def main():
    #Aks for name
    fname = str(input("First Name: "))
    lname = str(input("Last Name: "))
    midinit = str(input("Middle Initial or NA: "))
    
    #Check for Middle Initial
    if midinit == "NA":
        fullname = fname + " " + lname
    else:
        fullname = fname + " " + midinit + " " + lname
    print(fullname)

    operation = int(input("1 - Add, 2 - Subtract, 3 - Divide, 4 - Multiply, 5 - Mod: "))

    #Ask for Number to user in operations
    num1 = int(input("1st Number: "))
    num2 = int(input("2nd Number: "))

    #Switch Statements that runs function based on input
    switch = {
        1 : add,
        2 : sub,
        3 : divide,
        4 : mult,
        5 : mod
        }
    total = switch.get(operation, "error")(num1, num2)
    print("total: " + str(total))

    #Runs The Function (Main) over and over again
    main()
    
if __name__ == "__main__":
    main()
