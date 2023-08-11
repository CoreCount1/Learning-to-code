print("2 circle overlap calculator")
print("put the coordinates and radius in the following boxes and this calculator will tell you if they overlap")

x_coordinate_1 = int(input("X coordinate for the first circle"))
print("X Coordinate1: " + str(x_coordinate_1))

y_coordinate_1 = int(input("Y coordinate for the first circle"))
print("Y Coordinate1: " + str(y_coordinate_1))

radius_1 = int(input("Radius for the first circle"))
print("Radius1: " + str(radius_1))

x_coordinate_2 = int(input("X coordinate for the second circle"))
print("X Coordinate2: " + str(x_coordinate_2))

y_coordinate_2 = int(input("Y coordinate for the second circle"))
print("Y Coordinate2: " + str(y_coordinate_2))

radius_2 = int(input("Radius for the second circle"))
print("Radius2: " + str(radius_2))

distance_between_centers = ((x_coordinate_2 - x_coordinate_1) ** 2 + (y_coordinate_2 - y_coordinate_1) ** 2) ** 0.5

if distance_between_centers < radius_1 + radius_2:
    print("Your selected circles overlap")
else:
    print("Your selected circles do not overlap")
