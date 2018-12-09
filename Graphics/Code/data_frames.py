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
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Male-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_male, 'Alvaro Dias-Male-IBOPE': models.data_reader.candidates[i_alvaro].ibope_male,
        'Alvaro Dias-Male-Facebook': models.data_reader.candidates[i_alvaro].facebook_male,
        'Alvaro Dias-Male-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Alvaro Dias-Male-Distribuition Census': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame({'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Female-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_female, 'Alvaro Dias-Female-IBOPE': models.data_reader.candidates[i_alvaro].ibope_female,
        'Alvaro Dias-Female-Facebook': models.data_reader.candidates[i_alvaro].facebook_female,
        'Alvaro Dias-Female-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Alvaro Dias-Female-Distribuition Census': models.data_distribuition.census_gender_female
    })]

class Region:
    data_frame_bolsonaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Sudeste-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_sudeste, 'Jair Bolsonaro-Sudeste-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_sudeste,
        'Jair Bolsonaro-Sudeste-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_sudeste,
        'Jair Bolsonaro-Sudeste-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Jair Bolsonaro-Sudeste-Distribuition Census': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Nordeste-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_nordeste, 'Jair Bolsonaro-Nordeste-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_nordeste,
        'Jair Bolsonaro-Nordeste-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_nordeste,
        'Jair Bolsonaro-Nordeste-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Jair Bolsonaro-Nordeste-Distribuition Census': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Norte/Centro Oeste-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_norte_coeste, 'Jair Bolsonaro-Norte/Centro Oeste-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_norte_coeste,
        'Jair Bolsonaro-Norte/Centro Oeste-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_norte_coeste,
        'Jair Bolsonaro-Norte/Centro Oeste-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Jair Bolsonaro-Norte/Centro Oeste-Distribuition Census': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Sul-DataFolha': models.data_reader.candidates[i_bolsonaro].dfolha_sul, 'Jair Bolsonaro-Sul-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_sul,
        'Jair Bolsonaro-Sul-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_sul,
        'Jair Bolsonaro-Sul-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Jair Bolsonaro-Sul-Distribuition Census': models.data_distribuition.census_region_sul
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
        'Fernando Haddad-Norte/Centro Oeste-DataFolha': models.data_reader.candidates[i_haddad].dfolha_norte_coeste, 'Fernando Haddad-Norte/Centro Oeste-IBOPE': models.data_reader.candidates[i_haddad].ibope_norte_coeste,
        'Fernando Haddad-Norte/Centro Oeste-Facebook': models.data_reader.candidates[i_haddad].facebook_norte_coeste
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
        'Lula-Norte/Centro Oeste-DataFolha': models.data_reader.candidates[i_lula].dfolha_norte_coeste, 'Lula-Norte/Centro Oeste-IBOPE': models.data_reader.candidates[i_lula].ibope_norte_coeste,
        'Lula-Norte/Centro Oeste-Facebook': models.data_reader.candidates[i_lula].facebook_norte_coeste
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
        'Ciro Gomes-Norte/Centro Oeste-DataFolha': models.data_reader.candidates[i_ciro].dfolha_norte_coeste, 'Ciro Gomes-Norte/Centro Oeste-IBOPE': models.data_reader.candidates[i_ciro].ibope_norte_coeste,
        'Ciro Gomes-Norte/Centro Oeste-Facebook': models.data_reader.candidates[i_ciro].facebook_norte_coeste
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
        'Marina Silva-Norte/Centro Oeste-DataFolha': models.data_reader.candidates[i_marina].dfolha_norte_coeste, 'Marina Silva-Norte/Centro Oeste-IBOPE': models.data_reader.candidates[i_marina].ibope_norte_coeste,
        'Marina Silva-Norte/Centro Oeste-Facebook': models.data_reader.candidates[i_marina].facebook_norte_coeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
        'Marina Silva-Sul-DataFolha': models.data_reader.candidates[i_marina].dfolha_sul, 'Marina Silva-Sul-IBOPE': models.data_reader.candidates[i_marina].ibope_sul,
        'Marina Silva-Sul-Facebook': models.data_reader.candidates[i_marina].facebook_sul
    })]

    data_frame_alckmin = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-Sudeste-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_sudeste, 'Geraldo Alckmin-Sudeste-IBOPE': models.data_reader.candidates[i_alckmin].ibope_sudeste,
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
        'Geraldo Alckmin-Norte/Centro Oeste-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_norte_coeste, 'Geraldo Alckmin-Norte/Centro Oeste-IBOPE': models.data_reader.candidates[i_alckmin].ibope_norte_coeste,
        'Geraldo Alckmin-Norte/Centro Oeste-Facebook': models.data_reader.candidates[i_alckmin].facebook_norte_coeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-Sul-DataFolha': models.data_reader.candidates[i_alckmin].dfolha_sul, 'Geraldo Alckmin-Sul-IBOPE': models.data_reader.candidates[i_alckmin].ibope_sul,
        'Geraldo Alckmin-Sul-Facebook': models.data_reader.candidates[i_alckmin].facebook_sul
    })]

    data_frame_alvaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Sudeste-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_sudeste, 'Alvaro Dias-Sudeste-IBOPE': models.data_reader.candidates[i_alvaro].ibope_sudeste,
        'Alvaro Dias-Sudeste-Facebook': models.data_reader.candidates[i_alvaro].facebook_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Nordeste-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_nordeste, 'Alvaro Dias-Nordeste-IBOPE': models.data_reader.candidates[i_alvaro].ibope_nordeste,
        'Alvaro Dias-Nordeste-Facebook': models.data_reader.candidates[i_alvaro].facebook_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Norte/Centro Oeste-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_norte_coeste, 'Geraldo Alckmin-Norte/Centro Oeste-IBOPE': models.data_reader.candidates[i_alvaro].ibope_norte_coeste,
        'Alvaro Dias-Norte/Centro Oeste-Facebook': models.data_reader.candidates[i_alvaro].facebook_norte_coeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Sul-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_sul, 'Alvaro Dias-Sul-IBOPE': models.data_reader.candidates[i_alvaro].ibope_sul,
        'Alvaro Dias-Sul-Facebook': models.data_reader.candidates[i_alvaro].facebook_sul
    })]

class Age:
    # AGE
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

    data_frame_alvaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-16 a 24-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_16a24, 'Alvaro Dias-16 a 24-IBOPE': models.data_reader.candidates[i_alvaro].ibope_16a24,
        'Alvaro Dias-16 a 24-Facebook': models.data_reader.candidates[i_alvaro].facebook_16a24            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-25 a 34-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_25a34, 'Alvaro Dias-25 a 34-IBOPE': models.data_reader.candidates[i_alvaro].ibope_25a34,
        'Alvaro Dias-25 a 34-Facebook': models.data_reader.candidates[i_alvaro].facebook_25a34            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-35 a 44-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_35a44, 'Alvaro Dias-35 a 44-IBOPE': models.data_reader.candidates[i_alvaro].ibope_35a44,
        'Alvaro Dias-35 a 44-Facebook': models.data_reader.candidates[i_alvaro].facebook_35a44            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-45 a 54-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_45a54, 'Alvaro Dias-45 a 54-IBOPE': models.data_reader.candidates[i_alvaro].ibope_45a54,
        'Alvaro Dias-45 a 54-Facebook': models.data_reader.candidates[i_alvaro].facebook_45a54          
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-Acima de 55-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_55, 'Alvaro Dias-Acima de 55-IBOPE': models.data_reader.candidates[i_alvaro].ibope_55,
        'Alvaro Dias-Acima de 55-Facebook': models.data_reader.candidates[i_alvaro].facebook_55          
    })]


class Education:
    # EDUCATION
    data_frame = [pd.DataFrame(
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
    })]

    data_frame2 = [pd.DataFrame(
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
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Ensino Fundamental-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_fundamental, 'Alvaro Dias-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_alvaro].ibope_fundamental,
        'Alvaro Dias-Ensino Fundamental-Facebook': models.data_reader.candidates[i_alvaro].facebook_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Ensino Médio-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_medio, 'Alvaro Dias-Ensino Médio-IBOPE': models.data_reader.candidates[i_alvaro].ibope_medio,
        'Alvaro Dias-Ensino Médio-Facebook': models.data_reader.candidates[i_alvaro].facebook_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Ensino Superior-DataFolha': models.data_reader.candidates[i_alvaro].dfolha_superior, 'Alvaro Dias-Ensino Superior-IBOPE': models.data_reader.candidates[i_alvaro].ibope_superior,
        'Alvaro Dias-Ensino Superior-Facebook': models.data_reader.candidates[i_alvaro].facebook_superior
    })]