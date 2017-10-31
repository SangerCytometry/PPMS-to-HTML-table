#Copyright (c) 2017 Genome Research Ltd.

#PPMS to CSV
#v1.0 May 2017
#Python 2.7 (2016)
#Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk
#Big contribution from https://www.rosettacode.org (GFDLv1.2)

#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

#This script takes the daily bookings from PPMS and creates an ordered CSV file and then an HTML file to load in a browser
#You should contact Stratocore support about how to use there API system and remember it is best to test on a non production environment first

#'Requests' and 'petl' need to be installed using PIP.  See the Python documentation, or http://docs.python-requests.org/en/master/ for details.
import requests
import time
import csv
from cgi import escape
import os
import petl
import re

#insert the directory of the script.  Remember that in windows you need to change the \ for /
os.chdir('')

#Insert your PUMAPI address here
url=''
date=time.strftime("%Y-%m-%d")

#Insert the API details into apikey and plateformid
payload = {'apikey': '', 'action': 'getrunningsheet', 'plateformid': '', 'day': date}
headers = {'content-type': 'application/x-www-form-urlencoded'}
#gets the information from ppms and creates a csv file
r = requests.post(url, data=payload, headers=headers)
f = open('todays_bookings.csv', 'wb')
f.write(r.text)
f.close()

#Load the table
table1 = petl.fromcsv('todays_bookings.csv')
# Alter the columns
table2 = petl.cut(table1,' Object', ' User',' Start time',' End time',' Training',' Assisted')
# Reorder the user names
table3 = petl.convert(table2, ' User', lambda row:" ".join(re.findall("\S+",row)[::-1]))
# Reorder the rows
table4 = petl.sort(table3,key=[' Object', ' Start time'])
# Save to new file
petl.tocsv(table4, 'new.csv')

#Reopens the CSV file (stupid, I know) and removes unnecessary characters
csvfile=""
ppmscal = csv.reader(open('new.csv'), delimiter=',')
for row in ppmscal:
	csvfile+=str(row)+'\n'
csvtxt=csvfile.replace("(", "").replace(")", "").replace("'", "").replace("[", "").replace("]", "")
csvtxt=csvtxt[:-1]

#The CSV to HTML code has come from https://www.rosettacode.org/wiki/CSV_to_HTML_translation#Python
#It creates an html file of the CSV so I can load, and auto-refresh it in  browser
def _row2trextra(row, attr=None):
    cols = escape(row).split(',')
    attr_tr = attr.get('TR', '')
    attr_td = attr.get('TD', '')
    return (('<TR%s>' % attr_tr)
            + ''.join('<TD%s>%s</TD>' % (attr_td, data) for data in cols)
            + '</TR>')

def csv2htmlextra(txt, header=True, attr=None):
    ' attr is a dictionary mapping tags to attributes to add to that tag'
 
    attr_table = attr.get('TABLE', '')
    attr_thead = attr.get('THEAD', '')
    attr_tbody = attr.get('TBODY', '') 
    htmltxt = '<TABLE%s>\n' % attr_table
    for rownum, row in enumerate(txt.split('\n')):
        htmlrow = _row2trextra(row, attr)
        rowclass = ('THEAD%s' % attr_thead) if (header and rownum == 0) else ('TBODY%s' % attr_tbody)
        htmlrow = '  <%s>%s</%s>\n' % (rowclass, htmlrow, rowclass[:5])
        htmltxt += htmlrow
    htmltxt += '</TABLE>\n'
    return htmltxt

htmltxt = csv2htmlextra(csvtxt, True,
                        dict(TABLE=' border="1" width="100%" summary="csv2html extra program output"',
                             THEAD=' bgcolor="White "',
                             TBODY=' bgcolor="White"' 
                             )
                        )
#This section reformats the table to produce pretty colours.  Change our cytometer names to the names of your instruments and remove the excess, or add more.
newhtml=[]
htmltxt=htmltxt.splitlines()
for line in htmltxt:
    if 'BD Fortessa 1' in line:
        newhtml.append(line.replace("White","#C38EC7"))
    elif 'BD Fortessa 2' in line:
        newhtml.append(line.replace("White","#E2A76F"))    
    elif 'BDLSRII' in line:
        newhtml.append(line.replace("White","#F660AB"))    
    elif 'Cytoflex' in line:
        newhtml.append(line.replace("White","orange"))    
    elif 'Sony 1' in line:
        newhtml.append(line.replace("White","Cyan"))   
    elif 'Sony 2' in line:
        newhtml.append(line.replace("White","MistyRose")) 
    elif 'Influx' in line:
        newhtml.append(line.replace("White","PaleGreen"))         
    elif 'XDP' in line:
        newhtml.append(line.replace("White","Yellow"))    
    elif 'MoFlo' in line:
        newhtml.append(line.replace("White","#3374FF"))
    else:
        newhtml.append(line)
newhtml=str(newhtml)
newhtml=newhtml.replace("', '","").replace("['","").replace("']","")

#creates the final html file
f = open('todaysbookings.html', 'wb')
f.write(newhtml)
f.close()

