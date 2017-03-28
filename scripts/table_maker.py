#!/usr/bin/python

import cgitb, cgi
import os
import pandas as pd
import io
import sys

path = os.path.abspath(__file__)
sys.path.append(os.path.join(os.path.dirname(path), "../"))

from html_template import header

cgitb.enable()
print("Content-type: text/html")
print("")

form = cgi.FieldStorage()
map_csv = form['csv']

table_data = pd.read_csv(map_csv.file)

def tablemaker(df):
    f = io.StringIO()

    f.write('<table><thead><tr>\n')

    # Create a header for each row in the table.
    columns = list(df)
    for i, column in enumerate(columns):
        f.write('<th class="column' + str(i) + '">' + str(column).title() + '</th>\n')

    f.write('</tr></thead><tbody>')

    # For each row in the csv, iterate through the cells and create <td>s. Additioanlly, assign them each a
    # corresponding class.
    for index, row in df.iterrows():
        f.write('<tr class="row' + str(index) + '">')
        for i, column in enumerate(columns):
            # If a decimal or large number, change the formatting.
            if isinstance(row[column],int):
                f.write('<td class="column' + str(i) + '">' + str(format(row[column],",d")) + '</td>')
            elif isinstance(row[column],float):
                if row[column] >= 1000:
                    f.write('<td class="column' + str(i) + '">' + str(format(int(row[column]),",d")) + '</td>')
                elif row[column] < 1:
                    f.write('<td class="column' + str(i) + '">' + str(round(row[column]*100,2)) + '%</td>')
                else:
                    f.write('<td class="column' + str(i) + '">' + str(int(row[column])) + '</td>')
            else:
                f.write('<td class="column' + str(i) + '">' + str(row[column]).title() + '</td>')
        f.write('</tr>\n')

    f.write('</tbody></table>')
    content = f.getvalue()
    f.close()
    return content

table_html = tablemaker(table_data)

html = '<body> \
<h1>Table Results</h1> \
<h2>Copy Code Into Wordpress</h2> \
<ul> \
<li>Can only have max 3 columns on mobile.</li> \
<li>If you need to hide columns on mobile, find and replace the class for the column to "hide-on-mobile".</li> \
<li>For example, find replace "column0" with "hide-on-mobile".</li> \
</ul> \
<textarea style="width:100%;height:400px;">{}</textarea> \
<h2>Quick Idea of what to expect</h2>{}</body></html>'.format(table_html,table_html)

context = {'head' : ''}
print(header.format(**context))
print(html)
