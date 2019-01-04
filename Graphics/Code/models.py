class Data:
    def __init__(self):
        self.candidates = [Candidate('Jair Bolsonaro', True), Candidate('Fernando Haddad', True), Candidate('Ciro Gomes', False), Candidate('Lula', False), Candidate('Marina Silva', False), Candidate('Geraldo Alckmin', False), Candidate('Alvaro Dias', False)]
    
# xticks_facebook = ["17-11",  "18-07",  "08-06",  "09-10",  "09-17",  "09-24",  "10-01",  "10-05", "10-06", "10-08", "10-15",  "10-22",  "10-26", "10-27", "10-29"]
# xticks_dfolha = ["17-11-30",  "06-07",  "08-21",  "09-10",  "09-18",  "09-28",  "10-02",  "10-04", "10-06", "10-07", "10-10", "10-18",  "10-25",  "10-27", "10-28"]
# xticks_ibope = ["17-10-22",  "06-24",  "08-19",  "09-10",  "09-18",  "09-24",  "09-30",  "10-02", "10-06", "10-07", "10-07", "10-14",  "10-23",  "10-27", "10-28"]

# dates_graph = ["17-10-22", "17-11-28", "17-11-30", "18-06-07", "18-06-24", "18-07-09", "18-08-06", "18-08-19", "18-08-21", "18-09-10", "18-09-17", "18-09-18", 
# "18-09-24", "18-09-28", "18-09-30", "18-10-01", "18-10-02", "18-10-04", "18-10-05", "18-10-06", "18-10-07", "18-10-08", "18-10-10", "18-10-14", "18-10-15",
# "18-10-18", "18-10-22", "18-10-23", "18-10-25", "18-10-26", "18-10-27", "18-10-28", "18-10-29"]

# data_dfolha = ["2017-11-30",  "2018-06-07",  "2018-08-21",  "2018-09-10",  "2018-09-18",  "2018-09-28",  "2018-10-02",  "2018-10-04", "2018-10-06", "2018-10-07", 
# "2018-10-10", "10-18",  "2018-10-25",  "2018-10-27", "2018-10-28"]

# data_ibope = ["2017-10-22",  "2018-06-24",  "2018-08-19",  "2018-09-10",  "2018-09-18",  "2018-09-24",  "2018-09-30", 
# "2018-10-02", "2018-10-06", "2018-10-07", "2018-10-07", "2018-10-14",  "2018-10-23",  "2018-10-27", "2018-10-28"]

def return_index(name):
    if(name == 'Jair Bolsonaro'):
        return 0
    elif(name == 'Fernando Haddad'):
        return 1
    elif(name == 'Ciro Gomes'):
        return 2
    elif(name == 'Lula'):
        return 3
    elif(name == 'Marina Silva'):
        return 4
    elif(name == 'Geraldo Alckmin'):
        return 5
    elif(name == 'Alvaro Dias'):
        return 6
    return -1
    
class Distribuition:
    def __init__(self):
        self.census_gender_male = []
        self.census_gender_female = []

        self.census_education_fundamental = []
        self.census_education_medio = []
        self.census_education_superior = []

        self.census_region_sudeste = []
        self.census_region_norte_centro_oeste = []
        self.census_region_nordeste = []
        self.census_region_sul = []

        self.census_age_16a24 = []
        self.census_age_25a34 = []
        self.census_age_35a44 = []
        self.census_age_45a54 = []
        self.census_age_acima55 = []

        #FACEBOOK
        self.facebook_gender_male = []
        self.facebook_gender_female = []

        self.facebook_education_fundamental = []
        self.facebook_education_medio = []
        self.facebook_education_superior = []

        self.facebook_region_sudeste = []
        self.facebook_region_norte_centro_oeste = []
        self.facebook_region_nordeste = []
        self.facebook_region_sul = []

        self.facebook_age_16a24 = []
        self.facebook_age_25a34 = []
        self.facebook_age_35a44 = []
        self.facebook_age_45a54 = []
        self.facebook_age_acima55 = []

class Candidate:    
   def __init__(self, name, round2):
        self.name = name
        self.round2 = round2

        # FACEBOOK
        self.facebook_male =[]
        self.facebook_female =[]
        self.facebook_16a24 =[]
        self.facebook_25a34 =[]
        self.facebook_35a44 =[]
        self.facebook_45a54 =[]
        self.facebook_55 =[]
        self.facebook_norte_coeste =[]
        self.facebook_sul =[]
        self.facebook_sudeste =[]
        self.facebook_nordeste =[]       

        self.facebook_superior =[]
        self.facebook_medio =[]
        self.facebook_fundamental =[]

        self.facebook_likes = []

        self.facebook_talking_about = []

        #IBOPE
        self.ibope_male = []
        self.ibope_female = []  
   
        self.ibope_16a24 =[]
        self.ibope_25a34 =[]
        self.ibope_35a44 =[]
        self.ibope_45a54 =[]
        self.ibope_55 =[]

        self.ibope_norte_coeste =[]
        self.ibope_sul =[]
        self.ibope_sudeste =[]
        self.ibope_nordeste =[]

        self.ibope_superior =[]
        self.ibope_medio =[]
        self.ibope_fundamental =[]   

        self.ibope_score =[]

        #DATAFOLHA
        self.dfolha_male = []
        self.dfolha_female = []

        self.dfolha_16a24 =[]
        self.dfolha_25a34 =[]
        self.dfolha_35a44 =[]
        self.dfolha_45a54 =[]
        self.dfolha_55 =[]

        self.dfolha_norte_coeste =[]
        self.dfolha_sul =[]
        self.dfolha_sudeste =[]
        self.dfolha_nordeste =[]

        self.dfolha_superior =[]
        self.dfolha_medio =[]
        self.dfolha_fundamental =[] 

        self.dfolha_score =[]

data_distribuition = Distribuition()      
data_reader = Data()

def complete_data_zero():
    for c in data_reader.candidates:
        while len(c.ibope_male) < 15:
            c.ibope_male.append(-100)
            c.dfolha_male.append(-100)
            c.ibope_female.append(-100)
            c.dfolha_female.append(-100)       

            c.dfolha_16a24.append(-100)
            c.dfolha_25a34.append(-100)
            c.dfolha_35a44.append(-100)
            c.dfolha_45a54.append(-100)
            c.dfolha_55.append(-100)

            c.ibope_16a24.append(-100)
            c.ibope_25a34.append(-100)
            c.ibope_35a44.append(-100)
            c.ibope_45a54.append(-100)
            c.ibope_55.append(-100)

            c.dfolha_norte_coeste.append(-100)  
            c.dfolha_nordeste.append(-100) 
            c.dfolha_sudeste.append(-100) 
            c.dfolha_sul.append(-100) 

            c.ibope_norte_coeste.append(-100) 
            c.ibope_nordeste.append(-100)
            c.ibope_sudeste.append(-100) 
            c.ibope_sul.append(-100)

            c.ibope_fundamental.append(-100)  
            c.ibope_medio.append(-100)
            c.ibope_superior.append(-100) 

            c.dfolha_fundamental.append(-100)  
            c.dfolha_medio.append(-100)
            c.dfolha_superior.append(-100) 

