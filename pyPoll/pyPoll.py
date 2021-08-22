import os
import csv

filepath = os.path.join = ('election_data.csv')

# Define functions
def totalVotes(election_data):
    voter_id = row[0]
    county = row[1]
    candidate = row[2]
    
    

with open(filepath, newline='', encoding='utf-8') as f:
    poll_csv = csv.reader(f, delimiter=',')
    for row in poll_csv:
        print(row)
