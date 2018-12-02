import json
import os
import models

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

def return_index(name):
    if(name == 'Jair Bolsonaro'):
        return 0
    elif(name == 'Fernando Haddad'):
        return 1
    elif(name == 'Ciro Gomes'):
        return 2
    elif(name == 'Lula'):
        return 3
    return -1

def read_json():
    with open(os.getcwd() + '\Graphics\Data\PresidentialElection.json') as js:
        poolElection = json.load(js)

    for data in poolElection['elections_poll']:
        for candidate in data['candidates']:

            i = return_index(candidate['name'])

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

    for c in models.data_reader.candidates:
        while len(c.ibope_male) < 15:
            c.ibope_male.append(0)
            c.dfolha_male.append(0)
            c.ibope_female.append(0)
            c.dfolha_female.append(0)       

            c.dfolha_16a24.append(0)
            c.dfolha_25a34.append(0)
            c.dfolha_35a44.append(0)
            c.dfolha_45a54.append(0)
            c.dfolha_55.append(0)

            c.ibope_16a24.append(0)
            c.ibope_25a34.append(0)
            c.ibope_35a44.append(0)
            c.ibope_45a54.append(0)
            c.ibope_55.append(0)

            models.data_reader.candidates[i].ibope_16a24.append(0)
            models.data_reader.candidates[i].ibope_25a34.append(0)
            models.data_reader.candidates[i].ibope_35a44.append(0)
            models.data_reader.candidates[i].ibope_45a54.append(0)
            models.data_reader.candidates[i].ibope_55.append(0)

            models.data_reader.candidates[i].dfolha_16a24.append(0)
            models.data_reader.candidates[i].dfolha_25a34.append(0)
            models.data_reader.candidates[i].dfolha_35a44.append(0)
            models.data_reader.candidates[i].dfolha_45a54.append(0)
            models.data_reader.candidates[i].dfolha_55.append(0)

            models.data_reader.candidates[i].dfolha_norte_coeste.append(0)  
            models.data_reader.candidates[i].dfolha_nordeste.append(0) 
            models.data_reader.candidates[i].dfolha_sudeste.append(0) 
            models.data_reader.candidates[i].dfolha_sul.append(0) 

            models.data_reader.candidates[i].ibope_norte_coeste.append(0) 
            models.data_reader.candidates[i].ibope_nordeste.append(0)
            models.data_reader.candidates[i].ibope_sudeste.append(0) 
            models.data_reader.candidates[i].ibope_sul.append(0)

            models.data_reader.candidates[i].ibope_fundamental.append(0)  
            models.data_reader.candidates[i].ibope_medio.append(0)
            models.data_reader.candidates[i].ibope_superior.append(0) 

            models.data_reader.candidates[i].dfolha_fundamental.append(models.data_reader.candidates[i].dfolha_fundamental)  
            models.data_reader.candidates[i].dfolha_medio.append(models.data_reader.candidates[i].dfolha_medio)
            models.data_reader.candidates[i].dfolha_superior.append(models.data_reader.candidates[i].dfolha_superior) 
            
    a = 0
    # for data in poolElection['elections_poll']:
        
    #     for candidate in data['candidates']:

    #         i = return_index(candidate['name'])

    #         if(data['institute'] == 'DataFolha'):
    #             if(candidate['name'] == 'Jair Bolsonaro'):
    #                 vec_dfolha_17_male.append(candidate['gender']['male'])
    #                 vec_dfolha_17_female.append(candidate['gender']['female'])
                
    #             elif (candidate['name'] == 'Fernando Haddad'):
    #                 vec_dfolha_13_male.append(candidate['gender']['male'])
    #                 vec_dfolha_13_female.append(candidate['gender']['female'])     

    #             elif(candidate['name'] == 'Lula'):
    #                 vec_dfolha_lula_male.append(candidate['gender']['male'])
    #                 vec_dfolha_lula_female.append(candidate['gender']['female'])    

    #             elif(candidate['name'] == 'Ciro Gomes'):
    #                 vec_dfolha_ciro_male.append(candidate['gender']['male'])
    #                 vec_dfolha_ciro_female.append(candidate['gender']['female'])       
            
    #         elif (data['institute'] == 'IBOPE'):
    #             if(candidate['name'] == 'Jair Bolsonaro'):
    #                 vec_ibope_17_male.append(candidate['gender']['male'])
    #                 vec_ibope_17_female.append(candidate['gender']['female'])

    #             elif(candidate['name'] == 'Fernando Haddad'):
    #                 vec_ibope_13_male.append(candidate['gender']['male'])
    #                 vec_ibope_13_female.append(candidate['gender']['female'])

    #             elif(candidate['name'] == 'Lula'):
    #                 vec_ibope_lula_male.append(candidate['gender']['male'])
    #                 vec_ibope_lula_female.append(candidate['gender']['female'])

    #             elif(candidate['name'] == 'Ciro Gomes'):
    #                 vec_ibope_ciro_male.append(candidate['gender']['male'])
    #                 vec_ibope_ciro_female.append(candidate['gender']['female'])
            
    #         # (Resultado ou Boca de urna) Eleicao                
    #         elif (data['institute'] == 'Resultado'):                                                
    #             if(candidate['name'] == 'Jair Bolsonaro'):                      
    #                 vec_dfolha_17_male.append(candidate['gender']['male'])
    #                 vec_dfolha_17_female.append(candidate['gender']['female'])
    #                 vec_ibope_17_male.append(candidate['gender']['male'])
    #                 vec_ibope_17_female.append(candidate['gender']['female'])
                    
    #                 if(data["round"] == 1):
    #                     vec_ibope_17_male.append(vec_ibope_17_male[len(vec_ibope_17_male) - 1])
    #                     vec_ibope_17_female.append(vec_ibope_17_female[len(vec_ibope_17_female) - 1])

    #             elif (candidate['name'] == 'Fernando Haddad'):
    #                 vec_dfolha_13_male.append(candidate['gender']['male'])
    #                 vec_dfolha_13_female.append(candidate['gender']['female'])                    
    #                 vec_ibope_13_male.append(candidate['gender']['male'])
    #                 vec_ibope_13_female.append(candidate['gender']['female'])

    #                 if(data["round"] == 1):
    #                     vec_ibope_13_male.append(vec_ibope_13_male[len(vec_ibope_13_male) - 1])
    #                     vec_ibope_13_female.append(vec_ibope_13_female[len(vec_ibope_13_female) - 1])
                
    #             elif (candidate['name'] == 'Ciro Gomes'):
    #                 vec_dfolha_ciro_male.append(candidate['gender']['male'])
    #                 vec_dfolha_ciro_female.append(candidate['gender']['female'])                    
    #                 vec_ibope_ciro_male.append(candidate['gender']['male'])
    #                 vec_ibope_ciro_female.append(candidate['gender']['female'])
    
    # #Completando outros pontos
    # while len(vec_ibope_lula_male) < len(vec_ibope_17_male):
    #     #Lula
    #     vec_ibope_lula_male.append(0)
    #     vec_ibope_lula_female.append(0)
    #     vec_dfolha_lula_male.append(0)
    #     vec_dfolha_lula_female.append(0)

    # while len(vec_dfolha_ciro_male) < len(vec_ibope_17_male):
    #     #Ciro Gomes
    #     vec_dfolha_ciro_male.append(0)
    #     vec_dfolha_ciro_female.append(0)                    
    #     vec_ibope_ciro_male.append(0)
    #     vec_ibope_ciro_female.append(0)
       
        

