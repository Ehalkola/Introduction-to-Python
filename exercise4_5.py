# Ask the user are they a student and the traveling month, if not student or they are traveling on months between 6-8
# Not alleged for special prize

special_prize = False

# User input
student_yn = input("Are you a student? (yes/no): ")

# If student == yes:
if student_yn == "yes":
    special_prize = True
    travel_month = int(input("During which month are you traveling in? (1-12): "))

    # Ask the user traveling month to base the prize
    if 6 <= travel_month <= 8:
        special_prize = False
    else:
        special_prize = True
    if special_prize is True:
        print("Special prize!")
    else:
        print("Normal prize")


elif student_yn == "no":
    special_prize = False
    travel_month = int(input("During which month are you traveling in? (1-12): "))
    if special_prize is False:
        print("Normal prize")
