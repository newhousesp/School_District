#Open and read data file
electresults = open("Resources/election_results.csv", "r")

# Add dependencies.
import csv
import os

# Assign variables to load/save files.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# set counters
total_votes = 0
candidates = []
candidate_votes = {}
votepercent ={}

# Open the election results and read the file.
with open(file_to_load) as electresults:
    file_reader = csv.reader(electresults)

# Define header row.
    headers = next(file_reader)
 # Read through the file.
    for row in file_reader:
# Count total votes cast.
        total_votes += 1
# Get names of candidates.
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
# Count votes for each candidate
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate percent share of vote for each candidate
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    votepercent[candidate] = round(float(votes) / float(total_votes)*100, 2)
    print(f"{candidate}: received {votepercent[candidate]}% of the vote.")





