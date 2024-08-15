"""3.  Write  a  program  to  check  if  two  cities  belong  to  the  same  country.Ask  the  user  to  enter  two  cities  and  print  whether  they  belong  to  thesame country or not. Example: Enter the first city: "Mumbai" Enter the second city: "Chennai" Output: "Both cities are in India" Example: Enter the first city: "Sydney" Enter the second city: "Dubai" Output: "They don't belong to the same country" 
"""

# ----- List of countries and cities ----- #
countries_cities = [
    ("Australia", ["Sydney", "Melbourne", "Brisbane", "Perth"]),
    ("UAE", ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]),
    ("India", ["Mumbai", "Bangalore", "Chennai", "Delhi"])
]

# ----- Ask the user for two city names ----- #
city1 = input("Enter the first city: ").title()
city2 = input("Enter the second city: ").title()

# ----- Find the countries corresponding to the two cities ----- #
for country, cities in countries_cities:
    if city1 in cities and city2 in cities:
        print("Both cities are in " + country)
        break
else:
    print("They don't belong to the same country")

# ----- Exit Program ----- #
exit()abu dhabi