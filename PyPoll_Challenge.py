# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Create a county list and county votes dictionary.
counties = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the county with the largest turnout.
high_county = ""
high_county_votes = 0
high_county_percent = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate and county name from each row.
        candidate_name = row[2]
        county = row[1]

   # If they aren't in a list of candidates or counties,  add them and count votes for them
    # candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    #counties
        if county not in counties:
            counties.append(county)
            county_votes[county] = 0
        county_votes[county] += 1

#Print the final vote count.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")

    for candidate_name in candidate_votes:

        # Retrieve vote count, calculate percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    for county in county_votes:

        # Retrieve vote count, calculate percentage
        cvotes = county_votes.get(county)
        county_vote_percentage = float(cvotes) / float(total_votes) * 100
        county_results = (
            f"{county}: {county_vote_percentage:.1f}% ({cvotes:,})\n")
        print(county_results)

        # Determine highest turnout, and percentage.
        if (cvotes > high_county_votes):
            high_county_votes = cvotes
            high_county = county
            high_county_percent = county_vote_percentage

    # Print the highest turnout county.
    high_county_summary = (
        f"-------------------------\n"
        f"Highest turnout county: {high_county}\n"
        f"Vote count: {high_county_votes:,}\n"
        f"Percent of vote: {high_county_percent:.1f}%\n"
        f"-------------------------\n")
    print(high_county_summary)

# save results to a text file.
with open(file_to_save, "w") as txt_file:
     txt_file.write(election_results)
     txt_file.write(winning_candidate_summary)
     txt_file.write(county_results)
     txt_file.write(high_county_summary)
