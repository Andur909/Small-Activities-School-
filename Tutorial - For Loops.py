#Name: Anderson R.
#Description: Tutorial on how to make for loops
#Start Date: 02/07/2024
#End Date: 02/07/2024

def main():
    AskInput();

def AskInput():
    global numgrades

    numgrades = int(input("How many grades would you like to average? "));

    if numgrades < 0:
        print("Unable to calculate infinite numbers!")
        AskInput();

    else:
        CalcAvg();

def CalcAvg():
    totalgrade = 0;

    for i in range(0,numgrades):
        grade = float(input("Enter The Grade: "));
        totalgrade = totalgrade + grade;

    avg = totalgrade / numgrades;

    print("The Average is " + str(avg));

if __name__ == "__main__":
    main();
