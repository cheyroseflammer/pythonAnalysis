import os
import csv

filepath = os.path.join = ('budget_data.csv')

# Define functions
def totalMonths(bank_data):
    date = row[0]
    profit_losses = int(row[1])
    
    

with open(filepath, newline='', encoding='utf-8') as f:
    bank_csv = csv.reader(f, delimiter=',')
    for row in bank_csv:
        print(row)
