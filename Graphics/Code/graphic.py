import matplotlib.pyplot as plt
import read_facebook as facebook
import read_elections as election
import pandas as pd

xticks_DataFolha = ["17-11",  "18-07",  "08-06",  "09-10",  "09-17",  "09-24",  "10-01",  "10-05",  "10-08",  "10-15",  "10-22",  "10-26",  "10-29"]
xticks_Ibope = ["17-11",  "18-07",  "08-06",  "09-10",  "09-17",  "09-24",  "10-01",  "10-05",  "10-08",  "10-15",  "10-22",  "10-26",  "10-29"]

def plot_gender():
    facebook.readJson()

    df = pd.DataFrame(
        {
            'x': range(0, len(election.vec_dfolha_17_male)), 
            '17_male_dtfolha': election.vec_dfolha_17_male, '17_female_dtfolha': election.vec_dfolha_17_female,
            '17_male_ibope': election.vec_ibope_17_male, '17_female_ibope': election.vec_ibope_17_female,
            '13_male_dtfolha': election.vec_dfolha_13_male, '13_female_dtfolha': election.vec_dfolha_13_female,
            '13_male_ibope': election.vec_ibope_13_male, '13_female_ibope': election.vec_ibope_13_female,
            '17_male_facebook': facebook.vec_facebook_17_male, '17_female_facebook': facebook.vec_facebook_17_female,
            '13_male_facebook': facebook.vec_facebook_13_male, '13_female_facebook': facebook.vec_facebook_13_female,
            'lula_male_facebook': facebook.vec_facebook_lula_male, 'lula_female_facebook': facebook.vec_facebook_lula_female
        })

    count_x = len(election.vec_dfolha_17_male)

    G1 = plt.subplot(221)
    plt.title('Male', fontsize=12, color='gray', loc='center')
    plt.plot('x', '17_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_male_ibope', data=df, marker='o', color="red", linestyle='dashed', alpha=0.4, label='IBOPE')
    plt.plot('x', '17_male_facebook', data=df, marker='o', color="blue", alpha=0.4)
    plt.xticks(range(0, count_x), xticks_DataFolha)
    G1.set_ylim(15,75)

    G2 = plt.subplot(222)
    plt.title('Female', fontsize=12, color='gray', loc='center')
    plt.plot('x', '17_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', '17_female_facebook', data=df, marker='o', color="blue", alpha=0.4)
    plt.xticks(range(0, count_x), xticks_Ibope)
    G2.set_ylim(15,75)

    G3 = plt.subplot(223)
    plt.plot('x', '13_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '13_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', '13_male_facebook', data=df, marker='o', color="blue", alpha=0.4)
    plt.xticks(range(0, count_x), xticks_DataFolha)
    G3.set_ylim(15,75)

    G4 = plt.subplot(224)
    plt.plot('x', '13_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '13_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', '13_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks_Ibope)
    G4.set_ylim(15,75)
    plt.legend()

    plt.suptitle('Gender')
    plt.show()

    
# 2 partes
# G1 = plt.subplot(221)
# plt.title('Jair Bolsonaro', fontsize=12, color='gray', loc='center')
# plt.plot('x', '17_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.5, label='DataFolha')
# plt.plot('x', '17_male_ibope', data=df, marker='o', color="green", linestyle='dashed', alpha=0.4, label='IBOPE')
# plt.plot('x', '17_female_dtfolha', data=df, marker='o', color="red", ls='-', alpha=0.4)
# plt.plot('x', '17_female_ibope', data=df, marker='o', color="red", linestyle='dashed', alpha=0.4)
# plt.plot('x', '17_male_facebook', data=df, marker='o', color="blue", alpha=0.4)
# plt.plot('x', '17_female_facebook', data=df, marker='o', color="blue", linestyle='dashed', alpha=0.4)
# plt.xticks(range(0, len(axisY_DFolha_17_male)), xticks_DataFolha)
# G1.set_ylim(35,65)

# G2 = plt.subplot(222)
# plt.title('Fernando Haddad', fontsize=12, color='gray', loc='center')
# plt.plot('x', '13_male_dtfolha', data=df, marker='o', color="green", alpha=0.5, label='DataFolha - Male')
# plt.plot('x', '13_male_ibope', data=df, marker='o', color="green", linestyle='dashed', alpha=0.4, label='IBOPE - Male')
# plt.plot('x', '13_female_dtfolha', data=df, marker='o', color="red", alpha=0.4, label='DataFolha - Female')
# plt.plot('x', '13_female_ibope', data=df, marker='o', color="red", linestyle='dashed', alpha=0.4, label='IBOPE - Female')
# plt.plot('x', '13_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook - Male')
# plt.plot('x', '13_female_facebook', data=df, marker='o', color="blue", linestyle='dashed', alpha=0.4, label='Facebook - Female')
# plt.xticks(range(0, len(axisY_DFolha_17_male)), xticks_DataFolha)
# G2.set_ylim(35,65)

# plt.legend(loc='upper center', bbox_to_anchor=(-0.1, -0.2),  shadow=True, ncol=2)
# plt.suptitle('Gender')
# plt.show()


# 4 partes