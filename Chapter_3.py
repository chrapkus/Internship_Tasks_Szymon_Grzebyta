# ----------------------------------------------------------------------------------------------
# Oh no, you're in trouble! You forgot the sudo password for your computer.
# You remember though that it was a number, and that it had some interesting properties:
# There are at least two groups of identical adjacent digits (like 11 and 33 in 1123345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same
# ----------------------------------------------------------------------------------------------

def is_valid(number):

    number = str(number)
    group_counter = 1
    number_of_groups =

    # looping thru number digits
    for index in range(1,len(number)):

        # checks if numbers are not decreasing
        if int(number[index]) < int(number[index-1]):
            return False

        # checks if there is group of identical adjacent digits
        elif number[index] == number[index-1]:
            group_counter +=1

        # if 2 numbers are not the same checks the length of last chain
        # if chain is at least 2 long then we increase number of groups
        elif number[index] != number[index - 1]:
            if group_counter != 1:
                number_of_groups += 1
            group_counter = 1

    if number_of_groups >= 2:
        return True

    else:
        return False

if __name__ == '__main__':

    solution = 0

    # loop to check all values in range between
    # 372 ** 2 and 809 ** 2(both ends inclusive).
    for x in range(372**2, (809**2)+1):

        if is_valid(x):
            solution += 1
            print("is valid: {}".format(x))

    print(solution)
