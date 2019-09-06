This page has been archived and further updates will be on Christopher’s [GitHub page]( https://github.com/hally166/PPMS-to-HTML-table).

# PPMS to HTML table

Copyright (c) 2017 Genome Research Ltd.

Author : Christopher Hall, Wellcome Trust Sanger Institute.

The CSV to HTML code has come from https://www.rosettacode.org/wiki/CSV_to_HTML_translation#Python (GFDLv1.2)

http://www.sanger.ac.uk/science/groups/cytometry-core-facility

We have a daily schedule TV in the lab and have produced a script to run this.  The script queries the PPMS calendar system and produces a sorted HTML file of the day’s schedule.

You should contact Stratocore support about how to use the API system.

## Example
![alt text](PPMS%20calendar.png)

## INSTRUCTIONS
Install the Python dependency 'Requests' and 'petl' using PIP in the python command line.  http://docs.python-requests.org/en/master/user/install/.  Do this by opening the command prompt, navigating to your python\scripts directory (i.e. C:\Python27\Scripts) and typeing 'pip install requests' (or petl).  You cannot do this from within the python shell.

On line 21 add the folder name of where the script resides.  This is to allow the script to run from the Windows Task Scheduler.

On line 24 insert the API web address to your PPMS website between the ''

On line 28 add the API key and platform ID between the two ''.  The platform ID is the pf?= number found in the address bar when you log into PPMS.

The last large section of the script should be changed to match your instrumentation.

Run the script and it produces a .html file

Load this in a browser and 'auto-refresh' the page to keep it up to date.  (look for plugins or extensions, we use Chrome)

Use windows task scheduler to run the python script every 10 minutes to keep the CSV file up to date.

The file ppms_to_csv_sched.bat can be used to do this.  Just replace the first portion with the location of your python installation and the second with the location of your script.

We also run a slideshow of picture posters on the same screen as shown above using IrfanView. www.irfanview.com/ 
