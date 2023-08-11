print("fixx-buzz game")
print("due to poor technology (my brain) in canada i am not able to make a more interesting game")

user_input_number = int(input("Put in a non decimal number"))
if user_input_number % 3 == 0: # if divisible by 3 with 0 remainder
    if user_input_number % 5 == 0: # if divisible by 5 with 0 remainder
        print("fizz-buzz")
    else: # if divisible by 3 but not 5
        print("fizz")
else:
    print(user_input_number)
