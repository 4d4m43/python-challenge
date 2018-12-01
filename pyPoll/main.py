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
    votesKhan = 0
    votesLi = 0
    votesCorrey = 0
    votesOtooley = 0
    voteWinner = ""
    list_candidates = []
    dict_candidates = {}

    for row in csvreader:

        #VoterID = int(row[0])
        #County = str(row[1])
        Candidate = str(row[2])

        if not any(Candidate in list_item for list_item in list_candidates):
            list_candidates.append(Candidate)
            dict_candidates.update({Candidate: 0})
        voteCounter += 1
    
election_csv = os.path.join("C:/Users/adama/Desktop/python-challenge/PyPoll/Resources", "election_data.csv")

with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    
    csv_header = next(csvreader)
    print(list_candidates)

    for row in csvreader:

        Candidate = str(row[2])

        if Candidate == list_candidates[0]:
            votesKhan += 1
            dict_candidates.update({Candidate: votesKhan})
        elif Candidate == list_candidates[1]:
            votesCorrey += 1
            dict_candidates.update({Candidate: votesCorrey})
        elif Candidate == list_candidates[2]:
            votesLi += 1
            dict_candidates.update({Candidate: votesLi})
        elif Candidate == list_candidates[3]:
            votesOtooley += 1
            dict_candidates.update({Candidate: votesOtooley})

voteWinner = max(dict_candidates.values())
maxLetters = [k for k,v in dict_candidates.items() if v == voteWinner]

pctKhan = round(votesKhan/voteCounter*100,2)
pctCorrey = round(votesCorrey/voteCounter*100,2)
pctLi = round(votesLi/voteCounter*100,2)
pctOtooley = round(votesOtooley/voteCounter*100,2)

print("Election Results")
print(" ----------------------------")
print(f"Total Votes    :   {voteCounter}")
print(f" ----------------------------")
print(f"{list_candidates[0]}    :   {pctKhan}% ({votesKhan})")
print(f"{list_candidates[1]}    :   {pctCorrey}% ({votesCorrey})")
print(f"{list_candidates[2]}    :   {pctLi}% ({votesLi})")
print(f"{list_candidates[3]}    :   {pctOtooley}% ({votesOtooley})")
print(f" ----------------------------")
print(f" Winner : {maxLetters}")
print(f" ----------------------------")

with open("Output.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print(" ----------------------------", file=text_file)
    print(f"Total Votes    :   {voteCounter}", file=text_file)
    print(f" ----------------------------", file=text_file)
    print(f"list_candidates[0]    :   {pctKhan}% ({votesKhan})", file=text_file)
    print(f"list_candidates[1]    :   {pctCorrey}% ({votesCorrey})", file=text_file)
    print(f"list_candidates[2]    :   {pctLi}% ({votesLi})", file=text_file)
    print(f"list_candidates[3]    :   {pctOtooley}% ({votesOtooley})", file=text_file)
    print(f" ----------------------------", file=text_file)
    print(f" Winner : {maxLetters}", file=text_file)
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