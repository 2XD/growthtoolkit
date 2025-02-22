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

#Get variables to calc BSP
print("This break-point calculator will determine the number of units that must be sold to cover both fixed and variable costs.")
revenue = get_valid_float("What is your revenue? ($) ")
fixed_costs = get_valid_float("What is your total fixed costs? This includes rent, utilities, and insurance. ($) ")
variable_costs = get_valid_float("What are your total variable costs? This includes sales commisions, advertising, and gas, ($) ")
units = get_valid_float("How many units are you selling? : ")

#Do math calcs
rev_per = revenue/units
vc_per = variable_costs/units
contribution_margin = rev_per - vc_per

if vc_per == rev_per:
    print("variable costs cannot be equal to revenue. Please run the calculator again.")
else:
    besp = fixed_costs / contribution_margin
    print(f"Your break-even sales point is {besp:.2f} units.")
    print(f"Contribution Margin per Unit: ${contribution_margin:.2f}")


file_name = input("What do you want to save the file as?: ")
if file_name == "":
    print("No input detected. Saving as 'breakpointcalculation.csv'.")
    file_name = "breakpointcalculation"

csv_filename = file_name + ".csv"

with open(csv_filename, "w", newline="") as file:
    writer = csv.writer(file)
    headers = ["Revenue", "Revenue Per Unit", "Fixed Costs", "Variable Costs", "Variable Costs Per Unit", "Units" "Break-Even Sales Point", "Contribution Margin"]
    writer.writerow(headers)
    writer.writerow([revenue, rev_per, fixed_costs, variable_costs, vc_per, units, besp, contribution_margin])

print("\n Data saved successfully to " + csv_filename + "!")
print("The csv file will contain the revenue, fixed costs, variable costs, and Units that you entered,\n The Revenue Per Unit, Variable Costs Per Unit, Break-Even Sales Point and Contribution Margin were all calculated by this tool.")
input("Press Enter to Exit")
