import json
import os
import matplotlib.pyplot as plt
import numpy as np


with open(os.getcwd() + '\Graphics\Data\PresidentialElection.json') as js:
    data = json.load(js)

xticks_DataFolha = []
xticks_Ibope = []

#DataFolha
axisY_DFolha_17_male = []
axisY_DFolha_17_female = []
axisY_DFolha_13_male = []
axisY_DFolha_13_female = []

#Ibope
axisY_Ibope_17_female = []
axisY_Ibope_17_male = []
axisY_Ibope_13_female = []
axisY_Ibope_13_male = []


for d in data['elections_poll']:

    if(d['round'] == 2):
        
        if(d['institute'] == 'DataFolha'):
            xticks_DataFolha.append(d['date'])
        else:
            xticks_Ibope.append(d['date'])
        

        for c in d['candidates']:                        
            if(d['institute'] == 'DataFolha'):
                if(c['name'] == 'Jair Bolsonaro'):
                    axisY_DFolha_17_male.append(c['gender']['male'])
                    axisY_DFolha_17_female.append(c['gender']['female'])
                elif (c['name'] == 'Fernando Haddad'):
                    axisY_DFolha_13_male.append(c['gender']['male'])
                    axisY_DFolha_13_female.append(c['gender']['female'])
            else:
                if(c['name'] == 'Jair Bolsonaro'):
                    axisY_Ibope_17_male.append(c['gender']['male'])
                    axisY_Ibope_17_female.append(c['gender']['female'])
                elif(c['name'] == 'Fernando Haddad'):
                    axisY_Ibope_13_male.append(c['gender']['male'])
                    axisY_Ibope_13_female.append(c['gender']['female'])


# f, ax = plt.subplots(1)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(range(0, len(axisY_DFolha_17_male)), axisY_DFolha_17_male, 'go', ls='-', label='Bolsonaro (Masculino)')
ax.plot(range(0,len(axisY_DFolha_17_female)), axisY_DFolha_17_female, 'g--', label='Bolsonaro (Feminino)')

ax.plot(range(0, len(axisY_DFolha_13_male)), axisY_DFolha_13_male, 'ro', ls='-', label='Haddad (Masculino)')
ax.plot(range(0,len(axisY_DFolha_13_female)), axisY_DFolha_13_female, 'r--', label='Haddad (Feminino)')

# plt.plot(range(0, len(axisY_DFolha_17_male)), axisY_DFolha_17_male, label='Masculino')
# plt.plot(range(0,len(axisY_DFolha_17_female)), axisY_DFolha_17_female, 'k', label='Feminino')

plt.xticks(range(0, len(axisY_DFolha_17_male)), xticks_DataFolha)
plt.title('DataFolha 2º Turno')
ax.set_ylim(ymin=0)
plt.grid(True)
plt.legend()
plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)

# # Major ticks every 20, minor ticks every 5
# major_ticks = np.arange(0, 101, 20)
# minor_ticks = np.arange(0, 101, 5)

# ax.set_xticks(major_ticks)
# ax.set_xticks(minor_ticks, minor=True)
# ax.set_yticks(major_ticks)
# ax.set_yticks(minor_ticks, minor=True)

# ax.plot(range(0, len(axisY_DFolha_17_male)), axisY_DFolha_17_male)

# # And a corresponding grid
# ax.grid(which='both')

# # Or if you want different settings for the grids:
# ax.grid(which='minor', alpha=0.2)
# ax.grid(which='major', alpha=0.5)

# plt.show()