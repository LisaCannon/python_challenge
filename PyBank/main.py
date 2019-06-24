import os
import csv

csvpath = os.path.join('..','..','RICEHOU201906DATA1','HW','03-Python',
    'Instructions','PyBank','Resources','budget_data.csv')
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    month_count = 0
    pl_tot = 0
    incmax = 0
    decmax = 0

    for a in csvreader :
        month_count += 1
        pl_tot += int(a[1])
        if int(a[1]) > incmax:
            incmax = int(a[1])
            incdate = str(a[0])
        elif int(a[1]) < decmax:
            decmax = int(a[1])
            decdate = str(a[0])

    avg_chg = '${:,.2f}'.format(pl_tot/month_count)
    total_money = '${}'.format(pl_tot)
    dec_money = '${}'.format(decmax)
    inc_money = '${}'.format(incmax)

    print("Finalcial Analysis")
    print('--------------------------------')
    print(f'Total Months: {month_count}')
    print(f'Total:  {total_money}') 
    print(f'Average Change: {avg_chg}')
    print(f'Greatest Increase in Profits: {incdate} {inc_money}')
    print(f'Greatest Decrease in Profits: {decdate} {dec_money}')

import sys
sys.stdout = open('budget_output.txt', 'w')
print("Finalcial Analysis")
print('--------------------------------')
print(f'Total Months: {month_count}')
print(f'Total:  {total_money}') 
print(f'Average Change: {avg_chg}')
print(f'Greatest Increase in Profits: {incdate} {inc_money}')
print(f'Greatest Decrease in Profits: {decdate} {dec_money}')