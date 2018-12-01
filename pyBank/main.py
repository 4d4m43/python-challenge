# PyBank main.py
# author @ Adam Abdelmalek
# date @ 120118

import os
import csv

bank_csv = os.path.join("C:/Users/adama/Desktop/3/Activities/01-Stu_CerealCleaner/Resources", "cereal_bonus.csv")

with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    
    #csv_header = next(csvreader)
    #print(f"{csv_header}")
      
    for row in csvreader:
        if float(row[7]) >= 5: 
            print(row)  
