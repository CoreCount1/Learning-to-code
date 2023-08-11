print("right angle triangle calculator")
print("This determines whether or not your three numbers make a right angle triangle")

first_number = float(input("First number, it can be a decimal/negative"))
second_number = float(input("Second number, it can be a decimal/negative"))
third_number = float(input("Third number, it can be a decimal/negative"))


if  (first_number ** 2 + second_number ** 2) == third_number ** 2: #a2 + b2 = c2 is more convienient than square rooting it back into a + b = c probably faster as well
    print("your numbers do make a right angled triangle")
elif    (second_number ** 2 + third_number ** 2) == first_number ** 2:
    print("your numbers do make a right angled triangle")
elif    (third_number ** 2 + first_number ** 2) == second_number ** 2:
    print("your numbers do make a right angled triangle")
else: 
    (print("your numbers dont make a right angled triangle"))
  
