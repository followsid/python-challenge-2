
import os
import csv


csvpath = os.path.join('election_data.csv')


total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""


with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        
        total_votes += 1
        
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        
        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

       
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]



