# In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π)

pi = 3.14   # value of pi = 3.14
r = 84     # radius = 84 meters

pond_area = pi*r*r    # calculating circle area

print(f"The are of pond is {pond_area} meters square.")

# ----------------------------------- #
# Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter

per_square = 1.4

total_water = per_square*pond_area

print(f"The total amount of water in the pond is {total_water} liters.")