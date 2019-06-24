import os
import csv

#csvpath = os.path.join('election_data.csv')
csvpath = os.path.join('..','..','RICEHOU201906DATA1','HW','03-Python',
    'Instructions','PyPoll','Resources','election_data.csv')

total_vote = 0
candidate_list = []
candidate_vote = []
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for rows in csvreader:
        total_vote += 1
        if rows[2] not in candidate_list:
            candidate_list.append(rows[2])
            candidate_vote.append(0)
        for index, cand in enumerate(candidate_list):
            if rows[2] == cand:
                candidate_vote[index] += 1
print('Election Results')
print('----------------------------------')
print(f'Total votes: {total_vote}')
print('----------------------------------')
for index, cand in enumerate(candidate_list):
    cand_pct = '{0:.3%}'.format(candidate_vote[index]/total_vote)
    print(f'{cand}: {cand_pct} ({candidate_vote[index]})')
win_index = candidate_vote.index(max(candidate_vote))
winner = candidate_list[win_index]
print('----------------------------------')
print(f'Winner :{winner}')
print('----------------------------------')

import sys
sys.stdout = open('election_output.txt', 'w')
print('Election Results')
print('----------------------------------')
print(f'Total votes: {total_vote}')
print('----------------------------------')
for index, cand in enumerate(candidate_list):
    cand_pct = '{0:.3%}'.format(candidate_vote[index]/total_vote)
    print(f'{cand}: {cand_pct} ({candidate_vote[index]})')
win_index = candidate_vote.index(max(candidate_vote))
winner = candidate_list[win_index]
print('----------------------------------')
print(f'Winner :{winner}')
print('----------------------------------')