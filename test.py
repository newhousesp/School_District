# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "test2.txt")

# Initialize a total vote counter.
total_votes = 0

# Create a county list and county votes dictionary.
counties = []
county_votes = {}
county_votepercent = {}

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        county = row[1]

    #counties
        if county not in counties:
            counties.append(county)
            county_votes[county] = 0
        county_votes[county] += 1

# Determine county with highest turnout, determine winner
high_county = ""
high_county_votes = 0
high_county_percent = 0

for county in counties:
    county_votepercent[county] = round(float(county_votes.get(county)) / float(total_votes)*100, 2)
    if int(county_votes[county]) > high_county_votes:   
        high_county_votes = int(county_votes[county])
        high_county_percentage = county_votepercent
        high_county = county

# Print the final vote count by county
for county in counties:
    county_results = (
        f"-------------------------\n"
        f"County Votes: {county_votes}\n"
        f"Counties as percent of total: {county_votepercent}\n")
    print(county_results, end="")

# Print the highest turnout county summary
    high_county_summary = (
        f"-------------------------\n"
        f"Highest turnout County: {high_county}\n"
        f"Highest turnot County's votes: {high_county_votes:,}\n"
        f"Percentage of state: {high_county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(high_county_summary)