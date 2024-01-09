# 3. Write a program that manages a list of countries and their capital cities. It should
# prompt the user to enter the name of a country. If the program already "knows"
# the name of the capital city, it should display it. Otherwise it should ask the user to
# enter it. This should carry on until the user terminates the program (how this
# happens is up to you).
# Note: A good solution to this task will be able to cope with the country being entered
# variously as, for example, "Wales", "wales", "WALES" and so on.


# Initialize an empty dictionary to store countries and their capitals
countries = {}

while True:
    # get input
    country = input("Enter a country (or 'q' to stop): ")
    
    # Convert the country name to lowercase
    country = country.lower()
    
    # Check if the user wants to quit
    if country == 'quit':
        break
    
    # Check if the country is in the dictionary
    if country in countries:
        print(f"The capital of {country} is {countries[country]}")
    else:
        # If the country is not in the dictionary, ask the user for the capital
        capital = input(f"I don't know the capital of {country}. Please enter it: ")
        countries[country] = capital
        print(f"Data updated. The capital of {country} is {countries[country]}")
