import json
import os

# Bolsonaro
vec_facebook_17_male =[]
vec_facebook_17_female =[]

# Haddad
vec_facebook_13_male =[]
vec_facebook_13_female =[]

# Lula
vec_facebook_lula_male =[]
vec_facebook_lula_female =[]

# Ciro
vec_facebook_12_male =[]
vec_facebook_12_female =[]

xticks_facebook = ["17-11",  "18-07",  "08-06",  "09-10",  "09-17",  "09-24",  "10-01",  "10-05", "10-06", "10-08", "10-15",  "10-22",  "10-26", "10-27", "10-29"]

# Adicionar data depois "10-05" - Resultado 1
# Adicionar data depois "10-26" - Resultado 2
def readJson():
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
            for collected_date in collected_dates:             
                if(collected_date == "10-06" or collected_date == "10-27"):                    
                    vec_facebook_17_male.append(vec_facebook_17_male[len(vec_facebook_17_male) - 1])
                    vec_facebook_17_female.append(vec_facebook_17_female[0])                
                else:
                    vec_facebook_17_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male'] * 100)
                    vec_facebook_17_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female'] * 100)
        elif(presid_key == '3'):        
            for collected_date in collected_dates:
                if(collected_date == "10-06" or collected_date == "10-27"):
                    vec_facebook_13_male.append(vec_facebook_13_male[len(vec_facebook_13_male) - 1])
                    vec_facebook_13_female.append(vec_facebook_13_female[len(vec_facebook_13_female) - 1])
                else:
                    vec_facebook_13_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male']* 100)
                    vec_facebook_13_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female']* 100)
        elif(presid_key == '4'):        
            for collected_date in collected_dates:   
                if(collected_date == "10-06" or collected_date == "10-27"):        
                    vec_facebook_lula_male.append(vec_facebook_lula_male[len(vec_facebook_lula_male) - 1])
                    vec_facebook_lula_female.append(vec_facebook_lula_female[len(vec_facebook_lula_female) - 1])
                else:  
                    vec_facebook_lula_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male']* 100)
                    vec_facebook_lula_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female']* 100)