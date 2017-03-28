#!/usr/bin/python

# Turn on debug mode.
import cgitb, cgi
import os
from html_template import header
from html_template import footer as template_footer

cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

context = {'head' : '<title>Site Statistics - Zippia</title>'}

print(header.format(**context))

list_of_graphs = '''<h1>Site Statistics</h1> <div id="hiddenData">'''
print(list_of_graphs)

def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))

# for filename in os.listdir('graphs'):

for filename in sorted_ls('graphs'):
    data_div = '<a target="_blank" href="graphs/' + filename + '"><img src="graphs/' + filename + '" style="width:100%;" /></a>'
    data_div += '<p><a target="_blank" href="csvs/' + filename.replace('.png','') + '.csv">Download Data</a></p>'
    data_div += '<hr style="margin-top:20px;margin-bottom:20px;"></hr>'
    print (data_div)

print(template_footer)
