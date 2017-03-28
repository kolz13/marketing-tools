#!/usr/bin/python

import cgitb, cgi
import os
import sys

path = os.path.abspath(__file__)
sys.path.append(os.path.join(os.path.dirname(path), "../"))

from html_template import header
from html_template import footer as template_footer

cgitb.enable()

print('Content-Type: text/html')
print()


style ='''<style>
    .formlayout{
        border: 1px solid #efefef;
	margin: 20px;
	padding: 20px;
    }
    .exampleImage{
        width:100%;
    }
    .formlayout input,select{
        padding:10px;
	border-radius:5px;
	width:100%;
    }
    .dropDown{
        width:25%;
    }
    </style>
'''

context = {'head' : style}

print(header.format(**context))

html = '''
<h1>Table Maker</h1>
<h2>Where we turn CSVs into HTML tables.</h2>
<div class='row'>
<div class='formlayout col-sm-4'>
<h3>Upload Table Data</h3>
<form action="/scripts/table_maker.py" method="POST" enctype="multipart/form-data" >
  Table Data:<br>
  <input type="file" name="csv" accept=".csv"><br><br>
  <input type="submit" value="Create HTML Table">
</form>
</div><!--col-sm-4-->
</div><!--row-->
'''
print(html)


print(template_footer)
