#!/usr/bin/python

# Turn on debug mode.
import cgitb, cgi
import os
import pandas as pd
import map_svg
from map_svg import map_svg_data
from map_svg import state_label_mapping
from map_svg import header
from map_svg import sequential_ending
cgitb.enable()

'''
How To Format Input CSV:
1. state, st, brewery,label,rating,rank,type
s
'''


form = cgi.FieldStorage()
state = form.getvalue('state')
city = form.getvalue('city')
organization = form.getvalue('organization')


df = pd.read_csv('map-maker/data/highest-paying-jobs-data.csv')

def mailgun_emailer(cities,states,organizations):
    #import os
    #os.system('python ~/ga-reporting/HelloAnalytics.py')
    return ' '.join([cities,states,organizations])

result = mailgun_emailer(city,state,organization)
# Print necessary headers.
print("Content-Type: text/html")
print()

print(result)
