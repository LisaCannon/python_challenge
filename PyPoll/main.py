#import modules needed to pull in data and output results
import os
import csv
import sys

#point to location of cvs file
csvpath = os.path.join('..','..','RICEHOU201906DATA1','HW','03-Python',
    'Instructions','PyPoll','Resources','election_data.csv')

#initialize variables
#will keep count of the total number of overall votes
total_vote = 0
#will store the names of the candidates that are voted for
candidate_list = []
#will store the number of votes for each candidate
candidate_vote = []
#open data file useing defined path
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #look at each row to count votes for eah candidate
    for rows in csvreader:
        total_vote += 1
        #checks to see if candidate listed is in the candidate list
        if rows[2] not in candidate_list:
            candidate_list.append(rows[2])
            candidate_vote.append(0)
        #loops through candidate list to add to the number of votes for given candidate
        for index, cand in enumerate(candidate_list):
            #adds a tally to the list containing number of votes per candidate
            if rows[2] == cand:
                candidate_vote[index] += 1

#finds the index postition of the candidate with the most votes; 
# index of candidate list corresponds to index of number of votes
win_index = candidate_vote.index(max(candidate_vote))
winner = candidate_list[win_index]

#output to the terminal
print('Election Results')
print('----------------------------------')
print(f'Total votes: {total_vote}')
print('----------------------------------')
#for loop prints results for each candidate in the cadidate list
for index, cand in enumerate(candidate_list):
    #calculates the percentage of votes for given candidate
    cand_pct = '{0:.3%}'.format(candidate_vote[index]/total_vote)
    print(f'{cand}: {cand_pct} ({candidate_vote[index]})')
print('----------------------------------')
print(f'Winner :{winner}')
print('----------------------------------')

#creates an output txt file in the same folder
sys.stdout = open('election_output.txt', 'w')
print('Election Results')
print('----------------------------------')
print(f'Total votes: {total_vote}')
print('----------------------------------')
for index, cand in enumerate(candidate_list):
    cand_pct = '{0:.3%}'.format(candidate_vote[index]/total_vote)
    print(f'{cand}: {cand_pct} ({candidate_vote[index]})')
print('----------------------------------')
print(f'Winner :{winner}')
print('----------------------------------')