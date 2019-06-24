#import modules needed to pull in data and output results
import os
import csv
import sys

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#point to location of csv input file
csvpath = os.path.join('..','..','RICEHOU201906DATA1','HW','03-Python',
    'ExtraContent','Instructions','PyBoss','employee_data.csv')
#point to lcation of csv output file
outpath = os.path.join("employee_output.csv")


with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    print(csv_header)

    with open(outpath, 'w', newline='') as outfile:

        # Initialize csv.writer
        csvwriter = csv.writer(outfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Emp ID','First Name', 'Last Name','DOB', 'SSN','State'])



        for rows in csvreader:
            name_temp = rows[1]
            date_temp = ['','','']
            name_list = name_temp.split()
            first_name = name_list[0]
            last_name = name_list[1]
            date_list = rows[2].split('-',)
            for i in range(3):
                if int(date_list[i]) < 10:
                    date_temp[i]=' ' +str(date_list[i])
                else:
                    date_temp[i] = str(date_list[i])
            date_format = date_temp[1] +'/'+date_temp[2]+'/'+date_temp[0]
            ssn = rows[3].split('-',)
            new_ssn = '***-**-'+str(ssn[2])
            full_state = rows[4]
            abrv_state = str(us_state_abbrev[full_state])
            csvwriter.writerow([rows[0],first_name, last_name, date_format, new_ssn, abrv_state])
    #print(abrv_state)

