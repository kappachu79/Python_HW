# import dependencies
import os
import csv

# file location 
poll_path = os.path.join( "election_data.csv")

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
    Khan_votes += 1
if row[2] == "Li":
    Li_votes += 1
if row[2] == "O'Tooley":
    otooley_votes += 1

# List of candidates and votes 
candidates = ["Correy", "O'Tooley", "Khan", "Li"]
votes = [correy_votes, Li_votes, Khan_votes, otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print summary
percent_correy = (correy_votes/total_votes) * 100
percent_Li = (Li_votes/total_votes) * 100
percent_khan = (Khan_votes/total_votes) * 100
percent_otooley = (otooley_votes/total_votes) *100

# Print Summary table
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------")
print(f"Khan: {percent_khan:.3f}% ({Khan_votes})")
print(f"Correy: {percent_correy:.3f}% ({correy_votes})")
print(f"Li: {percent_Li:.3f}% ({Li_votes})")
print(f"O'Tooley: {percent_otooley:.3f}% ({otooley_votes})")
print(f"----------------------------")

