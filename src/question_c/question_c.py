#write functions here, don't add input('') statements here!

def get_bonus_pay_amount(sales):
    
    bonusPayAmount = 0 

    if(sales >= 0 and sales <= 499 ):
        salesDivPercentage = int(sales) * (5/100) #5 percent bonus
        bonusPayAmount = int(salesDivPercentage)

    elif(sales >= 500 and sales <= 999 ):
        salesDivPercentage = int(sales) * (6/100) #6 percent bonus
        bonusPayAmount = int(salesDivPercentage)

    elif(sales >= 1000 and sales <= 1499 ):
        salesDivPercentage = int(sales) * (7/100) #7 percent bonus
        bonusPayAmount = int(salesDivPercentage)
    
    elif(sales >= 1500 and sales <= 1999 ):
        salesDivPercentage = int(sales) * (8/100) #8 percent bonus
        bonusPayAmount = int(salesDivPercentage)

    else:
        bonusPayAmount = "Invalid"
    
    return bonusPayAmount