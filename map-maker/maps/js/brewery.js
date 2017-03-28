var USdata = {
'AL' :'#33',
'AK' :'#1',
'AZ' :'#33',
'AR' :'#6',
'CA' :'#3',
'CO' :'#9',
'CT' :'#12',
'DE' :'#26',
'FL' :'#2',
'GA' :'#30',
'HI' :'#45',
'ID' :'#43',
'IL' :'#35',
'IN' :'#27',
'IA' :'#29',
'KS' :'#41',
'KY' :'#30',
'LA' :'#20',
'ME' :'#14',
'MD' :'#35',
'MA' :'#13',
'MI' :'#22',
'MN' :'#24',
'MS' :'#16',
'MO' :'#22',
'MT' :'#5',
'NE' :'#37',
'NV' :'#44',
'NH' :'#7',
'NJ' :'#16',
'NM' :'#30',
'NY' :'#15',
'NC' :'#20',
'ND' :'#46',
'OH' :'#19',
'OK' :'#49',
'OR' :'#28',
'PA' :'#24',
'RI' :'#40',
'SC' :'#8',
'SD' :'#37',
'TN' :'#42',
'TX' :'#9',
'UT' :'#48',
'VT' :'#9',
'VA' :'#16',
'WA' :'#37',
'WV' :'#50',
'WI' :'#4',
'WY' :'#47'
};

var living_wage = new Datamap({
  scope: 'usa',
  element: document.getElementById('heatmap'),
  responsive: true,
  geographyConfig: {
    highlightBorderColor: '#bada55',
   popupTemplate: function(geography, data) {
      return '<div class="hoverinfo" style="text-align:center;">' + geography.properties.name + '</br>Rank: ' +  data.rank + '</br>Map: ' +  data.average_salary + ' '
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
'AL' : {'fillKey' : 'Bottom40', 'rank' : '33', 'average_salary' : '4.39'},
'AK' : {'fillKey' : 'Bottom100', 'rank' : '1', 'average_salary' : '4.87'},
'AZ' : {'fillKey' : 'Bottom40', 'rank' : '33', 'average_salary' : '4.39'},
'AR' : {'fillKey' : 'Bottom100', 'rank' : '6', 'average_salary' : '4.74'},
'CA' : {'fillKey' : 'Bottom100', 'rank' : '3', 'average_salary' : '4.83'},
'CO' : {'fillKey' : 'Bottom100', 'rank' : '9', 'average_salary' : '4.61'},
'CT' : {'fillKey' : 'Bottom80', 'rank' : '12', 'average_salary' : '4.6'},
'DE' : {'fillKey' : 'Bottom60', 'rank' : '26', 'average_salary' : '4.48'},
'FL' : {'fillKey' : 'Bottom100', 'rank' : '2', 'average_salary' : '4.85'},
'GA' : {'fillKey' : 'Bottom60', 'rank' : '30', 'average_salary' : '4.41'},
'HI' : {'fillKey' : 'Bottom20', 'rank' : '45', 'average_salary' : '4.17'},
'ID' : {'fillKey' : 'Bottom20', 'rank' : '43', 'average_salary' : '4.2'},
'IL' : {'fillKey' : 'Bottom40', 'rank' : '35', 'average_salary' : '4.37'},
'IN' : {'fillKey' : 'Bottom60', 'rank' : '27', 'average_salary' : '4.47'},
'IA' : {'fillKey' : 'Bottom60', 'rank' : '29', 'average_salary' : '4.42'},
'KS' : {'fillKey' : 'Bottom20', 'rank' : '41', 'average_salary' : '4.26'},
'KY' : {'fillKey' : 'Bottom60', 'rank' : '30', 'average_salary' : '4.41'},
'LA' : {'fillKey' : 'Bottom80', 'rank' : '20', 'average_salary' : '4.52'},
'ME' : {'fillKey' : 'Bottom80', 'rank' : '14', 'average_salary' : '4.56'},
'MD' : {'fillKey' : 'Bottom40', 'rank' : '35', 'average_salary' : '4.37'},
'MA' : {'fillKey' : 'Bottom80', 'rank' : '13', 'average_salary' : '4.59'},
'MI' : {'fillKey' : 'Bottom60', 'rank' : '22', 'average_salary' : '4.51'},
'MN' : {'fillKey' : 'Bottom60', 'rank' : '24', 'average_salary' : '4.5'},
'MS' : {'fillKey' : 'Bottom80', 'rank' : '16', 'average_salary' : '4.54'},
'MO' : {'fillKey' : 'Bottom60', 'rank' : '22', 'average_salary' : '4.51'},
'MT' : {'fillKey' : 'Bottom100', 'rank' : '5', 'average_salary' : '4.75'},
'NE' : {'fillKey' : 'Bottom40', 'rank' : '37', 'average_salary' : '4.32'},
'NV' : {'fillKey' : 'Bottom20', 'rank' : '44', 'average_salary' : '4.18'},
'NH' : {'fillKey' : 'Bottom100', 'rank' : '7', 'average_salary' : '4.67'},
'NJ' : {'fillKey' : 'Bottom80', 'rank' : '16', 'average_salary' : '4.54'},
'NM' : {'fillKey' : 'Bottom60', 'rank' : '30', 'average_salary' : '4.41'},
'NY' : {'fillKey' : 'Bottom80', 'rank' : '15', 'average_salary' : '4.55'},
'NC' : {'fillKey' : 'Bottom80', 'rank' : '20', 'average_salary' : '4.52'},
'ND' : {'fillKey' : 'Bottom20', 'rank' : '46', 'average_salary' : '4.08'},
'OH' : {'fillKey' : 'Bottom80', 'rank' : '19', 'average_salary' : '4.53'},
'OK' : {'fillKey' : 'Bottom20', 'rank' : '49', 'average_salary' : '3.96'},
'OR' : {'fillKey' : 'Bottom60', 'rank' : '28', 'average_salary' : '4.44'},
'PA' : {'fillKey' : 'Bottom60', 'rank' : '24', 'average_salary' : '4.5'},
'RI' : {'fillKey' : 'Bottom40', 'rank' : '40', 'average_salary' : '4.3'},
'SC' : {'fillKey' : 'Bottom100', 'rank' : '8', 'average_salary' : '4.62'},
'SD' : {'fillKey' : 'Bottom40', 'rank' : '37', 'average_salary' : '4.32'},
'TN' : {'fillKey' : 'Bottom20', 'rank' : '42', 'average_salary' : '4.25'},
'TX' : {'fillKey' : 'Bottom100', 'rank' : '9', 'average_salary' : '4.61'},
'UT' : {'fillKey' : 'Bottom20', 'rank' : '48', 'average_salary' : '4.04'},
'VT' : {'fillKey' : 'Bottom100', 'rank' : '9', 'average_salary' : '4.61'},
'VA' : {'fillKey' : 'Bottom80', 'rank' : '16', 'average_salary' : '4.54'},
'WA' : {'fillKey' : 'Bottom40', 'rank' : '37', 'average_salary' : '4.32'},
'WV' : {'fillKey' : 'Bottom20', 'rank' : '50', 'average_salary' : '3.95'},
'WI' : {'fillKey' : 'Bottom100', 'rank' : '4', 'average_salary' : '4.78'},
'WY' : {'fillKey' : 'Bottom20', 'rank' : '47', 'average_salary' : '4.05'}

}
});

if(window.innerWidth>800){
    living_wage.labels({'customLabelText': USdata, fontSize: 14, transform: 'translate(1000,0)'});
    living_wage.legend({
        legendTitle : 'Brewery',
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
