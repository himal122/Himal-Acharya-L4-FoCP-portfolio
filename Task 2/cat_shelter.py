# import sys module to access command line
import sys

# constants
OURS = "OURS"
THEIRS = "THEIRS"

def format_time(minutes):
    # Convert minutes to hours and remaining minutes
    hours = minutes // 60
    minutes = minutes % 60
    
    # Format the time based on the presence of hours
    if hours == 0:
        return f"{minutes} Minutes"
    elif hours == 1:
        return f"{hours} Hour, {minutes} Minutes"
    else:
        return f"{hours} Hours, {minutes} Minutes"
    

# define function to analyze the log files
def analyze_log_file(lines):
    # initialize variables
    cat_visits, other_cats, total_time = 0, 0, 0
    min_time, max_time = sys.maxsize, 0

    # iterate through each lines of logs file and break when END line is encountered
    for line in lines:
        if line == "END\n":
            break
        # split the line by comma to extract file values
        file_values = line.strip().split(",")
        # skip lines with invalid number of values
        if len(file_values) != 3:
            continue

        cat_type, entry_time, exit_time = file_values

        # handle the file if entry and exit time is not an integer or entry time is greater than exit time
        try:
            entry_time, exit_time = int(entry_time), int(exit_time)
        except ValueError:
            print(f"\n{line}Skipped! Non-integer entry or exit time.")
            print(f"----------------------------------------")
            continue

        if entry_time > exit_time:
            print(f"\n{line}Skipped! Entry time is greater than exit time.")
            print(f"----------------------------------------------")
            continue

        if cat_type not in [OURS, THEIRS]:
            print(f"\n{line}Skipped! Unrecognized cat type")
            print(f"------------------------------")
            continue

        # calculate total duration of cats in shelter
        total_duration = exit_time - entry_time

         # Update variable based on cat type
        if cat_type == OURS:
            cat_visits += 1
            total_time += total_duration
            min_time = min(min_time, total_duration)
            max_time = max(max_time, total_duration)
        elif cat_type == THEIRS:
            other_cats += 1

    # return the anlyzed values
    return cat_visits, other_cats, total_time, min_time, max_time

# function defination to display the analyzed result
def display_analyzed_result(cat_visits, other_cats, total_time, min_time, max_time):

    # print the result
    if cat_visits == 0:
        print("Our cats visits are not recorded in the file.")
        return
    
    print("\nLog File Analysis")
    print("==================\n")
    print(f"Cat Visits: {cat_visits}")
    print(f"Other Cats: {other_cats}\n")
    print(f"Total Time in House: {format_time(total_time)}\n")
    print(f"Average Visit Length: {format_time(total_time // cat_visits)}") # calculates average visit length
    print(f"Longest Visit:        {format_time(max_time)}")
    print(f"Shortest Visit:       {format_time(min_time)}\n")


# main function defination to handle the command line agrguments and use file handling to read the log files
def main():
    # Check if the correct number of command line arguments is entered
    if len(sys.argv) != 2:
        print("Missing command line argument!")
        sys.exit(1)
    
    # get the file name from the command line arguement
    file_name = sys.argv[1]

    try:
        # open file and read all the lines
        with open(file_name) as file:
            lines = file.readlines()

        # Analyze the log and print the results
        cat_visits, other_cats, total_time, min_time, max_time = analyze_log_file(lines)
        display_analyzed_result(cat_visits, other_cats, total_time, min_time, max_time)

    except FileNotFoundError:
        # handle file not found error
        print(f"Cannot open \"{file_name}\"!")
        sys.exit(1)


main()
