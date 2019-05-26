amt =float(input("Enter the Amount: "))
r =float(input("Enter the rate: "))
years =float(input("Enter the years: "))

future_value  = amt*((1+(0.01*r)) ** years)
print(round(future_value,2))