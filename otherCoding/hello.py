
def isSelfDescribing(number, base):
    selfDescribing = True
    strNumber = str(number)

    for i in range(len(strNumber)):
        num_count = strNumber.count(str(i))
        num = int(strNumber[i])

        if num_count != num:
            print("False")
            return False

    print("True")
    return True


isSelfDescribing(3211000, 8)
