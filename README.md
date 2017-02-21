#PPMS to CSV (now with added HTML)
 
Copyright (c) 2017 Genome Research Ltd.

Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk

The CSV to HTML code has come from https://www.rosettacode.org/wiki/CSV_to_HTML_translation#Python (GFDLv1.2)

http://www.sanger.ac.uk/science/groups/cytometry-core-facility

We are in the process of creating a dally schedule view to display on a TV in the lab.  This is the prototype that queries PPMS and produces a sorted html document.

You should contact Stratocore support about how to use the API system and remember it is best to test on a non production environment first.

##INSTRUCTIONS
Install the Python dependency 'Requests' using PIP in the python command line.  http://docs.python-requests.org/en/master/user/install/  Do this by opening the command prompt, navigating to your python\scripts directory (i.e. C:\Python27\Scripts) and typeing 'pip install requests'.  You cannot do this from within the python shell.

On line 29 insert the API web address to your PPMS website between the ''

On line 33 add the API key and platform ID between the two ''.  The platform ID is the pf?= number found in the address bar when you log into PPMS.

Run the script and it produces a .html file

Load this in a browser and 'auo-refresh' the page to keep it up to date.  (look for plugins or extensions)

Use windows task scheduler to run the python script every 10 minutes to keep the CSV file up to date.

The file ppms_to_csv_sched.bat can be used to do this.  Just replace the first portion with the location of your python installation and the second with the location of your script.

