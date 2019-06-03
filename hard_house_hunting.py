total_cost = int(input("what is the total cost of your dream home? "))
portion_down_payment_input = input("What portion of your total payment are you using for your down payment")
if (portion_down_payment_input == ''):
    portion_down_payment = 0.25
else:
    portion_down_payment = float(portion_down_payment_input)
down_payment = total_cost * portion_down_payment
current_savings = 0
r_input = input("What rate of return will you be getting?")

if (r_input == ''):
    r = .04
else:
    r = float(r_input)

annual_salary = int(input("What is your annual salary? "))
portion_saved = float(input("What portion of your salary are you going to save? Please respond with a decimal amount. "))
months = 0

while (current_savings < down_payment):
    current_savings += (current_savings*(r/12)) + ((annual_salary * portion_saved)/12)
    months += 1

print("It will take you " + str(months) + " months to save enough money.")