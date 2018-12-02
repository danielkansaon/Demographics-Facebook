class Data:
    def __init__(self):
        self.candidates = [Candidate('Jair Bolsonaro'), Candidate('Fernando Haddad'), Candidate('Ciro Gomes'), Candidate('Lula')]

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
        
data_reader = Data()