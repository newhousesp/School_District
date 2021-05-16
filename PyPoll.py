#Open and read data file
electresults = open("Resources/election_results.csv", "r")

# Add dependencies.
import csv
import os

# Assign variables to load/save files.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# set counters and proxy variables
total_votes = 0
candidates = []
candidate_votes = {}
votepercent = {}
winner = ""
winning_count = 0
winning_percentage = 0

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

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Calculate percent share of vote for each candidate
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        votepercent = round(float(votes) / float(total_votes)*100, 2)
        print(f"{candidate}: received {votepercent}% of the vote.")

        candidate_results = (f"{candidate}: {votepercent:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

# Determine winner
        if (votes > winning_count):
            winning_count = votes
            winning_percentage = votepercent
            winner = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

