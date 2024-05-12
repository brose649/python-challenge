# Modules
import csv

# Set the file path
csvpath = "Resources/budget_data.csv"

# After opening and reading in the file, create the variables, assign them here, in between csvpath and with open()
total_months = 0 # have to start with 0 when adding or looping through rows
net_total = 0 # have to start with 0 when adding or looping through rows
last_month_profit = 0 # could also have this as = None
month_changes = [] # creates an empty list, column index is [0]
changes = [] # creates an empty list, column index is [1]

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (if there is no header row, this step is unnecessary)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # print(row) # Uncomment to show all rows

        # Now assign values to variables (before beginning conditions)
        
        # Total number of months
        total_months = total_months + 1
        # # can also list the above as:
        # total_months += 1

        # Net total amount of profits
        net_total = net_total + int(row[1])
        # can also write as: net_total += int(row[1])

        # Create conditions - first account for the first row
        if (total_months == 1):
            # if it IS the FIRST row, which it is, then there is no change:
            last_month_profit = int(row[1])
        else:
            # calculate the changes, adds to changes & month_changes []
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            # reset last month profit
            last_month_profit = int(row[1])

# calculate the average change
changes_avg = sum(changes) / len(changes)

# calculate greatest increase in profits (month and amount)
max_change = max(changes)
max_month_indx = changes.index(max_change)
max_month = month_changes[max_month_indx]

# calculate greatest decrease in profits (month and amount)
min_change = min(changes)
min_month_indx = changes.index(min_change)
min_month = month_changes[min_month_indx]

# Fincancial Analysis
# output for txt file
output = f"""Financial Analysis
-------------------------
Total Months: {total_months}
Total : {net_total}
Average Change: {changes_avg}
Greatest Increase in Profits: {max_month} {max_change}
Greatest Decrease in Profits: {min_month} {min_change}
\n""" # special formatting for spacing

print(output)

# create txt file
with open('main.py.txt', 'w') as file:
    # Write data to the file
    file.write(output)