def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    rate = input ("Enter Rate: ")
    try:
        hrs = float(hrs)
        rate = float(rate)
    except:
        hrs = -1
        rate = -1
    
    if hrs > 0 :
        if hrs <= 40 :
            pay = hrs * rate
            print(pay)
        if hrs > 40 :
            pay = (40 * rate) + (((hrs - 40) * rate ) * 1.5)
            print(pay)
    else :
        print("Error, please enter numeric input")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()