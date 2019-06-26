#import modules needed to pull in data and output result
import os
import csv
import sys

#point to location of cvs file
csvpath = os.path.join('..','..','RICEHOU201906DATA1','HW','03-Python',
    'Instructions','PyBank','Resources','budget_data.csv')

#initialize variables
#counts the number of months of data
month_count = 0
#totals the P&L values
pl_tot = 0
#will hold greatest increase
incmax = 0
#will hold greatest decrease
decmax = 0
#will total the month-over-month change
change_tot = 0

#open data file using defined path
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #loop through each row in P&L data to calculate results
    for i, a in enumerate(csvreader) :
        month_count += 1
        pl_tot += int(a[1])
        #subtracts last month P&L from current month to get change and gets running total
        if i > 0:
            change_calc = int(a[1]) - pl_last
            change_tot += change_calc
        pl_last = int(a[1])
        #check to see if monthly value is the greatest increase
        if int(a[1]) > incmax:
            incmax = int(a[1])
            incdate = str(a[0])
        #check to see if montly value is the greatest decrease
        elif int(a[1]) < decmax:
            decmax = int(a[1])
            decdate = str(a[0])

#calculations and formatting
avg_chg = '${:,.2f}'.format(change_tot/month_count)
total_money = '${}'.format(pl_tot)
dec_money = '${}'.format(decmax)
inc_money = '${}'.format(incmax)

#output to the terminal
print("Finalcial Analysis")
print('--------------------------------')
print(f'Total Months: {month_count}')
print(f'Total:  {total_money}') 
print(f'Average Change: {avg_chg}')
print(f'Greatest Increase in Profits: {incdate} {inc_money}')
print(f'Greatest Decrease in Profits: {decdate} {dec_money}')

#creates an output file in the same folder
sys.stdout = open('budget_output.txt', 'w')
print("Finalcial Analysis")
print('--------------------------------')
print(f'Total Months: {month_count}')
print(f'Total:  {total_money}') 
print(f'Average Change: {avg_chg}')
print(f'Greatest Increase in Profits: {incdate} {inc_money}')
print(f'Greatest Decrease in Profits: {decdate} {dec_money}')