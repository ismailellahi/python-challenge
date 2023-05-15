import os
import csv

# Path to the election data file
election_data = os.path.join("..", "Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner_votes = 0
winner_candidate = ""

# Open the election data file
with open(election_data, 'r') as file:
    data = csv.reader(file)
    header = next(data) # remove the header
    
    # Loop through each row of the data
    for row in data:
        # Count the total number of votes
        total_votes += 1
        
        # Track the candidates and their vote counts
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
    
    # Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates.items():
        # Calculate the percentage of votes for each candidate
        percentage = round((votes / total_votes) * 100, 3)
        
        # Print the candidate's name, vote count, and percentage of votes
        print(f"{candidate}: {percentage}% ({votes})")
        
        # Track the winner based on popular vote
        if votes > winner_votes:
            winner_candidate = candidate
            winner_votes = votes
    
    print("-------------------------")
    print(f"Winner: {winner_candidate}")
    print("-------------------------")
