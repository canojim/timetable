import csv
import time
from datetime import datetime
from datetime import timedelta

def read_timetable(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)

        rownum = 0
        timetable = {}
        for row in reader:
            key = row[0] + '_' + row[1]
            timetable[key] = row
            #print key, row
        return timetable

#########################
odd_even_dict = { 0: 'Even', 1: 'Odd'}
day_of_week_dict = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}

timetable = read_timetable('timetable.csv')
#print timetable

localtime = datetime.now()

num_of_days=7
for i in range(num_of_days):
    wkday = localtime.weekday()
    odddoreven = localtime.isocalendar()[1] % 2
    if wkday < 5:
        print odd_even_dict[odddoreven], "Week:", localtime.strftime("%A, %d. %B %Y")
        #print "dayofweek", day_of_week_dict[localtime.weekday()], "odd/even", odd_even_dict[localtime.day % 2]
        key  = day_of_week_dict[wkday] + '_' + odd_even_dict[odddoreven]
        print timetable[key]

    localtime += timedelta(days=1)
