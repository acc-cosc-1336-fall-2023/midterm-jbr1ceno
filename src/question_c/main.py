#add import
import question_c

get_sales_amount = input("Please input a sales amount that is in the range from 0 to 1999 to get your bonus pay amount: ")

result = question_c.get_bonus_pay_amount(int(get_sales_amount))

print("Your bonus pay amount is: " + str(result))