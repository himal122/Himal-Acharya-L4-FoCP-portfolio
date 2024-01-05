# 4. A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.


# getting input
total_sweets = int(input("Enter the total number of sweets: "))
num_of_pupils = int(input("Enter the number of pupils: "))

# calculating no. of sweets and lef overs
sweets_per_pupil = total_sweets // num_of_pupils
total_left_over_sweets = total_sweets % num_of_pupils

if total_left_over_sweets > 1:
    left_over_sweets = 'sweets'
else:
    left_over_sweets = "sweet"

# displaying output
print(f"Each pupil will receive {sweets_per_pupil} sweets and there will be {total_left_over_sweets} {left_over_sweets} left over.")