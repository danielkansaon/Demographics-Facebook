import matplotlib.pyplot as plt
import read_facebook as facebook
import read_elections as election
import pandas as pd
import models

# xticks_facebook = ["17-11",  "18-07",  "08-06",  "09-10",  "09-17",  "09-24",  "10-01",  "10-05", "10-06", "10-08", "10-15",  "10-22",  "10-26", "10-27", "10-29"]
# xticks_dataf = ["17-11-30",  "06-07",  "08-21",  "09-10",  "09-18",  "09-28",  "10-02",  "10-04", "10-06", "10-07", "10-10", "10-18",  "10-25",  "10-27", "10-28"]
# xticks_ibope = ["17-10-22",  "06-24",  "08-19",  "09-10",  "09-18",  "09-24",  "09-30",  "10-02", "10-06", "10-07", "10-07", "10-14",  "10-23",  "10-27", "10-28"]

xticks = ["17\n11",  "18\n07",  "08\n06",  "09\n10",  "09\n17",  "09\n24",  "10\n01",  "10\n05", "10\n06",  "10\n08",  "10\n15",  "10\n22",  "10\n26", "10\n27",  "10\n29"]

i_bolsonaro = models.return_index("Jair Bolsonaro")
i_haddad = models.return_index("Fernando Haddad")
i_lula = models.return_index("Lula")
i_ciro = models.return_index("Ciro Gomes")

def plot_gender():
    facebook.readJson() 

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
    facebook.readJson() 
    
    df = pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
            '17_sudeste_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_sudeste, '17_nordeste_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_nordeste,
            '17_coeste_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_norte_coeste, '17_sul_dtfolha': models.data_reader.candidates[i_bolsonaro].dfolha_sul,

            '17_sudeste_ibope': models.data_reader.candidates[i_bolsonaro].ibope_sudeste, '17_nordeste_ibope': models.data_reader.candidates[i_bolsonaro].ibope_nordeste,
            '17_coeste_ibope': models.data_reader.candidates[i_bolsonaro].ibope_norte_coeste, '17_sul_ibope': models.data_reader.candidates[i_bolsonaro].ibope_sul,
           
            '17_sudeste_facebook': models.data_reader.candidates[i_bolsonaro].facebook_sudeste, '17_sul_facebook': models.data_reader.candidates[i_bolsonaro].facebook_sul,
            '17_coeste_facebook': models.data_reader.candidates[i_bolsonaro].facebook_norte_coeste, '17_nordeste_facebook': models.data_reader.candidates[i_bolsonaro].facebook_nordeste
        })
    
    count_x = len(models.data_reader.candidates[0].dfolha_male)

    G1 = plt.subplot(2,2,1)
    plt.title('Sudeste', fontsize=12, color='gray', loc='center')
    plt.ylabel('Jair Bolsonaro', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', '17_sudeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_sudeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  #linestyle='dashed' (--)
    plt.plot('x', '17_sudeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G1.set_ylim(5,65)
    plt.legend()

    G2 = plt.subplot(2,2,2)
    plt.title('Nordeste', fontsize=12, color='gray', loc='center')
    plt.ylabel('Jair Bolsonaro', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', '17_nordeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_nordeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  #linestyle='dashed' (--)
    plt.plot('x', '17_nordeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G2.set_ylim(5,65)
    plt.legend()

    G3 = plt.subplot(2,2,3)
    plt.title('Centro oeste', fontsize=12, color='gray', loc='center')
    plt.ylabel('Jair Bolsonaro', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', '17_coeste_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_coeste_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  #linestyle='dashed' (--)
    plt.plot('x', '17_coeste_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G3.set_ylim(5,65)
    plt.legend()

    G4 = plt.subplot(2,2,4)
    plt.title('Sul', fontsize=12, color='gray', loc='center')
    plt.ylabel('Jair Bolsonaro', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', '17_sul_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_sul_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  #linestyle='dashed' (--)
    plt.plot('x', '17_sul_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G4.set_ylim(5,65)
    plt.legend()

    plt.suptitle('Region')
    plt.show()
