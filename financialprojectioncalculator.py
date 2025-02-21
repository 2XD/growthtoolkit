import csv

#make sure that any input the user makes won't break the program.
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
rev = float(rev)
expenses = get_valid_float("Enter your current monthly expenses: ")
expenses = float(expenses)

profit = rev - expenses
print("\nNow we need some past revenue data in order to calculate your growth rate.")

months_ago = 0
while months_ago <= 0:
    months_ago = int(get_valid_float("How many months ago of revenue data do you want to use? "))
    if months_ago <= 0:
        print("Enter a valid number (must be greater than 0).")

rev_data = []
while len(rev_data) < months_ago:
    rev_input = get_valid_float("Enter revenue for month " + str(len(rev_data) + 1) + ": ")
    rev_data.append(rev_input)

if len(rev_data) == 0:
    print("Assuming revenue for this period was 0 because nothing was entered.")
    rev_data.append(0)
else:
    prev = rev_data[-1]

    if prev == 0:
        gr = 0
    else:
        gr = ((rev - prev) / prev) * 100

print("\nGrowth rate calculated: " + str(round(gr, 2)) + "%" + " based on the last " + str(months_ago) + " months of data.")

newgr = input("\nWant to override this? Enter a new growth rate or just press Enter to continue with the calculated amount: ").strip()
if newgr != "":
    try:
        gr = float(newgr)
    except:
        print("The input wasn't a number, so we're sticking with " + str(round(gr, 2)) + "%.")

#do the calculations that will be saved to the csv later
check = 0
while check == 0:
    futuremonths = input("\nHow many months ahead do you want to project your revenue? ")
    
    if futuremonths.isdigit() and int(futuremonths) > 0:
        futuremonths = int(futuremonths)
        check = 1  # Exit loop once valid input is received
    else:
        print("Enter a non-zero number value.")

projrev = rev * (1 + gr / 100) ** futuremonths
projexp = expenses * (1 + gr / 100) ** futuremonths
projprofit = projrev - projexp

#save as a csv
file_name = input("What do you want to save the file as?: ")
if file_name == "":
    print("No input detected. Saving as 'financialprojectioncalculation.csv'.")
    file_name = "financialprojectioncalculation"

csv_filename = file_name + ".csv"

with open(csv_filename, "w", newline="") as file:
    writer = csv.writer(file)
    headers = ["Revenue", "Expenses", "Profit", "Months Ago", "Previous Revenue", "Growth Rate", "Projected Revenue", "Projected Expenses", "Projected Profit"]
    writer.writerow(headers)
    writer.writerow([rev, expenses, profit, months_ago, prev, gr, projrev, projexp, projprofit])

print("\n Data saved successfully to " + csv_filename + "!")
print("The csv file will contain the revenue, expenses, profit, months ago, previous revenue that you entered,\n The growth rate, projected revenue, projected expenses, and projected profit were all calculated by the Financial Calculator.")
