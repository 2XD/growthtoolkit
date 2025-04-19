#This calculator uses expenses and revenues to determine the growth rate and give a financial projection
#It calculates the growth rate separately from month to month and adds them all up
#Then the calculator divides by the number of months to get the most accurate result possible

import csv

# Make sure that any input the user makes won't break the program.
def get_valid_float(prompt):
    while True:
        value = input(prompt).strip()

        if not value:
            print("Please enter a number.")
            continue

        try:
            num = float(value)
            if num < 0:
                print("Negative numbers are not allowed.")
                continue
            return num
        except ValueError:
            print("Enter a valid number.")

print("Welcome! Let's calculate your Financial Projections ")

rev = get_valid_float("Enter your current monthly revenue: ")
expenses = get_valid_float("Enter your current monthly expenses: ")

profit = rev - expenses
print("\nNow we need some past revenue data in order to calculate your growth rate.")

months_ago = 0
while months_ago <= 0:
    months_ago = get_valid_float("How many months ago of revenue data do you want to use? ")
    months_ago = int(months_ago)  # Convert to integer after validation
    if months_ago <= 0:
        print("Enter a valid number (must be greater than 0).")

rev_data = []
exp_data = []  # Added for expenses

while len(rev_data) < months_ago:
    rev_input = get_valid_float("Enter revenue for month " + str(len(rev_data) + 1) + ": ")
    rev_data.append(rev_input)
    exp_input = get_valid_float("Enter expenses for month " + str(len(exp_data) + 1) + ": ")  # Added prompt for expenses
    exp_data.append(exp_input)  # Added expense data storage

# Calculate growth rate for each month and average them
growth_rates = []
for i in range(1, len(rev_data)):
    growth_rate = ((rev_data[i] - rev_data[i-1]) / rev_data[i-1]) * 100  # Month-to-month growth rate
    growth_rates.append(growth_rate)

# Average the growth rates
if growth_rates:
    avg_growth_rate = sum(growth_rates) / len(growth_rates)
else:
    avg_growth_rate = 0  # If there's no growth data, set to 0%

print("\nAverage growth rate calculated: " + str(round(avg_growth_rate, 2)) + "%" + " based on the last " + str(months_ago) + " months of data.")

# Allow user to override growth rate if desired
newgr = input("\nWant to override this? Enter a new growth rate or just press Enter to continue with the calculated amount: ").strip()
if newgr != "":
    try:
        avg_growth_rate = float(newgr)
    except ValueError:  # More specific exception
        print("The input wasn't a number, so we're sticking with " + str(round(avg_growth_rate, 2)) + "%.")

# Do the calculations that will be saved to the csv later
check = 0
while check == 0:
    futuremonths = input("\nHow many months ahead do you want to project your revenue? ")
    
    if futuremonths.isdigit() and int(futuremonths) > 0:
        futuremonths = int(futuremonths)
        check = 1  # Exit loop once valid input is received
    else:
        print("Enter a non-zero number value.")

projrev = rev * (1 + avg_growth_rate / 100) ** futuremonths
projexp = expenses * (1 + avg_growth_rate / 100) ** futuremonths
projprofit = projrev - projexp

# Cumulative projections over time
cumulative_rev = 0
cumulative_exp = 0

for i in range(1, futuremonths + 1):
    month_rev = rev * (1 + avg_growth_rate / 100) ** i
    month_exp = expenses * (1 + avg_growth_rate / 100) ** i
    cumulative_rev += month_rev
    cumulative_exp += month_exp

cumulative_profit = cumulative_rev - cumulative_exp

# Save as a CSV
file_name = input("What do you want to save the file as?: ")
if file_name == "":
    print("No input detected. Saving as 'financialprojectioncalculation.csv'.")
    file_name = "financialprojectioncalculation"

csv_filename = file_name + ".csv"

with open(csv_filename, "w", newline="") as file:
    writer = csv.writer(file)
    headers = ["Revenue", "Expenses", "Profit", "Months Ago", "Growth Rate", "Projected Revenue", "Projected Expenses", "Projected Profit"]
    writer.writerow(headers)
    writer.writerow([rev, expenses, profit, months_ago, avg_growth_rate, projrev, projexp, projprofit])
    writer.writerow([])  # Blank row for separation
    writer.writerow(["Cumulative over " + str(futuremonths) + " months", "", "", "", "", cumulative_rev, cumulative_exp, cumulative_profit])

print("\nData saved successfully to " + csv_filename + "!")
print("The csv file will contain the revenue, expenses, profit, and months ago that you entered,\nThe growth rate and the projected revenue, expenses, and profit were calculated by the Financial Calculator.")
