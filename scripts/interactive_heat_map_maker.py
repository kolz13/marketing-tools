#!/usr/bin/python

import cgitb, cgi
import os
import pandas as pd
import sys

path = os.path.abspath(__file__)
sys.path.append(os.path.join(os.path.dirname(path), "../"))

from html_template import header
from html_template import footer as template_footer

cgitb.enable()
print("Content-type: text/html")
print("")

def generate_heat_map(map_title,job_data,topic):
    base_directory = '/var/www/test/'
    js_directory = 'map-maker/maps/js'
    if not os.path.exists(os.path.join(base_directory,js_directory)):
        os.makedirs(os.path.join(base_directory,js_directory))
    file_name ='/' + map_title.replace(" ","-").lower() + '.js'
    html_path = base_directory + js_directory + file_name
    with open(html_path, 'w') as m:
        code = 'var USdata = {\n'
        for index, state in job_data.iterrows():
            if index == 49:
                code += "'" + state['st'].upper() + "' :'" + str(state['label']) + "'\n"
            else:
                code += "'" + state['st'].upper() + "' :'" + str(state['label']) + "',\n"

        code += '};\n'

        code += """
var living_wage = new Datamap({
  scope: 'usa',
  element: document.getElementById('heatmap'),
  responsive: true,
  geographyConfig: {
    highlightBorderColor: '#bada55',
   popupTemplate: function(geography, data) {
      return '<div class="hoverinfo" style="text-align:center;">' + geography.properties.name + '</br>Rank: ' +  data.rank + '</br>""" + topic + """: ' +  data.average_salary + ' '
    },
    highlightBorderWidth: 3
  },

  fills: {
  'Bottom20': '#fef0d9', //Lightest
  'Bottom40': '#fdcc8a',
  'Bottom60': '#fc8d59',
  'Bottom80': '#e34a33',
  'Bottom100': '#b30000', //Darkest
  defaultFill: '#fff'
},
data:{
"""
        for index, state in job_data.iterrows():
            if state['rank'] <= 10:
                fillKey = 'Bottom100'
            elif state['rank'] <= 20:
                fillKey = 'Bottom80'
            elif state['rank'] <= 30:
                fillKey = 'Bottom60'
            elif state['rank'] <= 40:
                fillKey = 'Bottom40'
            else:
                fillKey = 'Bottom20'
            if index == 49:
                code += "'" + state['st'].upper()+ "' : {'fillKey' : '" + fillKey + "', 'rank' : '" + str(int(state['rank'])) + "', 'average_salary' : '" + str(state['topic_value']).replace("'",r"\'") + "'}\n"
            else:
                code += "'" + state['st'].upper()+ "' : {'fillKey' : '" + fillKey + "', 'rank' : '" + str(int(state['rank'])) + "', 'average_salary' : '" + str(state['topic_value']) + "'},\n"
        code += """
}
});

if(window.innerWidth>800){
    living_wage.labels({'customLabelText': USdata, fontSize: 14, transform: 'translate(1000,0)'});
    living_wage.legend({
        legendTitle : '""" + map_title + """',
        labels: {
          'Bottom20': "Bottom Quintile:", //Lightest
          'Bottom40': '&nbsp;&nbsp;&nbsp;&nbsp;2nd Quintile:',
          'Bottom60': '&nbsp;&nbsp;&nbsp;&nbsp;3rd Quintile:',
          'Bottom80': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4th Quintile:',
          'Bottom100': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Top Quintile:', //Darkest
        }
      });
  }
  else{
    living_wage.labels({'customLabelText': USdata, fontSize: 8, transform: 'translate(1000,0)'});
  };

    // Pure JavaScript
window.addEventListener('resize', function() {
    living_wage.resize();
});

var legend_width = document.getElementsByClassName("datamaps-legend")[0].scrollWidth
var container_width = document.getElementById("heatmap").scrollWidth;
var new_length = (container_width/2) - (legend_width/2)

console.log(new_length);
var legend = document.getElementsByClassName("datamaps-legend")[0];
legend.style.left = new_length + 'px';

document.querySelector("div.datamaps-legend h2").style.textAlign = "center";
document.querySelector("div.datamaps-legend h2").style.marginTop = "-20px";
"""
        m.write(code)
        m.close()

        return js_directory + file_name


form = cgi.FieldStorage()
title = form.getvalue('title')
map_csv = form['csv']
topic = form.getvalue('topic')

# Need 'rank' column with ranking
# Need 'st' column with state abbreviation
# Need 'label' column. Will be shown on map. Ideally <4 characters.
# Need 'topic_value' column. Will be displayed when you mouse over.
job_data = pd.read_csv(map_csv.file)

html_path = '/' + generate_heat_map(title,job_data,topic)

textarea_content = """
<div id="heatmap" style="width:100%;"></div>
<p style="height:0px;">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"></script><br />
<script src="https://cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min.js"></script><br />
<script src="https://research.zippia.com/files/datamaps.usa.min.js"></script><br />
<script src="{}"></script>
</p>
"""

html ='<h1>Interactive Map Assets</h1> \
<h2>Download js file and upload to Amazon.</h2> \
<ul> \
<li><b><a href="{}">Download This</a></b></li> \
<li>Add the following code to the wordpress article.</li> \
<li>Substitute the Amazon link to the js file for the ############################.</li> \
</ul> \
<textarea style="width:100%;height:300px;">{}</textarea>'.format(html_path,textarea_content.format('###########'))


context = {'head' : ''}
print(header.format(**context))
print(html)
print(textarea_content.format(html_path))
print(template_footer)
