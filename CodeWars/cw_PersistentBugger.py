# turn the number into a string
# split the numbers' digits into a list

# if the number already has a length of 1
    # just return 0

# while length of the number is not 1
    # for loop through each digit of the number
        # new number is product of all the digits in old number (digits are converted into int)
    # find the length of the new number (which had now been converted to string)
    # take count of how many times the while loop is running

# once length of number is finally 1
    # return how many times the while loop ran


def persistence(n):

    nList = list(str(n))
    total = 1
    lengthNum = len(nList)
    count = 0

    if lengthNum == 1:
        return 0

    while lengthNum != 1:
        for num in nList:
            total *= int(num)

        nList = list(str(total))
        lengthNum = len(nList)
        total = 1
        count += 1

    return count

print(persistence(25))