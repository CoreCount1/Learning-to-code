print("number swapper, input your two numbers")
first_number = int(input("first number"))
second_number = int(input("second number"))

first_answer = first_number - first_number + second_number 
second_answer = second_number - second_number + first_number 

first_printed_answer = ("first number:" + str(first_answer))
second_printed_answer = ("second number:" + str(second_answer))

print(first_printed_answer)
print(second_printed_answer)