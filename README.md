#XDP sort statistics extractor
 
Copyright (c) 2017 Genome Research Ltd.

Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk

http://www.sanger.ac.uk/science/groups/cytometry-core-facility

We are in the process of creating a dally schedule view to display on a TV in the lab.  This is the prototype that queries PPMS and produces a sorted CSV file of the day’s schedule.  From this you can create a live data link into an Excel spreadsheet, have them both update regularly and display them real time on screen.  The next stage will be to produce a graphical representation of this data.

This script takes the daily bookings from PPMS and creates an ordered CSV file.
You should contact Stratocore support about how to use the API system and remember it is best to test on a non production environment first.

##INSTRUCTIONS
Install the Python dependency 'Requests' using PIP in the python command line.  http://docs.python-requests.org/en/master/user/install/  It's a bit of a pain, and not as easy as this page suggests.  Find a Python person (google it) if you cannot do it.

On line 23 insert the API web address to your PPMS website between the ''

On line 27 add the API key and platform ID between the two ''.  The platform ID is the pf?= number found in the address bar when you log into PPMS.

Run the script and it produces a CSV file

You can then create an excel sheet with a live data source and have it automatically update.

Use windows task scheduler to run the python script every 10 minutes to keep the CSV file up to date.

The file ppms_to_csv_sched.bat can be used to do this.  Just replace the first portion with the location of your python installation and the second with the location of your script.

