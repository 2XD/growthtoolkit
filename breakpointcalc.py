import csv

# Make sure that any input the user makes won't break the program.
def get_valid_float(prompt):
    while True:
        value = input(prompt).strip()
        
        if not value:
            print("Please enter a valid number.")
            continue

        try:
            num = float(value)
            if num < 0:
                print("Negative numbers are not allowed.")
                continue
            return num
        except ValueError:
            print("Enter a valid number.")

# Get variables to calculate Break-Even Sales Point (BESP)
print("This calculator will determine the dollar amount you need to cover both fixed and variable costs.")
revenue = get_valid_float("What is your total revenue from sales ($)? ")
fixed_costs = get_valid_float("What are your total fixed costs? This includes rent, utilities, etc. ($) ")
variable_costs = get_valid_float("What are your total variable costs? This includes inventory, card swipe fees, etc. ($) ")

print("\nNow, we will calculate the dollar amount you need to cover your costs.\nFirst, let's determine the selling price per unit and sales frequency for each product.") 
numproducts = get_valid_float("How many different products do you sell? ")
numproducts = int(numproducts)  # Ensure it's an integer

products = []
product_names = []
frequency = []

temp = 0
while temp < numproducts:
    temp += 1
    name = input(f"What is the name of product {temp}? ").strip()
    product_names.append(name)
    products.append(get_valid_float(f"What is the selling price of {name} ($)? "))
    frequency.append(get_valid_float(f"How many units of {name} do you sell in a month? "))

# Calculate the average cost per unit weighted to the amount that is sold
total_revenue_units = sum(products[i] * frequency[i] for i in range(numproducts))
total_units = sum(frequency)
rev_per = total_revenue_units / total_units if total_units > 0 else 0
vc_per = variable_costs / total_units if total_units > 0 else 0
contribution_margin = rev_per - vc_per

if total_units == 0:
    print("Error: No units sold. Cannot calculate break-even point.")
else:
    if vc_per == rev_per:
        print("Variable costs cannot be equal to revenue per unit. Please run the calculator again.")
    else:
        besp = fixed_costs / contribution_margin
        units_needed = (fixed_costs + variable_costs) / rev_per if rev_per > 0 else 0
        print(f"Your break-even sales point is ${besp:.2f}. This is the dollar amount you need to cover all your fixed costs and contribution margin.")
        print(f"Contribution Margin per Unit: ${contribution_margin:.2f}.")
        print(f"The total number of units you need to sell to cover both variable and fixed costs is {units_needed:.2f}. This is based on the sales frequency you provided.")
        
        # Save data to CSV
        file_name = input("What would you like to name the file to save the results? ").strip()
        if not file_name:
            print("No input detected. Saving as 'breakpointcalculation.csv'.")
            file_name = "breakpointcalculation"
        
        csv_filename = file_name + ".csv"

        with open(csv_filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Selling Price", "Sales Frequency"])
            for name, price, qty in zip(product_names, products, frequency):
                writer.writerow([name, price, qty])
            
            writer.writerow([])  # Empty row for better readability in the CSV
            writer.writerow(["Revenue", revenue])
            writer.writerow(["Revenue Per Unit", rev_per])
            writer.writerow(["Fixed Costs", fixed_costs])
            writer.writerow(["Variable Costs", variable_costs])
            writer.writerow(["Variable Costs Per Unit", vc_per])
            writer.writerow(["Break-Even Sales Point (in dollars)", besp])
            writer.writerow(["Contribution Margin", contribution_margin])
            writer.writerow(["Unit Sales to Cover Both Variable and Fixed Costs", units_needed])

        print("\nData saved successfully to " + csv_filename + "!")
        print("This tool calculated your break-even sales point and contribution margin, and stored other financial details you entered.")

input("Press Enter to Exit")
