from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# function definition to get input from the user
def get_user_input(get_input):
    while True:
        try:
            num = int(input(get_input))
            if num <= 0:
                print(f"{Fore.RED}Please enter a positive integer greater than 0!{Style.RESET_ALL}")
            else:
                return num

        except ValueError:
            print(f"{Fore.RED}Please enter a number!{Style.RESET_ALL}")

# another function definition to get a valid yes or no from the user
def getYesNo(get_input):
    while True:
        yes_no = input(get_input).strip().upper()
        # check if the user's answer is yes(y) or no(n)
        if yes_no not in ['Y', 'N']:
            print(f"{Fore.RED}Please answer 'Y' or 'N'.{Style.RESET_ALL}")
        else:
            return yes_no

# function definition to display total price breakdown
def price_breakdown(total_price, cost_per_pizza, tuesday_discount, delivery_cost, app_discount, total_pizzas):
    print(f"\n=====================================")
    print(f"\t  {Fore.CYAN}Price Breakdown{Style.RESET_ALL}")
    print(f"=====================================\n")
    print(f"Total Pizzas:".ljust(30) + f"{Fore.CYAN}{total_pizzas}{Style.RESET_ALL}")
    print(f"Cost per Pizza:".ljust(30) + f"{Fore.CYAN}£{cost_per_pizza:.2f}{Style.RESET_ALL}")
    print(f"Total Price w/o Discounts:".ljust(30) + f"{Fore.CYAN}£{total_pizzas*pizza_price}{Style.RESET_ALL}")

    if tuesday_discount > 0:
        print(f"Tuesday Offer (50% off):".ljust(30) + f"{Fore.CYAN}-£{tuesday_discount:.2f}{Style.RESET_ALL}")

    if delivery_cost > 0:
        print(f"Delivery Cost:".ljust(30) + f"{Fore.CYAN}£{delivery_cost:.2f}{Style.RESET_ALL}")

    if app_discount > 0:
        print(f"BPP App Discount (25% off):".ljust(30) + f"{Fore.CYAN}-£{app_discount:.2f}{Style.RESET_ALL}")

    print(f"\n{Fore.WHITE}-------------------------------------{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Total Price:{Style.RESET_ALL}".ljust(39) + f"{Fore.CYAN}£{total_price:.2f}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}-------------------------------------{Style.RESET_ALL}\n")


while True:
    # Display header
    print(f"\n=====================================")
    print(f"     {Fore.CYAN}BPP Pizza Price Calculator{Style.RESET_ALL}")
    print(f"=====================================\n")

    # get the number of ordered pizzas
    total_pizzas = get_user_input("How many pizzas ordered? ")

    # get delivery requirement
    delivery_required = getYesNo(f"Is delivery required{Fore.YELLOW} (Y/N){Style.RESET_ALL}? ")

    # get Tuesday status
    tuesday_offer = getYesNo(f"Is it Tuesday{Fore.YELLOW} (Y/N){Style.RESET_ALL}? ")

    # get app usage
    bpp_app_use = getYesNo(f"Did the customer use the app{Fore.YELLOW} (Y/N){Style.RESET_ALL}? ")

    # Calculate total price
    pizza_price = 12
    total_price = total_pizzas * pizza_price

    # Apply Tuesday discount
    if tuesday_offer == 'Y':
        tuesday_discount = total_price * 0.5
        total_price -= tuesday_discount
    else:
        tuesday_discount = 0

    # Add delivery cost if required
    if delivery_required == 'Y' and total_pizzas < 5:
        delivery_cost = 2.5
        total_price += delivery_cost
    elif total_pizzas > 20:
        delivery_cost = 5
        total_price += delivery_cost
    else:
        delivery_cost = 0

    # Apply 25% discount if the app is used
    if bpp_app_use == 'Y':
        app_discount = total_price * 0.25
        total_price -= app_discount
    else:
        app_discount = 0

    price_breakdown(total_price, pizza_price, tuesday_discount, delivery_cost, app_discount, total_pizzas)

    add_more_orders = getYesNo(f"Do you want to add more orders{Fore.YELLOW} (Y/N){Style.RESET_ALL}? ")
    if add_more_orders == 'N':
        break
    print("-------------------------------------")
