"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""
def calculate_total():
# initialize total to 0
    total = 0

    for i in range(5):

        # make this input an int
        number = int(input("Enter a number: "))
        
        total += number

    # add a comma after the string literal
    print("The running total is: ", total)
    
# Define the main function
def main():
    calculate_total()
if __name__ == "__main__": # Run main only when the script is executed directly
    main()