print ('How much was your meal?')

meal_cost = float(raw_input(">"))

sales_tax = .0825

tax_dollars = sales_tax * meal_cost

total_cost = meal_cost + tax_dollars

print ('What percent do you want to tip?')

tip_percent = float(raw_input('>'))

actual_percent = tip_percent/100

total_of_totals = (1+actual_percent)*total_cost

msg = "Your meal plus tax and tip was %s" % (total_of_totals)

print (msg)
