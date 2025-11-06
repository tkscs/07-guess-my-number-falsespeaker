# the user will choose a number
# this program will guess the number
# the user will say "yes" or "higher" or "lower"
# the program will ask to play again or exit
i = 10
while True:
    response = input(f"is your number {i}")
    if response == "lower":
        i = i-1
    elif response == "higher":
        i = i+1
    elif response == "yes":
        break