def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    try:
        hrs = float(hrs)
    except:
        hrs = -1
    
    if hrs > 0 :
        if hrs <= 40 :
            pay = hrs * 10
            print(pay)
        if hrs > 40 :
            pay = (40 * 10) + (((hrs - 40) * 10 ) * 1.5)
            print(pay)
    else :
        print('not a number')
    

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
calculatePay()