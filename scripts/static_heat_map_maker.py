#!/usr/bin/python

import cgitb, cgi
import os
import pandas as pd
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

def sequential_legend(colors,legend_description_left,legend_description_right):
    legend_code = '<div style="margin-left:auto;margin-right:auto;width:625px;margin-top:20px;padding-bottom:20px;">'
    legend_code += '<div>'
    for index, color in enumerate(colors):
        i = 0 - index - 1
        legend_code += '<div style="height:20px; width:' + str(int(625 / len(colors))) + 'px; background:' + str(colors[i]) + ';float:left;"></div>'
    legend_code += '</br>'
    legend_code += '<div style="width:625px;">'
    legend_code += '<div style="float:left;" class="degrees">' + legend_description_left + '</div>'
    legend_code += '<div style="float:right;" class="degrees">' + legend_description_right + '</div>'
    legend_code += '</div>'
    legend_code += '</div>'
    legend_code += '</div>'
    return legend_code

def generate_static_heat_map(map_title,job_data,legend_description_left,legend_description_right,number_of_categories=5):
    """
    :param profession: file naming
    :param job_data: a pandas df
    :param map_type: sequential, qualitative
    :return:
    """
    base_directory = '/var/www/test/'    
    html_path = '/map-maker/maps/' + map_title.replace(" ", "-").lower() + '-heat-map.html'
    with open(base_directory + html_path, 'w') as m:
        code = ''
        code += header
        code += map_svg_data
        # Sets the colors for the background of the states.
        # Color Pallete
        # Lightest To Darketst
        colors = ['#67001f', '#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#d1e5f0', '#92c5de','#4393c3', '#2166ac', '#053061']
        for index, state in job_data.iterrows():
            # Whatever we are going to use for a label --> Either catergorical or heat map. These are the values.
            code += "usa." + state['st'].lower() + ".temperature = " + str(state['rank']) + ";"

        code += """
            var current = null;
            for (var state in usa) {
                usa[state].color = Raphael.getColor();
                usa[state].scale(1,1,0,0);
                (function (st, state) {
                """

        categories = int(number_of_categories)
        for i in range(0,categories):
            percentile = 50 / categories
            color = (-1 * categories) + i
            if i == 0:
                code += "if (st.temperature > " + str(int(50 - percentile)) + "){"
                code += "st[0].style.fill = '" + str(colors[color]) + "';"
                code += "}\n"
            elif i == categories-1:
                code += "else{"
                code += "st[0].style.fill = '" + str(colors[color]) + "';"
                code += "}\n"
            else:
                code += "else if (st.temperature > " + str(int(50 - (percentile * (i + 1)))) + "){"
                code += "st[0].style.fill = '" + str(colors[color]) + "';"
                code += "}\n"
        code += """
                })(usa[state], state);
            }
        """

        # We need to handle the labeling on the map for different states. The east coast states need the state abbrev in
        # front of them. Examples above each of the
        # Need st == state_abbrev | rank = ranking ordinal
        for z, state_label in state_label_mapping.iterrows():
            for y, state in job_data.iterrows():
                if state_label['state_abbrev'].lower() == state['st'].lower():
                    if state_label['abbrev_needed'] == 1:
                        # var MAName = R.text(913,139, 'MA - #1').attr(labelBlack).toFront();
                        code += """ var """ + state_label['state_abbrev'].upper() + """Name = R.text(""" \
                                + str(int(state_label['x'])) + """, """ + str(int(state_label['y'])) + """, '""" \
                                + state_label['state_abbrev'].upper() + """ - #""" + str(state['rank']) + """').attr(labelBlack).toFront();"""
                    elif state['st'].lower() in('hi'):
                        # var NYName = R.text(913,139, '#1').attr(labelBlack).toFront();
                        code += """ var """ + state_label['state_abbrev'].upper() + """Name = R.text(""" \
                                + str(int(state_label['x'])) + """, """ + str(int(state_label['y'])) + """, '#"""\
                                + str(state['rank']) + """').attr(labelBlack).toFront();"""
                    else:
                        # var MAName = R.text(913,139, '#1').attr(labelWhite).toFront();
                        code += """ var """ + state_label['state_abbrev'].upper() + """Name = R.text(""" \
                                + str(int(state_label['x'])) + """, """ + str(int(state_label['y'])) + """, '#"""\
                                + str(state['rank']) + """').attr(labelBlack).toFront();"""
            code += "\n"

        color_slice = 10 - categories
        code += sequential_ending % (map_title,sequential_legend(colors[color_slice:],legend_description_left,legend_description_right))

        m.write(code)
        m.close()

        return html_path

form = cgi.FieldStorage()
title = form.getvalue('title')
legend_description_left = form.getvalue('left')
legend_description_right = form.getvalue('right')
categories = form.getvalue('categories')
map_csv = form['csv']

job_data = pd.read_csv(map_csv.file)
html_path = generate_static_heat_map(title,job_data,legend_description_left,legend_description_right,categories)

print("Location: " + html_path + "\n\n")
