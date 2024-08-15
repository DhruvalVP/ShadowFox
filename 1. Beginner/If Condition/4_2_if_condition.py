"""2. Write a program to determine which country a city belongs to. Givenlist of cities per country: Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] Ask the user to enter a city name and print the corresponding country."""

# ----- List of countries and cities ----- #
countries_cities = [
    ("Australia", ["Sydney", "Melbourne", "Brisbane", "Perth"]),
    ("UAE", ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]),
    ("India", ["Mumbai", "Bangalore", "Chennai", "Delhi"])
]

# ----- Ask user for a city name ----- #
city = input("Enter a city name: ").title()

# ----- Check which country the city belongs to ----- #
for country, cities in countries_cities:
    if city in cities:
        print(f"{city} is in {country}.")
        break
else:
    print(f"The city {city} is not in our database.")

# ----- Exit Program ----- #
exit()