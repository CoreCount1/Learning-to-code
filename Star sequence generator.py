print("Star sequence generator") # the name is more impressive than the program

user_input = int(input("Enter your chosen number: (no decimals or negatives) ")) # the user inputs a number sounds crazy i know
i = 0
j = 0

while user_input <= 0: # if the user inputs a negative number or 0 the program will tell them to try again
    int(input("Please enter a positive number: "))

while i < user_input: # while i is less than the number the user inputted it will print a star, so if user inputted 3 this will print up to 2 stars before stopping
    print("*" * i) # Starting from zero.
    i += 1 # counts up to the number the user inputted

while i >= j: # prints the stars in reverse order, so if the user inputted 3 it will print 2 stars then 1 star then 0 stars
   print("*" * i)  # this prints the exact number of stars as the user inputted 
   i -= 1 # starts counting down to zero here
