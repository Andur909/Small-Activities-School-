#Name: Anderson R.
#Description: While Loop Tutorial
#Start Date: 02-06-2024
#End Date: 02-06-2024

def main():
    Initialize()

def Initialize():
    wordguess = "apple, pear, cucumbers, shoe, watermelon";
    msg = "try to guess my word. \nYou only have attempts."
    print(msg + "\n" + wordguess)
    AskInput();

def AskInput():
    userinput = ""
    attempts = 4
    wordgame = "apple"

    userinput = str(input("Enter Word: "))
    while (attempts > 1 and userinput != "apple"):
        attempts -= 1
        print("You have " + str(attempts) + " attempts left")
        userinput = str(input("Enter a word: "));
        
    if (attempts == 1 and userinput != "apple"):
        print("You Lost")
    else:
        print("congrats")

if __name__ == "__main__":
    main()
