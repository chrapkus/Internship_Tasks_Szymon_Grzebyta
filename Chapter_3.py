
def is_valid(number):
    number = str(number)
    group_counter = 1
    number_of_groups = 0
    for index in range(1,len(number)):

        if int(number[index]) < int(number[index-1]):
            return False

        elif number[index] == number[index-1]:
            group_counter +=1

        else:
            if group_counter != 1:
                number_of_groups += 1
            group_counter = 1

    if number_of_groups >= 2:
        return True

    else:
        return False

if __name__ == '__main__':

    solution = 0
    for x in range((372**2)+1, 809**2):
        if is_valid(x):
            solution += 1
            print(x)

    print(solution)
