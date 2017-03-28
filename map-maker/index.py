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
<h1>Zippia Map Maker</h1>
<h2>Where we turn CSVs into maps using magic.</h2>
<div class='row'>
<div class='formlayout col-sm-4'>
<h3>Qualatative Map</h3>
<img src="https://www.zippia.com/wp-content/uploads/2017/03/lowest-paying-job-in-each-state.jpg" class="exampleImage"/>
<ul>
<li><a href='/csvs/example-map.csv' target="blank">Download Example CSV</a>
<li>Include a "label" column. Will be the words on the map.</li>
<li>Include a "st" column with state abreviations.</li>
<li>Include a "type" column. Will color coordinate map.</li>
</ul>

<form action="/scripts/qual_map_maker.py" method="POST" enctype="multipart/form-data" >
  <label>Map Title:</label><br>
  <input type="text" name="title" value=""><br><br>
  <label>Map Data:</label><br>
  <input type="file" name="csv" accept=".csv"><br><br>
  <input type="submit" value="Create Qualatative Map">
</form>
</div><!--col-sm-4-->
<div class='formlayout col-sm-4'>
<h3>Static Heat Map</h3>
<img src="https://www.zippia.com/wp-content/uploads/2017/03/map-2015.jpg" class='exampleImage'/>
<ul>
<li><a href='/csvs/example-map.csv' target="blank">Download Example CSV</a>
<li>Don't include DC.</li>
<li>Include a "rank" column. Will be how the heat map colors.</li>
<li>Include a "st" column with state abreviations.</li>
</ul>

<form action="/scripts/static_heat_map_maker.py" method="POST" enctype="multipart/form-data" >
  Map Title:<br>
  <input type="text" name="title" value=""><br><br>
  Best Description On Legend:<br>
  <input type="text" name="left" value="Best"><br><br>
  Worst Description On Legend:<br>
  <input type="text" name="right" value="Worst"><br><br>
  Categories:<br>
  <select name="categories" class="dropDown">
    <option value="5" selected>5</option>
    <option value="10">10</option>
  </select><br><br>
  Map Data:<br>
  <input type="file" name="csv" accept=".csv"><br><br>
  <input type="submit" value="Create Static Heat Map">
</form>
</div><!--col-sm-4-->
<div class='formlayout col-sm-4'>
<h3>Interactive Heat Map</h3>
<div id="heatmap" style="width:100%;"></div>
<p style="height:0px;">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"></script><br />
<script src="https://cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min.js"></script><br />
<script src="https://research.zippia.com/files/datamaps.usa.min.js"></script><br />
<script src="https://www.zippia.com/research/profession-assets/nurses.js"></script>
</p>
<ul>
<li><a href='/csvs/example-interactive-heat-map.csv' target="blank">Download Example CSV</a>
<li>DC can be included.</li>
<li>Include a "rank" column. Will be how the heat map add colors.</li>
<li>Include a "st" column with state abreviations.</li>
<li>Include a "topic_value" column with the values in the mouse over.</li>
<li>Include a "label" column with the values to go on states. Should be <= 4 characters.</li>
</ul>

<form action="/scripts/interactive_heat_map_maker.py" method="POST" enctype="multipart/form-data" >
  <label>Map Title:</label><br>
  <input type="text" name="title" value="" required><br><br>
  <label>Topic (will be displayed on mouse over):</label><br>
  <input type="text" name="topic" value="" required><br><br>
  <label>Map Data:</label><br>
  <input type="file" name="csv" accept=".csv" required><br><br>
  <input type="submit" value="Create Interactive Heat Map">
</form>
</div><!--col-sm-4-->
</div><!--row-->
'''
print(html)

print('<div style="margin-top:40px;"><h2>Past Maps</h2>')

for filename in os.listdir('maps'):
    data_div = '<a target="_blank" href="maps/' + filename + '">' + filename + '</a></br>'
    print (data_div)

print('</div>')

print(template_footer)
