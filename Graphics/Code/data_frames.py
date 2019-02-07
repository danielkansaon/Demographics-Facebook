import read_elections as election
import read_facebook as facebook
import pandas as pd
import models

election.read_json(False)
facebook.readJson() 

i_bolsonaro = models.return_index("Jair Bolsonaro")
i_haddad = models.return_index("Fernando Haddad")
i_lula = models.return_index("Lula")
i_ciro = models.return_index("Ciro Gomes")
i_marina = models.return_index("Marina Silva")
i_alckmin = models.return_index("Geraldo Alckmin")
i_alvaro = models.return_index("Alvaro Dias")

d_pesquisa = 1
d_facebook = 100000

class Gender:
    data_frame_1 = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        'Jair Bolsonaro-Male-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_male, 'Jair Bolsonaro-Male-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_male,
        'Jair Bolsonaro-Male-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_male, 
        'Jair Bolsonaro-Male-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Jair Bolsonaro-Male-Distribuition Census': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        'Jair Bolsonaro-Female-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_female, 'Jair Bolsonaro-Female-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_female,
        'Jair Bolsonaro-Female-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_female,
        'Jair Bolsonaro-Female-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Jair Bolsonaro-Female-Distribuition Census': models.data_distribuition.census_gender_female
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Male-DataFolha': models.data_reader.candidates[i_haddad].dfolha_male, 'Fernando Haddad-Male-IBOPE': models.data_reader.candidates[i_haddad].ibope_male,
        'Fernando Haddad-Male-Facebook': models.data_reader.candidates[i_haddad].facebook_male,
        'Fernando Haddad-Male-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Fernando Haddad-Male-Distribuition Census': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Female-DataFolha': models.data_reader.candidates[i_haddad].dfolha_female, 'Fernando Haddad-Female-IBOPE': models.data_reader.candidates[i_haddad].ibope_female,
        'Fernando Haddad-Female-Facebook': models.data_reader.candidates[i_haddad].facebook_female,
        'Fernando Haddad-Female-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Fernando Haddad-Female-Distribuition Census': models.data_distribuition.census_gender_female
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Male-DataFolha': models.data_reader.candidates[i_ciro].dfolha_male, 'Ciro Gomes-Male-IBOPE': models.data_reader.candidates[i_ciro].ibope_male,
        'Ciro Gomes-Male-Facebook': models.data_reader.candidates[i_ciro].facebook_male,
        'Ciro Gomes-Male-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Ciro Gomes-Male-Distribuition Census': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Female-DataFolha': models.data_reader.candidates[i_ciro].dfolha_female, 'Ciro Gomes-Female-IBOPE': models.data_reader.candidates[i_ciro].ibope_female,
        'Ciro Gomes-Female-Facebook': models.data_reader.candidates[i_ciro].facebook_female,
        'Ciro Gomes-Female-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Ciro Gomes-Female-Distribuition Census': models.data_distribuition.census_gender_female
    })
    # ,
    # pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Male-DataFolha': models.data_reader.candidates[i_lula].dfolha_male, 'Lula-Male-IBOPE': models.data_reader.candidates[i_lula].ibope_male,
    #     'Lula-Male-Facebook': models.data_reader.candidates[i_lula].facebook_male
    # }),
    # pd.DataFrame({'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Female-DataFolha': models.data_reader.candidates[i_lula].dfolha_female, 'Lula-Female-IBOPE': models.data_reader.candidates[i_lula].ibope_female,
    #     'Lula-Female-Facebook': models.data_reader.candidates[i_lula].facebook_female
    # })
    ]

    data_frame_2 = [pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Male-DataFolha': models.data_reader.candidates[i_marina].dfolha_male, 'Marina Silva-Male-IBOPE': models.data_reader.candidates[i_marina].ibope_male,
        'Marina Silva-Male-Facebook': models.data_reader.candidates[i_marina].facebook_male,
        'Marina Silva-Male-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Marina Silva-Male-Distribuition Census': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Female-DataFolha': models.data_reader.candidates[i_marina].dfolha_female, 'Marina Silva-Female-IBOPE': models.data_reader.candidates[i_marina].ibope_female,
        'Marina Silva-Female-Facebook': models.data_reader.candidates[i_marina].facebook_female,
        'Marina Silva-Female-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Marina Silva-Female-Distribuition Census': models.data_distribuition.census_gender_female
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Male-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_male, 'Geraldo Alckmin-Male-IBOPE': models.data_reader.candidates[i_alckmin].ibope_male,
        'Geraldo Alckmin-Male-Facebook': models.data_reader.candidates[i_alckmin].facebook_male,
        'Geraldo Alckmin-Male-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Geraldo Alckmin-Male-Distribuition Census': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame({'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Female-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_female, 'Geraldo Alckmin-Female-IBOPE': models.data_reader.candidates[i_alckmin].ibope_female,
        'Geraldo Alckmin-Female-Facebook': models.data_reader.candidates[i_alckmin].facebook_female,
        'Geraldo Alckmin-Female-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Geraldo Alckmin-Female-Distribuition Census': models.data_distribuition.census_gender_female
    })
    # ,pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
    #     'Alvaro Dias-Male-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_male, 'Alvaro Dias-Male-IBOPE': models.data_reader.candidates[i_alvaro].ibope_male,
    #     'Alvaro Dias-Male-Facebook': models.data_reader.candidates[i_alvaro].facebook_male,
    #     'Alvaro Dias-Male-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
    #     'Alvaro Dias-Male-Distribuition Census': models.data_distribuition.census_gender_male
    # }),
    # pd.DataFrame({'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
    #     'Alvaro Dias-Female-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_female, 'Alvaro Dias-Female-IBOPE': models.data_reader.candidates[i_alvaro].ibope_female,
    #     'Alvaro Dias-Female-Facebook': models.data_reader.candidates[i_alvaro].facebook_female,
    #     'Alvaro Dias-Female-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
    #     'Alvaro Dias-Female-Distribuition Census': models.data_distribuition.census_gender_female
    # })
    ]

class Region:
    data_frame_bolsonaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Southeast-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_sudeste, 'Jair Bolsonaro-Southeast-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_sudeste,
        'Jair Bolsonaro-Southeast-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_sudeste,
        'Jair Bolsonaro-Southeast-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Jair Bolsonaro-Southeast-Distribuition Census': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Northeast-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_nordeste, 'Jair Bolsonaro-Northeast-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_nordeste,
        'Jair Bolsonaro-Northeast-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_nordeste,
        'Jair Bolsonaro-Northeast-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Jair Bolsonaro-Northeast-Distribuition Census': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-North/Center West-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_norte_coeste, 'Jair Bolsonaro-North/Center West-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_norte_coeste,
        'Jair Bolsonaro-North/Center West-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_norte_coeste,
        'Jair Bolsonaro-North/Center West-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Jair Bolsonaro-North/Center West-Distribuition Census': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-South-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_sul, 'Jair Bolsonaro-South-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_sul,
        'Jair Bolsonaro-South-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_sul,
        'Jair Bolsonaro-South-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Jair Bolsonaro-South-Distribuition Census': models.data_distribuition.census_region_sul
    })]

    data_frame_haddad = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
        'Fernando Haddad-Southeast-DataFolha': models.data_reader.candidates[i_haddad].dfolha_sudeste, 'Fernando Haddad-Southeast-IBOPE': models.data_reader.candidates[i_haddad].ibope_sudeste,
        'Fernando Haddad-Southeast-Facebook': models.data_reader.candidates[i_haddad].facebook_sudeste,
        'Fernando Haddad-Southeast-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Fernando Haddad-Southeast-Distribuition Census': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
        'Fernando Haddad-Northeast-DataFolha': models.data_reader.candidates[i_haddad].dfolha_nordeste, 'Fernando Haddad-Northeast-IBOPE': models.data_reader.candidates[i_haddad].ibope_nordeste,
        'Fernando Haddad-Northeast-Facebook': models.data_reader.candidates[i_haddad].facebook_nordeste,
        'Fernando Haddad-Northeast-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Fernando Haddad-Northeast-Distribuition Census': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
        'Fernando Haddad-North/Center West-DataFolha': models.data_reader.candidates[i_haddad].dfolha_norte_coeste, 'Fernando Haddad-North/Midwest Oeste-IBOPE': models.data_reader.candidates[i_haddad].ibope_norte_coeste,
        'Fernando Haddad-North/Center West-Facebook': models.data_reader.candidates[i_haddad].facebook_norte_coeste,
        'Fernando Haddad-North/Center West-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Fernando Haddad-North/Center West-Distribuition Census': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
        'Fernando Haddad-South-DataFolha': models.data_reader.candidates[i_haddad].dfolha_sul, 'Fernando Haddad-South-IBOPE': models.data_reader.candidates[i_haddad].ibope_sul,
        'Fernando Haddad-South-Facebook': models.data_reader.candidates[i_haddad].facebook_sul,
        'Fernando Haddad-South-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Fernando Haddad-South-Distribuition Census': models.data_distribuition.census_region_sul
    })]

    data_frame_lula = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
        'Lula-Southeast-DataFolha': models.data_reader.candidates[i_lula].dfolha_sudeste, 'Lula-Southeast-IBOPE': models.data_reader.candidates[i_lula].ibope_sudeste,
        'Lula-Southeast-Facebook': models.data_reader.candidates[i_lula].facebook_sudeste,
        'Lula-Southeast-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Lula-Southeast-Distribuition Census': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
        'Lula-Northeast-DataFolha': models.data_reader.candidates[i_lula].dfolha_nordeste, 'Lula-Northeast-IBOPE': models.data_reader.candidates[i_lula].ibope_nordeste,
        'Lula-Northeast-Facebook': models.data_reader.candidates[i_lula].facebook_nordeste,
        'Lula-Northeast-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Lula-Northeast-Distribuition Census': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
        'Lula-North/Center West-DataFolha': models.data_reader.candidates[i_lula].dfolha_norte_coeste, 'Lula-North/Center West-IBOPE': models.data_reader.candidates[i_lula].ibope_norte_coeste,
        'Lula-North/Center West-Facebook': models.data_reader.candidates[i_lula].facebook_norte_coeste,
        'Lula-North/Center West-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Lula-North/Center West-Distribuition Census': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
        'Lula-South-DataFolha': models.data_reader.candidates[i_lula].dfolha_sul, 'Lula-South-IBOPE': models.data_reader.candidates[i_lula].ibope_sul,
        'Lula-South-Facebook': models.data_reader.candidates[i_lula].facebook_sul,
        'Lula-South-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Lula-South-Distribuition Census': models.data_distribuition.census_region_sul
    })]

    data_frame_ciro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
        'Ciro Gomes-Southeast-DataFolha': models.data_reader.candidates[i_ciro].dfolha_sudeste, 'Ciro Gomes-Southeast-IBOPE': models.data_reader.candidates[i_ciro].ibope_sudeste,
        'Ciro Gomes-Southeast-Facebook': models.data_reader.candidates[i_ciro].facebook_sudeste,
        'Ciro Gomes-Southeast-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Ciro Gomes-Southeast-Distribuition Census': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
        'Ciro Gomes-Northeast-DataFolha': models.data_reader.candidates[i_ciro].dfolha_nordeste, 'Ciro Gomes-Northeast-IBOPE': models.data_reader.candidates[i_ciro].ibope_nordeste,
        'Ciro Gomes-Northeast-Facebook': models.data_reader.candidates[i_ciro].facebook_nordeste,
        'Ciro Gomes-Northeast-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Ciro Gomes-Northeast-Distribuition Census': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
        'Ciro Gomes-North/Center West-DataFolha': models.data_reader.candidates[i_ciro].dfolha_norte_coeste, 'Ciro Gomes-North/Center West-IBOPE': models.data_reader.candidates[i_ciro].ibope_norte_coeste,
        'Ciro Gomes-North/Center West-Facebook': models.data_reader.candidates[i_ciro].facebook_norte_coeste,
        'Ciro Gomes-North/Center West-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Ciro Gomes-North/Center West-Distribuition Census': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
        'Ciro Gomes-South-DataFolha': models.data_reader.candidates[i_ciro].dfolha_sul, 'Ciro Gomes-South-IBOPE': models.data_reader.candidates[i_ciro].ibope_sul,
        'Ciro Gomes-South-Facebook': models.data_reader.candidates[i_ciro].facebook_sul,
        'Ciro Gomes-South-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Ciro Gomes-South-Distribuition Census': models.data_distribuition.census_region_sul
    })]

    data_frame_marina = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
        'Marina Silva-Southeast-DataFolha': models.data_reader.candidates[i_marina].dfolha_sudeste, 'Ciro Gomes-Southeast-IBOPE': models.data_reader.candidates[i_marina].ibope_sudeste,
        'Marina Silva-Southeast-Facebook': models.data_reader.candidates[i_marina].facebook_sudeste,
        'Marina Silva-Southeast-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Marina Silva-Southeast-Distribuition Census': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
        'Marina Silva-Northeast-DataFolha': models.data_reader.candidates[i_marina].dfolha_nordeste, 'Marina Silva-Northeast-IBOPE': models.data_reader.candidates[i_marina].ibope_nordeste,
        'Marina Silva-Northeast-Facebook': models.data_reader.candidates[i_marina].facebook_nordeste,
        'Marina Silva-Northeast-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Marina Silva-Northeast-Distribuition Census': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
        'Marina Silva-North/Center West-DataFolha': models.data_reader.candidates[i_marina].dfolha_norte_coeste, 'Marina Silva-North/Center West-IBOPE': models.data_reader.candidates[i_marina].ibope_norte_coeste,
        'Marina Silva-North/Center West-Facebook': models.data_reader.candidates[i_marina].facebook_norte_coeste,
        'Marina Silva-North/Center West-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Marina Silva-North/Center West-Distribuition Census': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
        'Marina Silva-South-DataFolha': models.data_reader.candidates[i_marina].dfolha_sul, 'Marina Silva-South-IBOPE': models.data_reader.candidates[i_marina].ibope_sul,
        'Marina Silva-South-Facebook': models.data_reader.candidates[i_marina].facebook_sul,
        'Marina Silva-South-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Marina Silva-South-Distribuition Census': models.data_distribuition.census_region_sul
    })]

    data_frame_alckmin = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-Southeast-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_sudeste, 'Geraldo Alckmin-Southeast-IBOPE': models.data_reader.candidates[i_alckmin].ibope_sudeste,
        'Geraldo Alckmin-Southeast-Facebook': models.data_reader.candidates[i_alckmin].facebook_sudeste,
        'Geraldo Alckmin-Southeast-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Geraldo Alckmin-Southeast-Distribuition Census': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-Northeast-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_nordeste, 'Geraldo Alckmin-Northeast-IBOPE': models.data_reader.candidates[i_alckmin].ibope_nordeste,
        'Geraldo Alckmin-Northeast-Facebook': models.data_reader.candidates[i_alckmin].facebook_nordeste,
        'Geraldo Alckmin-Northeast-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Geraldo Alckmin-Northeast-Distribuition Census': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-North/Center West-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_norte_coeste, 'Geraldo Alckmin-North/Center West-IBOPE': models.data_reader.candidates[i_alckmin].ibope_norte_coeste,
        'Geraldo Alckmin-North/Center West-Facebook': models.data_reader.candidates[i_alckmin].facebook_norte_coeste,
        'Geraldo Alckmin-North/Center West-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Geraldo Alckmin-North/Center West-Distribuition Census': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-South-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_sul, 'Geraldo Alckmin-South-IBOPE': models.data_reader.candidates[i_alckmin].ibope_sul,
        'Geraldo Alckmin-South-Facebook': models.data_reader.candidates[i_alckmin].facebook_sul,
        'Geraldo Alckmin-South-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Geraldo Alckmin-South-Distribuition Census': models.data_distribuition.census_region_sul
    })]

    data_frame_alvaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Southeast-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_sudeste, 'Alvaro Dias-Southeast-IBOPE': models.data_reader.candidates[i_alvaro].ibope_sudeste,
        'Alvaro Dias-Southeast-Facebook': models.data_reader.candidates[i_alvaro].facebook_sudeste,
        'Alvaro Dias-Southeast-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Alvaro Dias-Southeast-Distribuition Census': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Northeast-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_nordeste, 'Alvaro Dias-Northeast-IBOPE': models.data_reader.candidates[i_alvaro].ibope_nordeste,
        'Alvaro Dias-Northeast-Facebook': models.data_reader.candidates[i_alvaro].facebook_nordeste,
        'Alvaro Dias-Northeast-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Alvaro Dias-Northeast-Distribuition Census': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-North/Center West-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_norte_coeste, 'Geraldo Alckmin-North/Center West-IBOPE': models.data_reader.candidates[i_alvaro].ibope_norte_coeste,
        'Alvaro Dias-North/Center West-Facebook': models.data_reader.candidates[i_alvaro].facebook_norte_coeste,
        'Alvaro Dias-North/Center West-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Alvaro Dias-North/Center West-Distribuition Census': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-South-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_sul, 'Alvaro Dias-South-IBOPE': models.data_reader.candidates[i_alvaro].ibope_sul,
        'Alvaro Dias-South-Facebook': models.data_reader.candidates[i_alvaro].facebook_sul,
        'Alvaro Dias-South-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Alvaro Dias-South-Distribuition Census': models.data_distribuition.census_region_sul
    })]

class Age:
    # AGE
    data_frame_bolsonaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
        'Jair Bolsonaro-16 a 24-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_16a24, 'Jair Bolsonaro-16 a 24-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_16a24,
        'Jair Bolsonaro-16 a 24-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_16a24,
        'Jair Bolsonaro-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Jair Bolsonaro-16 a 24-Distribuition Census': models.data_distribuition.census_age_16a24      
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_25a34)), 
        'Jair Bolsonaro-25 a 34-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_25a34, 'Jair Bolsonaro-25 a 34-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_25a34,
        'Jair Bolsonaro-25 a 34-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_25a34,
        'Jair Bolsonaro-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Jair Bolsonaro-25 a 34-Distribuition Census': models.data_distribuition.census_age_25a34              
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
        'Jair Bolsonaro-35 a 44-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_35a44, 'Jair Bolsonaro-35 a 44-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_35a44,
        'Jair Bolsonaro-35 a 44-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_35a44,
        'Jair Bolsonaro-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Jair Bolsonaro-35 a 44-Distribuition Census': models.data_distribuition.census_age_35a44            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
        'Jair Bolsonaro-45 a 54-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_45a54, 'Jair Bolsonaro-45 a 54-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_45a54,
        'Jair Bolsonaro-45 a 54-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_45a54,
        'Jair Bolsonaro-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Jair Bolsonaro-45 a 54-Distribuition Census': models.data_distribuition.census_age_45a54           
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
        'Jair Bolsonaro-Acima de 55-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_55, 'Jair Bolsonaro-Acima de 55-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_55,
        'Jair Bolsonaro-Acima de 55-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_55,
        'Jair Bolsonaro-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Jair Bolsonaro-Acima de 55-Distribuition Census': models.data_distribuition.census_age_acima55             
    })]

    data_frame_haddad = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-16 a 24-DataFolha': models.data_reader.candidates[i_haddad].dfolha_16a24, 'Fernando Haddado-16 a 24-IBOPE': models.data_reader.candidates[i_haddad].ibope_16a24,
        'Fernando Haddad-16 a 24-Facebook': models.data_reader.candidates[i_haddad].facebook_16a24,
        'Fernando Haddad-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Fernando Haddad-16 a 24-Distribuition Census': models.data_distribuition.census_age_16a24              
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-25 a 34-DataFolha': models.data_reader.candidates[i_haddad].dfolha_25a34, 'Fernando Haddad-25 a 34-IBOPE': models.data_reader.candidates[i_haddad].ibope_25a34,
        'Fernando Haddad-25 a 34-Facebook': models.data_reader.candidates[i_haddad].facebook_25a34,
        'Fernando Haddad-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Fernando Haddad-25 a 34-Distribuition Census': models.data_distribuition.census_age_25a34               
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-35 a 44-DataFolha': models.data_reader.candidates[i_haddad].dfolha_35a44, 'Fernando Haddad-35 a 44-IBOPE': models.data_reader.candidates[i_haddad].ibope_35a44,
        'Fernando Haddad-35 a 44-Facebook': models.data_reader.candidates[i_haddad].facebook_35a44,
        'Fernando Haddad-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Fernando Haddad-35 a 44-Distribuition Census': models.data_distribuition.census_age_35a44             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-45 a 54-DataFolha': models.data_reader.candidates[i_haddad].dfolha_45a54, 'Fernando Haddad-45 a 54-IBOPE': models.data_reader.candidates[i_haddad].ibope_45a54,
        'Fernando Haddad-45 a 54-Facebook': models.data_reader.candidates[i_haddad].facebook_45a54,
        'Fernando Haddad-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Fernando Haddad-45 a 54-Distribuition Census': models.data_distribuition.census_age_45a54             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-Acima de 55-DataFolha': models.data_reader.candidates[i_haddad].dfolha_55, 'Fernando Haddad-Acima de 55-IBOPE': models.data_reader.candidates[i_haddad].ibope_55,
        'Fernando Haddad-Acima de 55-Facebook': models.data_reader.candidates[i_haddad].facebook_55,
        'Fernando Haddad-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Fernando Haddad-Acima de 55-Distribuition Census': models.data_distribuition.census_age_acima55          
    })]

    data_frame_lula = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-16 a 24-DataFolha': models.data_reader.candidates[i_lula].dfolha_16a24, 'Lula-16 a 24-IBOPE': models.data_reader.candidates[i_lula].ibope_16a24,
        'Lula-16 a 24-Facebook': models.data_reader.candidates[i_lula].facebook_16a24,
        'Lula-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Lula-16 a 24-Distribuition Census': models.data_distribuition.census_age_16a24             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-25 a 34-DataFolha': models.data_reader.candidates[i_lula].dfolha_25a34, 'Lula-25 a 34-IBOPE': models.data_reader.candidates[i_lula].ibope_25a34,
        'Lula-25 a 34-Facebook': models.data_reader.candidates[i_lula].facebook_25a34,
        'Lula-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Lula-25 a 34-Distribuition Census': models.data_distribuition.census_age_25a34            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-35 a 44-DataFolha': models.data_reader.candidates[i_lula].dfolha_35a44, 'Lula-35 a 44-IBOPE': models.data_reader.candidates[i_lula].ibope_35a44,
        'Lula-35 a 44-Facebook': models.data_reader.candidates[i_lula].facebook_35a44,
        'Lula-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Lula-35 a 44-Distribuition Census': models.data_distribuition.census_age_35a44            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-45 a 54-DataFolha': models.data_reader.candidates[i_lula].dfolha_45a54, 'Lula-45 a 54-IBOPE': models.data_reader.candidates[i_lula].ibope_45a54,
        'Lula-45 a 54-Facebook': models.data_reader.candidates[i_lula].facebook_45a54,
        'Lula-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Lula-45 a 54-Distribuition Census': models.data_distribuition.census_age_45a54           
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-Acima de 55-DataFolha': models.data_reader.candidates[i_lula].dfolha_55, 'Lula-Acima de 55-IBOPE': models.data_reader.candidates[i_lula].ibope_55,
        'Lula-Acima de 55-Facebook': models.data_reader.candidates[i_lula].facebook_55,
        'Lula-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Lula-Acima de 55-Distribuition Census': models.data_distribuition.census_age_acima55           
    })]

    data_frame_ciro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-16 a 24-DataFolha': models.data_reader.candidates[i_ciro].dfolha_16a24, 'Ciro Gomes-16 a 24-IBOPE': models.data_reader.candidates[i_ciro].ibope_16a24,
        'Ciro Gomes-16 a 24-Facebook': models.data_reader.candidates[i_ciro].facebook_16a24,
        'Ciro Gomes-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Ciro Gomes-16 a 24-Distribuition Census': models.data_distribuition.census_age_16a24             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-25 a 34-DataFolha': models.data_reader.candidates[i_ciro].dfolha_25a34, 'Ciro Gomes-25 a 34-IBOPE': models.data_reader.candidates[i_ciro].ibope_25a34,
        'Ciro Gomes-25 a 34-Facebook': models.data_reader.candidates[i_ciro].facebook_25a34,
        'Ciro Gomes-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Ciro Gomes-25 a 34-Distribuition Census': models.data_distribuition.census_age_25a34             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-35 a 44-DataFolha': models.data_reader.candidates[i_ciro].dfolha_35a44, 'Ciro Gomes-35 a 44-IBOPE': models.data_reader.candidates[i_ciro].ibope_35a44,
        'Ciro Gomes-35 a 44-Facebook': models.data_reader.candidates[i_ciro].facebook_35a44,
        'Ciro Gomes-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Ciro Gomes-35 a 44-Distribuition Census': models.data_distribuition.census_age_35a44             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-45 a 54-DataFolha': models.data_reader.candidates[i_ciro].dfolha_45a54, 'Ciro Gomes-45 a 54-IBOPE': models.data_reader.candidates[i_ciro].ibope_45a54,
        'Ciro Gomes-45 a 54-Facebook': models.data_reader.candidates[i_ciro].facebook_45a54,
        'Ciro Gomes-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Ciro Gomes-45 a 54-Distribuition Census': models.data_distribuition.census_age_45a54           
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-Acima de 55-DataFolha': models.data_reader.candidates[i_ciro].dfolha_55, 'Ciro Gomes-Acima de 55-IBOPE': models.data_reader.candidates[i_ciro].ibope_55,
        'Ciro Gomes-Acima de 55-Facebook': models.data_reader.candidates[i_ciro].facebook_55,
        'Ciro Gomes-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Ciro Gomes-Acima de 55-Distribuition Census': models.data_distribuition.census_age_acima55          
    })]

    data_frame_marina = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-16 a 24-DataFolha': models.data_reader.candidates[i_marina].dfolha_16a24, 'Marina Silva-16 a 24-IBOPE': models.data_reader.candidates[i_marina].ibope_16a24,
        'Marina Silva-16 a 24-Facebook': models.data_reader.candidates[i_marina].facebook_16a24,
        'Marina Silva-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Marina Silva-16 a 24-Distribuition Census': models.data_distribuition.census_age_16a24             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-25 a 34-DataFolha': models.data_reader.candidates[i_marina].dfolha_25a34, 'Marina Silva-25 a 34-IBOPE': models.data_reader.candidates[i_marina].ibope_25a34,
        'Marina Silva-25 a 34-Facebook': models.data_reader.candidates[i_marina].facebook_25a34,
        'Marina Silva-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Marina Silva-25 a 34-Distribuition Census': models.data_distribuition.census_age_25a34            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-35 a 44-DataFolha': models.data_reader.candidates[i_marina].dfolha_35a44, 'Marina Silva-35 a 44-IBOPE': models.data_reader.candidates[i_marina].ibope_35a44,
        'Marina Silva-35 a 44-Facebook': models.data_reader.candidates[i_marina].facebook_35a44,
        'Marina Silva-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Marina Silva-35 a 44-Distribuition Census': models.data_distribuition.census_age_35a44              
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-45 a 54-DataFolha': models.data_reader.candidates[i_marina].dfolha_45a54, 'Marina Silva-45 a 54-IBOPE': models.data_reader.candidates[i_marina].ibope_45a54,
        'Marina Silva-45 a 54-Facebook': models.data_reader.candidates[i_marina].facebook_45a54,
        'Marina Silva-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Marina Silva-45 a 54-Distribuition Census': models.data_distribuition.census_age_45a54          
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-Acima de 55-DataFolha': models.data_reader.candidates[i_marina].dfolha_55, 'Marina Silva-Acima de 55-IBOPE': models.data_reader.candidates[i_marina].ibope_55,
        'Marina Silva-Acima de 55-Facebook': models.data_reader.candidates[i_marina].facebook_55,
        'Marina Silva-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Marina Silva-Acima de 55-Distribuition Census': models.data_distribuition.census_age_acima55          
    })]

    data_frame_alckmin = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-16 a 24-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_16a24, 'Geraldo Alckmin-16 a 24-IBOPE': models.data_reader.candidates[i_alckmin].ibope_16a24,
        'Geraldo Alckmin-16 a 24-Facebook': models.data_reader.candidates[i_alckmin].facebook_16a24,
        'Geraldo Alckmin-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Geraldo Alckmin-16 a 24-Distribuition Census': models.data_distribuition.census_age_16a24             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-25 a 34-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_25a34, 'Geraldo Alckmin-25 a 34-IBOPE': models.data_reader.candidates[i_alckmin].ibope_25a34,
        'Geraldo Alckmin-25 a 34-Facebook': models.data_reader.candidates[i_alckmin].facebook_25a34,
        'Geraldo Alckmin-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Geraldo Alckmin-25 a 34-Distribuition Census': models.data_distribuition.census_age_25a34             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-35 a 44-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_35a44, 'Geraldo Alckmin-35 a 44-IBOPE': models.data_reader.candidates[i_alckmin].ibope_35a44,
        'Geraldo Alckmin-35 a 44-Facebook': models.data_reader.candidates[i_alckmin].facebook_35a44,
        'Geraldo Alckmin-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Geraldo Alckmin-35 a 44-Distribuition Census': models.data_distribuition.census_age_35a44            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-45 a 54-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_45a54, 'Geraldo Alckmin-45 a 54-IBOPE': models.data_reader.candidates[i_alckmin].ibope_45a54,
        'Geraldo Alckmin-45 a 54-Facebook': models.data_reader.candidates[i_alckmin].facebook_45a54,
        'Geraldo Alckmin-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Geraldo Alckmin-45 a 54-Distribuition Census': models.data_distribuition.census_age_45a54          
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-Acima de 55-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_55, 'Geraldo Alckmin-Acima de 55-IBOPE': models.data_reader.candidates[i_alckmin].ibope_55,
        'Geraldo Alckmin-Acima de 55-Facebook': models.data_reader.candidates[i_alckmin].facebook_55,
        'Geraldo Alckmin-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Geraldo Alckmin-Acima de 55-Distribuition Census': models.data_distribuition.census_age_acima55          
    })]

    data_frame_alvaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-16 a 24-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_16a24, 'Alvaro Dias-16 a 24-IBOPE': models.data_reader.candidates[i_alvaro].ibope_16a24,
        'Alvaro Dias-16 a 24-Facebook': models.data_reader.candidates[i_alvaro].facebook_16a24,
        'Alvaro Dias-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Alvaro Dias-16 a 24-Distribuition Census': models.data_distribuition.census_age_16a24            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-25 a 34-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_25a34, 'Alvaro Dias-25 a 34-IBOPE': models.data_reader.candidates[i_alvaro].ibope_25a34,
        'Alvaro Dias-25 a 34-Facebook': models.data_reader.candidates[i_alvaro].facebook_25a34,
        'Alvaro Dias-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Alvaro Dias-25 a 34-Distribuition Census': models.data_distribuition.census_age_25a34             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-35 a 44-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_35a44, 'Alvaro Dias-35 a 44-IBOPE': models.data_reader.candidates[i_alvaro].ibope_35a44,
        'Alvaro Dias-35 a 44-Facebook': models.data_reader.candidates[i_alvaro].facebook_35a44,
        'Alvaro Dias-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Alvaro Dias-35 a 44-Distribuition Census': models.data_distribuition.census_age_35a44            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-45 a 54-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_45a54, 'Alvaro Dias-45 a 54-IBOPE': models.data_reader.candidates[i_alvaro].ibope_45a54,
        'Alvaro Dias-45 a 54-Facebook': models.data_reader.candidates[i_alvaro].facebook_45a54,
        'Alvaro Dias-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Alvaro Dias-45 a 54-Distribuition Census': models.data_distribuition.census_age_45a54          
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-Acima de 55-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_55, 'Alvaro Dias-Acima de 55-IBOPE': models.data_reader.candidates[i_alvaro].ibope_55,
        'Alvaro Dias-Acima de 55-Facebook': models.data_reader.candidates[i_alvaro].facebook_55,
        'Alvaro Dias-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Alvaro Dias-Acima de 55-Distribuition Census': models.data_distribuition.census_age_acima55          
    })]


class Education:
    # EDUCATION
    data_frame = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        'Jair Bolsonaro-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_fundamental, 'Jair Bolsonaro-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_fundamental,
        'Jair Bolsonaro-Ensino Fundamental-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_fundamental
        # 'Jair Bolsonaro-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Jair Bolsonaro-Ensino Fundamental-Distribuition Census': models.data_distribuition.census_education_fundamental        
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        'Jair Bolsonaro-Ensino Médio-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_medio, 'Jair Bolsonaro-Ensino Médio-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_medio,
        'Jair Bolsonaro-Ensino Médio-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_medio
        # 'Jair Bolsonaro-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Jair Bolsonaro-Ensino Médio-Distribuition Census': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        'Jair Bolsonaro-Ensino Superior-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_superior, 'Jair Bolsonaro-Ensino Superior-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_superior,
        'Jair Bolsonaro-Ensino Superior-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_superior
        # 'Jair Bolsonaro-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Jair Bolsonaro-Ensino Superior-Distribuition Census': models.data_distribuition.census_education_superior
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_haddad].dfolha_fundamental, 'Fernando Haddad-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_haddad].ibope_fundamental,
        'Fernando Haddad-Ensino Fundamental-Facebook': models.data_reader.candidates[i_haddad].facebook_fundamental
        # 'Fernando Haddad-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Fernando Haddad-Ensino Fundamental-Distribuition Census': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Ensino Médio-DataFolha': models.data_reader.candidates[i_haddad].dfolha_medio, 'Fernando Haddad-Ensino Médio-IBOPE': models.data_reader.candidates[i_haddad].ibope_medio,
        'Fernando Haddad-Ensino Médio-Facebook': models.data_reader.candidates[i_haddad].facebook_medio
        # 'Fernando Haddad-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Fernando Haddad-Ensino Médio-Distribuition Census': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Ensino Superior-DataFolha': models.data_reader.candidates[i_haddad].dfolha_superior, 'Fernando Haddad-Ensino Superior-IBOPE': models.data_reader.candidates[i_haddad].ibope_superior,
        'Fernando Haddad-Ensino Superior-Facebook': models.data_reader.candidates[i_haddad].facebook_superior
        # 'Fernando Haddad-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Fernando Haddad-Ensino Superior-Distribuition Census': models.data_distribuition.census_education_superior
    }),
    # pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_lula].dfolha_fundamental, 'Lula-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_lula].ibope_fundamental,
    #     'Lula-Ensino Fundamental-Facebook': models.data_reader.candidates[i_lula].facebook_fundamental
    # }),
    # pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Ensino Médio-DataFolha': models.data_reader.candidates[i_lula].dfolha_medio, 'Lula-Ensino Médio-IBOPE': models.data_reader.candidates[i_lula].ibope_medio,
    #     'Lula-Ensino Médioo-Facebook': models.data_reader.candidates[i_lula].facebook_medio
    # }),
    # pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Ensino Superior-DataFolha': models.data_reader.candidates[i_lula].dfolha_superior, 'Lula-Ensino Superior-IBOPE': models.data_reader.candidates[i_lula].ibope_superior,
    #     'Lula-Ensino Superior-Facebook': models.data_reader.candidates[i_lula].facebook_superior
    # })
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_ciro].dfolha_fundamental, 'Ciro Gomes-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_ciro].ibope_fundamental,
        'Ciro Gomes-Ensino Fundamental-Facebook': models.data_reader.candidates[i_ciro].facebook_fundamental
        # 'Ciro Gomes-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Ciro Gomes-Ensino Fundamental-Distribuition Census': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Ensino Médio-DataFolha': models.data_reader.candidates[i_ciro].dfolha_medio, 'Ciro Gomes-Ensino Médio-IBOPE': models.data_reader.candidates[i_ciro].ibope_medio,
        'Ciro Gomes-Ensino Médio-Facebook': models.data_reader.candidates[i_ciro].facebook_medio
        # 'Ciro Gomes-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Ciro Gomes-Ensino Médio-Distribuition Census': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Ensino Superior-DataFolha': models.data_reader.candidates[i_ciro].dfolha_superior, 'Ciro Gomes-Ensino Superior-IBOPE': models.data_reader.candidates[i_ciro].ibope_superior,
        'Ciro Gomes-Ensino Superior-Facebook': models.data_reader.candidates[i_ciro].facebook_superior
        # 'Ciro Gomes-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Ciro Gomes-Ensino Superior-Distribuition Census': models.data_distribuition.census_education_superior
    })]

    data_frame2 = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_marina].dfolha_fundamental, 'Marina Silva-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_marina].ibope_fundamental,
        'Marina Silva-Ensino Fundamental-Facebook': models.data_reader.candidates[i_marina].facebook_fundamental
        # 'Marina Silva-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Marina Silva-Ensino Fundamental-Distribuition Census': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Ensino Médio-DataFolha': models.data_reader.candidates[i_marina].dfolha_medio, 'Marina Silva-Ensino Médio-IBOPE': models.data_reader.candidates[i_marina].ibope_medio,
        'Marina Silva-Ensino Médio-Facebook': models.data_reader.candidates[i_marina].facebook_medio
        # 'Marina Silva-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Marina Silva-Ensino Médio-Distribuition Census': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Ensino Superior-DataFolha': models.data_reader.candidates[i_marina].dfolha_superior, 'Marina Silva-Ensino Superior-IBOPE': models.data_reader.candidates[i_marina].ibope_superior,
        'Marina Silva-Ensino Superior-Facebook': models.data_reader.candidates[i_marina].facebook_superior
        # 'Marina Silva-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Marina Silva-Ensino Superior-Distribuition Census': models.data_distribuition.census_education_superior
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_fundamental, 'Geraldo Alckmin-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_alckmin].ibope_fundamental,
        'Geraldo Alckmin-Ensino Fundamental-Facebook': models.data_reader.candidates[i_alckmin].facebook_fundamental
        # 'Geraldo Alckmin-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Geraldo Alckmin-Ensino Fundamental-Distribuition Census': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Ensino Médio-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_medio, 'Geraldo Alckmin-Ensino Médio-IBOPE': models.data_reader.candidates[i_alckmin].ibope_medio,
        'Geraldo Alckmin-Ensino Médio-Facebook': models.data_reader.candidates[i_alckmin].facebook_medio
        # 'Geraldo Alckmin-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Geraldo Alckmin-Ensino Médio-Distribuition Census': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Ensino Superior-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_superior, 'Geraldo Alckmin-Ensino Superior-IBOPE': models.data_reader.candidates[i_alckmin].ibope_superior,
        'Geraldo Alckmin-Ensino Superior-Facebook': models.data_reader.candidates[i_alckmin].facebook_superior
        # 'Geraldo Alckmin-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Geraldo Alckmin-Ensino Superior-Distribuition Census': models.data_distribuition.census_education_superior
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_fundamental, 'Alvaro Dias-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_alvaro].ibope_fundamental,
        'Alvaro Dias-Ensino Fundamental-Facebook': models.data_reader.candidates[i_alvaro].facebook_fundamental
        # 'Alvaro Dias-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Alvaro Dias-Ensino Fundamental-Distribuition Census': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Ensino Médio-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_medio, 'Alvaro Dias-Ensino Médio-IBOPE': models.data_reader.candidates[i_alvaro].ibope_medio,
        'Alvaro Dias-Ensino Médio-Facebook': models.data_reader.candidates[i_alvaro].facebook_medio
        # 'Alvaro Dias-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Alvaro Dias-Ensino Médio-Distribuition Census': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Ensino Superior-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_superior, 'Alvaro Dias-Ensino Superior-IBOPE': models.data_reader.candidates[i_alvaro].ibope_superior,
        'Alvaro Dias-Ensino Superior-Facebook': models.data_reader.candidates[i_alvaro].facebook_superior
        # 'Alvaro Dias-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Alvaro Dias-Ensino Superior-Distribuition Census': models.data_distribuition.census_education_superior
    })]

class ScoreVsLike:

    data_frame = [        
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_score)), 
            'Jair Bolsonaro-Jair Bolsonaro-DataFolha': [x/d_pesquisa for x in models.data_reader.candidates[i_bolsonaro].dfolha_score], 'Jair Bolsonaro-Jair Bolsonaro-IBOPE': [x/d_pesquisa for x in models.data_reader.candidates[i_bolsonaro].ibope_score],
            'Jair Bolsonaro-Jair Bolsonaro-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_bolsonaro].facebook_likes]
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_score)), 
            'Fernando Haddad-Fernando Haddad-DataFolha': [x/d_pesquisa for x in models.data_reader.candidates[i_haddad].dfolha_score], 'Fernando Haddad-Fernando Haddad-IBOPE':  [x/d_pesquisa for x in models.data_reader.candidates[i_haddad].ibope_score],
            'Fernando Haddad-Fernando Haddad-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_haddad].facebook_likes]
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_score)), 
            'Ciro Gomes-Ciro Gomes-DataFolha': [x/d_pesquisa for x in models.data_reader.candidates[i_ciro].dfolha_score], 'Ciro Gomes-Ciro Gomes-IBOPE': [x/d_pesquisa for x in models.data_reader.candidates[i_ciro].ibope_score],
            'Ciro Gomes-Ciro Gomes-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_ciro].facebook_likes]
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_score)), 
            'Marina Silva-Marina Silva-DataFolha': [x/d_pesquisa for x in models.data_reader.candidates[i_ciro].dfolha_score], 'Marina Silva-Marina Silva-IBOPE': [x/d_pesquisa for x in models.data_reader.candidates[i_marina].ibope_score],
            'Marina Silva-Marina Silva-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_marina].facebook_likes]
        }),       
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_score)), 
            'Geraldo Alckmin-Geraldo Alckmin-DataFolha': [x/d_pesquisa for x in models.data_reader.candidates[i_alckmin].dfolha_score], 'Geraldo Alckmin-Geraldo Alckmin-IBOPE': [x/d_pesquisa for x in models.data_reader.candidates[i_marina].ibope_score],
            'Geraldo Alckmin-Geraldo Alckmin-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_marina].facebook_likes]
        })]

class Score:

    data_frame = [        
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_score)), 
            'Jair Bolsonaro-Jair Bolsonaro-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_score, 'Jair Bolsonaro-Jair Bolsonaro-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_score
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_score)), 
            'Fernando Haddad-Fernando Haddad-DataFolha': models.data_reader.candidates[i_haddad].dfolha_score, 'Fernando Haddad-Fernando Haddad-IBOPE':  models.data_reader.candidates[i_haddad].ibope_score
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_score)), 
            'Ciro Gomes-Ciro Gomes-DataFolha': models.data_reader.candidates[i_ciro].dfolha_score, 'Ciro Gomes-Ciro Gomes-IBOPE': models.data_reader.candidates[i_ciro].ibope_score
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_score)), 
            'Marina Silva-Marina Silva-DataFolha': models.data_reader.candidates[i_ciro].dfolha_score, 'Marina Silva-Marina Silva-IBOPE': models.data_reader.candidates[i_marina].ibope_score
        }),       
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_score)), 
            'Geraldo Alckmin-Geraldo Alckmin-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_score, 'Geraldo Alckmin-Geraldo Alckmin-IBOPE': models.data_reader.candidates[i_marina].ibope_score
        })]