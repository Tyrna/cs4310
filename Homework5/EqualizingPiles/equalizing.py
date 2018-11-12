## CS 4310 - Algorithms Problem 1, HW 5
## By: Oscar Vanderhorst
## Using: Python3

# -----------------------------------------------------------------

def main():
    #f = open(input("Please provide the name of the input file. Example: input.txt\n"), "r+")
    f = open("input.txt", "r+")

    #Get n; number of piles
    n = int(f.readline())

    #Get the next like that has n integers
    piles = [int(x) for x in list(f.readline().split(" "))]

    #First get the summation of cards on all pile, to now what we are equalizing to
    sumVal = reduce((lambda x, y: x + y), piles)

    #Check if (sumOfNumbers % n != 0), if it is, the input is invalid
    if (sumVal % n):
        print("The input is invalid.\n\tThe remainder of the sumation of the numbers by the amount of numbers is not 0")
        exit(0)

    #Get the desired value you want the piles to be
    eqVal = sumVal/n

    #Let's find out the minimum amount of movements to equalize this list...
    movements = 0
    toMove = 0
    for i in range(0, n):
        #If we have to move...
        if (piles[i] != eqVal):
            movements = movements + 1
            toMove = piles[i] - eqVal
            piles[i+1] = piles[i+1] + toMove

    print(movements)

#If called not as a module
if __name__ == "__main__":
    main()