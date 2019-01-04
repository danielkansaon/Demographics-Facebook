import json
import os
import models

age_intervals = {     
    'adolescent' :{'age_min': 13, 'age_max': 17},
    'young_1' :{'age_min': 18, 'age_max': 24},
    'young_2' :{'age_min': 25, 'age_max': 34},
    'mid_aged_1' :{'age_min': 35, 'age_max': 44},
    'mid_aged_2' :{'age_min': 45, 'age_max': 54},        
    'old_1': {'age_min': 55, 'age_max': 64},
    'old_2': {'age_min': 65}                              
}    

education_dic = {
    'UNDERGRAD' : 'college',
    'ALUM': 'college',
    'SOME_COLLEGE': 'college',
    'ASSOCIATE_DEGREE': 'college',
    'high_school': 'high_school',
    'HIGH_SCHOOL_GRAD': 'high_school',
    'SOME_HIGH_SCHOOL': 'high_school',
    'IN_GRAD_SCHOOL': 'grad_school',
    'SOME_GRAD_SCHOOL': 'grad_school',
    'MASTER_DEGREE': 'grad_school',
    'PROFESSIONAL_DEGREE': 'grad_school',
    'DOCTORATE_DEGREE': 'grad_school'              
}

education_status = ['UNDERGRAD','ALUM','SOME_COLLEGE','ASSOCIATE_DEGREE', 'high_school','HIGH_SCHOOL_GRAD','SOME_HIGH_SCHOOL', 
'IN_GRAD_SCHOOL','SOME_GRAD_SCHOOL','MASTER_DEGREE','PROFESSIONAL_DEGREE','DOCTORATE_DEGREE']

regions = ["northeast", "south", "southeast", "midwest", "north"]

collected_dates = ["17_11_28",  "18_07_09",  "18_08_06",  "18_09_10",  "18_09_17",  "18_09_24",  "18_10_01",  "18_10_05",  "18_10_08",  "18_10_15",  "18_10_22",  "18_10_26", "18_10_29"]

dates_graph = ["2017-10-22", "17_11_28", "2017-11-30", "2018-06-07", "2018-06-24", "18_07_09", "18_08_06", "2018-08-19", "2018-08-21", 
"18_09_10", "18_09_17", "2018-09-18", "18_09_24", "2018-09-28", "2018-09-30", "18_10_01", "2018-10-02", "2018-10-04", "18_10_05",
"18_10_06", "2018-10-07", "18_10_08", "2018-10-10", "2018-10-14", "18_10_15", "2018-10-18", "18_10_22", "2018-10-23", "2018-10-25", 
"18_10_26", "18_10_27", "2018-10-28", "18_10_29"]

presids_dict = {
        3:"Fernando Haddad",
        4:"Luiz Inácio Lula da Silva",
        7:"Geraldo Alckmin",
        10:"Marina Silva",
        12:"Alvaro Dias",
        110:"Ciro Gomes",
        16:"Jair Bolsonaro",
}
    
def return_index(presid_key):
    if(presid_key == '16'):
        return 0
    elif(presid_key == '3'):
        return 1
    elif(presid_key == '110'):
        return 2
    elif(presid_key == '4'):
        return 3
    elif(presid_key == '10'):
        return 4
    elif(presid_key == '7'):
        return 5
    elif(presid_key == '12'):
        return 6
    return -1

def readJson():
    input_file = open(os.getcwd() + '\Graphics\Data\\audiencia_presidenciaveis.json')
    load_census()
               
    for line in input_file:
        json_line = json.loads(line.strip())
        adicionarIdoso = True

        for j in json_line:
            presid_key = j           
        
        i = return_index(presid_key)

        if(i >= 0):  
            for collected_date in dates_graph:   

                AdicionarFundamental = True
                AdicionarMedio = True
                AdicionarSuperior = True

                if(json_line[presid_key].get(collected_date, '') == ''):                     
                    models.data_reader.candidates[i].facebook_male.append(-1)
                    models.data_reader.candidates[i].facebook_female.append(-1)
                    models.data_reader.candidates[i].facebook_16a24.append(-1)
                    models.data_reader.candidates[i].facebook_25a34.append(-1)
                    models.data_reader.candidates[i].facebook_35a44.append(-1)
                    models.data_reader.candidates[i].facebook_45a54.append(-1)
                    models.data_reader.candidates[i].facebook_55.append(-1)
                    models.data_reader.candidates[i].facebook_nordeste.append(-1)
                    models.data_reader.candidates[i].facebook_sul.append(-1)
                    models.data_reader.candidates[i].facebook_sudeste.append(-1)
                    models.data_reader.candidates[i].facebook_norte_coeste.append(-1)
                    models.data_reader.candidates[i].facebook_likes.append(-1)
                    models.data_reader.candidates[i].facebook_talking_about.append(-1)
                    models.data_reader.candidates[i].facebook_fundamental.append(-1)
                    models.data_reader.candidates[i].facebook_medio.append(-1)
                    models.data_reader.candidates[i].facebook_superior.append(-1)
                else:
                    models.data_reader.candidates[i].facebook_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male'] * 100)
                    models.data_reader.candidates[i].facebook_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female'] * 100)
                    
                    # Idade
                    for age_group in age_intervals:                        
                        #16 a 24
                        if(age_group == "adolescent" or age_group == "young_1"):
                            if(age_group != "adolescent"):
                                models.data_reader.candidates[i].facebook_16a24.append(json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group] *100)
                        #25 a 34
                        elif(age_group == "young_2"):
                            models.data_reader.candidates[i].facebook_25a34.append(json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group]*100)
                        #35 a 44
                        elif(age_group == "mid_aged_1"):
                            models.data_reader.candidates[i].facebook_35a44.append(json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group]*100)
                        #45 a 54
                        elif(age_group == "mid_aged_2"):
                            models.data_reader.candidates[i].facebook_45a54.append(json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group]*100)
                        #Acima 55
                        else:
                            if(adicionarIdoso == False):
                                models.data_reader.candidates[i].facebook_55[-1] = (models.data_reader.candidates[i].facebook_55[-1] + json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group]*100)
                                adicionarIdoso = True
                            else:
                                models.data_reader.candidates[i].facebook_55.append(json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group]*100)
                                adicionarIdoso = False
                    
                    models.data_reader.candidates[i].facebook_nordeste.append(json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['northeast'] * 100)
                    models.data_reader.candidates[i].facebook_sul.append(json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['south'] * 100)
                    models.data_reader.candidates[i].facebook_sudeste.append(json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['southeast'] * 100)
                    models.data_reader.candidates[i].facebook_norte_coeste.append(json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['midwest'] * 100)
                    models.data_reader.candidates[i].facebook_norte_coeste[-1] += (json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['north'] * 100)

                    models.data_reader.candidates[i].facebook_likes.append(json_line[presid_key][collected_date]['num_likes'])
                    models.data_reader.candidates[i].facebook_talking_about.append(json_line[presid_key][collected_date]['talking_about'])

                    for edu in education_status:
                        if(education_dic[edu] == "college"):
                            if(AdicionarFundamental == False):
                                models.data_reader.candidates[i].facebook_fundamental[-1] += (json_line[presid_key][collected_date]['percent_values_dict']['education_status'][edu] * 100)
                            else:
                                models.data_reader.candidates[i].facebook_fundamental.append(json_line[presid_key][collected_date]['percent_values_dict']['education_status'][edu] * 100)
                                AdicionarFundamental = False
                        if(education_dic[edu] == "high_school"):
                            if(AdicionarMedio == False):
                                models.data_reader.candidates[i].facebook_medio[-1] += (json_line[presid_key][collected_date]['percent_values_dict']['education_status'][edu] * 100)
                            else:
                                models.data_reader.candidates[i].facebook_medio.append(json_line[presid_key][collected_date]['percent_values_dict']['education_status'][edu] * 100)
                                AdicionarMedio = False
                        if(education_dic[edu] == "grad_school"):
                            if(AdicionarSuperior == False):
                                models.data_reader.candidates[i].facebook_superior[-1] += (json_line[presid_key][collected_date]['percent_values_dict']['education_status'][edu] * 100)
                            else:
                                models.data_reader.candidates[i].facebook_superior.append(json_line[presid_key][collected_date]['percent_values_dict']['education_status'][edu] * 100)
                                AdicionarSuperior = False
    update_value_empty()

def load_census():
    json_file = open(os.getcwd() + '\Graphics\Data\\census_data.json')
    census_dict = json.loads(json_file.readline())
    adicionarIdoso = True

    for collected_date in dates_graph:   
        
        if collected_date not in collected_dates:
            models.data_distribuition.facebook_gender_male.append(-1)
            models.data_distribuition.facebook_gender_female.append(-1)

            models.data_distribuition.facebook_age_16a24.append(-1)     
            models.data_distribuition.facebook_age_25a34.append(-1)
            models.data_distribuition.facebook_age_35a44.append(-1)
            models.data_distribuition.facebook_age_45a54.append(-1) 
            models.data_distribuition.facebook_age_acima55.append(-1) 
            
            models.data_distribuition.facebook_region_sudeste.append(-1) 
            models.data_distribuition.facebook_region_nordeste.append(-1) 
            models.data_distribuition.facebook_region_norte_centro_oeste.append(-1)
            models.data_distribuition.facebook_region_sul.append(-1) 

            #CENSUS
            models.data_distribuition.census_gender_male.append(-1)
            models.data_distribuition.census_gender_female.append(-1)

            models.data_distribuition.census_region_sudeste.append(-1) 
            models.data_distribuition.census_region_nordeste.append(-1) 
            models.data_distribuition.census_region_norte_centro_oeste.append(-1)
            models.data_distribuition.census_region_sul.append(-1) 
            
            models.data_distribuition.census_age_16a24.append(-1)
            models.data_distribuition.census_age_25a34.append(-1)
            models.data_distribuition.census_age_35a44.append(-1)
            models.data_distribuition.census_age_45a54.append(-1)
            models.data_distribuition.census_age_acima55.append(-1)         
        else:
            models.data_distribuition.facebook_gender_male.append(census_dict['genders']['male'][collected_date] * 100)
            models.data_distribuition.facebook_gender_female.append(census_dict['genders']['female'][collected_date] * 100)
            models.data_distribuition.census_gender_male.append(census_dict['genders']['female']['census'] * 100)
            models.data_distribuition.census_gender_female.append(census_dict['genders']['female']['census'] * 100)
            
            for age_group in age_intervals:                        
                #16 a 24
                if(age_group == "young_1"):                          
                    models.data_distribuition.facebook_age_16a24.append(census_dict['age_intervals'][age_group][collected_date] * 100)
                    models.data_distribuition.census_age_16a24.append(census_dict['age_intervals'][age_group]['census'] * 100)                                  
                #25 a 34
                elif(age_group == "young_2"):
                    models.data_distribuition.facebook_age_25a34.append(census_dict['age_intervals'][age_group][collected_date] * 100)
                    models.data_distribuition.census_age_25a34.append(census_dict['age_intervals'][age_group]['census'] * 100)
                #35 a 44
                elif(age_group == "mid_aged_1"):
                    models.data_distribuition.facebook_age_35a44.append(census_dict['age_intervals'][age_group][collected_date] * 100)  
                    models.data_distribuition.census_age_35a44.append(census_dict['age_intervals'][age_group]['census'] * 100)
                #45 a 54
                elif(age_group == "mid_aged_2"):
                    models.data_distribuition.facebook_age_45a54.append(census_dict['age_intervals'][age_group][collected_date] * 100) 
                    models.data_distribuition.census_age_45a54.append(census_dict['age_intervals'][age_group]['census'] * 100)
                #Acima 55
                elif(age_group != "adolescent"):
                    if(adicionarIdoso == False):                                
                        models.data_distribuition.facebook_age_acima55[-1] = (models.data_distribuition.facebook_age_acima55[-1] + census_dict['age_intervals'][age_group][collected_date] * 100)
                        models.data_distribuition.census_age_acima55[-1] = (models.data_distribuition.census_age_acima55[-1] + census_dict['age_intervals'][age_group]['census'] * 100)
                        adicionarIdoso = True
                    else:
                        models.data_distribuition.facebook_age_acima55.append(census_dict['age_intervals'][age_group][collected_date] * 100) 
                        models.data_distribuition.census_age_acima55.append(census_dict['age_intervals'][age_group]['census'] * 100)
                        adicionarIdoso = False                     

            models.data_distribuition.facebook_region_sudeste.append(census_dict['brazilian_regions']['southeast'][collected_date] * 100) 
            models.data_distribuition.facebook_region_nordeste.append(census_dict['brazilian_regions']['northeast'][collected_date] * 100) 
            models.data_distribuition.facebook_region_norte_centro_oeste.append(census_dict['brazilian_regions']['north'][collected_date] * 100)
            models.data_distribuition.facebook_region_norte_centro_oeste[-1] += (census_dict['brazilian_regions']['midwest'][collected_date] * 100) 
            models.data_distribuition.facebook_region_sul.append(census_dict['brazilian_regions']['south'][collected_date] * 100) 

            models.data_distribuition.census_region_sudeste.append(census_dict['brazilian_regions']['southeast']['census'] * 100) 
            models.data_distribuition.census_region_nordeste.append(census_dict['brazilian_regions']['northeast']['census'] * 100) 
            models.data_distribuition.census_region_norte_centro_oeste.append(census_dict['brazilian_regions']['north']['census'] * 100)
            models.data_distribuition.census_region_norte_centro_oeste[-1] += (census_dict['brazilian_regions']['midwest']['census'] * 100) 
            models.data_distribuition.census_region_sul.append(census_dict['brazilian_regions']['south']['census'] * 100) 

    update_value_empty_census()
    
def update_value_empty_census():

    last_i_facebook = 0
    last_i_census = 0

    for i in range(0, len(dates_graph)):
     
        #FACEBOOK
        if(models.data_distribuition.facebook_gender_male[i] == -1):                
            models.data_distribuition.facebook_gender_male[i] = return_new_value_graph(models.data_distribuition.facebook_gender_male, last_i_facebook, i)                    
            models.data_distribuition.facebook_gender_female[i] = return_new_value_graph(models.data_distribuition.facebook_gender_female, last_i_facebook, i)
            models.data_distribuition.facebook_age_16a24[i] = return_new_value_graph(models.data_distribuition.facebook_age_16a24, last_i_facebook, i)
            models.data_distribuition.facebook_age_25a34[i] = return_new_value_graph(models.data_distribuition.facebook_age_25a34, last_i_facebook, i)
            models.data_distribuition.facebook_age_35a44[i] = return_new_value_graph(models.data_distribuition.facebook_age_35a44, last_i_facebook, i)
            models.data_distribuition.facebook_age_45a54[i] = return_new_value_graph(models.data_distribuition.facebook_age_45a54, last_i_facebook, i)
            models.data_distribuition.facebook_age_acima55[i] = return_new_value_graph(models.data_distribuition.facebook_age_acima55, last_i_facebook, i)
        
            models.data_distribuition.facebook_region_norte_centro_oeste[i] = return_new_value_graph(models.data_distribuition.facebook_region_norte_centro_oeste, last_i_facebook, i)
            models.data_distribuition.facebook_region_nordeste[i] = return_new_value_graph(models.data_distribuition.facebook_region_nordeste, last_i_facebook, i)
            models.data_distribuition.facebook_region_sudeste[i] = return_new_value_graph(models.data_distribuition.facebook_region_sudeste, last_i_facebook, i)
            models.data_distribuition.facebook_region_sul[i] = return_new_value_graph(models.data_distribuition.facebook_region_sul, last_i_facebook, i)
        else:
            last_i_facebook = i
        
        #CENSUS
        if(models.data_distribuition.census_gender_male[i] == -1):
            models.data_distribuition.census_gender_male[i] = return_new_value_graph(models.data_distribuition.census_gender_male, last_i_census, i)                    
            models.data_distribuition.census_gender_female[i] = return_new_value_graph(models.data_distribuition.census_gender_female, last_i_census, i)
            models.data_distribuition.census_age_16a24[i] = return_new_value_graph(models.data_distribuition.census_age_16a24, last_i_census, i)
            models.data_distribuition.census_age_25a34[i] = return_new_value_graph(models.data_distribuition.census_age_25a34, last_i_census, i)
            models.data_distribuition.census_age_35a44[i] = return_new_value_graph(models.data_distribuition.census_age_35a44, last_i_census, i)
            models.data_distribuition.census_age_45a54[i] = return_new_value_graph(models.data_distribuition.census_age_45a54, last_i_census, i)
            models.data_distribuition.census_age_acima55[i] = return_new_value_graph(models.data_distribuition.census_age_acima55, last_i_census, i)
        
            models.data_distribuition.census_region_norte_centro_oeste[i] = return_new_value_graph(models.data_distribuition.census_region_norte_centro_oeste, last_i_census, i)
            models.data_distribuition.census_region_nordeste[i] = return_new_value_graph(models.data_distribuition.census_region_nordeste, last_i_census, i)
            models.data_distribuition.census_region_sudeste[i] = return_new_value_graph(models.data_distribuition.census_region_sudeste, last_i_census, i)
            models.data_distribuition.census_region_sul[i] = return_new_value_graph(models.data_distribuition.census_region_sul, last_i_census, i)
        else:
            last_i_census = i


def update_value_empty():
    for candidate in models.data_reader.candidates:
        
        c = models.return_index(candidate.name)
        last_i = 0

        for i in range(0, len(dates_graph)):

            #Verifica se o candidato foi para o segundo turno 
            # if(i <= 21 or models.data_reader.candidates[c].round2 == True):            

            if(models.data_reader.candidates[c].facebook_male[i] == -1):
                models.data_reader.candidates[c].facebook_male[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_male, last_i, i)                    
                models.data_reader.candidates[c].facebook_female[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_female, last_i, i)
                models.data_reader.candidates[c].facebook_16a24[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_16a24, last_i, i)
                models.data_reader.candidates[c].facebook_25a34[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_25a34, last_i, i)
                models.data_reader.candidates[c].facebook_35a44[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_35a44, last_i, i)
                models.data_reader.candidates[c].facebook_45a54[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_45a54, last_i, i)
                models.data_reader.candidates[c].facebook_55[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_55, last_i, i)
                models.data_reader.candidates[c].facebook_norte_coeste[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_norte_coeste, last_i, i)
                models.data_reader.candidates[c].facebook_nordeste[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_nordeste, last_i, i)
                models.data_reader.candidates[c].facebook_sudeste[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_sudeste, last_i, i)
                models.data_reader.candidates[c].facebook_sul[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_sul, last_i, i)
                models.data_reader.candidates[c].facebook_fundamental[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_fundamental, last_i, i)
                models.data_reader.candidates[c].facebook_medio[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_medio, last_i, i)
                models.data_reader.candidates[c].facebook_superior[i] = return_new_value_graph(models.data_reader.candidates[c].facebook_superior, last_i, i)
            else:
                last_i = i

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