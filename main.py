"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""

# initialize total to 0
total = 0

for i in range(5):

    # make this input an int
    number = int(input("Enter a number: "))
    
    total += number

# add a comma after the string literal
print("The running total is: ", total)
