"""
Calculates pay with time-and-a-half overtime.
"""

def computePay(hours, rate):
    rawPay = hours * rate
    # if worked overtime, add 50% more pay for hours worked OT.
    if (hours-40 > 0) :
        bonusFromOvertime = (hours - 40) * rate * 0.5
        return rawPay + bonusFromOvertime
    else:
        return rawPay

while True:
    try:
        hours = float(input("enter hours: "))
        rate = float(input("enter rate: "))
        break
    except:
        print('please enter a number.')

pay = computePay(hours, rate)
print('your pay is : ' + str(pay))
