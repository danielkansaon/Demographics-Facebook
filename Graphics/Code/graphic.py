import matplotlib.pyplot as plt
import read_facebook as facebook
import read_elections as election
import pandas as pd

# xticks_facebook = ["17-11",  "18-07",  "08-06",  "09-10",  "09-17",  "09-24",  "10-01",  "10-05", "10-06", "10-08", "10-15",  "10-22",  "10-26", "10-27", "10-29"]
# xticks_dataf = ["17-11-30",  "06-07",  "08-21",  "09-10",  "09-18",  "09-28",  "10-02",  "10-04", "10-06", "10-07", "10-10", "10-18",  "10-25",  "10-27", "10-28"]
# xticks_ibope = ["17-10-22",  "06-24",  "08-19",  "09-10",  "09-18",  "09-24",  "09-30",  "10-02", "10-06", "10-07", "10-07", "10-14",  "10-23",  "10-27", "10-28"]

xticks = ["17\n11",  "18\n07",  "08\n06",  "09\n10",  "09\n17",  "09\n24",  "10\n01",  "10\n05", "10\n06",  "10\n08",  "10\n15",  "10\n22",  "10\n26", "10\n27",  "10\n29"]

def plot_gender():
    facebook.readJson()

    df = pd.DataFrame(
        {
            'x': range(0, len(election.vec_dfolha_17_male)), 
            '17_male_dtfolha': election.vec_dfolha_17_male, '17_female_dtfolha': election.vec_dfolha_17_female,
            '17_male_ibope': election.vec_ibope_17_male, '17_female_ibope': election.vec_ibope_17_female,

            '13_male_dtfolha': election.vec_dfolha_13_male, '13_female_dtfolha': election.vec_dfolha_13_female,
            '13_male_ibope': election.vec_ibope_13_male, '13_female_ibope': election.vec_ibope_13_female,

            'lula_male_dtfolha': election.vec_dfolha_lula_male, 'lula_female_dtfolha': election.vec_dfolha_lula_female,
            'lula_male_ibope': election.vec_ibope_lula_male, 'lula_female_ibope': election.vec_ibope_lula_female,

            'ciro_male_dtfolha': election.vec_dfolha_ciro_male, 'ciro_female_dtfolha': election.vec_dfolha_ciro_female,
            'ciro_male_ibope': election.vec_ibope_ciro_male, 'ciro_female_ibope': election.vec_ibope_ciro_female,

            '17_male_facebook': facebook.vec_facebook_17_male, '17_female_facebook': facebook.vec_facebook_17_female,
            '13_male_facebook': facebook.vec_facebook_13_male, '13_female_facebook': facebook.vec_facebook_13_female,
            'lula_male_facebook': facebook.vec_facebook_lula_male, 'lula_female_facebook': facebook.vec_facebook_lula_female,
            'ciro_male_facebook': facebook.vec_facebook_12_male, 'ciro_female_facebook': facebook.vec_facebook_12_female
        })

    count_x = len(election.vec_dfolha_17_male)

    G1 = plt.subplot(4,2,1)
    plt.title('Male', fontsize=12, color='gray', loc='center')
    plt.ylabel('Jair Bolsonaro', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', '17_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')  #linestyle='dashed' (--)
    plt.plot('x', '17_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')    
    plt.xticks(range(0, count_x), xticks)
    G1.set_ylim(15,75)
    plt.legend()
    

    G2 = plt.subplot(4,2,2)
    plt.title('Female', fontsize=12, color='gray', loc='center')
    plt.plot('x', '17_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '17_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', '17_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G2.set_ylim(15,75)
    plt.legend()

    G3 = plt.subplot(4,2,3)
    plt.ylabel('Fernando Haddad', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', '13_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '13_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', '13_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G3.set_ylim(15,75)
    plt.legend()

    G4 = plt.subplot(4,2,4)
    plt.plot('x', '13_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', '13_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', '13_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G4.set_ylim(15,75)
    plt.legend()

    G5 = plt.subplot(4,2,5)
    plt.ylabel('Lula', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', 'lula_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'lula_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', 'lula_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G5.set_ylim(15,75)
    plt.legend()

    G6 = plt.subplot(4,2,6)
    plt.plot('x', 'lula_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'lula_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', 'lula_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G6.set_ylim(15,75)
    plt.legend()

    G7 = plt.subplot(4,2,7)
    plt.ylabel('Ciro Gomes', multialignment='center', color='gray', fontsize=12)
    plt.plot('x', 'ciro_male_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'ciro_male_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', 'ciro_male_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G7.set_ylim(15,75)
    plt.legend()

    G8 = plt.subplot(4,2,8)
    plt.plot('x', 'ciro_female_dtfolha', data=df, marker='o', color="green", ls='-', alpha=0.4, label='DataFolha')
    plt.plot('x', 'ciro_female_ibope', data=df, marker='o', color="red", alpha=0.4, label='IBOPE')
    plt.plot('x', 'ciro_female_facebook', data=df, marker='o', color="blue", alpha=0.4, label='Facebook')
    plt.xticks(range(0, count_x), xticks)
    G8.set_ylim(15,75)
    plt.legend()
    
    # plt.text(0.08, 0.3, 'TIME', ha='center', va='center')
    plt.suptitle('Gender')
    plt.show()


# def plot_age():

    
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