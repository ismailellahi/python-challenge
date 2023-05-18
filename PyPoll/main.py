import os
import csv

# Path to the election data file
election_data = os.path.join("..", "Resources", "election_data.csv")
file_output = os.path.join("..", "Analysis", "Results.txt")

# Initialize variables
total_votes = 0
candidates = {}
winner_votes = 0
winner_candidate = ""

# Open the election data file
with open(election_data, 'r') as file:
    data = csv.reader(file)
    header = next(data)  # remove the header

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

    # Prepare the result string
    result_string = ""
    result_string += "Election Results\n"
    result_string += "-------------------------\n"
    result_string += f"Total Votes: {total_votes}\n"
    result_string += "-------------------------\n"
    for candidate, votes in candidates.items():
        # Calculate the percentage of votes for each candidate
        percentage = round((votes / total_votes) * 100, 3)

        # Append the candidate's name, vote count, and percentage of votes to the result string
        result_string += f"{candidate}: {percentage}% ({votes})\n"

        # Track the winner based on popular vote
        if votes > winner_votes:
            winner_candidate = candidate
            winner_votes = votes

    result_string += "-------------------------\n"
    result_string += f"Winner: {winner_candidate}\n"
    result_string += "-------------------------\n"

print(result_string)

    # Write the result string to the output file
with open(file_output, 'w') as output_file:
        output_file.write(result_string)

# Print a message to indicate that the results have been saved
print(f"Results have been saved to {file_output}")

