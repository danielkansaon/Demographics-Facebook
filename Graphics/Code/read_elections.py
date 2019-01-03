import json
import os
import models

dates_graph = ["2017-10-22", "2017-11-28", "2017-11-30", "2018-06-07", "2018-06-24", "2018-07-09", "2018-08-06", "2018-08-19", "2018-08-21", 
"2018-09-10", "2018-09-17", "2018-09-18", "2018-09-24", "2018-09-28", "2018-09-30", "2018-10-01", "2018-10-02", "2018-10-04", "2018-10-05",
"2018-10-06", "2018-10-07", "2018-10-08", "2018-10-10", "2018-10-14", "2018-10-15", "2018-10-18", "2018-10-22", "2018-10-23", "2018-10-25", 
"2018-10-26", "2018-10-27", "2018-10-28", "2018-10-29"]


def read_json(comLula):
    set_empty = True

    if(comLula == True):
        with open(os.getcwd() + '\Graphics\Data\PresidentialElection-ComLula.json') as js:
            poolElection = json.load(js)
    else:
        with open(os.getcwd() + '\Graphics\Data\PresidentialElection-SemLula.json') as js:
            poolElection = json.load(js)

    for date in dates_graph:
        vec_data = return_election_by_date(poolElection, date)    
        
        if(len(vec_data) == 0):
            for candidate in models.data_reader.candidates:
                set_value_empty(True, models.return_index(candidate.name))
                set_value_empty(False, models.return_index(candidate.name))                

        set_empty = True
        if(len(vec_data) > 1):
            set_empty = False

        for data in vec_data:
            for candidate in data['candidates']:

                i = models.return_index(candidate['name'])

                if(i >= 0):
                    if(data['institute'] == 'DataFolha' or data['institute'] == 'Resultado'):      
                        models.data_reader.candidates[i].dfolha_male.append(candidate['gender']['male'])
                        models.data_reader.candidates[i].dfolha_female.append(candidate['gender']['female'])
                        models.data_reader.candidates[i].dfolha_16a24.append(candidate['age_intervals']['age_16_24'])    
                        models.data_reader.candidates[i].dfolha_25a34.append(candidate['age_intervals']['age_25_34'])    
                        models.data_reader.candidates[i].dfolha_35a44.append(candidate['age_intervals']['age_35_44'])    
                        models.data_reader.candidates[i].dfolha_45a54.append(candidate['age_intervals']['age_45_54'])
                        models.data_reader.candidates[i].dfolha_55.append(candidate['age_intervals']['above_55'])   
                        models.data_reader.candidates[i].dfolha_norte_coeste.append(candidate['regions']['north_midwest'])  
                        models.data_reader.candidates[i].dfolha_nordeste.append(candidate['regions']['northeast'])
                        models.data_reader.candidates[i].dfolha_sudeste.append(candidate['regions']['southeast']) 
                        models.data_reader.candidates[i].dfolha_sul.append(candidate['regions']['south'])
                        models.data_reader.candidates[i].dfolha_fundamental.append(candidate['education_status']['elementary_school'])  
                        models.data_reader.candidates[i].dfolha_medio.append(candidate['education_status']['high_school'])
                        models.data_reader.candidates[i].dfolha_superior.append(candidate['education_status']['higher_education'])  
                    elif(set_empty): 
                        set_value_empty(True, i)                 
                            
                    if (data['institute'] == 'IBOPE' or data['institute'] == 'Resultado'): 
                        models.data_reader.candidates[i].ibope_male.append(candidate['gender']['male'])
                        models.data_reader.candidates[i].ibope_female.append(candidate['gender']['female'])
                        models.data_reader.candidates[i].ibope_16a24.append(candidate['age_intervals']['age_16_24'])    
                        models.data_reader.candidates[i].ibope_25a34.append(candidate['age_intervals']['age_25_34'])    
                        models.data_reader.candidates[i].ibope_35a44.append(candidate['age_intervals']['age_35_44'])    
                        models.data_reader.candidates[i].ibope_45a54.append(candidate['age_intervals']['age_45_54'])
                        models.data_reader.candidates[i].ibope_55.append(candidate['age_intervals']['above_55'])      
                        models.data_reader.candidates[i].ibope_norte_coeste.append(candidate['regions']['north_midwest'])  
                        models.data_reader.candidates[i].ibope_nordeste.append(candidate['regions']['northeast'])
                        models.data_reader.candidates[i].ibope_sudeste.append(candidate['regions']['southeast']) 
                        models.data_reader.candidates[i].ibope_sul.append(candidate['regions']['south'])
                        models.data_reader.candidates[i].ibope_fundamental.append(candidate['education_status']['elementary_school'])  
                        models.data_reader.candidates[i].ibope_medio.append(candidate['education_status']['high_school'])
                        models.data_reader.candidates[i].ibope_superior.append(candidate['education_status']['higher_education'])                    
                    elif(set_empty):
                        set_value_empty(False, i)                  
    
    update_value_empty()

def set_value_empty(datafolha, i):    
    if(datafolha):
        models.data_reader.candidates[i].dfolha_male.append(-1)
        models.data_reader.candidates[i].dfolha_female.append(-1)
        models.data_reader.candidates[i].dfolha_16a24.append(-1)    
        models.data_reader.candidates[i].dfolha_25a34.append(-1)    
        models.data_reader.candidates[i].dfolha_35a44.append(-1)    
        models.data_reader.candidates[i].dfolha_45a54.append(-1)
        models.data_reader.candidates[i].dfolha_55.append(-1)   
        models.data_reader.candidates[i].dfolha_norte_coeste.append(-1)  
        models.data_reader.candidates[i].dfolha_nordeste.append(-1)
        models.data_reader.candidates[i].dfolha_sudeste.append(-1) 
        models.data_reader.candidates[i].dfolha_sul.append(-1)
        models.data_reader.candidates[i].dfolha_fundamental.append(-1)  
        models.data_reader.candidates[i].dfolha_medio.append(-1)
        models.data_reader.candidates[i].dfolha_superior.append(-1)
    else:
        models.data_reader.candidates[i].ibope_male.append(-1)
        models.data_reader.candidates[i].ibope_female.append(-1)
        models.data_reader.candidates[i].ibope_16a24.append(-1)    
        models.data_reader.candidates[i].ibope_25a34.append(-1)    
        models.data_reader.candidates[i].ibope_35a44.append(-1)    
        models.data_reader.candidates[i].ibope_45a54.append(-1)
        models.data_reader.candidates[i].ibope_55.append(-1)      
        models.data_reader.candidates[i].ibope_norte_coeste.append(-1)  
        models.data_reader.candidates[i].ibope_nordeste.append(-1)
        models.data_reader.candidates[i].ibope_sudeste.append(-1) 
        models.data_reader.candidates[i].ibope_sul.append(-1)
        models.data_reader.candidates[i].ibope_fundamental.append(-1)  
        models.data_reader.candidates[i].ibope_medio.append(-1)
        models.data_reader.candidates[i].ibope_superior.append(-1) 

def update_value_empty():
    for candidate in models.data_reader.candidates:
        
        c = models.return_index(candidate.name)
        last_i_dfolha = 0
        last_i_ibope = 0

        for i in range(0, len(dates_graph)):

            #Verifica se o candidato foi para o segundo turno 
            if(i <= 21 or models.data_reader.candidates[c].round2 == True):            

                #DataFolha
                if(models.data_reader.candidates[c].dfolha_male[i] == -1):
                    models.data_reader.candidates[c].dfolha_male[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_male, last_i_dfolha, i)                    
                    models.data_reader.candidates[c].dfolha_female[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_female, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_16a24[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_16a24, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_25a34[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_25a34, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_35a44[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_35a44, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_45a54[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_45a54, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_55[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_55, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_norte_coeste[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_norte_coeste, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_nordeste[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_nordeste, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_sudeste[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_sudeste, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_sul[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_sul, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_fundamental[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_fundamental, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_medio[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_medio, last_i_dfolha, i)
                    models.data_reader.candidates[c].dfolha_superior[i] = return_new_value_graph(models.data_reader.candidates[c].dfolha_superior, last_i_dfolha, i)
                else:
                    last_i_dfolha = i

                #IBOPE
                if(models.data_reader.candidates[c].ibope_male[i] == -1):
                    models.data_reader.candidates[c].ibope_male[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_male, last_i_ibope, i)                    
                    models.data_reader.candidates[c].ibope_female[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_female, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_16a24[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_16a24, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_25a34[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_25a34, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_35a44[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_35a44, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_45a54[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_45a54, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_55[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_55, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_norte_coeste[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_norte_coeste, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_nordeste[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_nordeste, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_sudeste[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_sudeste, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_sul[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_sul, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_fundamental[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_fundamental, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_medio[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_medio, last_i_ibope, i)
                    models.data_reader.candidates[c].ibope_superior[i] = return_new_value_graph(models.data_reader.candidates[c].ibope_superior, last_i_ibope, i)
                else:
                    last_i_ibope = i

def return_new_value_graph(vec, last_i, i):    
    if(return_next_pos_poll(vec, i) == i):
        if(vec[i] == -1):
            return vec[last_i]
    else:        
        return (vec[last_i] + vec[return_next_pos_poll(vec, i)]) / 2

def return_next_pos_poll(vec, i_atual):
    for i in range(i_atual, len(vec)):     
        if(vec[i] >= 0):
            return i

    return i_atual

def return_election_by_date(json, date):
    result = []

    for data in json['elections_poll']:
        if (data['date'] == date):
            result.append(data)

    return result