import matplotlib.pyplot as plt
import read_facebook as facebook
import read_elections as election
import pandas as pd
import models
import os

# xticks_facebook = ["17-11",  "18-07",  "08-06",  "09-10",  "09-17",  "09-24",  "10-01",  "10-05", "10-06", "10-08", "10-15",  "10-22",  "10-26", "10-27", "10-29"]
# xticks_dataf = ["17-11-30",  "06-07",  "08-21",  "09-10",  "09-18",  "09-28",  "10-02",  "10-04", "10-06", "10-07", "10-10", "10-18",  "10-25",  "10-27", "10-28"]
# xticks_ibope = ["17-10-22",  "06-24",  "08-19",  "09-10",  "09-18",  "09-24",  "09-30",  "10-02", "10-06", "10-07", "10-07", "10-14",  "10-23",  "10-27", "10-28"]

xticks = ["17\n11",  "18\n07",  "08\n06",  "09\n10",  "09\n17",  "09\n24",  "10\n01",  "10\n05", "10\n06",  "10\n08",  "10\n15",  "10\n22",  "10\n26", "10\n27",  "10\n29"]

i_bolsonaro = models.return_index("Jair Bolsonaro")
i_haddad = models.return_index("Fernando Haddad")
i_lula = models.return_index("Lula")
i_ciro = models.return_index("Ciro Gomes")
i_marina = models.return_index("Marina Silva")
i_alckmin = models.return_index("Geraldo Alckmin")

def plot_gender():

    df = pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
            '17_male_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_male, '17_female_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_female,
            '17_male_ibope': models.data_reader.candidates[i_bolsonaro].ibope_male, '17_female_ibope': models.data_reader.candidates[i_bolsonaro].ibope_female,

            '13_male_dtfolha': models.data_reader.candidates[i_haddad].dfolha_male, '13_female_dtfolha': models.data_reader.candidates[i_haddad].dfolha_female,
            '13_male_ibope': models.data_reader.candidates[i_haddad].ibope_male, '13_female_ibope': models.data_reader.candidates[i_haddad].ibope_female,

            'lula_male_dtfolha': models.data_reader.candidates[i_lula].dfolha_male, 'lula_female_dtfolha': models.data_reader.candidates[i_lula].dfolha_female,
            'lula_male_ibope': models.data_reader.candidates[i_lula].ibope_male, 'lula_female_ibope': models.data_reader.candidates[i_lula].ibope_female,

            'ciro_male_dtfolha': models.data_reader.candidates[i_ciro].dfolha_male, 'ciro_female_dtfolha': models.data_reader.candidates[i_ciro].dfolha_female,
            'ciro_male_ibope': models.data_reader.candidates[i_ciro].ibope_male, 'ciro_female_ibope': models.data_reader.candidates[i_ciro].ibope_female,

            '17_male_facebook': models.data_reader.candidates[i_bolsonaro].facebook_male, '17_female_facebook': models.data_reader.candidates[i_bolsonaro].facebook_female,
            '13_male_facebook': models.data_reader.candidates[i_haddad].facebook_male, '13_female_facebook': models.data_reader.candidates[i_haddad].facebook_female,
            'lula_male_facebook': models.data_reader.candidates[i_lula].facebook_male, 'lula_female_facebook': models.data_reader.candidates[i_lula].facebook_female,
            'ciro_male_facebook': models.data_reader.candidates[i_ciro].facebook_male, 'ciro_female_facebook': models.data_reader.candidates[i_ciro].facebook_female
        })
    
    count_x = len(models.data_reader.candidates[0].dfolha_male)

    G1 = plt.subplot(3,2,1)
    plt.title('Male', fontsize=12, color='gray', loc='center')
    plt.ylabel('Jair Bolsonaro', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', '17_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  #linestyle='dashed' (--)
    plt.plot('x', '17_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G1.set_ylim(15,75)
    plt.legend()
    
    G2 = plt.subplot(3,2,2)
    plt.title('Female', fontsize=12, color='gray', loc='center')
    plt.plot('x', '17_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', '17_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G2.set_ylim(15,75)
    plt.legend()

    G3 = plt.subplot(3,2,3)
    plt.ylabel('Fernando Haddad', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', '13_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '13_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', '13_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G3.set_ylim(15,75)
    plt.legend()

    G4 = plt.subplot(3,2,4)
    plt.plot('x', '13_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '13_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', '13_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G4.set_ylim(15,75)
    plt.legend()

    G5 = plt.subplot(3,2,5)
    plt.ylabel('Lula', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', 'lula_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'lula_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', 'lula_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G5.set_ylim(15,75)
    plt.legend()

    G6 = plt.subplot(3,2,6)
    plt.plot('x', 'lula_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'lula_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', 'lula_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G6.set_ylim(15,75)
    plt.legend()

    # G7 = plt.subplot(4,2,7)
    # plt.ylabel('Ciro Gomes', multialignment='center', color='gray', fontsize=12)
    # plt.plot('x', 'ciro_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'ciro_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    # plt.plot('x', 'ciro_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G7.set_ylim(15,75)
    # plt.legend()

    # G8 = plt.subplot(4,2,8)
    # plt.plot('x', 'ciro_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'ciro_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    # plt.plot('x', 'ciro_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G8.set_ylim(15,75)
    # plt.legend()
    
    # plt.text(0.08, 0.3, 'TIME', ha='center', va='center')
    plt.suptitle('Gender')
    plt.show()


def plot_region():
    
    # df = pd.DataFrame(
    #     {
    #         'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
    #         '17_sudeste_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_sudeste, '17_nordeste_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_nordeste,
    #         '17_coeste_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_norte_coeste, '17_sul_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_sul,

    #         '17_sudeste_ibope': models.data_reader.candidates[i_bolsonaro].ibope_sudeste, '17_nordeste_ibope': models.data_reader.candidates[i_bolsonaro].ibope_nordeste,
    #         '17_coeste_ibope': models.data_reader.candidates[i_bolsonaro].ibope_norte_coeste, '17_sul_ibope': models.data_reader.candidates[i_bolsonaro].ibope_sul,
           
    #         '17_sudeste_facebook': models.data_reader.candidates[i_bolsonaro].facebook_sudeste, '17_sul_facebook': models.data_reader.candidates[i_bolsonaro].facebook_sul,
    #         '17_coeste_facebook': models.data_reader.candidates[i_bolsonaro].facebook_norte_coeste, '17_nordeste_facebook': models.data_reader.candidates[i_bolsonaro].facebook_nordeste
    #     })
    
    # count_x = len(models.data_reader.candidates[i_bolsonaro].dfolha_male)    
    # plt.suptitle('Jair Bolsonaro')    

    # # Jair Bolsonaro    
    # G1 = plt.subplot(2,2,1)
    # plt.title('Sudeste', fontsize=12, color='black', loc='center')
    # plt.plot('x', '17_sudeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '17_sudeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', '17_sudeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(5,65)
    # plt.legend()

    # G2 = plt.subplot(2,2,2)
    # plt.title('Nordeste', fontsize=12, color='black', loc='center')
    # plt.plot('x', '17_nordeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '17_nordeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', '17_nordeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G2.set_ylim(5,65)
    # plt.legend()

    # G3 = plt.subplot(2,2,3)
    # plt.title('Centro oeste', fontsize=12, color='black', loc='center')
    # plt.plot('x', '17_coeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '17_coeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', '17_coeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G3.set_ylim(5,65)
    # plt.legend()

    # G4 = plt.subplot(2,2,4)
    # plt.title('Sul', fontsize=12, color='black', loc='center')
    # plt.plot('x', '17_sul_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '17_sul_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', '17_sul_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(5,65)
    # plt.legend()

    # plt.show()
    # plt.savefig("Graphics\Figures\\region_bolsonaro.png")

    # df = pd.DataFrame(
    #     {
    #         'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
    #         '13_sudeste_dtfolha': models.data_reader.candidates[i_haddad].dfolha_sudeste, '13_nordeste_dtfolha': models.data_reader.candidates[i_haddad].dfolha_nordeste,
    #         '13_coeste_dtfolha': models.data_reader.candidates[i_haddad].dfolha_norte_coeste, '13_sul_dtfolha': models.data_reader.candidates[i_haddad].dfolha_sul,

    #         '13_sudeste_ibope': models.data_reader.candidates[i_haddad].ibope_sudeste, '13_nordeste_ibope': models.data_reader.candidates[i_haddad].ibope_nordeste,
    #         '13_coeste_ibope': models.data_reader.candidates[i_haddad].ibope_norte_coeste, '13_sul_ibope': models.data_reader.candidates[i_haddad].ibope_sul,
           
    #         '13_sudeste_facebook': models.data_reader.candidates[i_haddad].facebook_sudeste, '13_sul_facebook': models.data_reader.candidates[i_haddad].facebook_sul,
    #         '13_coeste_facebook': models.data_reader.candidates[i_haddad].facebook_norte_coeste, '13_nordeste_facebook': models.data_reader.candidates[i_haddad].facebook_nordeste
    #     })
    
    # count_x = len(models.data_reader.candidates[i_haddad].dfolha_male)

    # # Fernando Haddad
    # G1 = plt.subplot(2,2,1)
    # plt.title('Sudeste', fontsize=12, color='black', loc='center')
    # plt.plot('x', '13_sudeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '13_sudeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', '13_sudeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(5,75)
    # plt.legend()

    # G2 = plt.subplot(2,2,2)
    # plt.title('Nordeste', fontsize=12, color='black', loc='center')
    # plt.plot('x', '13_nordeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '13_nordeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', '13_nordeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G2.set_ylim(5,65)
    # plt.legend()

    # G3 = plt.subplot(2,2,3)
    # plt.title('Centro oeste', fontsize=12, color='black', loc='center')
    # plt.plot('x', '13_coeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '13_coeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', '13_coeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G3.set_ylim(5,65)
    # plt.legend()

    # G4 = plt.subplot(2,2,4)
    # plt.title('Sul', fontsize=12, color='black', loc='center')
    # plt.plot('x', '13_sul_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '13_sul_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', '13_sul_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(5,65)
    # plt.legend()

    # plt.suptitle('Fernando Haddad')    
    # plt.show()
    # plt.savefig("Graphics\Figures\\region_haddad.png")

    # df = pd.DataFrame(
    #     {
    #         'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
    #         'lula_sudeste_dtfolha': models.data_reader.candidates[i_lula].dfolha_sudeste, 'lula_nordeste_dtfolha': models.data_reader.candidates[i_lula].dfolha_nordeste,
    #         'lula_coeste_dtfolha': models.data_reader.candidates[i_lula].dfolha_norte_coeste, 'lula_sul_dtfolha': models.data_reader.candidates[i_lula].dfolha_sul,

    #         'lula_sudeste_ibope': models.data_reader.candidates[i_lula].ibope_sudeste, 'lula_nordeste_ibope': models.data_reader.candidates[i_lula].ibope_nordeste,
    #         'lula_coeste_ibope': models.data_reader.candidates[i_lula].ibope_norte_coeste, 'lula_sul_ibope': models.data_reader.candidates[i_lula].ibope_sul,
           
    #         'lula_sudeste_facebook': models.data_reader.candidates[i_lula].facebook_sudeste, 'lula_sul_facebook': models.data_reader.candidates[i_lula].facebook_sul,
    #         'lula_coeste_facebook': models.data_reader.candidates[i_lula].facebook_norte_coeste, 'lula_nordeste_facebook': models.data_reader.candidates[i_lula].facebook_nordeste
    #     })
    
    # count_x = len(models.data_reader.candidates[i_lula].dfolha_male)

    # # Lula    
    # plt.suptitle('Lula')  
    # G1 = plt.subplot(2,2,1)
    # plt.title('Sudeste', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'lula_sudeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_sudeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'lula_sudeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(5,75)
    # plt.legend()

    # G2 = plt.subplot(2,2,2)
    # plt.title('Nordeste', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'lula_nordeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_nordeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'lula_nordeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G2.set_ylim(5,65)
    # plt.legend()

    # G3 = plt.subplot(2,2,3)
    # plt.title('Centro oeste', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'lula_coeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_coeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'lula_coeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G3.set_ylim(5,65)
    # plt.legend()

    # G4 = plt.subplot(2,2,4)
    # plt.title('Sul', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'lula_sul_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_sul_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'lula_sul_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(5,65)
    # plt.legend()
  
    # plt.show()

    df = pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
            'ciro_sudeste_dtfolha': models.data_reader.candidates[i_ciro].dfolha_sudeste, 'ciro_nordeste_dtfolha': models.data_reader.candidates[i_ciro].dfolha_nordeste,
            'ciro_coeste_dtfolha': models.data_reader.candidates[i_ciro].dfolha_norte_coeste, 'ciro_sul_dtfolha': models.data_reader.candidates[i_ciro].dfolha_sul,

            'ciro_sudeste_ibope': models.data_reader.candidates[i_ciro].ibope_sudeste, 'ciro_nordeste_ibope': models.data_reader.candidates[i_ciro].ibope_nordeste,
            'ciro_coeste_ibope': models.data_reader.candidates[i_ciro].ibope_norte_coeste, 'ciro_sul_ibope': models.data_reader.candidates[i_ciro].ibope_sul,
           
            'ciro_sudeste_facebook': models.data_reader.candidates[i_ciro].facebook_sudeste, 'ciro_sul_facebook': models.data_reader.candidates[i_ciro].facebook_sul,
            'ciro_coeste_facebook': models.data_reader.candidates[i_ciro].facebook_norte_coeste, 'ciro_nordeste_facebook': models.data_reader.candidates[i_ciro].facebook_nordeste
        })
    
    count_x = len(models.data_reader.candidates[i_lula].dfolha_male)

    # Ciro Gomes    
    plt.suptitle('Ciro Gomes')  
    G1 = plt.subplot(2,2,1)
    plt.title('Sudeste', fontsize=12, color='black', loc='center')
    plt.plot('x', 'ciro_sudeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'ciro_sudeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'ciro_sudeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G1.set_ylim(5,75)
    plt.legend()

    G2 = plt.subplot(2,2,2)
    plt.title('Nordeste', fontsize=12, color='black', loc='center')
    plt.plot('x', 'ciro_nordeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'ciro_nordeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'ciro_nordeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G2.set_ylim(5,65)
    plt.legend()

    G3 = plt.subplot(2,2,3)
    plt.title('Centro oeste', fontsize=12, color='black', loc='center')
    plt.plot('x', 'ciro_coeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'ciro_coeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    plt.plot('x', 'ciro_coeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G3.set_ylim(5,65)
    plt.legend()

    G4 = plt.subplot(2,2,4)
    plt.title('Sul', fontsize=12, color='black', loc='center')
    plt.plot('x', 'ciro_sul_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'ciro_sul_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    plt.plot('x', 'ciro_sul_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G4.set_ylim(5,65)
    plt.legend()
  
    plt.show()

def plot_like():
    yticks = [0,1,2,3,4,5,6,7,8]
    
    df = pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].facebook_likes)), 
            'bolsonaro_like': models.data_reader.candidates[i_bolsonaro].facebook_likes, 'ciro_like': models.data_reader.candidates[i_ciro].facebook_likes,
            'haddad_like': models.data_reader.candidates[i_haddad].facebook_likes, 'marina_like': models.data_reader.candidates[i_marina].facebook_likes,
            'alckmin_like': models.data_reader.candidates[i_alckmin].facebook_likes, 'lula_like': models.data_reader.candidates[i_lula].facebook_likes
        })

    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_likes)

    plt.suptitle('Nº Likes')  
    G1 = plt.subplot(1,1,1)
    plt.plot('x', 'bolsonaro_like', data=df, marker='o', color="green", ls='-', alpha=0.4, label='Jair Bolsonaro')
    plt.plot('x', 'haddad_like', data=df, marker='o', color="red", alpha=0.4, label='Fernando Haddad')  
    plt.plot('x', 'ciro_like', data=df, marker='o', color="orange", alpha=0.4, label='Ciro Gomes')
    plt.plot('x', 'alckmin_like', data=df, marker='o', color="blue", alpha=0.4, label='Alckmin')
    plt.plot('x', 'marina_like', data=df, marker='o', color="black", alpha=0.4, label='Marina Silva')
    plt.plot('x', 'lula_like', data=df, marker='o', color="brown", alpha=0.4, label='Lula')
    
    plt.xticks(range(0, count_x), xticks)
    G1.set_ylim(0,8500000)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.11),
          fancybox=True, shadow=True, ncol=5)

    plt.show()

def talking_about():
    
    df = pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].facebook_talking_about)), 
            'bolsonaro_talking': models.data_reader.candidates[i_bolsonaro].facebook_talking_about, 'ciro_talking': models.data_reader.candidates[i_ciro].facebook_talking_about,
            'haddad_talking': models.data_reader.candidates[i_haddad].facebook_talking_about, 'marina_talking': models.data_reader.candidates[i_marina].facebook_talking_about,
            'alckmin_talking': models.data_reader.candidates[i_alckmin].facebook_talking_about, 'lula_talking': models.data_reader.candidates[i_lula].facebook_talking_about
        })

    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_talking_about)

    plt.suptitle('Talking About')  
    G1 = plt.subplot(1,1,1)
    plt.plot('x', 'bolsonaro_talking', data=df, marker='o', color="green", ls='-', alpha=0.4, label='Jair Bolsonaro')
    plt.plot('x', 'haddad_talking', data=df, marker='o', color="red", alpha=0.4, label='Fernando Haddad')  
    plt.plot('x', 'ciro_talking', data=df, marker='o', color="orange", alpha=0.4, label='Ciro Gomes')
    plt.plot('x', 'alckmin_talking', data=df, marker='o', color="blue", alpha=0.4, label='Alckmin')
    plt.plot('x', 'marina_talking', data=df, marker='o', color="black", alpha=0.4, label='Marina Silva')
    plt.plot('x', 'lula_talking', data=df, marker='o', color="brown", alpha=0.4, label='Lula')
    
    plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(0,8500000)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
          fancybox=True, shadow=True, ncol=5)

    plt.show()

def plot_age():
    # df = pd.DataFrame(
    #     {
    #         'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
    #         'bolsonaro_16a24_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_16a24, 'bolsonaro_35a44_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_35a44,
    #         'bolsonaro_25a34_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_25a34, 'bolsonaro_45a54_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_45a54,
    #         'bolsonaro_acima55_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_55,

    #         'bolsonaro_16a24_ibope': models.data_reader.candidates[i_bolsonaro].ibope_16a24, 'bolsonaro_35a44_ibope': models.data_reader.candidates[i_bolsonaro].ibope_35a44,
    #         'bolsonaro_25a34_ibope': models.data_reader.candidates[i_bolsonaro].ibope_25a34, 'bolsonaro_45a54_ibope': models.data_reader.candidates[i_bolsonaro].ibope_45a54,
    #         'bolsonaro_acima55_ibope': models.data_reader.candidates[i_bolsonaro].ibope_55,
           
    #         'bolsonaro_16a24_facebook': models.data_reader.candidates[i_bolsonaro].facebook_16a24, 'bolsonaro_35a44_facebook': models.data_reader.candidates[i_bolsonaro].facebook_35a44,
    #         'bolsonaro_25a34_facebook': models.data_reader.candidates[i_bolsonaro].facebook_25a34, 'bolsonaro_45a54_facebook': models.data_reader.candidates[i_bolsonaro].facebook_45a54,
    #         'bolsonaro_acima55_facebook': models.data_reader.candidates[i_bolsonaro].facebook_55
    #     })
    
    # count_x = len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)

    # # Jair Bolsonaro    
    # plt.suptitle('Jair Bolsonaro')  
    # G1 = plt.subplot(3,2,1)
    # plt.title('16 a 24', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'bolsonaro_16a24_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'bolsonaro_16a24_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'bolsonaro_16a24_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(0,60)
    # plt.legend()

    # G2 = plt.subplot(3,2,2)
    # plt.title('25 a 34', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'bolsonaro_25a34_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'bolsonaro_25a34_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'bolsonaro_25a34_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G2.set_ylim(0,60)
    # plt.legend()

    # G3 = plt.subplot(3,2,3)
    # plt.title('35 a 44', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'bolsonaro_35a44_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'bolsonaro_35a44_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'bolsonaro_35a44_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G3.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,4)
    # plt.title('45 a 54', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'bolsonaro_45a54_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'bolsonaro_45a54_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'bolsonaro_45a54_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,5)
    # plt.title('Acima 55', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'bolsonaro_acima55_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'bolsonaro_acima55_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'bolsonaro_acima55_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()
  
    # plt.show()

    # df = pd.DataFrame(
    #     {
    #         'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
    #         'haddad_16a24_dtfolha': models.data_reader.candidates[i_haddad].dfolha_16a24, 'haddad_35a44_dtfolha': models.data_reader.candidates[i_haddad].dfolha_35a44,
    #         'haddad_25a34_dtfolha': models.data_reader.candidates[i_haddad].dfolha_25a34, 'haddad_45a54_dtfolha': models.data_reader.candidates[i_haddad].dfolha_45a54,
    #         'haddad_acima55_dtfolha': models.data_reader.candidates[i_haddad].dfolha_55,

    #         'haddad_16a24_ibope': models.data_reader.candidates[i_haddad].ibope_16a24, 'haddad_35a44_ibope': models.data_reader.candidates[i_haddad].ibope_35a44,
    #         'haddad_25a34_ibope': models.data_reader.candidates[i_haddad].ibope_25a34, 'haddad_45a54_ibope': models.data_reader.candidates[i_haddad].ibope_45a54,
    #         'haddad_acima55_ibope': models.data_reader.candidates[i_haddad].ibope_55,
           
    #         'haddad_16a24_facebook': models.data_reader.candidates[i_haddad].facebook_16a24, 'haddad_35a44_facebook': models.data_reader.candidates[i_haddad].facebook_35a44,
    #         'haddad_25a34_facebook': models.data_reader.candidates[i_haddad].facebook_25a34, 'haddad_45a54_facebook': models.data_reader.candidates[i_haddad].facebook_45a54,
    #         'haddad_acima55_facebook': models.data_reader.candidates[i_haddad].facebook_55
    #     })
    
    # count_x = len(models.data_reader.candidates[i_haddad].dfolha_16a24)

    # # Fernando Haddad    
    # plt.suptitle('Fernando Haddad')  
    # G1 = plt.subplot(3,2,1)
    # plt.title('16 a 24', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'haddad_16a24_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'haddad_16a24_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'haddad_16a24_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(0,60)
    # plt.legend()

    # G2 = plt.subplot(3,2,2)
    # plt.title('25 a 34', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'haddad_25a34_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'haddad_25a34_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'haddad_25a34_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G2.set_ylim(0,60)
    # plt.legend()

    # G3 = plt.subplot(3,2,3)
    # plt.title('35 a 44', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'haddad_35a44_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'haddad_35a44_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'haddad_35a44_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G3.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,4)
    # plt.title('45 a 54', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'haddad_45a54_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'haddad_45a54_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'haddad_45a54_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,5)
    # plt.title('Acima 55', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'haddad_acima55_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'haddad_acima55_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'haddad_acima55_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()
  
    # plt.show()

    # df = pd.DataFrame(
    #     {
    #         'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
    #         'ciro_16a24_dtfolha': models.data_reader.candidates[i_ciro].dfolha_16a24, 'ciro_35a44_dtfolha': models.data_reader.candidates[i_ciro].dfolha_35a44,
    #         'ciro_25a34_dtfolha': models.data_reader.candidates[i_ciro].dfolha_25a34, 'ciro_45a54_dtfolha': models.data_reader.candidates[i_ciro].dfolha_45a54,
    #         'ciro_acima55_dtfolha': models.data_reader.candidates[i_ciro].dfolha_55,

    #         'ciro_16a24_ibope': models.data_reader.candidates[i_ciro].ibope_16a24, 'ciro_35a44_ibope': models.data_reader.candidates[i_ciro].ibope_35a44,
    #         'ciro_25a34_ibope': models.data_reader.candidates[i_ciro].ibope_25a34, 'ciro_45a54_ibope': models.data_reader.candidates[i_ciro].ibope_45a54,
    #         'ciro_acima55_ibope': models.data_reader.candidates[i_ciro].ibope_55,
           
    #         'ciro_16a24_facebook': models.data_reader.candidates[i_ciro].facebook_16a24, 'ciro_35a44_facebook': models.data_reader.candidates[i_ciro].facebook_35a44,
    #         'ciro_25a34_facebook': models.data_reader.candidates[i_ciro].facebook_25a34, 'ciro_45a54_facebook': models.data_reader.candidates[i_ciro].facebook_45a54,
    #         'ciro_acima55_facebook': models.data_reader.candidates[i_ciro].facebook_55
    #     })
    
    # count_x = len(models.data_reader.candidates[i_ciro].dfolha_16a24)

    # # Ciro Gomes    
    # plt.suptitle('Ciro Gomes')  
    # G1 = plt.subplot(3,2,1)
    # plt.title('16 a 24', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'ciro_16a24_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'ciro_16a24_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'ciro_16a24_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(0,60)
    # plt.legend()

    # G2 = plt.subplot(3,2,2)
    # plt.title('25 a 34', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'ciro_25a34_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'ciro_25a34_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'ciro_25a34_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G2.set_ylim(0,60)
    # plt.legend()

    # G3 = plt.subplot(3,2,3)
    # plt.title('35 a 44', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'ciro_35a44_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'ciro_35a44_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'ciro_35a44_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G3.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,4)
    # plt.title('45 a 54', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'ciro_45a54_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'ciro_45a54_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'ciro_45a54_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,5)
    # plt.title('Acima 55', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'ciro_acima55_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'ciro_acima55_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'ciro_acima55_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()
  
    # plt.show()

    # df = pd.DataFrame(
    #     {
    #         'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
    #         'lula_16a24_dtfolha': models.data_reader.candidates[i_lula].dfolha_16a24, 'lula_35a44_dtfolha': models.data_reader.candidates[i_lula].dfolha_35a44,
    #         'lula_25a34_dtfolha': models.data_reader.candidates[i_lula].dfolha_25a34, 'lula_45a54_dtfolha': models.data_reader.candidates[i_lula].dfolha_45a54,
    #         'lula_acima55_dtfolha': models.data_reader.candidates[i_lula].dfolha_55,

    #         'lula_16a24_ibope': models.data_reader.candidates[i_lula].ibope_16a24, 'lula_35a44_ibope': models.data_reader.candidates[i_lula].ibope_35a44,
    #         'lula_25a34_ibope': models.data_reader.candidates[i_lula].ibope_25a34, 'lula_45a54_ibope': models.data_reader.candidates[i_lula].ibope_45a54,
    #         'lula_acima55_ibope': models.data_reader.candidates[i_lula].ibope_55,
           
    #         'lula_16a24_facebook': models.data_reader.candidates[i_lula].facebook_16a24, 'lula_35a44_facebook': models.data_reader.candidates[i_lula].facebook_35a44,
    #         'lula_25a34_facebook': models.data_reader.candidates[i_lula].facebook_25a34, 'lula_45a54_facebook': models.data_reader.candidates[i_lula].facebook_45a54,
    #         'lula_acima55_facebook': models.data_reader.candidates[i_lula].facebook_55
    #     })
    
    # count_x = len(models.data_reader.candidates[i_lula].dfolha_16a24)

    # # Ciro Gomes    
    # plt.suptitle('Lula')  
    # G1 = plt.subplot(3,2,1)
    # plt.title('16 a 24', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'lula_16a24_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_16a24_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'lula_16a24_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(0,60)
    # plt.legend()

    # G2 = plt.subplot(3,2,2)
    # plt.title('25 a 34', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'lula_25a34_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_25a34_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'lula_25a34_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G2.set_ylim(0,60)
    # plt.legend()

    # G3 = plt.subplot(3,2,3)
    # plt.title('35 a 44', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'lula_35a44_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_35a44_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'lula_35a44_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G3.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,4)
    # plt.title('45 a 54', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'lula_45a54_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_45a54_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'lula_45a54_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,5)
    # plt.title('Acima 55', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'lula_acima55_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_acima55_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'lula_acima55_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()
  
    # plt.show()

    # df = pd.DataFrame(
    #     {
    #         'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
    #         'marina_16a24_dtfolha': models.data_reader.candidates[i_marina].dfolha_16a24, 'marina_35a44_dtfolha': models.data_reader.candidates[i_marina].dfolha_35a44,
    #         'marina_25a34_dtfolha': models.data_reader.candidates[i_marina].dfolha_25a34, 'marina_45a54_dtfolha': models.data_reader.candidates[i_marina].dfolha_45a54,
    #         'marina_acima55_dtfolha': models.data_reader.candidates[i_marina].dfolha_55,

    #         'marina_16a24_ibope': models.data_reader.candidates[i_marina].ibope_16a24, 'marina_35a44_ibope': models.data_reader.candidates[i_marina].ibope_35a44,
    #         'marina_25a34_ibope': models.data_reader.candidates[i_marina].ibope_25a34, 'marina_45a54_ibope': models.data_reader.candidates[i_marina].ibope_45a54,
    #         'marina_acima55_ibope': models.data_reader.candidates[i_marina].ibope_55,
           
    #         'marina_16a24_facebook': models.data_reader.candidates[i_marina].facebook_16a24, 'marina_35a44_facebook': models.data_reader.candidates[i_marina].facebook_35a44,
    #         'marina_25a34_facebook': models.data_reader.candidates[i_marina].facebook_25a34, 'marina_45a54_facebook': models.data_reader.candidates[i_marina].facebook_45a54,
    #         'marina_acima55_facebook': models.data_reader.candidates[i_marina].facebook_55
    #     })
    
    # count_x = len(models.data_reader.candidates[i_marina].dfolha_16a24)

    # # Marina Silva 
    # plt.suptitle('Marina Silva')  
    # G1 = plt.subplot(3,2,1)
    # plt.title('16 a 24', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'marina_16a24_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'marina_16a24_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'marina_16a24_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(0,60)
    # plt.legend()

    # G2 = plt.subplot(3,2,2)
    # plt.title('25 a 34', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'marina_25a34_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'marina_25a34_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'marina_25a34_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G2.set_ylim(0,60)
    # plt.legend()

    # G3 = plt.subplot(3,2,3)
    # plt.title('35 a 44', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'marina_35a44_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'marina_35a44_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'marina_35a44_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G3.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,4)
    # plt.title('45 a 54', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'marina_45a54_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'marina_45a54_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'marina_45a54_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()

    # G4 = plt.subplot(3,2,5)
    # plt.title('Acima 55', fontsize=12, color='black', loc='center')
    # plt.plot('x', 'marina_acima55_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'marina_acima55_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'marina_acima55_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,60)
    # plt.legend()
  
    # plt.show()

    df = pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
            'alckmin_16a24_dtfolha': models.data_reader.candidates[i_alckmin].dfolha_16a24, 'alckmin_35a44_dtfolha': models.data_reader.candidates[i_alckmin].dfolha_35a44,
            'alckmin_25a34_dtfolha': models.data_reader.candidates[i_alckmin].dfolha_25a34, 'alckmin_45a54_dtfolha': models.data_reader.candidates[i_alckmin].dfolha_45a54,
            'alckmin_acima55_dtfolha': models.data_reader.candidates[i_alckmin].dfolha_55,

            'alckmin_16a24_ibope': models.data_reader.candidates[i_alckmin].ibope_16a24, 'alckmin_35a44_ibope': models.data_reader.candidates[i_alckmin].ibope_35a44,
            'alckmin_25a34_ibope': models.data_reader.candidates[i_alckmin].ibope_25a34, 'alckmin_45a54_ibope': models.data_reader.candidates[i_alckmin].ibope_45a54,
            'alckmin_acima55_ibope': models.data_reader.candidates[i_alckmin].ibope_55,
           
            'alckmin_16a24_facebook': models.data_reader.candidates[i_alckmin].facebook_16a24, 'alckmin_35a44_facebook': models.data_reader.candidates[i_alckmin].facebook_35a44,
            'alckmin_25a34_facebook': models.data_reader.candidates[i_alckmin].facebook_25a34, 'alckmin_45a54_facebook': models.data_reader.candidates[i_alckmin].facebook_45a54,
            'alckmin_acima55_facebook': models.data_reader.candidates[i_alckmin].facebook_55
        })
    
    count_x = len(models.data_reader.candidates[i_alckmin].dfolha_16a24)

    # Marina Silva 
    plt.suptitle('Geraldo Alckmin')  
    G1 = plt.subplot(3,2,1)
    plt.title('16 a 24', fontsize=12, color='black', loc='center')
    plt.plot('x', 'alckmin_16a24_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'alckmin_16a24_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'alckmin_16a24_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G1.set_ylim(0,60)
    plt.legend()

    G2 = plt.subplot(3,2,2)
    plt.title('25 a 34', fontsize=12, color='black', loc='center')
    plt.plot('x', 'alckmin_25a34_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'alckmin_25a34_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'alckmin_25a34_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G2.set_ylim(0,60)
    plt.legend()

    G3 = plt.subplot(3,2,3)
    plt.title('35 a 44', fontsize=12, color='black', loc='center')
    plt.plot('x', 'alckmin_35a44_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'alckmin_35a44_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    plt.plot('x', 'alckmin_35a44_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G3.set_ylim(0,60)
    plt.legend()

    G4 = plt.subplot(3,2,4)
    plt.title('45 a 54', fontsize=12, color='black', loc='center')
    plt.plot('x', 'alckmin_45a54_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'alckmin_45a54_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    plt.plot('x', 'alckmin_45a54_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G4.set_ylim(0,60)
    plt.legend()

    G4 = plt.subplot(3,2,5)
    plt.title('Acima 55', fontsize=12, color='black', loc='center')
    plt.plot('x', 'alckmin_acima55_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'alckmin_acima55_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    plt.plot('x', 'alckmin_acima55_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G4.set_ylim(0,60)
    plt.legend()
  
    plt.show()

def plot_education():
    df = pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
            '17_fundamental_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_fundamental, '17_medio_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_medio,
            '17_fundamental_ibope': models.data_reader.candidates[i_bolsonaro].ibope_fundamental, '17_medio_ibope': models.data_reader.candidates[i_bolsonaro].ibope_medio,
            '17_superior_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_superior, '17_superior_ibope': models.data_reader.candidates[i_bolsonaro].ibope_superior,

            '13_fundamental_dtfolha': models.data_reader.candidates[i_haddad].dfolha_fundamental, '13_medio_dtfolha': models.data_reader.candidates[i_haddad].dfolha_medio,
            '13_fundamental_ibope': models.data_reader.candidates[i_haddad].ibope_fundamental, '13_medio_ibope': models.data_reader.candidates[i_haddad].ibope_medio,
            '13_superior_dtfolha': models.data_reader.candidates[i_haddad].dfolha_superior, '13_superior_ibope': models.data_reader.candidates[i_haddad].ibope_superior,

            'lula_fundamental_dtfolha': models.data_reader.candidates[i_lula].dfolha_fundamental, 'lula_medio_dtfolha': models.data_reader.candidates[i_lula].dfolha_medio,
            'lula_fundamental_ibope': models.data_reader.candidates[i_lula].ibope_fundamental, 'lula_medio_ibope': models.data_reader.candidates[i_lula].ibope_medio,
            'lula_superior_dtfolha': models.data_reader.candidates[i_lula].dfolha_superior, 'lula_superior_ibope': models.data_reader.candidates[i_lula].ibope_superior,

            'ciro_fundamental_dtfolha': models.data_reader.candidates[i_ciro].dfolha_fundamental, 'ciro_medio_dtfolha': models.data_reader.candidates[i_ciro].dfolha_medio,
            'ciro_fundamental_ibope': models.data_reader.candidates[i_ciro].ibope_fundamental, 'ciro_medio_ibope': models.data_reader.candidates[i_ciro].ibope_medio,
            'ciro_superior_dtfolha': models.data_reader.candidates[i_ciro].dfolha_superior, 'ciro_superior_ibope': models.data_reader.candidates[i_ciro].ibope_superior,

            'marina_fundamental_dtfolha': models.data_reader.candidates[i_marina].dfolha_fundamental, 'marina_medio_dtfolha': models.data_reader.candidates[i_marina].dfolha_medio,
            'marina_fundamental_ibope': models.data_reader.candidates[i_marina].ibope_fundamental, 'marina_medio_ibope': models.data_reader.candidates[i_marina].ibope_medio,
            'marina_superior_dtfolha': models.data_reader.candidates[i_marina].dfolha_superior, 'marina_superior_ibope': models.data_reader.candidates[i_marina].ibope_superior,

            'alckmin_fundamental_dtfolha': models.data_reader.candidates[i_alckmin].dfolha_fundamental, 'alckmin_medio_dtfolha': models.data_reader.candidates[i_alckmin].dfolha_medio,
            'alckmin_fundamental_ibope': models.data_reader.candidates[i_alckmin].ibope_fundamental, 'alckmin_medio_ibope': models.data_reader.candidates[i_alckmin].ibope_medio,
            'alckmin_superior_dtfolha': models.data_reader.candidates[i_alckmin].dfolha_superior, 'alckmin_superior_ibope': models.data_reader.candidates[i_alckmin].ibope_superior,

            '17_fundamental_facebook': models.data_reader.candidates[i_bolsonaro].facebook_fundamental, '17_medio_facebook': models.data_reader.candidates[i_bolsonaro].facebook_medio,
            '17_superior_facebook': models.data_reader.candidates[i_bolsonaro].facebook_superior,

            '13_fundamental_facebook': models.data_reader.candidates[i_haddad].facebook_fundamental, '13_medio_facebook': models.data_reader.candidates[i_haddad].facebook_medio,
            '13_superior_facebook': models.data_reader.candidates[i_haddad].facebook_superior,

            'lula_fundamental_facebook': models.data_reader.candidates[i_lula].facebook_fundamental, 'lula_medio_facebook': models.data_reader.candidates[i_lula].facebook_medio,
            'lula_superior_facebook': models.data_reader.candidates[i_lula].facebook_superior,

            'ciro_fundamental_facebook': models.data_reader.candidates[i_ciro].facebook_fundamental, 'ciro_medio_facebook': models.data_reader.candidates[i_ciro].facebook_medio,
            'ciro_superior_facebook': models.data_reader.candidates[i_ciro].facebook_superior,

            'marina_fundamental_facebook': models.data_reader.candidates[i_marina].facebook_fundamental, 'marina_medio_facebook': models.data_reader.candidates[i_marina].facebook_medio,
            'marina_superior_facebook': models.data_reader.candidates[i_marina].facebook_superior,

            'alckmin_fundamental_facebook': models.data_reader.candidates[i_alckmin].facebook_fundamental, 'alckmin_medio_facebook': models.data_reader.candidates[i_alckmin].facebook_medio,
            'alckmin_superior_facebook': models.data_reader.candidates[i_alckmin].facebook_superior,
        })
    
    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_fundamental)

    # # Jair Bolsonaro
    # plt.suptitle('Education')  
    # G1 = plt.subplot(3,3,1)
    # plt.ylabel('Jair Bolsonaro', multialignment='center', color='gray', fontsize=12)
    # plt.title('Nível Fundamental', fontsize=12, color='black', loc='center')
    # plt.plot('x', '17_fundamental_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '17_fundamental_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', '17_fundamental_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G1.set_ylim(0,75)
    # plt.legend()

    # G2 = plt.subplot(3,3,2)
    # plt.title('Nível Médio', fontsize=12, color='black', loc='center')
    # plt.plot('x', '17_medio_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '17_medio_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', '17_medio_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G2.set_ylim(0,75)
    # plt.legend()

    # G3 = plt.subplot(3,3,3)
    # plt.title('Nível Superior', fontsize=12, color='black', loc='center')
    # plt.plot('x', '17_superior_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '17_superior_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', '17_superior_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G3.set_ylim(0,75)
    # plt.legend()
  
    # # Fernando Haddad  
    # G4 = plt.subplot(3,3,4)
    # plt.ylabel('Fernando Haddad', multialignment='center', color='gray', fontsize=12)
    # plt.plot('x', '13_fundamental_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '13_fundamental_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', '13_fundamental_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G4.set_ylim(0,75)
    # plt.legend()

    # G5 = plt.subplot(3,3,5)
    # plt.plot('x', '13_medio_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '13_medio_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', '13_medio_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G5.set_ylim(0,75)
    # plt.legend()

    # G6 = plt.subplot(3,3,6)
    # plt.plot('x', '13_superior_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', '13_superior_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', '13_superior_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G6.set_ylim(0,75)
    # plt.legend()
  
    # # Ciro Gomes
    # G7 = plt.subplot(3,3,7)
    # plt.ylabel('Lula', multialignment='center', color='gray', fontsize=12)
    # plt.plot('x', 'lula_fundamental_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_fundamental_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'lula_fundamental_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    # plt.xticks(range(0, count_x), xticks)
    # G7.set_ylim(0,75)
    # plt.legend()

    # G8 = plt.subplot(3,3,8)
    # plt.plot('x', 'lula_medio_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_medio_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    # plt.plot('x', 'lula_medio_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G8.set_ylim(0,75)
    # plt.legend()

    # G9 = plt.subplot(3,3,9)
    # plt.plot('x', 'lula_superior_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    # plt.plot('x', 'lula_superior_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    # plt.plot('x', 'lula_superior_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    # plt.xticks(range(0, count_x), xticks)
    # G9.set_ylim(0,75)
    # plt.legend()
  
    # plt.show()


    # Ciro Gomes
    plt.suptitle('Education')  
    G1 = plt.subplot(3,3,1)
    plt.ylabel('Ciro Gomes', multialignment='center', color='gray', fontsize=12)
    plt.title('Nível Fundamental', fontsize=12, color='black', loc='center')
    plt.plot('x', 'ciro_fundamental_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'ciro_fundamental_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'ciro_fundamental_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G1.set_ylim(0,75)
    plt.legend()

    G2 = plt.subplot(3,3,2)
    plt.title('Nível Médio', fontsize=12, color='black', loc='center')
    plt.plot('x', 'ciro_medio_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'ciro_medio_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'ciro_medio_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G2.set_ylim(0,75)
    plt.legend()

    G3 = plt.subplot(3,3,3)
    plt.title('Nível Superior', fontsize=12, color='black', loc='center')
    plt.plot('x', 'ciro_superior_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'ciro_superior_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    plt.plot('x', 'ciro_superior_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G3.set_ylim(0,75)
    plt.legend()
  
    # Fernando Haddad  
    G4 = plt.subplot(3,3,4)
    plt.ylabel('Marina Silva', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', 'marina_fundamental_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'marina_fundamental_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'marina_fundamental_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G4.set_ylim(0,75)
    plt.legend()

    G5 = plt.subplot(3,3,5)
    plt.plot('x', 'marina_medio_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'marina_medio_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'marina_medio_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G5.set_ylim(0,75)
    plt.legend()

    G6 = plt.subplot(3,3,6)
    plt.plot('x', 'marina_superior_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'marina_superior_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    plt.plot('x', 'marina_superior_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G6.set_ylim(0,75)
    plt.legend()
  
    # Ciro Gomes
    G7 = plt.subplot(3,3,7)
    plt.ylabel('Geraldo Alckmin', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', 'alckmin_fundamental_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'alckmin_fundamental_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'alckmin_fundamental_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G7.set_ylim(0,75)
    plt.legend()

    G8 = plt.subplot(3,3,8)
    plt.plot('x', 'alckmin_medio_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'alckmin_medio_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  
    plt.plot('x', 'alckmin_medio_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G8.set_ylim(0,75)
    plt.legend()

    G9 = plt.subplot(3,3,9)
    plt.plot('x', 'alckmin_superior_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'alckmin_superior_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE') 
    plt.plot('x', 'alckmin_superior_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G9.set_ylim(0,75)
    plt.legend()
    
    # for i in range(len(r4)):
    # plt.text(x = 2 , y = 50, s = 't', size = 6)
    # plt.style.use('seaborn-darkgrid')
    # plt.savefig('PNG/#199_Matplotlib_style_sheet.png', dpi=96, bbox_inches='tight')


    plt.show()