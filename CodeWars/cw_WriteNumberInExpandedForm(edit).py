#https://www.codewars.com/kata/5842df8ccbd22792a4000245/python

# problems I came across
# Line 11 - Before I wrote numListCopy = numList on Line ___, to make a copy of the list so that I can editthe list
            # without editing the original. But I learned that using this method does not make a copy of the list,
            # and instead makes a REFERENCE to the list i.e. editing the copy will edit the original
# Using debugger helped a lot (pycharm)

def expanded_form(num):
    # to store the expanded values
    expanded = []

    # first convert the number to a string so that I can then turn the str(number) into a list, where
    # each index = a value in the str(number) e.g. ["7","5", "4"]
    num = str(num)
    numList = list(num)

    # make a copy of the number list for later removal of values
    numListCopy = numList.copy()

    # loop through every number in the list
    for number in numList:
        # IF the number is NOT 0 then find its place value
        if number != "0":
            # find the place value (in terms of powers of 10) of the number. (e.g. 70 would be 10, 400 would be 100)
            # e.g. ["7","5", "4"], place value (in terms of 10s) of 7 would be 10 to power of (length - 1) ->  10 power 2 -> 100
            tensPlaceValue = 10 ** (len(numListCopy)-1)

            # multiply the current number by its place value (in terms of 10s)
            x = int(number) * tensPlaceValue
            # append the calculated value into the list
            expanded.append(str(x))

            # delete the first value of the number, as we're now finished with it and can move onto the next number
            # in the next iteration
            del numListCopy[0]
            # the place value (in terms of 10s) should now decrease by 10 times, since we're moving to the next value
            tensPlaceValue /= 10
        # ELSE IF the number is 0, we don't need to find its place value
        else:
            # remove the first digit in the number
            del numListCopy[0]
            # the place value (in terms of 10s) should now decrease by 10 times, since we're moving to the next value
            tensPlaceValue /= 10

    # join the expanded values to give a "X + Y + Z" output
    return " + ".join(expanded)


print(expanded_form(70304))
