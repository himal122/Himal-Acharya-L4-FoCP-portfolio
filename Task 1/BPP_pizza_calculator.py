# function defination to get input from the user
def get_user_input(get_str):
    # looping until a valid integer is entered
    while True:
        try:
            num = int(input(get_str))
            # check if the entered number is positive integer
            if num <= 0:
                print("Pleasen enter a positive integer greater than 0!")
            else:
                return num

        except ValueError:
            # handles non-integer inputs
            print("Please enter a number!")

# another function defination to get a valid yes or no from the user
def get_yes_no(get_str):

    while True:
            yes_no_answer = input(get_str).strip().upper()
            # check if the user's answer is yes(y) or no(n)
            if yes_no_answer not in ['Y', 'N']:
                print("Please answer 'Y' or 'N'.")
            else:
                return yes_no_answer

# function defination to calculate the price of pizza order
def calculate_price(total_pizzas, tuesday_offer, delivery_required, bpp_app_use):
    # calculate total price of pizzas
    total_price = total_pizzas * 12

    # calculate tuesday offer
    if tuesday_offer == 'Y':
        total_price *= 0.5 # 100% - 50%

    # calculate delivey costs if required and add £2.50 if less than 5 pizzas are ordered
    if delivery_required == 'Y' and total_pizzas < 5:
        total_price += 2.5

    # apply 25% of discount if the order is made using BPP app
    if bpp_app_use == 'Y':
        total_price *= 0.75 # 100% - 25%

    return total_price

# display total price
def display_total_price(total_price):
    print(f"\nTotal Price: £{total_price:.2f}.")

# print program title as shown in the examples
print("\nBPP Pizza Price Calculator")
print("==========================\n")

# get the number of ordered pizzas
total_pizzas = get_user_input("How many pizzas ordered? ")

# get delivery requirement
delivery_required = get_yes_no("Is delivery required? ")

# get tuesday status
tuesday_offer = get_yes_no("Is it Tuesday? ")

# get ap usage
bpp_app_use = get_yes_no("Did the customer use the app? ")

# calculate the total price of pizza ordered
total_price = calculate_price(total_pizzas, tuesday_offer, delivery_required, bpp_app_use)

# display total price
display_total_price(total_price)