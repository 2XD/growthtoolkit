import openpyxl
from openpyxl.utils import get_column_letter

def startup_costs_calculator():
    categories = {
        "Equipment (Vehicles, Cooking Equipment, Utensils, etc.)": 0,
        "Food Supplies (How much are your ingredients costing?)": 0,
        "Utilities (electricity and other bills)": 0,
        "Licenses and Permits": 0,
        "Rent": 0,
        "Insurance": 0,
        "Lawyer and Accountant": 0,
        "Inventory": 0,
        "Employee Salaries": 0,
        "Advertising and Marketing": 0,
        "Market Research": 0,
        "Printed Marketing Materials": 0,
        "Making a Website": 0,
        "Please enter any other costs here": 0
    }
    file_name = input("What would you like to save the file as?: ")
    
    while True:
        try:
            months = int(input("How many months are your startup costs based upon? "))
            if months <= 0:
                print("Invalid number of months. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid number of months. Please try again.")
    
    print("Enter estimated costs for each category:")
    for category in categories:
        while True:
            try:
                categories[category] = float(input(f"How much was your {category.lower()} for {months} months? $") )
                break
            except ValueError:
                print("Invalid number detected! Please try again.")
    
    total_cost = sum(categories.values())
    monthly_cost = total_cost / months
    yearly_cost = monthly_cost * 12
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Startup Costs Report"
    
    # Writing header
    ws.append(["Category", "Cost ($)"])
    
    # Writing category data
    for category, cost in categories.items():
        ws.append([category, cost])
    
    # Writing total costs
    ws.append(["Total Estimated Start-Up Cost", total_cost])
    ws.append(["Average Monthly Cost", monthly_cost])
    ws.append(["Projected Yearly Cost", yearly_cost])
    
    # Adjust column widths
    for col in ws.columns:
        max_length = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        ws.column_dimensions[col_letter].width = max_length + 2
    
    wb.save(f"{file_name}.xlsx")
    print(f"\nReport saved as {file_name}.xlsx. Press Enter to exit.")
    input()

if __name__ == "__main__":
    startup_costs_calculator()
