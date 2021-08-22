import os
import csv

filepath = os.path.join = ('Resources/election_data.csv')

# Setting up variables


winner_votes = 0
winner = "" 
    
    

with open(filepath, newline='', encoding='utf-8') as f:
    poll_csv = csv.reader(f, delimiter=',')
    # Skip header
    next(f, None)
    # Set list amd dict variables
    total_votes_list = []
    canidate_list = []
    canidate_dict = {}
    # Loops through the csv rows
    for row in poll_csv:
        # Find length of votes
        voters = row[0]
        canidate = row[2]
        total_votes_list.append(voters)
    total_votes = len(total_votes_list)
    print(total_votes)

            

    
    

    
