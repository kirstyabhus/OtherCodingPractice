try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))

except:
    print("error, please enter numeric input")
    quit()

if hours <= 40:
    pay = hours * rate
else:
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))

print("Pay", pay)
