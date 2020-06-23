import os
import csv

input_budget = os.path.join("budget_data.csv")

# List to store budget_data
months_total = []
profit_total = []
profit_change = []

# Open csv to read file
with open(input_budget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip header
    header = next(csvreader)

# Loop through looking for rows is the csv file
    for row in csvreader:

        months_total.append(row[0])
        profit_total.append(int(row[1]))

# loop over profit/loss column to get change in profit s
for i in range(len(profit_total)-1):

    # Difference between the two consecutive months and append to  changes in profit/loss
    profit_change.append(profit_total[i+1]-profit_total[i])

# max and min variables of the profit change list
max_increase_value = max(profit_change)
max_decrease_value = min(profit_change)

# Match max and min values index to the proper month using month list and index from max and min

max_increase_month = profit_change.index(max(profit_change)) + 1
max_decrease_month = profit_change.index(min(profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months_total)}")
print(f"Total: ${sum(profit_total)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months_total[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {months_total[max_decrease_month]} (${(str(max_decrease_value))})")

 # Set variable for output file
output_file = os.path.join("budget_final.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Total Months", "profit_total", "Average Change", "Greatest Increase in Profits",
                     "Greatest Decrease in Profits"])

    