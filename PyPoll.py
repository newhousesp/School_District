#Open data file.
electresults = open("Resources/election_results.csv", "r")

# Add dependencies.
import csv
import os

# Assign variables to load/save files.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as electresults:
# Read the file object with the reader function.
    file_reader = csv.reader(electresults)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

# Write down the names of all the candidates.

#Add a vote count for each candidate.

#Get the total votes for each candidate.

#Get the total votes cast for the election.
