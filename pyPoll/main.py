# PyBank main.py
# author @ Adam Abdelmalek
# date @ 120118

import os
import csv

election_csv = os.path.join("C:/Users/adama/Desktop/python-challenge/PyPoll/Resources", "election_data.csv")

with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    
    csv_header = next(csvreader)
    #print(f"{csv_header}")
    
    #Calculated Values monthCounter, dollarTotal, avgChange, greatestInc, greatestDec
    voteCounter = 0
    list_candidates = []

    for row in csvreader:

        VoterID = int(row[0])
        County = str(row[1])
        Candidate = str(row[2])

        if not any(Candidate in list_item for list_item in list_candidates):
            list_candidates.append(Candidate)
            
        voteCounter += 1

print("Election Results")
print(" ----------------------------")
print(f"Total Votes    :   {voteCounter}")
print(f" ----------------------------")
print(list_candidates)


with open("Output.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print(" ----------------------------", file=text_file)
    print(f"Total Votes    :   {voteCounter}", file=text_file)
    print(f" ----------------------------", file=text_file)

 # Election Results
 # -------------------------
 # Total Votes: 3521001
 # -------------------------
 # Khan: 63.000% (2218231)
 # Correy: 20.000% (704200)
 # Li: 14.000% (492940)
 # O'Tooley: 3.000% (105630)
 # -------------------------
 # Winner: Khan
 # -------------------------