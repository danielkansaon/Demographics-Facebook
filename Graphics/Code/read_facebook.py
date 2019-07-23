# -*- coding: utf-8 -*-

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

# collected_dates_old = ["17_11_28",  "18_07_09",  "18_08_06",  "18_09_10",  "18_09_17",  "18_09_24",  "18_10_01",  "18_10_05", "18_10_06",  "18_10_08",  "18_10_15",  "18_10_22",  "18_10_26", "18_10_27", "18_10_29"]
collected_dates = ["17_11_28",  "18_07_09",  "18_08_06",  "18_09_10",  "18_09_17",  "18_09_24",  "18_10_01",  "18_10_05",  "18_10_08",  "18_10_15",  "18_10_22", "18_10_26", "18_10_29"]

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
    input_file = open(os.getcwd() + '\..\Data\\audiencia_presidenciaveis.json')
    load_census()
               
    for line in input_file:
        json_line = json.loads(line.strip())

        adicionarIdoso = True

        for j in json_line:
            presid_key = j           
        
        i = return_index(presid_key)

        if(i >= 0):  
            for collected_date in collected_dates:   

                if(json_line[presid_key].get(collected_date, '') == ''):                         
                    models.data_reader.candidates[i].facebook_male.append(0)
                    models.data_reader.candidates[i].facebook_female.append(0)
                    models.data_reader.candidates[i].facebook_16a24.append(0)
                    models.data_reader.candidates[i].facebook_25a34.append(0)
                    models.data_reader.candidates[i].facebook_35a44.append(0)
                    models.data_reader.candidates[i].facebook_45a54.append(0)
                    models.data_reader.candidates[i].facebook_55.append(0)
                    models.data_reader.candidates[i].facebook_nordeste.append(0)
                    models.data_reader.candidates[i].facebook_sul.append(0)
                    models.data_reader.candidates[i].facebook_sudeste.append(0)
                    models.data_reader.candidates[i].facebook_norte_coeste.append(0)
                    models.data_reader.candidates[i].facebook_fundamental.append(0)
                    models.data_reader.candidates[i].facebook_medio.append(0)
                    models.data_reader.candidates[i].facebook_superior.append(0)
                    
                    models.data_reader.candidates[i].facebook_likes.append(0)
                    models.data_reader.candidates[i].facebook_talking_about.append(0)
                    models.data_reader.candidates[i].facebook_engagement.append(0)
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
                    
                    #Region
                    models.data_reader.candidates[i].facebook_nordeste.append(json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['northeast'] * 100)
                    models.data_reader.candidates[i].facebook_sul.append(json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['south'] * 100)
                    models.data_reader.candidates[i].facebook_sudeste.append(json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['southeast'] * 100)
                    models.data_reader.candidates[i].facebook_norte_coeste.append(json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['midwest'] * 100)
                    models.data_reader.candidates[i].facebook_norte_coeste[-1] += (json_line[presid_key][collected_date]['percent_values_dict']['brazilian_regions']['north'] * 100)

                    #Education
                    models.data_reader.candidates[i].facebook_fundamental.append(json_line[presid_key][collected_date]['percent_values_dict']['education_status_grouped_brazil']["incomplete_high_school"] * 100)
                    models.data_reader.candidates[i].facebook_medio.append(json_line[presid_key][collected_date]['percent_values_dict']['education_status_grouped_brazil']["high_school"] * 100)
                    models.data_reader.candidates[i].facebook_superior.append(json_line[presid_key][collected_date]['percent_values_dict']['education_status_grouped_brazil']["college"] * 100)
                    
                    #Other Graph
                    models.data_reader.candidates[i].facebook_engagement.append(int(json_line[presid_key][collected_date]['raw_values_dict']['all']['all']))                    
                    models.data_reader.candidates[i].facebook_likes.append(json_line[presid_key][collected_date]['num_likes'])
                    models.data_reader.candidates[i].facebook_talking_about.append(json_line[presid_key][collected_date]['talking_about'])


def load_census():
    json_file = open(os.getcwd() + '\..\Data\census_data.json')
    census_dict = json.loads(json_file.readline())
    adicionarIdoso = True

    for collected_date in collected_dates:   
        
        if(collected_date == "18_10_06" or collected_date == "18_10_27"):
            models.data_distribuition.facebook_gender_male.append(models.data_distribuition.facebook_gender_male[-1])
            models.data_distribuition.facebook_gender_female.append(models.data_distribuition.facebook_gender_female[-1])

            models.data_distribuition.facebook_age_16a24.append(models.data_distribuition.facebook_age_16a24[-1])     
            models.data_distribuition.facebook_age_25a34.append(models.data_distribuition.facebook_age_25a34[-1])
            models.data_distribuition.facebook_age_35a44.append(models.data_distribuition.facebook_age_35a44[-1])
            models.data_distribuition.facebook_age_45a54.append(models.data_distribuition.facebook_age_45a54[-1]) 
            models.data_distribuition.facebook_age_acima55.append(models.data_distribuition.facebook_age_acima55[-1]) 
            
            models.data_distribuition.facebook_region_sudeste.append(models.data_distribuition.facebook_region_sudeste[-1]) 
            models.data_distribuition.facebook_region_nordeste.append(models.data_distribuition.facebook_region_nordeste[-1]) 
            models.data_distribuition.facebook_region_norte_centro_oeste.append(models.data_distribuition.facebook_region_norte_centro_oeste[-1])
            models.data_distribuition.facebook_region_sul.append(models.data_distribuition.facebook_region_sul[-1]) 

            #CENSUS
            models.data_distribuition.census_gender_male.append(models.data_distribuition.census_gender_male[-1])
            models.data_distribuition.census_gender_female.append(models.data_distribuition.census_gender_female[-1])

            models.data_distribuition.census_region_sudeste.append(models.data_distribuition.census_region_sudeste[-1]) 
            models.data_distribuition.census_region_nordeste.append(models.data_distribuition.census_region_nordeste[-1]) 
            models.data_distribuition.census_region_norte_centro_oeste.append(models.data_distribuition.census_region_norte_centro_oeste[-1])
            models.data_distribuition.census_region_sul.append(models.data_distribuition.census_region_sul[-1]) 
            
            models.data_distribuition.census_age_16a24.append(models.data_distribuition.census_age_16a24[-1])
            models.data_distribuition.census_age_25a34.append(models.data_distribuition.census_age_25a34[-1])
            models.data_distribuition.census_age_35a44.append(models.data_distribuition.census_age_35a44[-1])
            models.data_distribuition.census_age_45a54.append(models.data_distribuition.census_age_45a54[-1])
            models.data_distribuition.census_age_acima55.append(models.data_distribuition.census_age_acima55[-1])         
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
