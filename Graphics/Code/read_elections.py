import json
import os

# DataFolha
vec_dfolha_17_male = [0,0,0]
vec_dfolha_17_female = [0,0,0]
vec_dfolha_13_male = [0,0,0]
vec_dfolha_13_female = [0,0,0]

# IBOPE
vec_ibope_17_male = [0,0,0,0,0]
vec_ibope_17_female = [0,0,0,0,0]
vec_ibope_13_male = [0,0,0,0,0]
vec_ibope_13_female = [0,0,0,0,0]

def read_json():
    with open(os.getcwd() + '\Graphics\Data\PresidentialElection.json') as js:
        poolElection = json.load(js)

    for data in poolElection['elections_poll']:
        
        for candidate in data['candidates']:

            if(data['institute'] == 'DataFolha'):
                if(candidate['name'] == 'Jair Bolsonaro'):
                    vec_dfolha_17_male.append(candidate['gender']['male'])
                    vec_dfolha_17_female.append(candidate['gender']['female'])
                
                elif (candidate['name'] == 'Fernando Haddad'):
                    vec_dfolha_13_male.append(candidate['gender']['male'])
                    vec_dfolha_13_female.append(candidate['gender']['female'])                
            
            elif (data['institute'] == 'IBOPE'):
                if(candidate['name'] == 'Jair Bolsonaro'):
                    vec_ibope_17_male.append(candidate['gender']['male'])
                    vec_ibope_17_female.append(candidate['gender']['female'])

                elif(candidate['name'] == 'Fernando Haddad'):
                    vec_ibope_13_male.append(candidate['gender']['male'])
                    vec_ibope_13_female.append(candidate['gender']['female'])
            
            # (Resultado ou Boca de urna) Eleicao                
            elif (data['institute'] == 'Resultado'):                                                
                if(candidate['name'] == 'Bolsonaro'):                      
                    vec_dfolha_17_male.append(candidate['gender']['male'])
                    vec_dfolha_17_female.append(candidate['gender']['female'])
                    vec_ibope_17_male.append(candidate['gender']['male'])
                    vec_ibope_17_female.append(candidate['gender']['female'])

                elif (candidate['name'] == 'Haddad'):
                    vec_dfolha_13_male.append(candidate['gender']['male'])
                    vec_dfolha_13_female.append(candidate['gender']['female'])                    
                    vec_ibope_13_male.append(candidate['gender']['male'])
                    vec_ibope_13_female.append(candidate['gender']['female'])
                
                if(data["round"] == 1):
                    vec_ibope_17_male.append(vec_ibope_17_male[len(vec_ibope_17_male) - 1])
                    vec_ibope_17_female.append(vec_ibope_17_female[len(vec_ibope_17_female) - 1])
                    vec_ibope_13_male.append(vec_ibope_13_male[len(vec_ibope_13_male) - 1])
                    vec_ibope_13_female.append(vec_ibope_13_female[len(vec_ibope_13_female) - 1])