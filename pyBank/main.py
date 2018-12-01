# PyBank main.py
# author @ Adam Abdelmalek
# date @ 120118

import os
import csv

bank_csv = os.path.join("C:/Users/adama/Desktop/python-challenge/PyBank/Resources", "budget_data.csv")

with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    
    csv_header = next(csvreader)
    #print(f"{csv_header}")
    
    #Calculated Values monthCounter, dollarTotal, avgChange, greatestInc, greatestDec
    monthCounter = 0
    dollarTotal = 0
    avgChange = 0
    greatestInc = 0
    greatestDec = 0
    prevDollar = 0
    prevDelta = 0
    deltaTotal = 0
    delta = 0

    for row in csvreader:

        dollar = float(row[1])
        dollarTotal =  round(float(dollarTotal) + dollar,2)

        print(dollarTotal)
        if monthCounter >= 1:
            delta = dollar - prevDollar
            deltaTotal = deltaTotal + delta
        
        monthCounter = monthCounter + 1

        if delta > greatestInc:
            greatestInc = delta
            greatestIncDate = row[0]
        elif delta < greatestDec:
            greatestDec = delta
            greatestDecDate = row[0]

        prevDelta = delta
        prevDollar = dollar

avgChange = round(deltaTotal/(monthCounter-1),2)

print("Financial Analysis")
print(" ----------------------------")
print(f"Total Months    :   {monthCounter}")
print(f"Total           :   ${dollarTotal}")
print(f"Average Change  :   ${avgChange}")
print(f"Greatest Increase in Profits    :   {greatestIncDate} ${greatestInc}")
print(f"Greatest Decrease in Profits    :   {greatestDecDate} ${greatestDec}")


with open("Output.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print(" ----------------------------", file=text_file)
    print(f"Total Months    :   {monthCounter}", file=text_file)
    print(f"Total           :   ${dollarTotal}", file=text_file)
    print(f"Average Change  :   ${avgChange}", file=text_file)
    print(f"Greatest Increase in Profits    :   {greatestIncDate} ${greatestInc}", file=text_file)
    print(f"Greatest Decrease in Profits    :   {greatestDecDate} ${greatestDec}", file=text_file)

 #Financial Analysis
 # ----------------------------
 # Total Months: 86
 # Total: $38382578
 # Average  Change: $-2315.12
 # Greatest Increase in Profits: Feb-2012 ($1926159)
 # Greatest Decrease in Profits: Sep-2013 ($-2196167)

