# Modules
import csv

# Set the file path
csvpath = "Resources/election_data.csv"

# After opening and reading in the file, create the variables, assign them here, in between csvpath and with open()
total_votes = 0 # like with PyBank, have to start at 0 when adding and looping through rows
candidates = {} # empty dictionary

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (if there is no header row, this step is unnecessary)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # print(row)

        # Count total amount of votes
        total_votes = total_votes + 1 # OR: 1 total_votes += 1

        # Identify candidates and add to dictionary
        new_candidate = row[2]
        if new_candidate in candidates.keys():
            candidates[new_candidate] += 1
        else:
            candidates[new_candidate] = 1

# output for txt file
output = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n""" # special formatting for spacing

max_cand = ""
max_votes = 0

# create foor loop to find totals and percents from votes
for candidate in candidates.keys():
    votes = candidates[candidate]
    perc = 100 * (votes / total_votes)
    # main output that combines candidate, percent, and total together
    line = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    output += line

    # find the max voted candidate within dictionary
    if votes > max_votes:
        max_cand = candidate
        max_votes = votes

# create final line of output
last_line = f"""-------------------------
Winner: {max_cand}
-------------------------"""
output += last_line

print(output)

# create txt file
with open('main.py.txt', 'w') as file:
    # Write data to the file
    file.write(output)

# # Below is code I tried to create for the list of candidates after line 30, but ended up being unnecessary
# unique_candidates = []
# for value in candidates:
#     if value not in unique_candidates:
#         unique_candidates.append(value)