#!/usr/bin/python

import cgitb, cgi
import os
import pandas as pd
import sys

path = os.path.abspath(__file__)
sys.path.append(os.path.join(os.path.dirname(path), "../"))

from map_svg import map_svg_data
from map_svg import state_label_mapping
from map_svg import header
from map_svg import sequential_ending


cgitb.enable()


def format_label(label):
    """Takes a label for a state and formats according to the following rules.
    1. Split 2 words onto 2 lines
    2. Anything grater than 2 words, split after the 2nd word onto 2 lines
    3. Make sure to escape single quote"""
    words = str(label).replace("'",r"\'").split(" ")
    if len(words) == 1:
        return label
    elif len(words) == 2 and (len(words[1])+len(words[0]))<=10:
        return " ".join(words)
    elif len(words) == 2:
        return str(r"\n").join(words)
    else:
        phrase = ''
        phrase += str(words[0]) + " " + str(words[1]) + str(r'\n')
        for i in range(2,len(words)):
            phrase += words[i] + " "
        return phrase


def qualitative_legend(colors,labels):
    legend_code = ''
    legend_code += """<div style="margin-top:20px;padding-bottom:20px;line-height:20px;position:absolute;bottom:0;right:10;font-size:12px;text-align:center;">"""
    for i in range(0,len(labels)):
        legend_code += """<div style='height:20px; width:125px; background:""" + str(colors[i]) + """;float:left;clear: both;'>""" + str(labels[i]) + """</div></br>"""
    legend_code += """</div>"""
    return legend_code

def generate_qualitative_map(map_title,job_data):
    """
    :param profession: file naming
    :param job_data: a pandas df
    :param map_type: sequential, qualitative
    :return:
    """
    base_directory = '/var/www/test'    
    html_path = '/map-maker/maps/' + map_title.replace(" ","-").lower() + '-qualitative.html'
    with open(base_directory + html_path, 'w') as m:
        code = ''
        code += header
        code += map_svg_data
        # Sets the colors for the background of the states.
        # Color Pallete
        # qualitative
        qualitative_colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5',
                              '#d9d9d9', '#bc80bd', '#ccebc5', '#ffed6f']

        for index, state in job_data.iterrows():
            # Whatever we are going to use for a label --> Either catergorical or heat map. These are the values.
            code += "usa." + state['st'].lower() + ".temperature = '" + str(state['type']) + "';\n"

        code +="""
            var current = null;
            for (var state in usa) {
                usa[state].color = Raphael.getColor();
                usa[state].scale(1,1,0,0);
                (function (st, state) {
        """

        unique_labels = list(set(job_data.type))
        # print(len(unique_labels))
        # print(unique_labels)
        if len(unique_labels) > 12:
            # print("Too Many Categories".upper())
            exit()
        for i in range(0,len(unique_labels)):
            if i == 0:
                code += """if(st.temperature == '""" + str(unique_labels[i]) + """' ){st[0].style.fill = '""" + str(qualitative_colors[i]) + """';}\n"""
            else:
                code += """else if(st.temperature == '""" + str(unique_labels[i]) + """'){st[0].style.fill = '""" + str(qualitative_colors[i]) + """';}\n"""

        code += """
                else{
                    st[0].style.fill = "#ffffff";
                }
                })(usa[state], state);
            }
        """

        for z, state_label in state_label_mapping.iterrows():
            for y, state in job_data.iterrows():
                if state_label['state_abbrev'].lower() == state['st'].lower():
                    if state_label['abbrev_needed'] == 1:
                        # var MAName = R.text(913,139, 'MA - Reebok').attr(labelBlack).toFront();
                        code += """ var """ + state_label['state_abbrev'].upper() + """Name = R.text(""" \
                                + str(int(state_label['x'])) + """, """ + str(int(state_label['y'])) + """, '""" \
                                + state_label['state_abbrev'].upper() + """ - """ + format_label(state['label']) + """').attr(labelBlack).toFront();"""
                    else:
                        # var MAName = R.text(913,139, 'Reebok').attr(labelWhite).toFront();f
                        code += """ var """ + state_label['state_abbrev'].upper() + """Name = R.text(""" \
                                + str(int(state_label['x'])) + """, """ + str(int(state_label['y'])) + """, '"""\
                                + format_label(state['label']) + """').attr(labelBlack).toFront();"""
            code += "\n"

        code += sequential_ending % (map_title.title(),qualitative_legend(qualitative_colors,unique_labels))

        m.write(code)
        m.close()

        return html_path



form = cgi.FieldStorage()
title = form.getvalue('title')
map_csv = form['csv']

job_data = pd.read_csv(map_csv.file)

html_path = generate_qualitative_map(title,job_data)

print("Location: " + html_path + "\n\n")

