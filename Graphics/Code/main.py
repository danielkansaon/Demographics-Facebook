import json
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


facebook_17_male =[]
facebook_17_female =[]
facebook_13_male =[]
facebook_13_female =[]
facebook_data =[]

def readPresidenciaveis():
    input_file = open(os.getcwd() + '\Graphics\Data\\audiencia_presidenciaveis.json')
    collected_dates = ["17_11_28",  "18_07_09",  "18_08_06",  "18_09_10",  "18_09_17",  "18_09_24",  "18_10_01",  "18_10_05",  "18_10_08",  "18_10_15",  "18_10_22",  "18_10_26",  "18_10_29"]
    collected_dates_segundo_turno = ["18_10_08",  "18_10_15",  "18_10_22",  "18_10_26",  "18_10_29"]
    presids_dict = {
        3:"Fernando Haddad",
        4:"Luiz Inácio Lula da Silva",
        7:"Geraldo Alckmin",
        10:"Marina Silva",
        12:"Alvaro Dias",
        110:"Ciro Gomes",
        16:"Jair Bolsonaro",
    }
    
    for line in input_file:
        json_line = json.loads(line.strip())

        for j in json_line:
            presid_key = j 
            
        if(presid_key == '16'):        
            for collected_date in collected_dates_segundo_turno:             
                facebook_17_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male'] * 100)
                facebook_17_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female'] * 100)
                facebook_data.append(collected_date) 
        elif(presid_key == '3'):        
            for collected_date in collected_dates_segundo_turno:             
                facebook_13_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male']* 100)
                facebook_13_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female']* 100)
                facebook_data.append(collected_date) 


with open(os.getcwd() + '\Graphics\Data\PresidentialElection.json') as js:
    data = json.load(js)



xticks_DataFolha = []
xticks_Ibope = ["10-10"]

# DataFolha
axisY_DFolha_17_male = []
axisY_DFolha_17_female = []
axisY_DFolha_13_male = []
axisY_DFolha_13_female = []

# Ibope
axisY_Ibope_17_female = [0]
axisY_Ibope_17_male = [0]
axisY_Ibope_13_female = [0]
axisY_Ibope_13_male = [0]


for d in data['elections_poll']:

    if(d['round'] == 2):

        if(d['institute'] == 'DataFolha'):
            xticks_DataFolha.append(d['date'][-5:])
        elif(d['institute'] == 'IBOPE'):
            xticks_Ibope.append(d['date'][-5:])
        elif(d['institute'] == 'Resultado'):
            xticks_Ibope.append(d['date'][-5:])
            xticks_DataFolha.append(d['date'][-5:])

        for c in d['candidates']:
            if(d['institute'] == 'DataFolha'):
                if(c['name'] == 'Jair Bolsonaro'):
                    axisY_DFolha_17_male.append(c['gender']['male'])
                    axisY_DFolha_17_female.append(c['gender']['female'])
                elif (c['name'] == 'Fernando Haddad'):
                    axisY_DFolha_13_male.append(c['gender']['male'])
                    axisY_DFolha_13_female.append(c['gender']['female'])                
            elif (d['institute'] == 'IBOPE'):
                if(c['name'] == 'Jair Bolsonaro'):
                    axisY_Ibope_17_male.append(c['gender']['male'])
                    axisY_Ibope_17_female.append(c['gender']['female'])
                elif(c['name'] == 'Fernando Haddad'):
                    axisY_Ibope_13_male.append(c['gender']['male'])
                    axisY_Ibope_13_female.append(c['gender']['female'])

            elif (d['institute'] == 'Resultado'):
                if(c['name'] == 'Bolsonaro'):                      
                    axisY_DFolha_17_male.append(c['gender']['male'])
                    axisY_DFolha_17_female.append(c['gender']['female'])
                    axisY_Ibope_17_male.append(c['gender']['male'])
                    axisY_Ibope_17_female.append(c['gender']['female'])
                elif (c['name'] == 'Haddad'):
                    axisY_DFolha_13_male.append(c['gender']['male'])
                    axisY_DFolha_13_female.append(c['gender']['female'])                    
                    axisY_Ibope_13_male.append(c['gender']['male'])
                    axisY_Ibope_13_female.append(c['gender']['female'])

readPresidenciaveis()

df = pd.DataFrame(
    {
        'x': range(0, len(axisY_DFolha_17_male)), 
        '17_male_dtfolha': axisY_DFolha_17_male, '17_female_dtfolha': axisY_DFolha_17_female,
        '17_male_ibope': axisY_Ibope_17_male, '17_female_ibope': axisY_Ibope_17_female,
        '13_male_dtfolha': axisY_DFolha_13_male, '13_female_dtfolha': axisY_DFolha_13_female,
        '13_male_ibope': axisY_Ibope_13_male, '13_female_ibope': axisY_Ibope_13_female,
        '17_male_facebook': facebook_17_male, '17_female_facebook': facebook_17_female,
        '13_male_facebook': facebook_13_male, '13_female_facebook': facebook_13_female,

    })

# 2 partes
# G1 = plt.subplot(221)
# plt.title('Jair Bolsonaro', fontsize=12, color='gray', loc='center')
# plt.plot('x', '17_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.5, label='DataFolha')
# plt.plot('x', '17_male_ibope', data=df, marker='o', color="green", linestyle='dashed', alpha=0.4, label='IBOPE')
# plt.plot('x', '17_female_dtfolha', data=df, marker='o', color="red", ls='-', alpha=0.4)
# plt.plot('x', '17_female_ibope', data=df, marker='o', color="red", linestyle='dashed', alpha=0.4)
# plt.plot('x', '17_male_facebook', data=df, marker='o', color="blue", alpha=0.4)
# plt.plot('x', '17_female_facebook', data=df, marker='o', color="blue", linestyle='dashed', alpha=0.4)
# plt.xticks(range(0, len(axisY_DFolha_17_male)), xticks_DataFolha)
# G1.set_ylim(35,65)

# G2 = plt.subplot(222)
# plt.title('Fernando Haddad', fontsize=12, color='gray', loc='center')
# plt.plot('x', '13_male_dtfolha', data=df, marker='o', color="green", alpha=0.5, label='DataFolha - Male')
# plt.plot('x', '13_male_ibope', data=df, marker='o', color="green", linestyle='dashed', alpha=0.4, label='IBOPE - Male')
# plt.plot('x', '13_female_dtfolha', data=df, marker='o', color="red", alpha=0.4, label='DataFolha - Female')
# plt.plot('x', '13_female_ibope', data=df, marker='o', color="red", linestyle='dashed', alpha=0.4, label='IBOPE - Female')
# plt.plot('x', '13_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook - Male')
# plt.plot('x', '13_female_facebook', data=df, marker='o', color="blue", linestyle='dashed', alpha=0.4, label='Facebook - Female')
# plt.xticks(range(0, len(axisY_DFolha_17_male)), xticks_DataFolha)
# G2.set_ylim(35,65)

# plt.legend(loc='upper center', bbox_to_anchor=(-0.1, -0.2),  shadow=True, ncol=2)
# plt.suptitle('Gender')
# plt.show()


# 4 partes

# G1 = plt.subplot(221)
# plt.title('Male', fontsize=12, color='gray', loc='center')
# plt.plot('x', '17_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
# plt.plot('x', '17_male_ibope', data=df, marker='o', color="red", linestyle='dashed', alpha=0.4, label='IBOPE')
# plt.plot('x', '17_male_facebook', data=df, marker='o', color="blue", alpha=0.4)
# plt.xticks(range(0, len(axisY_DFolha_17_male)), xticks_DataFolha)
# G1.set_ylim(35,65)

# G2 = plt.subplot(222)
# plt.title('Female', fontsize=12, color='gray', loc='center')
# plt.plot('x', '17_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
# plt.plot('x', '17_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
# plt.plot('x', '17_female_facebook', data=df, marker='o', color="blue", alpha=0.4)
# plt.xticks(range(0, len(axisY_DFolha_17_male)), xticks_Ibope)
# G2.set_ylim(35,65)

# G3 = plt.subplot(223)
# plt.plot('x', '13_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
# plt.plot('x', '13_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
# plt.plot('x', '13_male_facebook', data=df, marker='o', color="blue", alpha=0.4)
# plt.xticks(range(0, len(axisY_DFolha_17_male)), xticks_DataFolha)
# G3.set_ylim(35,65)

# G4 = plt.subplot(224)
# plt.plot('x', '13_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
# plt.plot('x', '13_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
# plt.plot('x', '13_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
# plt.xticks(range(0, len(axisY_DFolha_17_male)), xticks_Ibope)
# G4.set_ylim(35,65)
# plt.legend()

# plt.text(1, 2, 'Time', ha='center', va='center')
# plt.text(0.06, 0.5, 'Note', ha='center', va='center', rotation='vertical')

# plt.suptitle('Gender')
# plt.show()