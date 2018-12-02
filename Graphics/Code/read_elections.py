import json
import os
import models

def read_json():
    with open(os.getcwd() + '\Graphics\Data\PresidentialElection.json') as js:
        poolElection = json.load(js)

    for data in poolElection['elections_poll']:
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
                if(data['institute'] == 'Resultado'):                        
                    if(data["round"] == 1 and (candidate['name'] == "Jair Bolsonaro" or candidate['name'] == "Fernando Haddad")):
                        models.data_reader.candidates[i].ibope_male.append(models.data_reader.candidates[i].ibope_male[-1])
                        models.data_reader.candidates[i].ibope_female.append(models.data_reader.candidates[i].ibope_female[-1])

                        models.data_reader.candidates[i].ibope_16a24.append( models.data_reader.candidates[i].ibope_16a24[-1])    
                        models.data_reader.candidates[i].ibope_25a34.append(models.data_reader.candidates[i].ibope_25a34[-1])    
                        models.data_reader.candidates[i].ibope_35a44.append(models.data_reader.candidates[i].ibope_35a44[-1])    
                        models.data_reader.candidates[i].ibope_45a54.append(models.data_reader.candidates[i].ibope_45a54[-1])
                        models.data_reader.candidates[i].ibope_55.append(models.data_reader.candidates[i].ibope_55[-1])

                        models.data_reader.candidates[i].ibope_norte_coeste.append(models.data_reader.candidates[i].ibope_norte_coeste[-1])  
                        models.data_reader.candidates[i].ibope_nordeste.append(models.data_reader.candidates[i].ibope_nordeste[-1])
                        models.data_reader.candidates[i].ibope_sudeste.append(models.data_reader.candidates[i].ibope_sudeste[-1]) 
                        models.data_reader.candidates[i].ibope_sul.append(models.data_reader.candidates[i].ibope_sul[-1])

                        models.data_reader.candidates[i].ibope_fundamental.append(models.data_reader.candidates[i].ibope_fundamental[-1])  
                        models.data_reader.candidates[i].ibope_medio.append(models.data_reader.candidates[i].ibope_medio[-1])
                        models.data_reader.candidates[i].ibope_superior.append(models.data_reader.candidates[i].ibope_superior[-1]) 

    models.complete_data_zero()