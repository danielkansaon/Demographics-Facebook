import json
import os
import models

# Bolsonaro
vec_facebook_17_male =[]
vec_facebook_17_female =[]

vec_facebook_17_16a24 =[]
vec_facebook_17_25a34 =[]
vec_facebook_17_35a44 =[]
vec_facebook_17_45a54 =[]
vec_facebook_17_55 =[]

# Haddad
vec_facebook_13_male =[]
vec_facebook_13_female =[]

vec_facebook_13_16a24 =[]
vec_facebook_13_25a34 =[]
vec_facebook_13_35a44 =[]
vec_facebook_13_45a54 =[]
vec_facebook_13_55 =[]

# Lula
vec_facebook_lula_male =[]
vec_facebook_lula_female =[]

vec_facebook_12_16a24 =[]
vec_facebook_12_25a34 =[]
vec_facebook_12_35a44 =[]
vec_facebook_12_45a54 =[]
vec_facebook_12_55 =[]

# Ciro
vec_facebook_12_male =[]
vec_facebook_12_female =[]

vec_facebook_12_16a24 =[]
vec_facebook_12_25a34 =[]
vec_facebook_12_35a44 =[]
vec_facebook_12_45a54 =[]
vec_facebook_12_55 =[]

age_intervals = {     
    'adolescent' :{'age_min': 13, 'age_max': 17},
    'young_1' :{'age_min': 18, 'age_max': 24},
    'young_2' :{'age_min': 25, 'age_max': 34},
    'mid_aged_1' :{'age_min': 35, 'age_max': 44},
    'mid_aged_2' :{'age_min': 45, 'age_max': 54},        
    'old_1': {'age_min': 55, 'age_max': 64},
    'old_2': {'age_min': 65}                              
    }    

def readJson():
    input_file = open(os.getcwd() + '\Graphics\Data\\audiencia_presidenciaveis.json')
    collected_dates = ["17_11_28",  "18_07_09",  "18_08_06",  "18_09_10",  "18_09_17",  "18_09_24",  "18_10_01",  "18_10_05", "18_10_06",  "18_10_08",  "18_10_15",  "18_10_22",  "18_10_26", "18_10_27", "18_10_29"]
    
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
            for collected_date in collected_dates:             
                if(collected_date == "18_10_06" or collected_date == "18_10_27"):                    
                    vec_facebook_17_male.append(vec_facebook_17_male[len(vec_facebook_17_male) - 1])
                    vec_facebook_17_female.append(vec_facebook_17_female[len(vec_facebook_17_female) - 1])                
                else:
                    vec_facebook_17_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male'] * 100)
                    vec_facebook_17_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female'] * 100)
        elif(presid_key == '3'):        
            for collected_date in collected_dates:
                if(collected_date == "18_10_06" or collected_date == "18_10_27"):
                    vec_facebook_13_male.append(vec_facebook_13_male[len(vec_facebook_13_male) - 1])
                    vec_facebook_13_female.append(vec_facebook_13_female[len(vec_facebook_13_female) - 1])
                else:
                    vec_facebook_13_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male']* 100)
                    vec_facebook_13_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female']* 100)
        elif(presid_key == '4'):        
            for collected_date in collected_dates:   
                if(collected_date == "18_10_06" or collected_date == "18_10_27"):        
                    vec_facebook_lula_male.append(vec_facebook_lula_male[len(vec_facebook_lula_male) - 1])
                    vec_facebook_lula_female.append(vec_facebook_lula_female[len(vec_facebook_lula_female) - 1])
                else:  
                    vec_facebook_lula_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male']* 100)
                    vec_facebook_lula_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female']* 100)
        elif(presid_key == '110'):        
            for collected_date in collected_dates:   
                if(collected_date == "18_10_06" or collected_date == "18_10_27"):        
                    vec_facebook_12_male.append(vec_facebook_12_male[len(vec_facebook_12_male) - 1])
                    vec_facebook_12_female.append(vec_facebook_12_female[len(vec_facebook_12_female) - 1])
                else:
                    if(collected_date != '17_11_28'):
                        vec_facebook_12_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male']* 100)
                        vec_facebook_12_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female']* 100)
                    else:
                        vec_facebook_12_male.append(0)
                        vec_facebook_12_female.append(0)
            
            # for age_group in age_intervals:
            #     print '\t\tPercent value: %.2f' % (json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group]*100)          
                    