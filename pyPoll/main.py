# Import modules
import os
import csv
# Grab csv 
filepath = os.path.join = ('Resources/election_data.csv')
# Open csv
with open(filepath, newline='', encoding='utf-8') as f:
    # CSV Reader and delimter val set
    poll_csv = csv.reader(f, delimiter=',')
    # Skip header
    next(f, None)
    # Set variables
    total_votes_list = []
    canidate_list = []
    canidate_votes = {}
    winner_votes = 0
    winner = ""
    print("Election Results")
    print("------------------------")
    # Loops through the csv rows
    for row in poll_csv:
        # Grab csv row values
        voters = row[0]
        canidate = row[2]
        # if candidate is not already in list
        if canidate not in canidate_list:
            # add canidate to canidate list
            canidate_list.append(canidate)
            canidate_votes[canidate] = 0
        # add a vote for everytime a canidate appears
        canidate_votes[canidate] +=1
        # append votes to total vote list
        total_votes_list.append(voters)
        # get length of total vote list
        total_votes = len(total_votes_list)
    print(f'Total votes: {total_votes}')
    # Canidate percentage calculation
    for canidate in canidate_list:
        canidate_percentage = round(int(canidate_votes[canidate])/int(total_votes),2)
        canidate_output = f'{canidate}: {canidate_percentage:.3%} ({canidate_votes[canidate]})'
        # Get winner
        votes = canidate_votes[canidate]
        if votes > winner_votes:
            winner_votes = votes
            winner = canidate
        print("------------------------")
        print(canidate_output)
    print("------------------------")
    print(f'Winner: {winner}')
    
# Output result file
results_file = "analysis/pyPoll_results.txt"
with open(results_file, 'w', newline='', encoding='utf-8') as file:
    file.write('Election Results!\n')
    file.write('----------------------\n')
    file.write(f'Total votes: {total_votes}\n')
    file.write('----------------------\n')
    # have to loop again to grab each canidates info
    for canidate in canidate_list:
        canidate_percentage = round(int(canidate_votes[canidate])/int(total_votes),2)
        file.write(f'{canidate}: {canidate_percentage:.3%} ({canidate_votes[canidate]})\n')
    file.write('----------------------\n')
    file.write(f'Winner: {winner}\n')

            
        

            

            

    
    

    
