import os
import csv

filepath = os.path.join = ('Resources/budget_data.csv')

# Loading csv file
with open(filepath, 'r', encoding='utf-8') as f:
    bank_csv = csv.reader(f, delimiter=',')
    # Skip header
    next(f, None)
    # Set list vars 
    months = []
    profit_loss = []
    change = []
    # Loop through csv rows
    for row in bank_csv:
        # Append total months and total amount to proper list
        date = row[0]
        months.append(date)
        profit = int(row[1])
        profit_loss.append(profit)
    # The total number of months included in the datasets
    total_months = len(months)
    # The net total amount of "Profit/Losses" over the entire period
    total_amount = sum(profit_loss)
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# Loop though range of length of profit_loss list 
for i in range(len(profit_loss)-1):
    # Add values to the change list 
    change.append(profit_loss[i+1]-profit_loss[i])
    # getting total change by summing the change list
    total_change = sum(change)
# Average Change
average_change = round((total_change/(total_months-1)), 2)
# Max profit and loss
max_profit = max(change)
max_loss = min(change)
# Find corresponding month for max and min
max_profit_month = change.index(max_profit)
max_loss_month = change.index(max_loss)
profit_month = months[max_profit_month+1]
loss_month = months[max_loss_month+1]
# Terminal print statements
print('Financial Analysis')
print('------------------------')
print(f'Total Months: {str(total_months)}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {profit_month} (${max_profit})')
print(f'Greatest decrease in Profits: {loss_month} (${max_loss})')

# Output result text file
results_file = 'analysis/pyBank_results.txt'
with open (results_file, 'w', newline='', encoding='utf-8') as file:
    file.write('Financial Analysis\n')
    file.write('------------------------\n')
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${total_amount}\n')
    file.write(f'Average Change: ${average_change}\n')
    file.write(f'Greatest Increase in Profits: {profit_month} (${max_profit})\n')
    file.write(f'Greatest Decrease in Profits: {loss_month} (${max_loss})\n')

        


    
        









        
        
        
