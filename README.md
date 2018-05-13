# Shopify Data to Facebook Custom Audience
Converts Shopify exports into clean data to import into Facebook Custom Audiences<br />
*I assume you already understand the basics of python and pandas*

## Step 1
Add exported data from Shopify to the exports directory. <br />
1. I create a new directory in /exports and name the it with the date (ex. /exports/4-4-18/ or whatever). 
2. Add the exported CSV(s) inside your newly created folder /exports/4-4-18/

## Step 2
~~Fire up jupyter notebook `jupyter notebook`~~
**Coming Soon**


## Step 3
**There are filters on the data which need to be preset or removed** <br />
Change the exports directory in shopify_to_fb_audience.py to match yours (ex. /exports/4-4-18/). <br />
Go to the bottom of the script, in the section 'Facebook to CSV' change CSV's output path and audience name to your choosing. 

## Step 4
run `python shopify_to_fb_audience.py`

## Step 5 
You will find your audience csv in the output path directory you set. Upload it to Facebook.

