#!/usr/bin/python
# Generate a time hierarchy: 
# YYYY, Quarter,Month, Week, day,day_of_month,day_of_year
from datetime import date
from dateutil.rrule import rrule, DAILY


start_date = date(1990,1,1)
end_date = date(2013,12,31)
q = 0

for dt in rrule(DAILY,dtstart=start_date,until=end_date):
	m = dt.strftime("%m")
	if m == '01' or m == '02' or m == '03':
		q = 1
	if m == '04' or m == '05' or m == '06':
		q = 2
	if m == '07' or m == '08' or m == '09':
		q = 3
	if m == '10' or m == '11' or m == '12':
		q = 4
	qtext = "Quarter%i" % q
	#print qtext
	print dt.strftime("%Y%m%d"),dt.strftime("%Y"),qtext,dt.strftime("%B"),dt.strftime("%U"),dt.strftime("%d"),dt.strftime("%j")
