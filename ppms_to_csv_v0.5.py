#Copyright (c) 2017 Genome Research Ltd.

#PPMS to CSV
#v0.5 Jan 2017
#Python 2.7 (2016)
#Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk

#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

#This script takes the daily bookings from PPMS and creates an ordered CSV file
#You should contact Stratocore support about how to use there API system and remember it is best to test on a non production environment first

#Requests needs to be installed using PIP.  See the Python documentation, or http://docs.python-requests.org/en/master/ for details.
import requests
import time
import csv
import operator
import sys

#Insert your API address here
url=''
date=time.strftime("%Y-%m-%d")

#Insert the API details into apikey and plateformid
payload = {'apikey': '', 'action': 'getrunningsheet', 'plateformid': '', 'day': date}
headers = {'content-type': 'application/x-www-form-urlencoded'}
#gets the information from ppms and creates a csv file
r = requests.post(url, data=payload, headers=headers)
f = open('todays_bookings.csv', 'w')
f.write(r.text)
f.close

#Sorts the CSV file
def csvsort(csvfilename, col1, col2):
	with open(csvfilename, 'rb') as f:
		csvread = csv.reader(f)
		csvdata = list(csvread)
	csvdata.sort(key=operator.itemgetter(col1,col2))
	with open(csvfilename, 'wb') as f:
		csvwrite = csv.writer(f)
		csvwrite.writerows(csvdata)
f.close()

filename= 'todays_bookings.csv'
csvsort(filename, 3, 1)


