from matplotlib.ticker import FuncFormatter
import read_elections as election
from scipy.stats import spearmanr
import read_facebook as facebook
import matplotlib.pyplot as plt
import data_frames as GFrame
import pandas as pd
import models
import os
import numpy as np
import subprocess

xticks = ["17\n11",  "18\n07",  "08\n06",  "09\n10",  "09\n17",  "09\n24",  "10\n01",  "10\n05", "10\n06",  "10\n08",  "10\n15",  "10\n22",  "10\n26", "10\n27",  "10\n29"]
n_xticks = 15

# xticks = ["10\n22", "11\n28", "11\n30", "06\n07", "06\n24", "07\n09", "08\n06", "08\n19", "08\n21", 
# "09\n10", "09\n17", "09\n18", "09\n24", "09\n28", "09\n30", "10\n01", "10\n02", "10\n04", "10\n05",
# "10\n06", "10\n07", "10\n08", "10\n10", "10\n14", "10\n15", "10\n18", "10\n22", "10\n23", "10\n25", 
# "10\n26", "10\n27", "10\n28", "10\n29"]

i_bolsonaro = models.return_index("Jair Bolsonaro")
i_haddad = models.return_index("Fernando Haddad")
i_lula = models.return_index("Lula")
i_ciro = models.return_index("Ciro Gomes")
i_marina = models.return_index("Marina Silva")
i_alckmin = models.return_index("Geraldo Alckmin")
i_alvaro = models.return_index("Alvaro Dias")

v_index = [i_bolsonaro, i_haddad, i_ciro, i_marina, i_alckmin, i_marina, i_alvaro]

error_facebook_1round = []
error_dfolha_1round = []
error_ibope_1round = []

error_facebook_2round = []
error_dfolha_2round = []
error_ibope_2round = []

pos_result_1_round = 9
pos_result_2_round = 14

dic_color = {
        "DataFolha":"green",
        "IBOPE":"red",
        "Facebook": "blue",
        "Variation (DataFolha)":"green",
        "Variation (IBOPE)":"red"
}

dic_index = {
        i_bolsonaro:"jair_bolsonaro",
        i_haddad:"fernando_haddad",
        i_ciro: "ciro_gomes",
        i_marina:"marina_silva",
        i_alckmin:"geraldo_alckmin",
        i_alvaro:"alvaro_dias"
}

dic_lines = {
    "points": [{"x": 5.8, "negative": 0.6, "plus": 7, "text": "#EleNao"}, 
    {"x": 2.7, "negative": 0.9, "plus": 4, "text": "Judgment\n   Lula "}, 
    {"x": 10.8, "negative": 0.6, "plus": 7, "text": "Protests"}]
}

def formatter_millions(x):
    return '%1.0f' % (x/1000000)

def calculate_correlattion(ibope, dfolha, facebook, resultado):
    v = []

    corrI, p_valueI = spearmanr(ibope, facebook)
    corrF, p_valueF = spearmanr(dfolha, facebook)
    v.append(corrI)
    v.append(corrF)
    v.append(p_valueI)
    v.append(p_valueF)

    return v

def plot_graph_events(range_fim, graph_error = False):
    if(graph_error == True):
        plt.text(x = pos_result_1_round - 0.8, y = range_fim - (range_fim * 0.20), s = "End\n1º Round", size = 11)
        plt.text(x = pos_result_2_round - 0.8, y = range_fim - (range_fim * 0.20), s = "End\n2º Round", size = 11)  
        plt.axvline(x=pos_result_1_round, color='gray', linestyle='--', alpha=0.5)
        plt.axvline(x=pos_result_2_round, color='gray', linestyle='--', alpha=0.5)
    else:
        for dic in dic_lines["points"]:
                plt.axvline(x=dic["x"], color='gray', linestyle='--', alpha=0.5)

                if(dic["text"] == "Judgment\n   Lula "):
                    plt.text(x = dic["x"] - dic["negative"], y =  range_fim - 8, s = dic["text"], size = 11)  
                else:               
                    plt.text(x = dic["x"] - dic["negative"], y =  range_fim - 5, s = dic["text"], size = 11)

def get_variation_graph(v_facebook, v_ibope, v_dfolha):
    v_facebook_ibope = []
    v_facebook_dfolha = []

    for i in range(0,n_xticks):
        if(v_ibope[i] == 0 or v_ibope[i] == -100):
            v_facebook_ibope.append(0)
        elif(v_facebook[i] > 0):
            v_facebook_ibope.append(((v_facebook[i] - v_ibope[i]) / v_ibope[i]) * 100)
        else:
             v_facebook_ibope.append(0)
             
        if(v_dfolha[i] == 0 or v_dfolha[i] == -100):
            v_facebook_dfolha.append(0)
        elif(v_facebook[i] > 0):
            v_facebook_dfolha.append(((v_facebook[i] - v_dfolha[i]) / v_dfolha[i]) * 100)      
        else:
            v_facebook_dfolha.append(0)  
    
    return v_facebook_dfolha, v_facebook_ibope
    
def get_error_agregatte(v_facebook, v_ibope, v_dfolha):    
    if(v_ibope[pos_result_1_round] != 0 and v_ibope[pos_result_1_round] != -100):
        error_facebook_1round.append((abs((v_facebook[pos_result_1_round] - v_ibope[pos_result_1_round])) / v_ibope[pos_result_1_round]) * 100)
        error_ibope_1round.append((abs((v_ibope[pos_result_1_round - 1] - v_ibope[pos_result_1_round])) / v_ibope[pos_result_1_round]) * 100)
        error_dfolha_1round.append((abs((v_dfolha[pos_result_1_round - 1] - v_dfolha[pos_result_1_round])) / v_dfolha[pos_result_1_round]) * 100)

    if(v_ibope[pos_result_2_round] != 0 and v_ibope[pos_result_2_round] != -100):
        error_facebook_2round.append((abs((v_facebook[pos_result_2_round - 1] - v_ibope[pos_result_2_round])) / v_ibope[pos_result_2_round]) * 100)
        error_ibope_2round.append((abs((v_ibope[pos_result_2_round - 1] - v_ibope[pos_result_2_round])) / v_ibope[pos_result_2_round]) * 100)
        error_dfolha_2round.append((abs((v_dfolha[pos_result_2_round - 1] - v_dfolha[pos_result_2_round])) / v_dfolha[pos_result_2_round]) * 100)   
    
def plot_table_error(name):
    fig = plt.figure()

    name = name.replace(".png","")
    name = name + "_table.png"

    df = pd.DataFrame({'Facebook': [str(round(sum(error_facebook_1round) / len(error_dfolha_1round),2)) + "%"],
                   'IBOPE': [str(round(sum(error_ibope_1round) / len(error_ibope_1round),2)) + "%"],
                   'DataFolha': [str(round(sum(error_dfolha_1round) / len(error_dfolha_1round),2)) + "%"]})  
    
    if(len(error_facebook_2round) > 0):
        df2 = pd.DataFrame({'Facebook': [str(round(sum(error_facebook_2round) / len(error_dfolha_2round),2)) + "%"],
                    'IBOPE': [str(round(sum(error_ibope_2round) / len(error_ibope_2round),2)) + "%"],
                    'DataFolha': [str(round(sum(error_dfolha_2round) / len(error_dfolha_2round),2)) + "%"]})  
    
    # plt.title('1º Round', fontdict=None, loc='center')
    G = fig.add_subplot(1, 2, 1)
    plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    plt.axis('tight')
    plt.axis('off')
    fig.patch.set_visible(False)

    if(len(error_facebook_2round) > 0):
        fig.add_subplot(1, 2, 2)    
        plt.table(cellText=df2.values, colLabels=df2.columns, loc='center', cellLoc='center')
        plt.axis('off')
        plt.axis('tight')
        
    fig.tight_layout()
    fig.savefig(name)
    
    error_facebook_1round.clear()
    error_ibope_1round.clear()
    error_dfolha_1round.clear()
    error_facebook_2round.clear()
    error_ibope_2round.clear()
    error_dfolha_2round.clear()

    # for key, cell in a.get_celld().items():
    #     if(key[0] != 0):
    #         cell.set_linewidth(0)
    #     # gg = key[0]

# Draw circle result in grpah
def draw_result_graph(plot_error, d, g, text_1Round, text_2Round, legend_result):
    if(plot_error == False):                        
        if(d[g].values[pos_result_1_round] != 0 and d[g].values[pos_result_1_round] != -100):
            plt.scatter(pos_result_1_round, y = 0, color='lightskyblue', s=130, alpha=1, label="Error Facebook %") 
            plt.text(x = pos_result_1_round - 0.5 , y = 4, s = str(round(d[g].values[pos_result_1_round],1)) + " %", size = 11)
        if(d[g].values[pos_result_2_round] != -100 and d[g].values[pos_result_2_round] != 0):
            plt.scatter(pos_result_2_round, 0, color='lightskyblue', s=130, alpha=1)
            plt.text(x = pos_result_2_round - 0.5 , y = 4, s = str(round(d[g].values[pos_result_2_round],1)) + " %", size = 11)   

    if(d[g].values[pos_result_1_round] != -100):
        plt.scatter(pos_result_1_round, d[g].values[pos_result_1_round], color='darkorange', s=130, alpha=1, label=legend_result) 
        plt.text(x = pos_result_1_round - 0.5 , y =  d[g].values[pos_result_1_round] + 3, s = text_1Round, size = 11)
            
    if(d[g].values[pos_result_2_round] != -100 and d[g].values[pos_result_2_round] != 0):
        plt.scatter(pos_result_2_round, d[g].values[pos_result_2_round], color='darkorange', s=130, alpha=1)
        plt.text(x = pos_result_2_round - 0.5 , y =  d[g].values[pos_result_2_round] + 3, s = text_2Round, size = 11)

def cal_dataframe_error(vector_dFrame, v_facebook, v_ibope, v_dfolha, label):                             
    variation_dfolha, variation_ibope = get_variation_graph(v_facebook, v_ibope, v_dfolha)

    v_error_pool_2round = [-100]*n_xticks
    v_error_pool_1round = [-100]*n_xticks

    if(v_ibope[pos_result_2_round] == 0 or v_dfolha[pos_result_2_round] == 0):
        v_error_pool_2round[1] = 0
    elif(v_ibope[pos_result_1_round] == 0 or v_dfolha[pos_result_1_round] == 0):
        v_error_pool_1round[1] = 0
    else:   
        v_error_pool_2round[1] = ((v_ibope[13] - v_ibope[pos_result_2_round]) / v_ibope[pos_result_2_round]) * 100
        v_error_pool_2round[0] = variation_ibope[13]
        v_error_pool_1round[1] = ((v_ibope[8] - v_ibope[pos_result_1_round]) / v_ibope[pos_result_1_round]) * 100
        v_error_pool_1round[0] = variation_ibope[8]
        
        if(v_error_pool_1round[1] >= 0):
            if(v_error_pool_1round[1] < ((v_dfolha[8] - v_dfolha[pos_result_1_round]) / v_dfolha[pos_result_1_round]) * 100):
                v_error_pool_1round[1] = ((v_dfolha[8] - v_dfolha[pos_result_1_round]) / v_dfolha[pos_result_1_round]) * 100
                v_error_pool_1round[0] = variation_dfolha[8]
            if(v_error_pool_2round[1] < ((v_dfolha[13] - v_dfolha[pos_result_2_round]) / v_dfolha[pos_result_2_round]) * 100 ):
                v_error_pool_2round[1] = ((v_dfolha[13] - v_dfolha[pos_result_2_round]) / v_dfolha[pos_result_2_round]) * 100
                v_error_pool_2round[0] = variation_dfolha[13]
        else:
            if(v_error_pool_1round[1] > ((v_dfolha[8] - v_dfolha[pos_result_1_round]) / v_dfolha[pos_result_1_round]) * 100):
                v_error_pool_1round[1] = ((v_dfolha[8] - v_dfolha[pos_result_1_round]) / v_dfolha[pos_result_1_round]) * 100
                v_error_pool_1round[0] = variation_dfolha[8]
            if(v_error_pool_2round[1] > ((v_dfolha[13] - v_dfolha[pos_result_2_round]) / v_dfolha[pos_result_2_round]) * 100 ):
                v_error_pool_2round[1] = ((v_dfolha[13] - v_dfolha[pos_result_2_round]) / v_dfolha[pos_result_2_round]) * 100
                v_error_pool_2round[0] = variation_dfolha[13]
    
    vector_dFrame.append(pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        label[0] + "-" + label[1] + "-Variation (DataFolha)": variation_dfolha, label[0] + "-" + label[1] + "-Variation (IBOPE)": variation_ibope,
        "calc_1round_pool": v_error_pool_1round, "calc_2round_pool" : v_error_pool_2round
    }))

    return vector_dFrame

def plot_graph(name, data_frame, line, col, range_ini, range_fim, count_x, firstitle, set_subtitle, all_subtitle, set_result, figsizeX, figsizeY,
 legend_posX, legend_posY, plot_error = True, plot_event = True, hspace=0):    
    
    fig = plt.figure(figsize=(figsizeX, figsizeY))    
    set_result_aux = set_result
    subtitle_aux = set_subtitle    
    text_1Round = "1º round"
    text_2Round = "2º round"    
    count_subtitle = 0    
    legend_result = ""
    vector_dFrame = []
    v_facebook = []
    v_labels = []
    v_dfolha = []
    v_ibope = []  
    pos = 1
   
    for d in data_frame:
        G = fig.add_subplot(line, col, pos)
        
        for g in d.drop('x', axis=1):               
            if(g == 'calc_1round_pool'):
                if(d[g].values[0] != 0 and d[g].values[0] != -100):
                    plt.scatter(8, d[g].values[0], color ='slategrey', s=130, alpha=1, label="Error Pool %")
                    plt.text(x = 8 - 0.5 , y = d[g].values[0] + 6, s = str(round(d[g].values[1])) + " %", size = 11)         

            elif(g == 'calc_2round_pool'):
                if(d[g].values[0] != 0 and d[g].values[0] != -100):
                    plt.scatter(13, d[g].values[0], color ='slategrey', s=130, alpha=1) 
                    plt.text(x = 13 - 0.5 , y = d[g].values[0] + 5, s = str(round(d[g].values[1])) + " %", size = 11)    
            else:
                label = g.split("-")
                            
                if(all_subtitle == False and pos <= col):
                    plt.title(label[1], fontsize=15, color='black', loc='center')
                elif(all_subtitle == True):
                    plt.title(label[1], fontsize=15, color='black', loc='center')           

                if(set_subtitle == True):                
                    plt.ylabel(label[0], multialignment='center', color='black', fontsize=14)                
                    set_subtitle = False
                    # , marker='o'

                #Plotando gráfico base
                if(plot_error == True):
                    if 'Distribuition' in label[2]:
                        if 'Facebook' in label[2]:
                            plt.plot('x', g, data=d, color='lightskyblue', ls='--', alpha=1, linewidth=2.0, label='Distribuition Facebook')
                        else:
                            plt.plot('x', g, data=d, color='darkgoldenrod', ls='--', alpha=1, linewidth=2.0, label='Distribuition Census')
                    else:
                        plt.plot('x', g, data=d, color=dic_color[label[2]], ls='-', marker='o',  alpha=0.8, label=label[2])
                else:
                    # marker='v',
                    plt.plot('x', g, data=d, color=dic_color[label[2]], marker='X', linewidth=2, linestyle='dashed', alpha=0.6, label=label[2])
                    plt.axhline(y=0, color='blue', linestyle='-', alpha=0.9)
                    legend_result = "Result Election"
                    text_1Round = ""
                    text_2Round = ""

                if 'Distribuition' not in g:
                    if 'Facebook' in g:
                        v_facebook = d[g].values
                    if 'DataFolha' in g:
                        v_dfolha = d[g].values
                    if 'IBOPE' in g:
                        v_ibope = d[g].values

                v_labels.append(g)

                #Setando Resultado
                if(set_result_aux == True):  
                    draw_result_graph(plot_error, d, g, text_1Round, text_2Round, legend_result)                    
                    set_result_aux = False
                               
        #Calculando Error                               
        if(plot_error == True and len(v_facebook) > 0):
            vector_dFrame = cal_dataframe_error(vector_dFrame, v_facebook, v_ibope, v_dfolha, label)       

        #Marcando eventos no grafico
        if(plot_event):
            plot_graph_events(range_fim)
        elif(plot_error == False):
            plot_graph_events(range_fim, True)
                              
        plt.xticks(range(0, count_x), xticks)   
           
        count_subtitle += 1
        if(count_subtitle == col):
            set_subtitle = subtitle_aux
            count_subtitle = 0
        
        G.set_ylim(range_ini,range_fim)
        set_result_aux = True
        pos += 1 
            
    if(hspace != 0):
        plt.subplots_adjust(hspace=hspace)

    # plt.subplots_adjust(top=18)
    plt.legend(loc='upper center', bbox_to_anchor=(legend_posX, legend_posY), fancybox=True, shadow=True, ncol=5, prop={'size':'13'})
    plt.suptitle(firstitle) 
    plt.savefig(name, dpi=100)
    
    return vector_dFrame

def plot_gender():   
           
    count_x = len(models.data_reader.candidates[0].dfolha_male)
    error_1 = plot_graph("gender_1.png", GFrame.Gender.data_frame_1, 3, 2, 0, 80, count_x, "Gender", True, False, True, 18, 10, -0.1, -0.19)
    plot_graph("gender_1_error.png", error_1, 3, 2, -50, 50, count_x, "Variation Polls", True, False, True, 19, 10,-0.1, -0.19, False, False)
    error_2 = plot_graph("gender_2.png", GFrame.Gender.data_frame_2, 3, 2, 0, 80, count_x, "Gender", True, False, True, 19, 10, -0.1, -0.19)
    plot_graph("gender_2_error.png", error_2, 3, 2, -40, 90, count_x, "Variation Polls", True, False, True, 19, 10, -0.1, -0.19, False, False)    

    # for i in v_index:
    #     get_error_agregatte(models.data_reader.candidates[i].facebook_male, models.data_reader.candidates[i].ibope_male, models.data_reader.candidates[i].dfolha_male)
    #     get_error_agregatte(models.data_reader.candidates[i].facebook_female, models.data_reader.candidates[i].ibope_female, models.data_reader.candidates[i].dfolha_female)
    #     plot_table_error("gender_" + dic_index[i] + "_error.png")
   

def plot_region():
        
    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_sul) 

    error_1 = plot_graph("region_bolsonaro.png", GFrame.Region.data_frame_bolsonaro, 2, 2, 5, 60, count_x, "Jair Bolsonaro", False, True, True, 18, 10, -0.1, -0.19)
    plot_graph("region_bolsonaro_error.png", error_1, 2, 2, -50, 90, count_x, "Jair Bolsonaro - Variation Polls", False, True, True, 18, 10, -0.1, -0.19, False, False)

    error_2 = plot_graph("region_haddad.png", GFrame.Region.data_frame_haddad, 2, 2, 5, 90, count_x, "Fernando Haddad", False, True, True, 18, 10, -0.1, -0.19)
    plot_graph("region_haddad_error.png", error_2, 2, 2, -75, 90, count_x, "Fernando Haddad - Variation Polls", False, True, True, 18, 10, -0.1, -0.19, False, False)

    error_3 = plot_graph("region_ciro.png", GFrame.Region.data_frame_ciro, 2, 2, 5, 60, count_x, "Ciro Gomes", False, True, True, 18, 10, -0.1, -0.19)
    plot_graph("region_ciro_error.png", error_3, 2, 2, -50, 125, count_x, "Ciro Gomes - Variation Polls", False, True, True, 18, 10, -0.1, -0.19, False, False)

    error_4 = plot_graph("region_marina.png", GFrame.Region.data_frame_marina, 2, 2, 5, 60, count_x, "Marina Silva", False, True, True, 18, 10, -0.1, -0.19)
    plot_graph("region_marina_error.png", error_4, 2, 2, -50, 150, count_x, "Marina Silva - Variation Polls", False, True, True, 18, 10, -0.1, -0.19, False, False)

    error_5 = plot_graph("region_alckmin.png", GFrame.Region.data_frame_alckmin, 2, 2, 5, 85, count_x, "Geraldo Alckmin", False, True, True, 18, 10, -0.1, -0.19)
    plot_graph("region_alckmin_error.png", error_5, 2, 2, -50, 100, count_x, "Geraldo Alckmin - Variation Polls", False, True, True, 18, 10, -0.1, -0.19, False, False)

    error_6 = plot_graph("region_alvaro.png", GFrame.Region.data_frame_alvaro, 2, 2, 0, 70, count_x, "Alvaro Dias", False, True, True, 18, 10, -0.1, -0.19)
    plot_graph("region_alvaro_error.png", error_6, 2, 2, -50, 200, count_x, "Alvaro Dias - Variation Polls", False, True, True, 18, 10, -0.1, -0.19, False, False)
    
    # plot_graph("region_lula.png", data_frame_lula, 2, 2, 5, 60, count_x, "Lula", False, True, True, 18, 10)

    for i in v_index:
        get_error_agregatte(models.data_reader.candidates[i].facebook_nordeste, models.data_reader.candidates[i].ibope_nordeste, models.data_reader.candidates[i].dfolha_nordeste)
        get_error_agregatte(models.data_reader.candidates[i].facebook_norte_coeste, models.data_reader.candidates[i].ibope_norte_coeste, models.data_reader.candidates[i].dfolha_norte_coeste)
        get_error_agregatte(models.data_reader.candidates[i].facebook_sul, models.data_reader.candidates[i].ibope_sul, models.data_reader.candidates[i].dfolha_sul)
        get_error_agregatte(models.data_reader.candidates[i].facebook_sudeste, models.data_reader.candidates[i].ibope_sudeste, models.data_reader.candidates[i].dfolha_sudeste)
        plot_table_error("region_" + dic_index[i] + "_error.png")


def plot_like():
        
    df = pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].facebook_likes)), 
            'bolsonaro_like': models.data_reader.candidates[i_bolsonaro].facebook_likes, 'ciro_like': models.data_reader.candidates[i_ciro].facebook_likes,
            'haddad_like': models.data_reader.candidates[i_haddad].facebook_likes, 'marina_like': models.data_reader.candidates[i_marina].facebook_likes,
            'alckmin_like': models.data_reader.candidates[i_alckmin].facebook_likes, 'lula_like': models.data_reader.candidates[i_lula].facebook_likes,
            'alvaro_like': models.data_reader.candidates[i_alvaro].facebook_likes
        })

    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_likes)

    fig, ax = plt.subplots()
    plt.suptitle('Nº Likes')  
    plt.plot('x', 'bolsonaro_like', data=df, marker='o', color="green", ls='-', alpha=0.7, label='Jair Bolsonaro')
    plt.plot('x', 'haddad_like', data=df, marker='o', color="red", alpha=0.7, label='Fernando Haddad')  
    plt.plot('x', 'ciro_like', data=df, marker='o', color="orange", alpha=0.7, label='Ciro Gomes')
    plt.plot('x', 'alckmin_like', data=df, marker='o', color="blue", alpha=0.7, label='Alckmin')
    plt.plot('x', 'marina_like', data=df, marker='o', color="violet", alpha=0.7, label='Marina Silva')
    plt.plot('x', 'lula_like', data=df, marker='o', color="brown", alpha=0.7, label='Lula')
    plt.plot('x', 'alvaro_like', data=df, marker='o', color="black", alpha=0.7, label='Alvaro Dias')
    
    plt.xticks(range(0, count_x), xticks)

    #Eventos    
    for dic in dic_lines["points"]:
        plt.axvline(x=dic["x"], color='gray', linestyle='--', alpha=0.5)

        if(dic["text"] == "Judgment\n   Lula "):
            plt.text(x = dic["x"] - dic["negative"], y =  8000000 - 8, s = dic["text"], size = pos_result_2_round)  
        else:               
            plt.text(x = dic["x"] - dic["negative"], y =  8000000 - 5, s = dic["text"], size = pos_result_2_round)  

    plt.axvline(x=pos_result_2_round, color='gray', linestyle='--', alpha=0.5) 
    plt.text(x = pos_result_2_round - dic["negative"], y =  8000000 - 15, s = 'End\n1º Round', size = pos_result_2_round)  
    plt.axvline(x=pos_result_2_round, color='gray', linestyle='--', alpha=0.5) 
    plt.text(x = pos_result_2_round - dic["negative"], y =  8000000 - 15, s = 'End\n2º Round', size = pos_result_2_round)  
    
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.11), fancybox=True, shadow=True, ncol=5)    
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: formatter_millions(int(x))))
    plt.ylabel("Millions (m)", multialignment='center', color='gray', fontsize=12)

    plt.show()

def talking_about():    
    df = pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].facebook_talking_about)), 
            'bolsonaro_talking': models.data_reader.candidates[i_bolsonaro].facebook_talking_about, 'ciro_talking': models.data_reader.candidates[i_ciro].facebook_talking_about,
            'haddad_talking': models.data_reader.candidates[i_haddad].facebook_talking_about, 'marina_talking': models.data_reader.candidates[i_marina].facebook_talking_about,
            'alckmin_talking': models.data_reader.candidates[i_alckmin].facebook_talking_about, 'lula_talking': models.data_reader.candidates[i_lula].facebook_talking_about,
            'alvaro_talking': models.data_reader.candidates[i_alvaro].facebook_talking_about
        })

    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_talking_about)

    fig, ax = plt.subplots()
    
    plt.suptitle('Talking About')  
    plt.plot('x', 'bolsonaro_talking', data=df, marker='o', color="green", ls='-', alpha=0.7, label='Jair Bolsonaro')
    plt.plot('x', 'haddad_talking', data=df, marker='o', color="red", alpha=0.7, label='Fernando Haddad')  
    plt.plot('x', 'ciro_talking', data=df, marker='o', color="orange", alpha=0.7, label='Ciro Gomes')
    plt.plot('x', 'alckmin_talking', data=df, marker='o', color="blue", alpha=0.7, label='Alckmin')
    plt.plot('x', 'marina_talking', data=df, marker='o', color="violet", alpha=0.7, label='Marina Silva')
    plt.plot('x', 'lula_talking', data=df, marker='o', color="brown", alpha=0.7, label='Lula')
    plt.plot('x', 'alvaro_talking', data=df, marker='o', color="black", alpha=0.7, label='Alvaro Dias')    
    plt.xticks(range(0, count_x), xticks)

    #Eventos    
    for dic in dic_lines["points"]:
        plt.axvline(x=dic["x"], color='gray', linestyle='--', alpha=0.5)

        if(dic["text"] == "Judgment\n   Lula "):
            plt.text(x = dic["x"] - dic["negative"], y =  4700000 - 8, s = dic["text"], size = pos_result_2_round)  
        else:               
            plt.text(x = dic["x"] - dic["negative"], y =  4700000 - 3, s = dic["text"], size = pos_result_2_round)  

    plt.axvline(x=pos_result_2_round, color='gray', linestyle='--', alpha=0.5) 
    plt.text(x = pos_result_2_round - dic["negative"], y =  4800000 - 12000, s = 'End\n1º Round', size = pos_result_2_round)  
    plt.axvline(x=pos_result_2_round, color='gray', linestyle='--', alpha=0.5) 
    plt.text(x = pos_result_2_round - dic["negative"], y =  4800000 - 10000, s = 'End\n2º Round', size = pos_result_2_round)  

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: formatter_millions(int(x))))
    plt.ylabel("Millions (m)", multialignment='center', color='gray', fontsize=12)

    plt.show()    

def plot_age():
    count_x = len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)

    # bbox_to_anchor=(1.2, -0.21),

    error_1 = plot_graph("age_bolsonaro.png", GFrame.Age.data_frame_bolsonaro, 3, 2, 0, 100, count_x, "Jair Bolsonaro", False, True, True, 18, 10, 1.2, -0.21, True, True, 0.4)
    plot_graph("age_bolsonaro_error.png", error_1, 3, 2, -100, 200, count_x, "Jair Bolsonaro - Variation Polls", False, True, True, 18, 10, 1.2, -0.21, False, False, 0.4)    
    
    error_2 = plot_graph("age_haddad.png", GFrame.Age.data_frame_haddad, 3, 2, 0, 60, count_x, "Fernando Haddad", False, True, True, 18, 10, 1.2, -0.21, True, True, 0.4)  
    plot_graph("age_haddad_error.png", error_2, 3, 2, -90, 250, count_x, "Fernando Haddad - Variation Polls", False, True, True, 18, 10, 1.2, -0.21, False, False, 0.4)   

    error_3 = plot_graph("age_ciro.png", GFrame.Age.data_frame_ciro, 3, 2, 0, 60, count_x, "Ciro Gomes", False, True, True, 18, 10, 1.2, -0.21, True, True, 0.4)
    plot_graph("age_ciro_error.png", error_3, 3, 2, -80, 200, count_x, "Ciro Gomes - Variation Polls", False, True, True, 18, 10, 1.2, -0.21, False, False, 0.4)

    error_4 = plot_graph("age_marina.png", GFrame.Age.data_frame_marina, 3, 2, 0, 60, count_x, "Marina Silva", False, True, True, 18, 10, 1.2, -0.21, True, True, 0.4)
    plot_graph("age_marina_error.png", error_4, 3, 2, -70, 100, count_x, "Marina Silva - Variation Polls", False, True, True, 18, 10, 1.2, -0.21, False, False, 0.4)

    error_5 = plot_graph("age_alckmin.png", GFrame.Age.data_frame_alckmin, 3, 2, 0, 60, count_x, "Geraldo Alckmin", False, True, True, 18, 10, 1.2, -0.21, True, True, 0.4)
    plot_graph("age_alckmin_error.png", error_5, 3, 2, -50, 75, count_x, "Geraldo Alckmin - Variation Polls", False, True, True, 18, 10, 1.2, -0.21, False, False, 0.4)

    error_6 = plot_graph("age_alvaro.png", GFrame.Age.data_frame_alvaro, 3, 2, 0, 60, count_x, "Alvaro Dias", False, True, True, 18, 10, 1.2, -0.21, True, True, 0.4)
    plot_graph("age_alvaro_error.png", error_6, 3, 2, -150, 200, count_x, "Alvaro Dias - Variation Polls", False, True, True, 18, 10, 1.2, -0.21, False, False, 0.4)
    # plot_graph("age_lula.png", data_frame_lula, 3, 2, 0, 60, count_x, "Lula", False, True, True, 18, 10, 0.4)

    for i in v_index:
        get_error_agregatte(models.data_reader.candidates[i].facebook_16a24, models.data_reader.candidates[i].ibope_16a24, models.data_reader.candidates[i].dfolha_16a24)
        get_error_agregatte(models.data_reader.candidates[i].facebook_25a34, models.data_reader.candidates[i].ibope_25a34, models.data_reader.candidates[i].dfolha_25a34)
        get_error_agregatte(models.data_reader.candidates[i].facebook_35a44, models.data_reader.candidates[i].ibope_35a44, models.data_reader.candidates[i].dfolha_35a44)
        get_error_agregatte(models.data_reader.candidates[i].facebook_45a54, models.data_reader.candidates[i].ibope_45a54, models.data_reader.candidates[i].dfolha_45a54)
        get_error_agregatte(models.data_reader.candidates[i].facebook_55, models.data_reader.candidates[i].ibope_55, models.data_reader.candidates[i].dfolha_55)
        plot_table_error("age_" + dic_index[i] + "_error.png")

    # plot_graph("age_bolsonaro.png", GFrame.Age.data_frame_bolsonaro, 3, 2, 0, 60, count_x, "Jair Bolsonaro", False, True, True, 18, 10, 0.4)
    # plot_graph("age_haddad.png", GFrame.Age.data_frame_haddad, 3, 2, 0, 60, count_x, "Fernando Haddad", False, True, True, 18, 10, 0.4)    
    # plot_graph("age_ciro.png", GFrame.Age.data_frame_ciro, 3, 2, 0, 60, count_x, "Ciro Gomes", False, True, True, 18, 10, 0.4)
    # plot_graph("age_marina.png", GFrame.Age.data_frame_marina, 3, 2, 0, 60, count_x, "Marina Silva", False, True, True, 18, 10, 0.4)
    # plot_graph("age_alckmin.png", GFrame.Age.data_frame_alckmin, 3, 2, 0, 60, count_x, "Geraldo Alckmin", False, True, True, 18, 10, 0.4)
    # plot_graph("age_alvaro.png", GFrame.Age.data_frame_alvaro, 3, 2, 0, 60, count_x, "Alvaro Dias", False, True, True, 18, 10, 0.4)
    # # plot_graph("age_lula.png", data_frame_lula, 3, 2, 0, 60, count_x, "Lula", False, True, True, 18, 10, 0.4)
   
def plot_education():   
    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_fundamental)

    error_1 = plot_graph("education_1.png", GFrame.Education.data_frame, 3, 3, 0, 75, count_x, "Education", True, False, True, 18, 10, -0.7, -0.19)
    plot_graph("education_1_error.png", error_1, 3, 3, -100, 280, count_x, "Variation Polls", True, False, True, 18, 10, -0.7, -0.25, False, False, False)

    error_2 = plot_graph("education_2.png", GFrame.Education.data_frame2, 3, 3, 0, 75, count_x, "Education", True, False, True, 18, 10, -0.7, -0.19)  
    plot_graph("education_2_error.png", error_2, 3, 3, -100, 150, count_x, "Variation Polls", True, False, True, 18, 10, -0.7, -0.21, False, False, False) 

    for i in v_index:
        get_error_agregatte(models.data_reader.candidates[i].facebook_fundamental, models.data_reader.candidates[i].ibope_fundamental, models.data_reader.candidates[i].dfolha_fundamental)
        get_error_agregatte(models.data_reader.candidates[i].facebook_medio, models.data_reader.candidates[i].ibope_medio, models.data_reader.candidates[i].dfolha_medio)
        get_error_agregatte(models.data_reader.candidates[i].facebook_superior, models.data_reader.candidates[i].ibope_superior, models.data_reader.candidates[i].dfolha_superior)
        plot_table_error("education_" + dic_index[i] + "_error.png")