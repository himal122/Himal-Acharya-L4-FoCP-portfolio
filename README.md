## Computer Programming Portfolio

### Overview
This is my programming portfolio for the Computer Programming course at Leeds Beckett University. It shows how I progressed and achieved throughout the term. I have done different programming activities and assignments, showing that I can understand and apply procedural programming ideas and write working computer programs using Python 3. In this portfolio, you will see how I learned and improved, as shown in the weekly tasks, three programming tasks (Task1, Task2, Task3). The README.md file explains how I think, solve problems, and make decisions when I create various programming solutions.

### Repository Structure
- **Portfolio**: Contains weekly task folders for each week.
  - **Week 1**: Includes Exercises01.pdf and solutions for 4 programming problems from Week 1.
  - **Week 2**: Contains Exercises02.pdf, Practical02.pdf, and solutions for 4 programming problems from Week 2.
  - **Week 3**: Consists of Exercises03.pdf, Practical03.pdf, and solutions for 8 programming problems from Week 3.
  - **Week 4**: Consists of Exercises04.pdf, Practical04.pdf, and solutions for 8 programming problems from Week 4.
  - **Week 5**: Holds Exercises05.pdf, Practical05.pdf, solutions for 6 programming problems, and 2 demofile.txt files from Week 5.
  - **Week 6**: Consists of Exercises06.pdf, Practical06.pdf, and solutions for 6 programming problems from Week 6.
  - **Week 7**: Contains Exercises07.pdf and solutions for 4 programming problems from Week 7.
  - **Week 8**: Holds Exercises08.pdf, Practical08.pdf, solutions for 5 programming problems, 6 demofile.txt files, and a dictionary - words_alpha.txt from Week 8.

- **Task 1**: Includes a Python script named BPP_pizza_calculator.py.
  - The script calculates pizza orders with discounts based on user inputs regarding delivery, day of the week, and app usage.
  
- **Task 2**: Contains a Python script named cat_shelter.py along with 3 additional shelter.log files.
  - The program analyzes shelter.log files, calculates various values, and displays results based on command line arguments. If no arguments are provided, an error is shown: "Missing command line arguments."
  
- **Task 3**: Holds 6 Python scripts and a passwd.txt file containing user details.
  - **adduser.py**: Adds a new user to passwd.txt if the username is not in use.
  - **common_functions.py**: Contains 3 common functions shared across all scripts.
  - **deluser.py**: Deletes a user from passwd.txt.
  - **login.py**: Checks the validity of a given username and password combination.
  - **passwd.py**: Changes the password for a user in passwd.txt.
  - **main.py**: Imports user-created modules, prompts for commands (adduser, deluser, passwd, login), and runs the scripts as the main program.
  - **passwd.txt**: File containing user details (username, real name, password).

### Task Details

#### Task 1: Pizza Calculator (BPP_pizza_calculator.py)
**Description**:
- The script `BPP_pizza_calculator.py` facilitates the calculation of the price for a pizza order based on various user inputs. It prompts the user for information such as the number of pizzas ordered, delivery requirement, Tuesday status (for special offers), and whether the BPP app was used. The script incorporates input validation and applies discounts to determine the total price of the pizza order.

**Code Summary**:
- The script defines three key functions:
  - `get_user_input(get_input)`: Prompts the user for input, validates it, and returns a positive integer.
  - `get_yes_no(get_input)`: Prompts the user for a yes or no answer and validates it.
  - `price_breakdown(total_price, cost_per_pizza, tuesday_discount, delivery_cost, app_discount, total_pizzas)`: Displays a breakdown of the total price, including individual costs and discounts.
- The main program (main) utilizes these functions to collect user inputs, calculate the total price based on specified conditions, and display the price breakdown to the user. Discounts such as the Tuesday offer and the BPP app discount are applied accordingly.

**Example Usage**:

```text
PS D:\Second Year\First Sem\FOCP\Task 1> python BPP_pizza_calculator.py

===================================== BPP Pizza Price Calculator
How many pizzas ordered? 4
Is delivery required (Y/N)? y
Is it Tuesday (Y/N)? n
Did the customer use the app (Y/N)? y

===================================== Price Breakdown
Total Pizzas:                 4
Cost per Pizza:               £12.00
Total Price w/o Discounts:    £48
Delivery Cost:                £2.50
BPP App Discount (25% off):   -£12.62

-------------------------------------
Total Price:                  £37.88
-------------------------------------

Do you want to add more orders (Y/N)? n
```
**Example Usage with Exception Handling**:

```text
PS D:\Second Year\First Sem\FOCP\Task 1> python BPP_pizza_calculator.py

=====================================
     BPP Pizza Price Calculator
=====================================

How many pizzas ordered? ten
Please enter a number!
How many pizzas ordered? -10
Please enter a positive integer greater than 0!
How many pizzas ordered? 10
Is delivery required (Y/N)? dunno
Please answer 'Y' or 'N'.
Is delivery required (Y/N)? n
Is it Tuesday (Y/N)? it's sunday
Please answer 'Y' or 'N'.
Is it Tuesday (Y/N)? n
Did the customer use the app (Y/N)? maybe
Please answer 'Y' or 'N'.
Did the customer use the app (Y/N)? n

=====================================
          Price Breakdown
=====================================

Total Pizzas:                 10
Cost per Pizza:               £12.00
Total Price w/o Discounts:    £120

-------------------------------------
Total Price:                  £120.00
-------------------------------------

Do you want to add more orders (Y/N)? y
-------------------------------------

=====================================
     BPP Pizza Price Calculator
=====================================

How many pizzas ordered? |
```
#### Task 2: Cat Shelter Analyzer (cat_shelter.py)
**Description**:
- The script `cat_shelter.py` is designed to analyze log files from a cat shelter, calculating various statistics such as the number of cat visits, time spent by our cats in the shelter, average visit length, and the longest and shortest visits. The script utilizes the sys module to access command line arguments, reads log files, and outputs the analyzed results.

**Code Summary**:
- The script defines two key functions:
  - `format_time(minutes)`: Converts minutes into a human-readable time format (hours and minutes).
  - `analyze_log_file(lines)`: Analyzes the log files, calculating statistics such as the number of cat visits, time spent, average visit length, and the longest and shortest visits.
- The main program (main) is responsible for checking if the correct number of command line arguments is provided, reading the specified log file, and performing the analysis. The results are then displayed using the `display_analyzed_result` function.

**Example Usage**:

```text
PS D:\Second Year\First Sem\FOCP\Task 2> python cat_shelter.py shelter_2023-08-26.log

Log File Analysis
==================

Cat Visits: 11
Other Cats: 45

Total Time in House: 5 Hours, 0 Minutes

Average Visit Length: 27 Minutes
Longest Visit:        45 Minutes
Shortest Visit:       10 Minutes
```
**Example Usage with Exception Handling**:

```text
PS D:\Second Year\First Sem\FOCP\Task 2> python cat_shelter.py shelter_2023-08-26.log

OURS,837.5,867.9
Skipped! Non-integer entry or exit time.
----------------------------------------

THEIRS,882,881
Skipped! Entry time is greater than exit time.
----------------------------------------------

WHOSE,904,934
Skipped! Unrecognized cat type
------------------------------

Log File Analysis
==================

Cat Visits: 11
Other Cats: 45

Total Time in House: 5 Hours, 0 Minutes

Average Visit Length: 27 Minutes
Longest Visit:        45 Minutes
Shortest Visit:       10 Minutes
```
```text
PS D:\Second Year\First Sem\FOCP\Task 2> python cat_shelter.py
Missing command line argument!
PS D:\Second Year\First Sem\FOCP\Task 2> python cat_shelter.py shelter_2023-08-26
Cannot open "shelter_2023-08-26"!
PS D:\Second Year\First Sem\FOCP\Task 2> python cat_shelter.py shelter_2023-08-26.log
Our cats visits are not recorded in the file.
```
#### Task 3: User Management System
- **3.1 adduser.py**
  - **Description**:
    - The `adduser.py` script adds a new user to the password file (`passwd.txt`) if the specified username is not already in use. It checks for the uniqueness of the username, and if valid, appends the new user details (username, real name, encoded password) to the password file.

  - **Code Summary**:
    - The script utilizes functions from the `common_functions` module to check existing usernames (`check_current_username`) and append lines to the password file (`PASSWORDS_FILE`). If the username is unique, it adds the new user details to the password file.
- **3.2 common_functions.py**
  - **Description**:
    - The module `common_functions.py` contains common functions shared across multiple scripts in the user management system. It includes functions to check existing usernames in the password file and append lines to the password file.

  - **Code Summary**:
    - The module defines functions:
      - `check_current_username(username)`: Checks if a username already exists in the `passwd.txt` file.
      - `encryption(text)`: Encrypts text using ROT13.
      - `is_lowercase(username)`: Checks whether the user entered username is in lowercase.
- **3.3 deluser.py**
  - **Description**:
    - The `deluser.py` script deletes a specified user from the password file (`passwd.txt`). It reads the existing lines from the password file, identifies the user to be deleted, and updates the file without the deleted user's details.

  - **Code Summary**:
    - The script utilizes functions from the `common_functions` module to read lines from and write lines to the password file (`PASSWORDS_FILE`). If the specified user is found, it updates the password file without the user's details.
- **3.4 login.py**
  - **Description**:
    - The `login.py` script checks if a given username and password combination is valid for login. It reads the username and password from the user, compares them with entries in the password file (`passwd.txt`), and grants access if the combination is valid.

  - **Code Summary**:
    - The script opens the `passwd.txt` file in read mode, iterates through each line, and checks if the provided username and password match any entry in the file.
- **3.5 passwd.py**
  - **Description**:
    - The `passwd.py` script changes the password for a specified user in the password file (`passwd.txt`). It reads the existing lines, checks the current password, and updates the file with the new password if the conditions are met.

  - **Code Summary**:
    - The script utilizes functions from the `common_functions` module to check existing usernames, append lines to the password file, and encode passwords. If the specified user and current password are found, it updates the password file with the new password.
- **3.6 main.py**
  - **Description**:
    - The `main.py` script serves as the main program for user interaction. It imports built-in and user-created modules (`adduser`, `deluser`, `passwd`, `login`) and prompts the user for a command. Based on the command, it executes the corresponding functionality.

  - **Code Summary**:
    - The script utilizes `getpass` for secure password input and encodes passwords using ROT13. It handles user commands (`adduser`, `deluser`, `passwd`, `login`) by calling the respective functions and providing a user-friendly interface.

  **Example Usage**:
  
  ```text
  PS D:\Second Year\First Sem\FOCP\Task 3> python main.py
  Welcome to the User Management System!
  -------------------------------------

  Commands:
  
  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command: add user
  Enter new username: himal
  Enter real name: Himal Acharya
  Enter password: himalacharya
  User Created.
  PS D:\Second Year\First Sem\FOCP\Task 3> cat passwd.txt
  keith:Keith Norton:svavfureavzoyljnfuqnl
  himal:Himal Acharya:uvznynpuneln
  ```
  
  ```text
  PS D:\Second Year\First Sem\FOCP\Task 3> python main.py
  Welcome to the User Management System!
  -------------------------------------
  
  Commands:
  
  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command: login
  Enter username: himal
  Enter password:
  Login successful!
  ```
  ```text
  PS D:\Second Year\First Sem\FOCP\Task 3> python main.py
  Welcome to the User Management System!
  -------------------------------------
  
  Commands:
  
  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command: change password
  Enter username: himal
  Enter current password:
  Enter new password:
  Confirm new password:
  Password changed.
  PS D:\Second Year\First Sem\FOCP\Task 3> cat passwd.txt
  keith:Keith Norton:svavfureavzoyljnfuqnl
  himal:Himal Acharya:uryybjbeyq
  ```
  ```text
  PS D:\Second Year\First Sem\FOCP\Task 3> python main.py
  Welcome to the User Management System!
  -------------------------------------
  
  Commands:
  
  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command: delete user
  Enter username to delete: himal
  User 'himal' deleted successfully!
  PS D:\Second Year\First Sem\FOCP\Task 3> cat passwd.txt
  keith:Keith Norton:svavfureavzoyljnfuqnl
  ```
  **Example Usage with Exception Handling**:
  
   ```text
  PS D:\Second Year\First Sem\FOCP\Task 3> python main.py
  Welcome to the User Management System!
  -------------------------------------
  
  Commands:
  
  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command: add user
  Enter new username: Himal
  Invalid username. Must be in lowercase letters and valid string.
  Enter new username: @himal
  Enter real name: Himal Acharya
  Enter password: hello
  Password must be at least 8 characters long.
  Enter password: himalacharya123
  User Created.
  PS D:\Second Year\First Sem\FOCP\Task 3> cat passwd.txt
  keith:Keith Norton:svavfureavzoyljnfuqnl
  @himal:Himal Acharya:uvznynpuneln123
  PS D:\Second Year\First Sem\FOCP\Task 3> python main.py
  Commands:
   
  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command: add user
  Enter new username: @himal
  Enter real name: Himal Acharya
  Enter password: himalacharya
  Cannot add. Most likely username already exists.
  ```
  ```text
  Commands:

  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command: login
  Enter username: himal
  Enter password:
  Login failed. Invalid username or password.
  Enter username:
  ```
  ```text
  Commands:

  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command: change password
  Enter username: himal
  Username not found. Please enter a valid username.
  Enter username: @himal
  Enter current password:
  Enter new password:
  New password must be at least 8 characters long.
  Enter new password:
  Confirm new password:
  Passwords do not match. Nothing changed.
  ```
  ```text
  Commands:

  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command: delete user
  Enter username to delete: himal
  User not found. Nothing changed.
  ```
  ```text
  PS D:\Second Year\First Sem\FOCP\Task 3> python main.py
  File not found.
  PS D:\Second Year\First Sem\FOCP\Task 3> python main.py
  Welcome to the User Management System!
  -------------------------------------
  
  Commands:
  
  1. Add User
  2. Login
  3. Change Password
  4. Delete User
  
  Enter a command:
  Program terminated by user.
  ```
- **Password File: passwd.txt**
  - **Description**:
    - The `passwd.txt` file contains user details (username, real name, encoded password) for the user management system. The user details are separated by ':' and are used by the scripts to perform user-related operations.
  - **Example Entry**:
    - `himal:Himal Acharya:uvznynpuneln`

### Language and Tools Used:
- **Programming Language**: Python 3.10.7
- **IDE/Text Editor**: Visual Studio Code (VSCode)/Windows PowerShell

### Contact Information
- **Email**: ahimal22@tbc.edu.np
- **GitHub**: [himal122](https://github.com/himal122/Himal-Acharya-L4-FoCP-portfolio)


<p align="center">This README.md file serves as documentation for my programming portfolio.</p>
