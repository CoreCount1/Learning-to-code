print("rabbit population calculator")
print("please enter how many years that the population will multiply for")

user_input_year_only = int(input("Input desired year here, example: 2")) # defines the user input as the input to use in the equation, also asks the user for the year they want
user_input_rabbit_value = int(input("please enter desired number of rabbits"))
sqr_number = (user_input_year_only * 12)  // 3  # spooky math, by doing, say 1 year * 12 gets you the months. the / 3 gets you the number of times to square (its when they double) 2 (in this case 4)
Answer = (2 ** sqr_number) * user_input_rabbit_value # to get the answer you sqr 2 (in this case 4 times) then its times by the number of rabbits to get the answer
print(Answer)
