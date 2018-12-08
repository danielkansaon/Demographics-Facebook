from matplotlib.ticker import FuncFormatter
import read_elections as election
from scipy.stats import spearmanr
import read_facebook as facebook
import matplotlib.pyplot as plt
import data_frames as GFrame
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
i_alvaro = models.return_index("Alvaro Dias")

dic_color = {
        "DataFolha":"green",
        "IBOPE":"red",
        "Facebook": "blue",
        "Variation (DataFolha)":"green",
        "Variation (IBOPE)":"red",

}

dic_lines = {
    "points": [{"x": 5.8, "negative": 0.6, "plus": 7, "text": "#EleNao"}, 
    {"x": 2.7, "negative": 0.6, "plus": 4, "text": "Judgment\n   Lula "}, 
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

def plot_graph_events(range_fim):
     for dic in dic_lines["points"]:
            plt.axvline(x=dic["x"], color='gray', linestyle='--', alpha=0.5)

            if(dic["text"] == "Judgment\n   Lula "):
                plt.text(x = dic["x"] - dic["negative"], y =  range_fim - 8, s = dic["text"], size = 9)  
            else:               
                plt.text(x = dic["x"] - dic["negative"], y =  range_fim - 5, s = dic["text"], size = 9)

def get_error_graph(v_facebook, v_ibope, v_dfolha):
    v_facebook_ibope = []
    v_facebook_dfolha = []

    for i in range(0,15):
        if(v_ibope[i] == 0):
            v_facebook_ibope.append(0)
        elif(v_facebook[i] > 0):
            v_facebook_ibope.append(((v_facebook[i] - v_ibope[i]) / v_ibope[i]) * 100)
        else:
             v_facebook_ibope.append(0)
             
        if(v_dfolha[i] == 0):
            v_facebook_dfolha.append(0)
        elif(v_facebook[i] > 0):
            v_facebook_dfolha.append(((v_facebook[i] - v_dfolha[i]) / v_dfolha[i]) * 100)      
        else:
            v_facebook_dfolha.append(0)  
    
    return v_facebook_dfolha, v_facebook_ibope


def plot_graph(name, data_frame, line, col, range_ini, range_fim, count_x, firstitle, set_subtitle, all_subtitle, set_result, figsizeX, figsizeY, plot_error = True, plot_event = True, hspace=0):    
    fig = plt.figure(figsize=(figsizeX, figsizeY))    
    set_result_aux = set_result
    subtitle_aux = set_subtitle    
    text_1Round = "1º round"
    text_2Round = "2º round"    
    m_before_1round = 0
    m_before_2round = 0  
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
            label = g.split("-")
                        
            if(all_subtitle == False and pos <= col):
                plt.title(label[1], fontsize=12, color='black', loc='center')
            elif(all_subtitle == True):
                plt.title(label[1], fontsize=12, color='black', loc='center')           

            if(set_subtitle == True):                
                plt.ylabel(label[0], multialignment='center', color='gray', fontsize=12)                
                set_subtitle = False
                # , marker='o'

            #Plotando Linhas
            if(plot_error == True):
                plt.plot('x', g, data=d, color=dic_color[label[2]], ls='-', alpha=0.8, label=label[2])
            else:
                plt.plot('x', g, data=d, marker='v', color=dic_color[label[2]], linewidth=2, linestyle='dashed', alpha=0.6, label=label[2])
                plt.axhline(y=0, color='blue', linestyle='-', alpha=0.9)

                text_1Round = str(round(d[g].values[9],1)) + " %"
                text_2Round = str(round(d[g].values[14],1)) + " %"
                legend_result = "Error Facebook %"

                if(m_before_1round < d[g].values[8]):
                    m_before_1round = d[g].values[8]
                if(m_before_2round < d[g].values[13]):
                    m_before_2round =  d[g].values[13]
            
                if(m_before_1round > d[g].values[8]):
                    m_before_1round = d[g].values[8]
                if(m_before_2round > d[g].values[13]):
                    m_before_2round =  d[g].values[13]

            if 'Facebook' in g:
                v_facebook = d[g].values
            if 'DataFolha' in g:
                v_dfolha = d[g].values
            if 'IBOPE' in g:
                v_ibope = d[g].values

            v_labels.append(g)

            #Setando Resultado
            if(set_result_aux == True):     
                if(d[g].values[9] != -100):
                    plt.scatter(9, d[g].values[9], color='darkorange', s=130, alpha=1) 
                    plt.text(x = 9 - 0.5 , y =  d[g].values[9] + 3, s = text_1Round, size = 10)
                elif(d[g].values[9] > 0 or d[g].values[8] > 0):
                    plt.scatter(9, 2, color='darkorange', s=110, alpha=1, label=legend_result) 
                    plt.text(x = 9 - 0.5 , y = 5, s = text_1Round + " %", size = 10)
                    
                if(d[g].values[14] != -100):
                    plt.scatter(14, d[g].values[14], color='darkorange', s=130, alpha=1, label=legend_result)
                    plt.text(x = 14 - 0.5 , y =  d[g].values[14] + 3, s = text_2Round, size = 10)
               
                set_result_aux = False
            
        #Plotando Erro Pesquisas
        if(m_before_1round > 0):
            plt.scatter(8, m_before_1round,  color ='slategrey', s=130, alpha=1, label="Worst Error Pools %")
            plt.text(x = 8 - 0.5 , y = m_before_1round + 3, s = str(round(m_before_1round - d[g].values[9], 1)) + " %", size = 10)         
        if(m_before_2round > 0):
            plt.scatter(13, m_before_2round,  color ='slategrey', s=130, alpha=1) 
            plt.text(x = 13 - 0.5 , y = m_before_2round + 3, s = str(round(m_before_2round - d[g].values[14],1)) + " %", size = 10)
            
        m_before_1round = 0
        m_before_2round = 0
        
            
        if(plot_error == True):
            a, b = get_error_graph(v_facebook, v_ibope, v_dfolha)

            vector_dFrame.append(pd.DataFrame(
            {
                'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
                label[0] + "-" + label[1] + "-Variation (DataFolha)": a, label[0] + "-" + label[1] + "-Variation (IBOPE)": b
            }))

        if(plot_event):
            plot_graph_events(range_fim)    
               
        plt.xticks(range(0, count_x), xticks)   
        plt.legend()        
           
        count_subtitle += 1
        if(count_subtitle == col):
            set_subtitle = subtitle_aux
            count_subtitle = 0
        
        G.set_ylim(range_ini,range_fim)
        set_result_aux = True
        pos += 1 
            
    if(hspace != 0):
        plt.subplots_adjust(hspace=hspace)

    plt.suptitle(firstitle) 
    plt.savefig(name, dpi=100)

    return vector_dFrame
    # plot_graph_error(name.replace(".png","") + "_error.png", vector_dFrame, line, col, range_ini, range_fim, count_x, firstitle, set_subtitle, all_subtitle, set_result, figsizeX, figsizeY)
    # plt.legend(loc='upper center', bbox_to_anchor=(-0.1, -0.21), shadow=True, ncol=2)    

def plot_gender():   
           
    count_x = len(models.data_reader.candidates[0].dfolha_male)
    error_1 = plot_graph("gender_1.png", GFrame.Gender.data_frame_1, 3, 2, 15, 80, count_x, "Gender", True, False, True, 19, 10)
    plot_graph("gender_1_error.png", error_1, 3, 2, -50, 50, count_x, "Variation Compared to Facebook", True, False, True, 19, 10, False, False)
    error_2 = plot_graph("gender_2.png", GFrame.Gender.data_frame_2, 3, 2, 15, 80, count_x, "Gender", True, False, True, 19, 10)
    plot_graph("gender_2_error.png", error_2, 3, 2, -40, 70, count_x, "Variation Compared to Facebook", True, False, True, 19, 10, False, False)
    

def plot_region():
        
    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_sul) 
    plot_graph("region_bolsonaro.png", GFrame.Region.data_frame_bolsonaro, 2, 2, 5, 70, count_x, "Jair Bolsonaro", False, True, True, 18, 10)
    plot_graph("region_haddad.png", GFrame.Region.data_frame_haddad, 2, 2, 5, 90, count_x, "Fernando Haddad", False, True, True, 18, 10)    
    plot_graph("region_ciro.png", GFrame.Region.data_frame_ciro, 2, 2, 5, 60, count_x, "Ciro Gomes", False, True, True, 18, 10)
    plot_graph("region_marina.png", GFrame.Region.data_frame_marina, 2, 2, 5, 70, count_x, "Marina Silva", False, True, True, 18, 10)
    plot_graph("region_alckmin.png", GFrame.Region.data_frame_alckmin, 2, 2, 5, 85, count_x, "Geraldo Alckmin", False, True, True, 18, 10)
    plot_graph("region_alvaro.png", GFrame.Region.data_frame_alvaro, 2, 2, 0, 70, count_x, "Alvaro Dias", False, True, True, 18, 10)
    # plot_graph("region_lula.png", data_frame_lula, 2, 2, 5, 60, count_x, "Lula", False, True, True, 18, 10)

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
            plt.text(x = dic["x"] - dic["negative"], y =  8000000 - 8, s = dic["text"], size = 9)  
        else:               
            plt.text(x = dic["x"] - dic["negative"], y =  8000000 - 5, s = dic["text"], size = 9)  

    plt.axvline(x=9, color='gray', linestyle='--', alpha=0.5) 
    plt.text(x = 9 - dic["negative"], y =  8000000 - 15, s = 'End\n1º Round', size = 9)  
    plt.axvline(x=14, color='gray', linestyle='--', alpha=0.5) 
    plt.text(x = 14 - dic["negative"], y =  8000000 - 15, s = 'End\n2º Round', size = 9)  
    
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
            plt.text(x = dic["x"] - dic["negative"], y =  4700000 - 8, s = dic["text"], size = 9)  
        else:               
            plt.text(x = dic["x"] - dic["negative"], y =  4700000 - 3, s = dic["text"], size = 9)  

    plt.axvline(x=9, color='gray', linestyle='--', alpha=0.5) 
    plt.text(x = 9 - dic["negative"], y =  4800000 - 12000, s = 'End\n1º Round', size = 9)  
    plt.axvline(x=14, color='gray', linestyle='--', alpha=0.5) 
    plt.text(x = 14 - dic["negative"], y =  4800000 - 10000, s = 'End\n2º Round', size = 9)  

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: formatter_millions(int(x))))
    plt.ylabel("Millions (m)", multialignment='center', color='gray', fontsize=12)

    plt.show()    

def plot_age():
    count_x = len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)

    plot_graph("age_bolsonaro.png", GFrame.Age.data_frame_bolsonaro, 3, 2, 0, 60, count_x, "Jair Bolsonaro", False, True, True, 18, 10, 0.4)
    plot_graph("age_haddad.png", GFrame.Age.data_frame_haddad, 3, 2, 0, 60, count_x, "Fernando Haddad", False, True, True, 18, 10, 0.4)    
    plot_graph("age_ciro.png", GFrame.Age.data_frame_ciro, 3, 2, 0, 60, count_x, "Ciro Gomes", False, True, True, 18, 10, 0.4)
    plot_graph("age_marina.png", GFrame.Age.data_frame_marina, 3, 2, 0, 60, count_x, "Marina Silva", False, True, True, 18, 10, 0.4)
    plot_graph("age_alckmin.png", GFrame.Age.data_frame_alckmin, 3, 2, 0, 60, count_x, "Geraldo Alckmin", False, True, True, 18, 10, 0.4)
    plot_graph("age_alvaro.png", GFrame.Age.data_frame_alvaro, 3, 2, 0, 60, count_x, "Alvaro Dias", False, True, True, 18, 10, 0.4)
    # plot_graph("age_lula.png", data_frame_lula, 3, 2, 0, 60, count_x, "Lula", False, True, True, 18, 10, 0.4)
   
def plot_education():   
    count_x = len(models.data_reader.candidates[i_bolsonaro].facebook_fundamental)

    plot_graph("education_1.png", GFrame.Education.data_frame, 3, 3, 0, 75, count_x, "Education", True, False, True, 18, 10)
    plot_graph("education_2.png", GFrame.Education.data_frame2, 3, 3, 0, 75, count_x, "Education", True, False, True, 18, 10)   