print("This program will tell you if your number is higher/lower than your previous number")
print("If you want to quit, enter 0")

x = float(input("Enter a number: "))

if x == 0:
    print("Goodbye!")
    exit() # i know what it do, but how it do, do not know

while x != 0: # if zero code dies, if not code runs
    y = float(input("Enter another number to compare against: "))
    if x == y: 
        print("Equal")
    elif x < y: 
        print("Higher")
    elif x > y:
        print("Lower")
    x = y # this switches the numbers so the first = second and second = third and so on
