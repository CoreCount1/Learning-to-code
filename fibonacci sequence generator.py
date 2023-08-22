print("strange fibonacci sequence generator")

user_input_quanitity = int(input("how many numbers do you want to generate? "))
first = 0
second = 1
i = 0

while user_input_quanitity <= int(0):
    print("if you dont wanna generate any numbers, why did you run this program?")
    user_input_quanitity = int(input("how many numbers do you want to generate? "))

# bold of you to assume i know how to do the next part without googling it

while i < user_input_quanitity: # besides this, i did this part without googling it
    print(first)
    first = first + second
    second = first - second
    i += 1 # besides this, i did this part without googling it