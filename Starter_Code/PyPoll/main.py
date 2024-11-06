# Import OS module for working with files and directories and to create file paths across operating systems
import os

# Import CSV module to read .csv files and write to it
import csv

# Set path for the source file
election_data = os.path.join("..", "Resources", "election_data.csv")

# Declare variables and set initial values
total_votes = 0
winner = ""

# Create dictionary to store total votes per candidate
votesPerCandidate ={} 

# Open and read csv file
with open (election_data, 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')

    for row in reader:
        total_votes = total_votes + 1

# Set candidate value 
        candidate = row['Candidate']

# If the candidate is not in the dictionary, add them else increment the candidate's count by 1
        if candidate not in votesPerCandidate:
            votesPerCandidate[candidate] =1
        else:
            votesPerCandidate[candidate] += 1

# Create the output string (Help: Xpert Learning Assistant)
output = f"Election Results\n"
output += f"-------------------------\n"
output += f"Total Votes: {total_votes}\n"
output += f"-------------------------\n"

# Calculate the percentage vote each candidate received and then output each candidate's name, their vote count and percentage  to the terminal       
for candidate, votes in votesPerCandidate.items():
    vote_percent = round((votes/ total_votes) * 100, 3)
    output += f"{candidate}: {vote_percent}% ({votes})\n"
output += f"-------------------------\n"

# Determine winning candidate.
winner = max(votesPerCandidate, key=votesPerCandidate.get) 

# Save the winning candidate name to the output string and then output it to the terminal.
output += f"Winner: {winner}\n"
output += f"-------------------------\n"

# Print the output to the terminal 
print(output)

# Create a text file to export all the analysis result and set the path of the text file
csvpath = os.path.join("..", "Analysis","Election_Results.txt")

with open(csvpath, 'w') as txtfile:
    txtfile.write(output)



