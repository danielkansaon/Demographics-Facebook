class Data:
    def __init__(self):
        self.candidates = [Candidate('Jair Bolsonaro'), Candidate('Fernando Haddad'), Candidate('Ciro Gomes'), Candidate('Lula')]

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
    
class Candidate:    
   def __init__(self, name):
        self.name = name

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
        
data_reader = Data()

def complete_data_zero():
    for c in data_reader.candidates:
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

            c.ibope_16a24.append(0)
            c.ibope_25a34.append(0)
            c.ibope_35a44.append(0)
            c.ibope_45a54.append(0)
            c.ibope_55.append(0)

            c.dfolha_16a24.append(0)
            c.dfolha_25a34.append(0)
            c.dfolha_35a44.append(0)
            c.dfolha_45a54.append(0)
            c.dfolha_55.append(0)

            c.dfolha_norte_coeste.append(0)  
            c.dfolha_nordeste.append(0) 
            c.dfolha_sudeste.append(0) 
            c.dfolha_sul.append(0) 

            c.ibope_norte_coeste.append(0) 
            c.ibope_nordeste.append(0)
            c.ibope_sudeste.append(0) 
            c.ibope_sul.append(0)

            c.ibope_fundamental.append(0)  
            c.ibope_medio.append(0)
            c.ibope_superior.append(0) 

            c.dfolha_fundamental.append(c.dfolha_fundamental)  
            c.dfolha_medio.append(c.dfolha_medio)
            c.dfolha_superior.append(c.dfolha_superior) 

