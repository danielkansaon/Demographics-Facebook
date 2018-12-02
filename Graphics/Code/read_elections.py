import json
import os

# DataFolha
vec_dfolha_17_male = []
vec_dfolha_17_female = []
vec_dfolha_13_male = []
vec_dfolha_13_female = []
vec_dfolha_lula_male = []
vec_dfolha_lula_female = []
vec_dfolha_ciro_male = []
vec_dfolha_ciro_female = []

# IBOPE
vec_ibope_17_male = []
vec_ibope_17_female = []
vec_ibope_13_male = []
vec_ibope_13_female = []
vec_ibope_lula_male = []
vec_ibope_lula_female = []
vec_ibope_ciro_male = []
vec_ibope_ciro_female = []


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

                elif(candidate['name'] == 'Lula'):
                    vec_dfolha_lula_male.append(candidate['gender']['male'])
                    vec_dfolha_lula_female.append(candidate['gender']['female'])    

                elif(candidate['name'] == 'Ciro Gomes'):
                    vec_dfolha_ciro_male.append(candidate['gender']['male'])
                    vec_dfolha_ciro_female.append(candidate['gender']['female'])       
            
            elif (data['institute'] == 'IBOPE'):
                if(candidate['name'] == 'Jair Bolsonaro'):
                    vec_ibope_17_male.append(candidate['gender']['male'])
                    vec_ibope_17_female.append(candidate['gender']['female'])

                elif(candidate['name'] == 'Fernando Haddad'):
                    vec_ibope_13_male.append(candidate['gender']['male'])
                    vec_ibope_13_female.append(candidate['gender']['female'])

                elif(candidate['name'] == 'Lula'):
                    vec_ibope_lula_male.append(candidate['gender']['male'])
                    vec_ibope_lula_female.append(candidate['gender']['female'])

                elif(candidate['name'] == 'Ciro Gomes'):
                    vec_ibope_ciro_male.append(candidate['gender']['male'])
                    vec_ibope_ciro_female.append(candidate['gender']['female'])
            
            # (Resultado ou Boca de urna) Eleicao                
            elif (data['institute'] == 'Resultado'):                                                
                if(candidate['name'] == 'Jair Bolsonaro'):                      
                    vec_dfolha_17_male.append(candidate['gender']['male'])
                    vec_dfolha_17_female.append(candidate['gender']['female'])
                    vec_ibope_17_male.append(candidate['gender']['male'])
                    vec_ibope_17_female.append(candidate['gender']['female'])
                    
                    if(data["round"] == 1):
                        vec_ibope_17_male.append(vec_ibope_17_male[len(vec_ibope_17_male) - 1])
                        vec_ibope_17_female.append(vec_ibope_17_female[len(vec_ibope_17_female) - 1])

                elif (candidate['name'] == 'Fernando Haddad'):
                    vec_dfolha_13_male.append(candidate['gender']['male'])
                    vec_dfolha_13_female.append(candidate['gender']['female'])                    
                    vec_ibope_13_male.append(candidate['gender']['male'])
                    vec_ibope_13_female.append(candidate['gender']['female'])

                    if(data["round"] == 1):
                        vec_ibope_13_male.append(vec_ibope_13_male[len(vec_ibope_13_male) - 1])
                        vec_ibope_13_female.append(vec_ibope_13_female[len(vec_ibope_13_female) - 1])
                
                elif (candidate['name'] == 'Ciro Gomes'):
                    vec_dfolha_ciro_male.append(candidate['gender']['male'])
                    vec_dfolha_ciro_female.append(candidate['gender']['female'])                    
                    vec_ibope_ciro_male.append(candidate['gender']['male'])
                    vec_ibope_ciro_female.append(candidate['gender']['female'])
    
    #Completando outros pontos
    while len(vec_ibope_lula_male) < len(vec_ibope_17_male):
        #Lula
        vec_ibope_lula_male.append(0)
        vec_ibope_lula_female.append(0)
        vec_dfolha_lula_male.append(0)
        vec_dfolha_lula_female.append(0)

    while len(vec_dfolha_ciro_male) < len(vec_ibope_17_male):
        #Ciro Gomes
        vec_dfolha_ciro_male.append(0)
        vec_dfolha_ciro_female.append(0)                    
        vec_ibope_ciro_male.append(0)
        vec_ibope_ciro_female.append(0)
       
        
