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

regions = ["northeast", "south", "southeast", "midwest", "north"]

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
    return -1

def readJson():
    input_file = open(os.getcwd() + '\Graphics\Data\\audiencia_presidenciaveis.json')
    collected_dates = ["17_11_28",  "18_07_09",  "18_08_06",  "18_09_10",  "18_09_17",  "18_09_24",  "18_10_01",  "18_10_05", "18_10_06",  "18_10_08",  "18_10_15",  "18_10_22",  "18_10_26", "18_10_27", "18_10_29"]
    adicionarJovem = True
    adicionarIdoso = True   
       
    for line in input_file:
        json_line = json.loads(line.strip())

        for j in json_line:
            presid_key = j           
        
        i = return_index(presid_key)

        if(i >= 0):  
            for collected_date in collected_dates:   
                if(json_line[presid_key].get(collected_date, '') == ''):     
                    if(collected_date == "18_10_06" or collected_date == "18_10_27"):
                        models.data_reader.candidates[i].facebook_male.append(models.data_reader.candidates[i].facebook_male[-1])                
                        models.data_reader.candidates[i].facebook_female.append(models.data_reader.candidates[i].facebook_female[-1])

                        models.data_reader.candidates[i].facebook_16a24.append( models.data_reader.candidates[i].facebook_16a24[-1])
                        models.data_reader.candidates[i].facebook_25a34.append( models.data_reader.candidates[i].facebook_25a34[-1])
                        models.data_reader.candidates[i].facebook_35a44.append( models.data_reader.candidates[i].facebook_35a44[-1])
                        models.data_reader.candidates[i].facebook_45a54.append( models.data_reader.candidates[i].facebook_45a54[-1])
                        models.data_reader.candidates[i].facebook_55.append( models.data_reader.candidates[i].facebook_55[-1])

                        models.data_reader.candidates[i].facebook_nordeste.append(models.data_reader.candidates[i].facebook_nordeste[-1])
                        models.data_reader.candidates[i].facebook_sul.append(models.data_reader.candidates[i].facebook_sul[-1])
                        models.data_reader.candidates[i].facebook_sudeste.append( models.data_reader.candidates[i].facebook_sudeste[-1])
                        models.data_reader.candidates[i].facebook_norte_coeste.append(models.data_reader.candidates[i].facebook_norte_coeste[-1])

                        models.data_reader.candidates[i].facebook_likes.append(models.data_reader.candidates[i].facebook_likes[-1])
                    else:
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
                        models.data_reader.candidates[i].facebook_likes.append(0)
                else:
                    models.data_reader.candidates[i].facebook_male.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['male'] * 100)
                    models.data_reader.candidates[i].facebook_female.append(json_line[presid_key][collected_date]['percent_values_dict']['gender']['female'] * 100)
                    
                    # Idade
                    for age_group in age_intervals:                        
                        #16 a 24
                        if(age_group == "adolescent" or age_group == "young_1"):
                            if(adicionarJovem == False):
                                 models.data_reader.candidates[i].facebook_16a24[0] = (models.data_reader.candidates[i].facebook_16a24[0] + json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group] *100)                           
                                 adicionarJovem = True
                            else:
                                models.data_reader.candidates[i].facebook_16a24.append(json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group] *100)    
                                adicionarJovem = False
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
                                models.data_reader.candidates[i].facebook_55[0] = (models.data_reader.candidates[i].facebook_55[0] + json_line[presid_key][collected_date]['percent_values_dict']['age_intervals'][age_group]*100)
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
                        