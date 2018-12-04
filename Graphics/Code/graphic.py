import matplotlib.pyplot as plt
import read_facebook as facebook
import read_elections as election
import pandas as pd
import models
import os

xticks = ["17\n11",  "18\n07",  "08\n06",  "09\n10",  "09\n17",  "09\n24",  "10\n01",  "10\n05", "10\n06",  "10\n08",  "10\n15",  "10\n22",  "10\n26", "10\n27",  "10\n29"]

i_bolsonaro = models.return_index("Jair Bolsonaro")
i_haddad = models.return_index("Fernando Haddad")
i_lula = models.return_index("Lula")
i_ciro = models.return_index("Ciro Gomes")
i_marina = models.return_index("Marina Silva")
i_alckmin = models.return_index("Geraldo Alckmin")

dic_color = {
        "DataFolha":"green",
        "IBOPE":"red",
        "Facebook":"blue"
    }
    
# xticks_facebook = ["17-11",  "18-07",  "08-06",  "09-10",  "09-17",  "09-24",  "10-01",  "10-05", "10-06", "10-08", "10-15",  "10-22",  "10-26", "10-27", "10-29"]
# xticks_dataf = ["17-11-30",  "06-07",  "08-21",  "09-10",  "09-18",  "09-28",  "10-02",  "10-04", "10-06", "10-07", "10-10", "10-18",  "10-25",  "10-27", "10-28"]
# xticks_ibope = ["17-10-22",  "06-24",  "08-19",  "09-10",  "09-18",  "09-24",  "09-30",  "10-02", "10-06", "10-07", "10-07", "10-14",  "10-23",  "10-27", "10-28"]

def plot_graph(name, data_frame, line, col, range_ini, range_fim, count_x, firstitle, subtitle, all_subtitle, figsizeX, figsizeY, hspace = 0):    

    fig = plt.figure(figsize=(figsizeX, figsizeY))    
    subtitle_aux = subtitle
    num = 1

    for d in data_frame:
        G = fig.add_subplot(line, col, num)
       
        for g in d.drop('x', axis=1):             
            label = g.split("-")
            
            if(all_subtitle == False and num <= col):
                plt.title(label[1], fontsize=12, color='black', loc='center')
            elif(all_subtitle == True):
                plt.title(label[1], fontsize=12, color='black', loc='center')

            if(subtitle == True):                
                plt.ylabel(label[0], multialignment='center', color='gray', fontsize=12)                
                subtitle = False

            plt.plot('x', g, data=d, marker='o', color=dic_color[label[2]], ls='-', alpha=0.4, label=label[2])

        plt.xticks(range(0, count_x), xticks)
        subtitle = subtitle_aux
        G.set_ylim(range_ini,range_fim)
        plt.legend()       
        num += 1

    # plt.scatter(2, 5, color='darkorange', s=180, alpha=1)
    # plt.text(x = r4[i]-0.5 , y = bars4[i]+0.1, s = label[i], size = 6)
    
    if(hspace != 0):
        plt.subplots_adjust(hspace=hspace)

    plt.suptitle(firstitle) 
    plt.savefig(name, dpi=100)

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
    
    data_frame_bolsonaro = [ pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
            'Jair Bolsonaro-Sudeste-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_sudeste, 'Jair Bolsonaro-Sudeste-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_sudeste,
            'Jair Bolsonaro-Sudeste-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_sudeste
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
            'Jair Bolsonaro-Nordeste-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_nordeste, 'Jair Bolsonaro-Nordeste-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_nordeste,
            'Jair Bolsonaro-Nordeste-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_nordeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
            'Jair Bolsonaro-Centro Oeste-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_norte_coeste, 'Jair Bolsonaro-Centro Oeste-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_norte_coeste,
            'Jair Bolsonaro-Centro Oeste-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_norte_coeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
            'Jair Bolsonaro-Sul-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_sul, 'Jair Bolsonaro-Sul-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_sul,
            'Jair Bolsonaro-Sul-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_sul
        })]

    data_frame_haddad = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
            'Fernando Haddad-Sudeste-DataFolha': models.data_reader.candidates[i_haddad].dfolha_sudeste, 'Fernando Haddad-Sudeste-IBOPE': models.data_reader.candidates[i_haddad].ibope_sudeste,
            'Fernando Haddad-Sudeste-Facebook': models.data_reader.candidates[i_haddad].facebook_sudeste
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
            'Fernando Haddad-Nordeste-DataFolha': models.data_reader.candidates[i_haddad].dfolha_nordeste, 'Fernando Haddad-Nordeste-IBOPE': models.data_reader.candidates[i_haddad].ibope_nordeste,
            'Fernando Haddad-Nordeste-Facebook': models.data_reader.candidates[i_haddad].facebook_nordeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
            'Fernando Haddad-Centro Oeste-DataFolha': models.data_reader.candidates[i_haddad].dfolha_norte_coeste, 'Fernando Haddad-Centro Oeste-IBOPE': models.data_reader.candidates[i_haddad].ibope_norte_coeste,
            'Fernando Haddad-Centro Oeste-Facebook': models.data_reader.candidates[i_haddad].facebook_norte_coeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
            'Fernando Haddad-Sul-DataFolha': models.data_reader.candidates[i_haddad].dfolha_sul, 'Fernando Haddad-Sul-IBOPE': models.data_reader.candidates[i_haddad].ibope_sul,
            'Fernando Haddad-Sul-Facebook': models.data_reader.candidates[i_haddad].facebook_sul
    })]

    data_frame_lula = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
            'Lula-Sudeste-DataFolha': models.data_reader.candidates[i_lula].dfolha_sudeste, 'Lula-Sudeste-IBOPE': models.data_reader.candidates[i_lula].ibope_sudeste,
            'Lula-Sudeste-Facebook': models.data_reader.candidates[i_lula].facebook_sudeste
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
            'Lula-Nordeste-DataFolha': models.data_reader.candidates[i_lula].dfolha_nordeste, 'Lula-Nordeste-IBOPE': models.data_reader.candidates[i_lula].ibope_nordeste,
            'Lula-Nordeste-Facebook': models.data_reader.candidates[i_lula].facebook_nordeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
            'Lula-Centro Oeste-DataFolha': models.data_reader.candidates[i_lula].dfolha_norte_coeste, 'Lula-Centro Oeste-IBOPE': models.data_reader.candidates[i_lula].ibope_norte_coeste,
            'Lula-Centro Oeste-Facebook': models.data_reader.candidates[i_lula].facebook_norte_coeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
            'Lula-Sul-DataFolha': models.data_reader.candidates[i_lula].dfolha_sul, 'Lula-Sul-IBOPE': models.data_reader.candidates[i_lula].ibope_sul,
            'Lula-Sul-Facebook': models.data_reader.candidates[i_lula].facebook_sul
    })]

    data_frame_ciro = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
            'Ciro Gomes-Sudeste-DataFolha': models.data_reader.candidates[i_ciro].dfolha_sudeste, 'Ciro Gomes-Sudeste-IBOPE': models.data_reader.candidates[i_ciro].ibope_sudeste,
            'Ciro Gomes-Sudeste-Facebook': models.data_reader.candidates[i_ciro].facebook_sudeste
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
            'Ciro Gomes-Nordeste-DataFolha': models.data_reader.candidates[i_ciro].dfolha_nordeste, 'Ciro Gomes-Nordeste-IBOPE': models.data_reader.candidates[i_ciro].ibope_nordeste,
            'Ciro Gomes-Nordeste-Facebook': models.data_reader.candidates[i_ciro].facebook_nordeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
            'Ciro Gomes-Centro Oeste-DataFolha': models.data_reader.candidates[i_ciro].dfolha_norte_coeste, 'Ciro Gomes-Centro Oeste-IBOPE': models.data_reader.candidates[i_ciro].ibope_norte_coeste,
            'Ciro Gomes-Centro Oeste-Facebook': models.data_reader.candidates[i_ciro].facebook_norte_coeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
            'Ciro Gomes-Sul-DataFolha': models.data_reader.candidates[i_ciro].dfolha_sul, 'Ciro Gomes-Sul-IBOPE': models.data_reader.candidates[i_ciro].ibope_sul,
            'Ciro Gomes-Sul-Facebook': models.data_reader.candidates[i_ciro].facebook_sul
    })]

    data_frame_marina = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
            'Marina Silva-Sudeste-DataFolha': models.data_reader.candidates[i_marina].dfolha_sudeste, 'Ciro Gomes-Sudeste-IBOPE': models.data_reader.candidates[i_marina].ibope_sudeste,
            'Marina Silva-Sudeste-Facebook': models.data_reader.candidates[i_marina].facebook_sudeste
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
            'Marina Silva-Nordeste-DataFolha': models.data_reader.candidates[i_marina].dfolha_nordeste, 'Marina Silva-Nordeste-IBOPE': models.data_reader.candidates[i_marina].ibope_nordeste,
            'Marina Silva-Nordeste-Facebook': models.data_reader.candidates[i_marina].facebook_nordeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
            'Marina Silva-Centro Oeste-DataFolha': models.data_reader.candidates[i_marina].dfolha_norte_coeste, 'Marina Silva-Centro Oeste-IBOPE': models.data_reader.candidates[i_marina].ibope_norte_coeste,
            'Marina Silva-Centro Oeste-Facebook': models.data_reader.candidates[i_marina].facebook_norte_coeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
            'Marina Silva-Sul-DataFolha': models.data_reader.candidates[i_marina].dfolha_sul, 'Marina Silva-Sul-IBOPE': models.data_reader.candidates[i_marina].ibope_sul,
            'Marina Silva-Sul-Facebook': models.data_reader.candidates[i_marina].facebook_sul
    })]

    data_frame_alckmin = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
            'Geraldo Alckmin-Sudeste-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_sudeste, 'Ciro Gomes-Sudeste-IBOPE': models.data_reader.candidates[i_alckmin].ibope_sudeste,
            'Geraldo Alckmin-Sudeste-Facebook': models.data_reader.candidates[i_alckmin].facebook_sudeste
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
            'Geraldo Alckmin-Nordeste-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_nordeste, 'Geraldo Alckmin-Nordeste-IBOPE': models.data_reader.candidates[i_alckmin].ibope_nordeste,
            'Geraldo Alckmin-Nordeste-Facebook': models.data_reader.candidates[i_alckmin].facebook_nordeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
            'Geraldo Alckmin-Centro Oeste-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_norte_coeste, 'Geraldo Alckmin-Centro Oeste-IBOPE': models.data_reader.candidates[i_alckmin].ibope_norte_coeste,
            'Geraldo Alckmin-Centro Oeste-Facebook': models.data_reader.candidates[i_alckmin].facebook_norte_coeste
        }),
        pd.DataFrame({
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
            'Geraldo Alckmin-Sul-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_sul, 'Geraldo Alckmin-Sul-IBOPE': models.data_reader.candidates[i_alckmin].ibope_sul,
            'Geraldo Alckmin-Sul-Facebook': models.data_reader.candidates[i_alckmin].facebook_sul
    })]

    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_sul) 
    plot_graph("bolsonaro_demografia.png", data_frame_bolsonaro, 2, 2, 5, 65, count_x, "Jair Bolsonaro", False, True, 18, 10)
    plot_graph("haddad_demografia.png", data_frame_haddad, 2, 2, 5, 70, count_x, "Fernando Haddad", False, True, 18, 10)
    plot_graph("lula_demografia.png", data_frame_lula, 2, 2, 5, 65, count_x, "Lula", False, True, 18, 10)
    plot_graph("ciro_demografia.png", data_frame_ciro, 2, 2, 5, 65, count_x, "Ciro Gomes", False, True, 18, 10)
    plot_graph("marina_demografia.png", data_frame_marina, 2, 2, 5, 65, count_x, "Marina Silva", False, True, 18, 10)
    plot_graph("alckmin_demografia.png", data_frame_alckmin, 2, 2, 5, 65, count_x, "Geraldo Alckmin", False, True, 18, 10)

def plot_like():
        
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

    data_frame_bolsonaro = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
            'Jair Bolsonaro-16 a 24-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_16a24, 'Jair Bolsonaro-16 a 24-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_16a24,
            'Jair Bolsonaro-16 a 24-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_16a24            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
            'Jair Bolsonaro-25 a 34-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_25a34, 'Jair Bolsonaro-25 a 34-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_25a34,
            'Jair Bolsonaro-25 a 34-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_25a34            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
            'Jair Bolsonaro-35 a 44-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_35a44, 'Jair Bolsonaro-35 a 44-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_35a44,
            'Jair Bolsonaro-35 a 44-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_35a44            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
            'Jair Bolsonaro-45 a 54-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_45a54, 'Jair Bolsonaro-45 a 54-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_45a54,
            'Jair Bolsonaro-45 a 54-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_45a54          
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
            'Jair Bolsonaro-Acima de 55-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_55, 'Jair Bolsonaro-Acima de 55-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_55,
            'Jair Bolsonaro-Acima de 55-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_55          
        })]

    data_frame_haddad = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
            'Fernando Haddad-16 a 24-DataFolha': models.data_reader.candidates[i_haddad].dfolha_16a24, 'Fernando Haddado-16 a 24-IBOPE': models.data_reader.candidates[i_haddad].ibope_16a24,
            'Fernando Haddad-16 a 24-Facebook': models.data_reader.candidates[i_haddad].facebook_16a24            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
            'Fernando Haddad-25 a 34-DataFolha': models.data_reader.candidates[i_haddad].dfolha_25a34, 'Fernando Haddad-25 a 34-IBOPE': models.data_reader.candidates[i_haddad].ibope_25a34,
            'Fernando Haddad-25 a 34-Facebook': models.data_reader.candidates[i_haddad].facebook_25a34            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
            'Fernando Haddad-35 a 44-DataFolha': models.data_reader.candidates[i_haddad].dfolha_35a44, 'Fernando Haddad-35 a 44-IBOPE': models.data_reader.candidates[i_haddad].ibope_35a44,
            'Fernando Haddad-35 a 44-Facebook': models.data_reader.candidates[i_haddad].facebook_35a44            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
            'Fernando Haddad-45 a 54-DataFolha': models.data_reader.candidates[i_haddad].dfolha_45a54, 'Fernando Haddad-45 a 54-IBOPE': models.data_reader.candidates[i_haddad].ibope_45a54,
            'Fernando Haddad-45 a 54-Facebook': models.data_reader.candidates[i_haddad].facebook_45a54          
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
            'Fernando Haddad-Acima de 55-DataFolha': models.data_reader.candidates[i_haddad].dfolha_55, 'Fernando Haddad-Acima de 55-IBOPE': models.data_reader.candidates[i_haddad].ibope_55,
            'Fernando Haddad-Acima de 55-Facebook': models.data_reader.candidates[i_haddad].facebook_55          
        })]
    
    data_frame_lula = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
            'Lula-16 a 24-DataFolha': models.data_reader.candidates[i_lula].dfolha_16a24, 'Lula-16 a 24-IBOPE': models.data_reader.candidates[i_lula].ibope_16a24,
            'Lula-16 a 24-Facebook': models.data_reader.candidates[i_lula].facebook_16a24            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
            'Lula-25 a 34-DataFolha': models.data_reader.candidates[i_lula].dfolha_25a34, 'Lula-25 a 34-IBOPE': models.data_reader.candidates[i_lula].ibope_25a34,
            'Lula-25 a 34-Facebook': models.data_reader.candidates[i_lula].facebook_25a34            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
            'Lula-35 a 44-DataFolha': models.data_reader.candidates[i_lula].dfolha_35a44, 'Lula-35 a 44-IBOPE': models.data_reader.candidates[i_lula].ibope_35a44,
            'Lula-35 a 44-Facebook': models.data_reader.candidates[i_lula].facebook_35a44            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
            'Lula-45 a 54-DataFolha': models.data_reader.candidates[i_lula].dfolha_45a54, 'Lula-45 a 54-IBOPE': models.data_reader.candidates[i_lula].ibope_45a54,
            'Lula-45 a 54-Facebook': models.data_reader.candidates[i_lula].facebook_45a54          
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
            'Lula-Acima de 55-DataFolha': models.data_reader.candidates[i_lula].dfolha_55, 'Lula-Acima de 55-IBOPE': models.data_reader.candidates[i_lula].ibope_55,
            'Lula-Acima de 55-Facebook': models.data_reader.candidates[i_lula].facebook_55          
    })]

    data_frame_ciro = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
            'Ciro Gomes-16 a 24-DataFolha': models.data_reader.candidates[i_ciro].dfolha_16a24, 'Ciro Gomes-16 a 24-IBOPE': models.data_reader.candidates[i_ciro].ibope_16a24,
            'Ciro Gomes-16 a 24-Facebook': models.data_reader.candidates[i_ciro].facebook_16a24            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
            'Ciro Gomes-25 a 34-DataFolha': models.data_reader.candidates[i_ciro].dfolha_25a34, 'Ciro Gomes-25 a 34-IBOPE': models.data_reader.candidates[i_ciro].ibope_25a34,
            'Ciro Gomes-25 a 34-Facebook': models.data_reader.candidates[i_ciro].facebook_25a34            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
            'Ciro Gomes-35 a 44-DataFolha': models.data_reader.candidates[i_ciro].dfolha_35a44, 'Ciro Gomes-35 a 44-IBOPE': models.data_reader.candidates[i_ciro].ibope_35a44,
            'Ciro Gomes-35 a 44-Facebook': models.data_reader.candidates[i_ciro].facebook_35a44            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
            'Ciro Gomes-45 a 54-DataFolha': models.data_reader.candidates[i_ciro].dfolha_45a54, 'Ciro Gomes-45 a 54-IBOPE': models.data_reader.candidates[i_ciro].ibope_45a54,
            'Ciro Gomes-45 a 54-Facebook': models.data_reader.candidates[i_ciro].facebook_45a54          
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
            'Ciro Gomes-Acima de 55-DataFolha': models.data_reader.candidates[i_ciro].dfolha_55, 'Ciro Gomes-Acima de 55-IBOPE': models.data_reader.candidates[i_ciro].ibope_55,
            'Ciro Gomes-Acima de 55-Facebook': models.data_reader.candidates[i_ciro].facebook_55          
    })]

    data_frame_marina = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
            'Marina Silva-16 a 24-DataFolha': models.data_reader.candidates[i_marina].dfolha_16a24, 'Marina Silva-16 a 24-IBOPE': models.data_reader.candidates[i_marina].ibope_16a24,
            'Marina Silva-16 a 24-Facebook': models.data_reader.candidates[i_marina].facebook_16a24            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
            'Marina Silva-25 a 34-DataFolha': models.data_reader.candidates[i_marina].dfolha_25a34, 'Marina Silva-25 a 34-IBOPE': models.data_reader.candidates[i_marina].ibope_25a34,
            'Marina Silva-25 a 34-Facebook': models.data_reader.candidates[i_marina].facebook_25a34            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
            'Marina Silva-35 a 44-DataFolha': models.data_reader.candidates[i_marina].dfolha_35a44, 'Marina Silva-35 a 44-IBOPE': models.data_reader.candidates[i_marina].ibope_35a44,
            'Marina Silva-35 a 44-Facebook': models.data_reader.candidates[i_marina].facebook_35a44            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
            'Marina Silva-45 a 54-DataFolha': models.data_reader.candidates[i_marina].dfolha_45a54, 'Marina Silva-45 a 54-IBOPE': models.data_reader.candidates[i_marina].ibope_45a54,
            'Marina Silva-45 a 54-Facebook': models.data_reader.candidates[i_marina].facebook_45a54          
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
            'Marina Silva-Acima de 55-DataFolha': models.data_reader.candidates[i_marina].dfolha_55, 'Marina Silva-Acima de 55-IBOPE': models.data_reader.candidates[i_marina].ibope_55,
            'Marina Silva-Acima de 55-Facebook': models.data_reader.candidates[i_marina].facebook_55          
    })]

    data_frame_alckmin = [pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
            'Geraldo Alckmin-16 a 24-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_16a24, 'Geraldo Alckmin-16 a 24-IBOPE': models.data_reader.candidates[i_alckmin].ibope_16a24,
            'Geraldo Alckmin-16 a 24-Facebook': models.data_reader.candidates[i_alckmin].facebook_16a24            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
            'Geraldo Alckmin-25 a 34-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_25a34, 'Geraldo Alckmin-25 a 34-IBOPE': models.data_reader.candidates[i_alckmin].ibope_25a34,
            'Geraldo Alckmin-25 a 34-Facebook': models.data_reader.candidates[i_alckmin].facebook_25a34            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
            'Geraldo Alckmin-35 a 44-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_35a44, 'Geraldo Alckmin-35 a 44-IBOPE': models.data_reader.candidates[i_alckmin].ibope_35a44,
            'Geraldo Alckmin-35 a 44-Facebook': models.data_reader.candidates[i_alckmin].facebook_35a44            
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
            'Geraldo Alckmin-45 a 54-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_45a54, 'Geraldo Alckmin-45 a 54-IBOPE': models.data_reader.candidates[i_alckmin].ibope_45a54,
            'Geraldo Alckmin-45 a 54-Facebook': models.data_reader.candidates[i_alckmin].facebook_45a54          
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
            'Geraldo Alckmin-Acima de 55-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_55, 'Geraldo Alckmin-Acima de 55-IBOPE': models.data_reader.candidates[i_alckmin].ibope_55,
            'Geraldo Alckmin-Acima de 55-Facebook': models.data_reader.candidates[i_alckmin].facebook_55          
    })]

    count_x = len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)

    plot_graph("idade_bolsonaro.png", data_frame_bolsonaro, 3, 2, 0, 60, count_x, "Jair Bolsonaro", False, True, 18, 10, 0.3)
    plot_graph("idade_haddad.png", data_frame_haddad, 3, 2, 0, 60, count_x, "Fernando Haddad", False, True, 18, 10, 0.3)
    plot_graph("idade_lula.png", data_frame_lula, 3, 2, 0, 60, count_x, "Lula", False, True, 18, 10, 0.3)
    plot_graph("idade_ciro.png", data_frame_ciro, 3, 2, 0, 60, count_x, "Ciro Gomes", False, True, 18, 10, 0.3)
    plot_graph("idade_marina.png", data_frame_marina, 3, 2, 0, 60, count_x, "Marina Silva", False, True, 18, 10, 0.3)
    plot_graph("idade_alckmin.png", data_frame_alckmin, 3, 2, 0, 60, count_x, "Geraldo Alckmin", False, True, 18, 10, 0.3)
   
def plot_education():   
    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_fundamental)

    data_frame = [
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
            'Jair Bolsonaro-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_fundamental, 'Jair Bolsonaro-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_fundamental,
            'Jair Bolsonaro-Ensino Fundamental-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_fundamental
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
            'Jair Bolsonaro-Ensino Médio-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_medio, 'Jair Bolsonaro-Ensino Médio-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_medio,
            'Jair Bolsonaro-Ensino Médio-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_medio
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
            'Jair Bolsonaro-Ensino Superior-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_superior, 'Jair Bolsonaro-Ensino Superior-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_superior,
            'Jair Bolsonaro-Ensino Superior-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_superior
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
            'Fernando Haddad-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_haddad].dfolha_fundamental, 'Fernando Haddad-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_haddad].ibope_fundamental,
            'Fernando Haddad-Ensino Fundamental-Facebook': models.data_reader.candidates[i_haddad].facebook_fundamental
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
            'Fernando Haddad-Ensino Médio-DataFolha': models.data_reader.candidates[i_haddad].dfolha_medio, 'Fernando Haddad-Ensino Médio-IBOPE': models.data_reader.candidates[i_haddad].ibope_medio,
            'Fernando Haddad-Ensino Médio-Facebook': models.data_reader.candidates[i_haddad].facebook_medio
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
            'Fernando Haddad-Ensino Superior-DataFolha': models.data_reader.candidates[i_haddad].dfolha_superior, 'Fernando Haddad-Ensino Superior-IBOPE': models.data_reader.candidates[i_haddad].ibope_superior,
            'Fernando Haddad-Ensino Superior-Facebook': models.data_reader.candidates[i_haddad].facebook_superior
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
            'Lula-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_lula].dfolha_fundamental, 'Lula-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_lula].ibope_fundamental,
            'Lula-Ensino Fundamental-Facebook': models.data_reader.candidates[i_lula].facebook_fundamental
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
            'Lula-Ensino Médio-DataFolha': models.data_reader.candidates[i_lula].dfolha_medio, 'Lula-Ensino Médio-IBOPE': models.data_reader.candidates[i_lula].ibope_medio,
            'Lula-Ensino Médioo-Facebook': models.data_reader.candidates[i_lula].facebook_medio
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
            'Lula-Ensino Superior-DataFolha': models.data_reader.candidates[i_lula].dfolha_superior, 'Lula-Ensino Superior-IBOPE': models.data_reader.candidates[i_lula].ibope_superior,
            'Lula-Ensino Superior-Facebook': models.data_reader.candidates[i_lula].facebook_superior
        })]

    data_frame2 =[
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
            'Ciro Gomes-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_ciro].dfolha_fundamental, 'Ciro Gomes-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_ciro].ibope_fundamental,
            'Ciro Gomes-Ensino Fundamental-Facebook': models.data_reader.candidates[i_ciro].facebook_fundamental
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
            'Ciro Gomes-Ensino Médio-DataFolha': models.data_reader.candidates[i_ciro].dfolha_medio, 'Ciro Gomes-Ensino Médio-IBOPE': models.data_reader.candidates[i_ciro].ibope_medio,
            'Ciro Gomes-Ensino Médio-Facebook': models.data_reader.candidates[i_ciro].facebook_medio
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
            'Ciro Gomes-Ensino Superior-DataFolha': models.data_reader.candidates[i_ciro].dfolha_superior, 'Ciro Gomes-Ensino Superior-IBOPE': models.data_reader.candidates[i_ciro].ibope_superior,
            'Ciro Gomes-Ensino Superior-Facebook': models.data_reader.candidates[i_ciro].facebook_superior
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
            'Marina Silva-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_marina].dfolha_fundamental, 'Marina Silva-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_marina].ibope_fundamental,
            'Marina Silva-Ensino Fundamental-Facebook': models.data_reader.candidates[i_marina].facebook_fundamental
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
            'Marina Silva-Ensino Médio-DataFolha': models.data_reader.candidates[i_marina].dfolha_medio, 'Marina Silva-Ensino Médio-IBOPE': models.data_reader.candidates[i_marina].ibope_medio,
            'Marina Silva-Ensino Médio-Facebook': models.data_reader.candidates[i_marina].facebook_medio
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
            'Marina Silva-Ensino Superior-DataFolha': models.data_reader.candidates[i_marina].dfolha_superior, 'Marina Silva-Ensino Superior-IBOPE': models.data_reader.candidates[i_marina].ibope_superior,
            'Marina Silva-Ensino Superior-Facebook': models.data_reader.candidates[i_marina].facebook_superior
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
            'Geraldo Alckmin-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_fundamental, 'Geraldo Alckmin-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_alckmin].ibope_fundamental,
            'Geraldo Alckmin-Ensino Fundamental-Facebook': models.data_reader.candidates[i_alckmin].facebook_fundamental
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
            'Geraldo Alckmin-Ensino Médio-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_medio, 'Geraldo Alckmin-Ensino Médio-IBOPE': models.data_reader.candidates[i_alckmin].ibope_medio,
            'Geraldo Alckmin-Ensino Médio-Facebook': models.data_reader.candidates[i_alckmin].facebook_medio
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
            'Geraldo Alckmin-Ensino Superior-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_superior, 'Geraldo Alckmin-Ensino Superior-IBOPE': models.data_reader.candidates[i_alckmin].ibope_superior,
            'Geraldo Alckmin-Ensino Superior-Facebook': models.data_reader.candidates[i_alckmin].facebook_superior
        })
        ]
    
    plot_graph("education_1.png", data_frame, 3, 3, 0, 75, count_x, "Education", True, False, 18, 10)
    plot_graph("education_2.png", data_frame2, 3, 3, 0, 75, count_x, "Education", True, False, 18, 10)   