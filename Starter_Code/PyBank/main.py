# Import OS module for working with files and directories and to create file paths across operating systems
import os

# Import CSV module to read .csv files and write to it
import csv

# Set path for the source file
budget_data = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv file
with open (budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

# Read the header row and store it
    csvheader = next(csvreader)
 
# Declare variables and set initial values
    total_months = 0
    total_net = 0
    previous_month_profit = 0
    current_month_profit = 0
    change = 0
    total_change = 0
    
# Declare lists and dictionaries to store values
    date_list = []
    profit_loss_list = []
    change_list = []
    increase = {"date": "", "amount": 0}
    decrease = {"date": "", "amount": 0}

# Loop through each row of csv file
    for row in csvreader:
# Create lists to store data for date and profit/loss column separately
        date_list.append(row[0])
# Set the initial value of profit/loss column as 
        profit_loss_list.append(row[1])
# Calculate change in profit/loss column over the entire period
        total_months += 1
# Calculate the total profit/loss over entire period by adding values to the column as we move through the loop
        total_net += int(row[1])
# As we dont have previous profit/loss to compare data in first entry so, check if its the first row, skip first row
        if total_months == 1:
            previous_month_profit = int(row[1]) 
        else: 
            current_month_profit = int(row[1]) 
            change = current_month_profit - previous_month_profit 
            change_list.append(change)
            total_change += int(change) 
            average_change = round(total_change / (total_months -1),2) 

# Reset the values
            previous_month_profit = current_month_profit   

# Calculate greatest increase in profits over entire period and also the date of the maximum profit
        if change > increase["amount"]:
            increase["amount"] = change
            increase["date"] = row[0] 

# Calculate greatest decrease in profits over entire period and also the date of the minimum profit
        if change < decrease["amount"]:
            decrease["amount"] = change
            decrease["date"] = row[0] 
    
# Generate summary
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${average_change}
Greatest Increase in Profits: {increase["date"]} (${increase["amount"]})
Greatest Decrease in Profits: {decrease["date"]} (${decrease["amount"]})
"""
print(output)

# Create a text file to export all the analysis result and set the path of the text file
csvpath = os.path.join("..", "Analysis","Budget_Analysis_Report.txt")

with open(csvpath, 'w') as datafile:
    datafile.write(output)

    

