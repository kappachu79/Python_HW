# import dependencies
import os
import csv

# file location 
poll_path = os.path.join("..", "Resources", "election_data.csv")

# Variables for Polls
Khan_votes = 0
correy_votes = 0
Li_votes = 0
otooley_votes = 0
total_votes = 0

# open csv file to read
with open(poll_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the header to iterate to the actural values
header = next(csvreader)

# Iterate between rows 
for row in csvreader:


    total_votes += 1

# count no. of time candidate name appears and put in a list

if row[2] == "Correy":
    correy_votes += 1
if row[2] == "Khan":
    khan_votes += 1
if row[2] == "Li":
    Li_votes += 1
if row[2] = "O'Tooley":
    otooley_votes += 1

# List of candidates and votes 
candidates = ["Correy", "O'Tooley", "Khan", "Li"]
votes = [correy_votes, Li_votes, khan_votes, otooley_votes]



# Print summary
percent_correy = (correy_votes/total_votes) * 100
percent_Li = (Li_votes/total_votes) * 100
percent_khan = (khan_votes/total_votes) * 100
percent_otooley = (otooley_votes/total_votes) *100

# Print Summary table
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")

