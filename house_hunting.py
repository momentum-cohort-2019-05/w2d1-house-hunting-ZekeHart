total_cost = int(input("what is the total cost of your dream home? "))
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04
annual_salary = int(input("What is your annual salary? "))
portion_saved = float(input("What portion of your salary are you going to save? Please respond with a decimal amount. "))
months = 0
while (current_savings < down_payment):
    current_savings += (current_savings*(r/12)) + ((annual_salary * portion_saved)/12)
    months += 1

print("It will take you " + str(months) + "months to save enough money.")