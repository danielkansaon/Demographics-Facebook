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
        'Jair Bolsonaro-Masculino-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_male, 'Jair Bolsonaro-Masculino-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_male,
        'Jair Bolsonaro-Masculino-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_male, 
        'Jair Bolsonaro-Masculino-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Jair Bolsonaro-Masculino-Distribuition Censo': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        'Jair Bolsonaro-Feminino-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_female, 'Jair Bolsonaro-Feminino-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_female,
        'Jair Bolsonaro-Feminino-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_female,
        'Jair Bolsonaro-Feminino-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Jair Bolsonaro-Feminino-Distribuition Censo': models.data_distribuition.census_gender_female
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Masculino-Datafolha': models.data_reader.candidates[i_haddad].dfolha_male, 'Fernando Haddad-Masculino-IBOPE': models.data_reader.candidates[i_haddad].ibope_male,
        'Fernando Haddad-Masculino-Facebook': models.data_reader.candidates[i_haddad].facebook_male,
        'Fernando Haddad-Masculino-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Fernando Haddad-Masculino-Distribuition Censo': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Feminino-Datafolha': models.data_reader.candidates[i_haddad].dfolha_female, 'Fernando Haddad-Feminino-IBOPE': models.data_reader.candidates[i_haddad].ibope_female,
        'Fernando Haddad-Feminino-Facebook': models.data_reader.candidates[i_haddad].facebook_female,
        'Fernando Haddad-Feminino-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Fernando Haddad-Feminino-Distribuition Censo': models.data_distribuition.census_gender_female
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Masculino-Datafolha': models.data_reader.candidates[i_ciro].dfolha_male, 'Ciro Gomes-Masculino-IBOPE': models.data_reader.candidates[i_ciro].ibope_male,
        'Ciro Gomes-Masculino-Facebook': models.data_reader.candidates[i_ciro].facebook_male,
        'Ciro Gomes-Masculino-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Ciro Gomes-Masculino-Distribuition Censo': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Feminino-Datafolha': models.data_reader.candidates[i_ciro].dfolha_female, 'Ciro Gomes-Feminino-IBOPE': models.data_reader.candidates[i_ciro].ibope_female,
        'Ciro Gomes-Feminino-Facebook': models.data_reader.candidates[i_ciro].facebook_female,
        'Ciro Gomes-Feminino-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Ciro Gomes-Feminino-Distribuition Censo': models.data_distribuition.census_gender_female
    })
    
    # ,
    # pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Masculino-Datafolha': models.data_reader.candidates[i_lula].dfolha_male, 'Lula-Masculino-IBOPE': models.data_reader.candidates[i_lula].ibope_male,
    #     'Lula-Masculino-Facebook': models.data_reader.candidates[i_lula].facebook_male
    # }),
    # pd.DataFrame({'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Feminino-Datafolha': models.data_reader.candidates[i_lula].dfolha_female, 'Lula-Feminino-IBOPE': models.data_reader.candidates[i_lula].ibope_female,
    #     'Lula-Feminino-Facebook': models.data_reader.candidates[i_lula].facebook_female
    # })
    ]

    data_frame_2 = [        
        pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Masculino-Datafolha': models.data_reader.candidates[i_marina].dfolha_male, 'Marina Silva-Masculino-IBOPE': models.data_reader.candidates[i_marina].ibope_male,
        'Marina Silva-Masculino-Facebook': models.data_reader.candidates[i_marina].facebook_male,
        'Marina Silva-Masculino-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Marina Silva-Masculino-Distribuition Censo': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Feminino-Datafolha': models.data_reader.candidates[i_marina].dfolha_female, 'Marina Silva-Feminino-IBOPE': models.data_reader.candidates[i_marina].ibope_female,
        'Marina Silva-Feminino-Facebook': models.data_reader.candidates[i_marina].facebook_female,
        'Marina Silva-Feminino-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Marina Silva-Feminino-Distribuition Censo': models.data_distribuition.census_gender_female
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Masculino-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_male, 'Geraldo Alckmin-Masculino-IBOPE': models.data_reader.candidates[i_alckmin].ibope_male,
        'Geraldo Alckmin-Masculino-Facebook': models.data_reader.candidates[i_alckmin].facebook_male,
        'Geraldo Alckmin-Masculino-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
        'Geraldo Alckmin-Masculino-Distribuition Censo': models.data_distribuition.census_gender_male
    }),
    pd.DataFrame({'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Feminino-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_female, 'Geraldo Alckmin-Feminino-IBOPE': models.data_reader.candidates[i_alckmin].ibope_female,
        'Geraldo Alckmin-Feminino-Facebook': models.data_reader.candidates[i_alckmin].facebook_female,
        'Geraldo Alckmin-Feminino-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
        'Geraldo Alckmin-Feminino-Distribuition Censo': models.data_distribuition.census_gender_female
    })
    # ,pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
    #     'Alvaro Dias-Masculino-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_male, 'Alvaro Dias-Masculino-IBOPE': models.data_reader.candidates[i_alvaro].ibope_male,
    #     'Alvaro Dias-Masculino-Facebook': models.data_reader.candidates[i_alvaro].facebook_male,
    #     'Alvaro Dias-Masculino-Distribuition Facebook': models.data_distribuition.facebook_gender_male,
    #     'Alvaro Dias-Masculino-Distribuition Censo': models.data_distribuition.census_gender_male
    # }),
    # pd.DataFrame({'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
    #     'Alvaro Dias-Feminino-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_female, 'Alvaro Dias-Feminino-IBOPE': models.data_reader.candidates[i_alvaro].ibope_female,
    #     'Alvaro Dias-Feminino-Facebook': models.data_reader.candidates[i_alvaro].facebook_female,
    #     'Alvaro Dias-Feminino-Distribuition Facebook': models.data_distribuition.facebook_gender_female,
    #     'Alvaro Dias-Feminino-Distribuition Censo': models.data_distribuition.census_gender_female
    # })
    ]

class Region:
    data_frame_bolsonaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Sudeste-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_sudeste, 'Jair Bolsonaro-Sudeste-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_sudeste,
        'Jair Bolsonaro-Sudeste-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_sudeste,
        'Jair Bolsonaro-Sudeste-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Jair Bolsonaro-Sudeste-Distribuition Censo': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Nordeste-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_nordeste, 'Jair Bolsonaro-Nordeste-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_nordeste,
        'Jair Bolsonaro-Nordeste-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_nordeste,
        'Jair Bolsonaro-Nordeste-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Jair Bolsonaro-Nordeste-Distribuition Censo': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Norte/Centro_Oeste-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_norte_coeste, 'Jair Bolsonaro-Norte/Centro_Oeste-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_norte_coeste,
        'Jair Bolsonaro-Norte/Centro_Oeste-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_norte_coeste,
        'Jair Bolsonaro-Norte/Centro_Oeste-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Jair Bolsonaro-Norte/Centro_Oeste-Distribuition Censo': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_sudeste)), 
        'Jair Bolsonaro-Sul-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_sul, 'Jair Bolsonaro-Sul-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_sul,
        'Jair Bolsonaro-Sul-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_sul,
        'Jair Bolsonaro-Sul-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Jair Bolsonaro-Sul-Distribuition Censo': models.data_distribuition.census_region_sul
    })]

    data_frame_haddad = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
        'Fernando Haddad-Sudeste-Datafolha': models.data_reader.candidates[i_haddad].dfolha_sudeste, 'Fernando Haddad-Sudeste-IBOPE': models.data_reader.candidates[i_haddad].ibope_sudeste,
        'Fernando Haddad-Sudeste-Facebook': models.data_reader.candidates[i_haddad].facebook_sudeste,
        'Fernando Haddad-Sudeste-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Fernando Haddad-Sudeste-Distribuition Censo': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
        'Fernando Haddad-Nordeste-Datafolha': models.data_reader.candidates[i_haddad].dfolha_nordeste, 'Fernando Haddad-Nordeste-IBOPE': models.data_reader.candidates[i_haddad].ibope_nordeste,
        'Fernando Haddad-Nordeste-Facebook': models.data_reader.candidates[i_haddad].facebook_nordeste,
        'Fernando Haddad-Nordeste-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Fernando Haddad-Nordeste-Distribuition Censo': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
        'Fernando Haddad-Norte/Centro_Oeste-Datafolha': models.data_reader.candidates[i_haddad].dfolha_norte_coeste, 'Fernando Haddad-Norte/Centro_Oeste-IBOPE': models.data_reader.candidates[i_haddad].ibope_norte_coeste,
        'Fernando Haddad-Norte/Centro_Oeste-Facebook': models.data_reader.candidates[i_haddad].facebook_norte_coeste,
        'Fernando Haddad-Norte/Centro_Oeste-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Fernando Haddad-Norte/Centro_Oeste-Distribuition Censo': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_sudeste)), 
        'Fernando Haddad-Sul-Datafolha': models.data_reader.candidates[i_haddad].dfolha_sul, 'Fernando Haddad-Sul-IBOPE': models.data_reader.candidates[i_haddad].ibope_sul,
        'Fernando Haddad-Sul-Facebook': models.data_reader.candidates[i_haddad].facebook_sul,
        'Fernando Haddad-Sul-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Fernando Haddad-Sul-Distribuition Censo': models.data_distribuition.census_region_sul
    })]

    data_frame_lula = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
        'Lula-Sudeste-Datafolha': models.data_reader.candidates[i_lula].dfolha_sudeste, 'Lula-Sudeste-IBOPE': models.data_reader.candidates[i_lula].ibope_sudeste,
        'Lula-Sudeste-Facebook': models.data_reader.candidates[i_lula].facebook_sudeste,
        'Lula-Sudeste-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Lula-Sudeste-Distribuition Censo': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
        'Lula-Nordeste-Datafolha': models.data_reader.candidates[i_lula].dfolha_nordeste, 'Lula-Nordeste-IBOPE': models.data_reader.candidates[i_lula].ibope_nordeste,
        'Lula-Nordeste-Facebook': models.data_reader.candidates[i_lula].facebook_nordeste,
        'Lula-Nordeste-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Lula-Nordeste-Distribuition Censo': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
        'Lula-Norte/Centro_Oeste-Datafolha': models.data_reader.candidates[i_lula].dfolha_norte_coeste, 'Lula-Norte/Centro_Oeste-IBOPE': models.data_reader.candidates[i_lula].ibope_norte_coeste,
        'Lula-Norte/Centro_Oeste-Facebook': models.data_reader.candidates[i_lula].facebook_norte_coeste,
        'Lula-Norte/Centro_Oeste-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Lula-Norte/Centro_Oeste-Distribuition Censo': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_sudeste)), 
        'Lula-Sul-Datafolha': models.data_reader.candidates[i_lula].dfolha_sul, 'Lula-Sul-IBOPE': models.data_reader.candidates[i_lula].ibope_sul,
        'Lula-Sul-Facebook': models.data_reader.candidates[i_lula].facebook_sul,
        'Lula-Sul-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Lula-Sul-Distribuition Censo': models.data_distribuition.census_region_sul
    })]

    data_frame_ciro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
        'Ciro Gomes-Sudeste-Datafolha': models.data_reader.candidates[i_ciro].dfolha_sudeste, 'Ciro Gomes-Sudeste-IBOPE': models.data_reader.candidates[i_ciro].ibope_sudeste,
        'Ciro Gomes-Sudeste-Facebook': models.data_reader.candidates[i_ciro].facebook_sudeste,
        'Ciro Gomes-Sudeste-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Ciro Gomes-Sudeste-Distribuition Censo': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
        'Ciro Gomes-Nordeste-Datafolha': models.data_reader.candidates[i_ciro].dfolha_nordeste, 'Ciro Gomes-Nordeste-IBOPE': models.data_reader.candidates[i_ciro].ibope_nordeste,
        'Ciro Gomes-Nordeste-Facebook': models.data_reader.candidates[i_ciro].facebook_nordeste,
        'Ciro Gomes-Nordeste-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Ciro Gomes-Nordeste-Distribuition Censo': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
        'Ciro Gomes-Norte/Centro_Oeste-Datafolha': models.data_reader.candidates[i_ciro].dfolha_norte_coeste, 'Ciro Gomes-Norte/Centro_Oeste-IBOPE': models.data_reader.candidates[i_ciro].ibope_norte_coeste,
        'Ciro Gomes-Norte/Centro_Oeste-Facebook': models.data_reader.candidates[i_ciro].facebook_norte_coeste,
        'Ciro Gomes-Norte/Centro_Oeste-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Ciro Gomes-Norte/Centro_Oeste-Distribuition Censo': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_sudeste)), 
        'Ciro Gomes-Sul-Datafolha': models.data_reader.candidates[i_ciro].dfolha_sul, 'Ciro Gomes-Sul-IBOPE': models.data_reader.candidates[i_ciro].ibope_sul,
        'Ciro Gomes-Sul-Facebook': models.data_reader.candidates[i_ciro].facebook_sul,
        'Ciro Gomes-Sul-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Ciro Gomes-Sul-Distribuition Censo': models.data_distribuition.census_region_sul
    })]

    data_frame_marina = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
        'Marina Silva-Sudeste-Datafolha': models.data_reader.candidates[i_marina].dfolha_sudeste, 'Ciro Gomes-Sudeste-IBOPE': models.data_reader.candidates[i_marina].ibope_sudeste,
        'Marina Silva-Sudeste-Facebook': models.data_reader.candidates[i_marina].facebook_sudeste,
        'Marina Silva-Sudeste-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Marina Silva-Sudeste-Distribuition Censo': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
        'Marina Silva-Nordeste-Datafolha': models.data_reader.candidates[i_marina].dfolha_nordeste, 'Marina Silva-Nordeste-IBOPE': models.data_reader.candidates[i_marina].ibope_nordeste,
        'Marina Silva-Nordeste-Facebook': models.data_reader.candidates[i_marina].facebook_nordeste,
        'Marina Silva-Nordeste-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Marina Silva-Nordeste-Distribuition Censo': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
        'Marina Silva-Norte/Centro_Oeste-Datafolha': models.data_reader.candidates[i_marina].dfolha_norte_coeste, 'Marina Silva-Norte/Centro_Oeste-IBOPE': models.data_reader.candidates[i_marina].ibope_norte_coeste,
        'Marina Silva-Norte/Centro_Oeste-Facebook': models.data_reader.candidates[i_marina].facebook_norte_coeste,
        'Marina Silva-Norte/Centro_Oeste-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Marina Silva-Norte/Centro_Oeste-Distribuition Censo': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_sudeste)), 
        'Marina Silva-Sul-Datafolha': models.data_reader.candidates[i_marina].dfolha_sul, 'Marina Silva-Sul-IBOPE': models.data_reader.candidates[i_marina].ibope_sul,
        'Marina Silva-Sul-Facebook': models.data_reader.candidates[i_marina].facebook_sul,
        'Marina Silva-Sul-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Marina Silva-Sul-Distribuition Censo': models.data_distribuition.census_region_sul
    })]

    data_frame_alckmin = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-Sudeste-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_sudeste, 'Geraldo Alckmin-Sudeste-IBOPE': models.data_reader.candidates[i_alckmin].ibope_sudeste,
        'Geraldo Alckmin-Sudeste-Facebook': models.data_reader.candidates[i_alckmin].facebook_sudeste,
        'Geraldo Alckmin-Sudeste-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Geraldo Alckmin-Sudeste-Distribuition Censo': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-Nordeste-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_nordeste, 'Geraldo Alckmin-Nordeste-IBOPE': models.data_reader.candidates[i_alckmin].ibope_nordeste,
        'Geraldo Alckmin-Nordeste-Facebook': models.data_reader.candidates[i_alckmin].facebook_nordeste,
        'Geraldo Alckmin-Nordeste-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Geraldo Alckmin-Nordeste-Distribuition Censo': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-Norte/Centro_Oeste-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_norte_coeste, 'Geraldo Alckmin-Norte/Centro_Oeste-IBOPE': models.data_reader.candidates[i_alckmin].ibope_norte_coeste,
        'Geraldo Alckmin-Norte/Centro_Oeste-Facebook': models.data_reader.candidates[i_alckmin].facebook_norte_coeste,
        'Geraldo Alckmin-Norte/Centro_Oeste-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Geraldo Alckmin-Norte/Centro_Oeste-Distribuition Censo': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_sudeste)), 
        'Geraldo Alckmin-Sul-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_sul, 'Geraldo Alckmin-Sul-IBOPE': models.data_reader.candidates[i_alckmin].ibope_sul,
        'Geraldo Alckmin-Sul-Facebook': models.data_reader.candidates[i_alckmin].facebook_sul,
        'Geraldo Alckmin-Sul-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Geraldo Alckmin-Sul-Distribuition Censo': models.data_distribuition.census_region_sul
    })]

    data_frame_alvaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Sudeste-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_sudeste, 'Alvaro Dias-Sudeste-IBOPE': models.data_reader.candidates[i_alvaro].ibope_sudeste,
        'Alvaro Dias-Sudeste-Facebook': models.data_reader.candidates[i_alvaro].facebook_sudeste,
        'Alvaro Dias-Sudeste-Distribuition Facebook': models.data_distribuition.facebook_region_sudeste,
        'Alvaro Dias-Sudeste-Distribuition Censo': models.data_distribuition.census_region_sudeste
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Nordeste-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_nordeste, 'Alvaro Dias-Nordeste-IBOPE': models.data_reader.candidates[i_alvaro].ibope_nordeste,
        'Alvaro Dias-Nordeste-Facebook': models.data_reader.candidates[i_alvaro].facebook_nordeste,
        'Alvaro Dias-Nordeste-Distribuition Facebook': models.data_distribuition.facebook_region_nordeste,
        'Alvaro Dias-Nordeste-Distribuition Censo': models.data_distribuition.census_region_nordeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Norte/Centro_Oeste-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_norte_coeste, 'Geraldo Alckmin-Norte/Centro_Oeste-IBOPE': models.data_reader.candidates[i_alvaro].ibope_norte_coeste,
        'Alvaro Dias-Norte/Centro_Oeste-Facebook': models.data_reader.candidates[i_alvaro].facebook_norte_coeste,
        'Alvaro Dias-Norte/Centro_Oeste-Distribuition Facebook': models.data_distribuition.facebook_region_norte_centro_oeste,
        'Alvaro Dias-Norte/Centro_Oeste-Distribuition Censo': models.data_distribuition.census_region_norte_centro_oeste
    }),
    pd.DataFrame({
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_sudeste)), 
        'Alvaro Dias-Sul-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_sul, 'Alvaro Dias-Sul-IBOPE': models.data_reader.candidates[i_alvaro].ibope_sul,
        'Alvaro Dias-Sul-Facebook': models.data_reader.candidates[i_alvaro].facebook_sul,
        'Alvaro Dias-Sul-Distribuition Facebook': models.data_distribuition.facebook_region_sul,
        'Alvaro Dias-Sul-Distribuition Censo': models.data_distribuition.census_region_sul
    })]

class Age:
    # AGE
    data_frame_bolsonaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
        'Jair Bolsonaro-16 a 24-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_16a24, 'Jair Bolsonaro-16 a 24-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_16a24,
        'Jair Bolsonaro-16 a 24-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_16a24,
        'Jair Bolsonaro-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Jair Bolsonaro-16 a 24-Distribuition Censo': models.data_distribuition.census_age_16a24      
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_25a34)), 
        'Jair Bolsonaro-25 a 34-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_25a34, 'Jair Bolsonaro-25 a 34-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_25a34,
        'Jair Bolsonaro-25 a 34-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_25a34,
        'Jair Bolsonaro-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Jair Bolsonaro-25 a 34-Distribuition Censo': models.data_distribuition.census_age_25a34              
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
        'Jair Bolsonaro-35 a 44-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_35a44, 'Jair Bolsonaro-35 a 44-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_35a44,
        'Jair Bolsonaro-35 a 44-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_35a44,
        'Jair Bolsonaro-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Jair Bolsonaro-35 a 44-Distribuition Censo': models.data_distribuition.census_age_35a44            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
        'Jair Bolsonaro-45 a 54-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_45a54, 'Jair Bolsonaro-45 a 54-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_45a54,
        'Jair Bolsonaro-45 a 54-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_45a54,
        'Jair Bolsonaro-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Jair Bolsonaro-45 a 54-Distribuition Censo': models.data_distribuition.census_age_45a54           
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_16a24)), 
        'Jair Bolsonaro-Acima de 55-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_55, 'Jair Bolsonaro-Acima de 55-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_55,
        'Jair Bolsonaro-Acima de 55-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_55,
        'Jair Bolsonaro-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Jair Bolsonaro-Acima de 55-Distribuition Censo': models.data_distribuition.census_age_acima55             
    })]

    data_frame_haddad = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-16 a 24-Datafolha': models.data_reader.candidates[i_haddad].dfolha_16a24, 'Fernando Haddado-16 a 24-IBOPE': models.data_reader.candidates[i_haddad].ibope_16a24,
        'Fernando Haddad-16 a 24-Facebook': models.data_reader.candidates[i_haddad].facebook_16a24,
        'Fernando Haddad-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Fernando Haddad-16 a 24-Distribuition Censo': models.data_distribuition.census_age_16a24              
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-25 a 34-Datafolha': models.data_reader.candidates[i_haddad].dfolha_25a34, 'Fernando Haddad-25 a 34-IBOPE': models.data_reader.candidates[i_haddad].ibope_25a34,
        'Fernando Haddad-25 a 34-Facebook': models.data_reader.candidates[i_haddad].facebook_25a34,
        'Fernando Haddad-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Fernando Haddad-25 a 34-Distribuition Censo': models.data_distribuition.census_age_25a34               
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-35 a 44-Datafolha': models.data_reader.candidates[i_haddad].dfolha_35a44, 'Fernando Haddad-35 a 44-IBOPE': models.data_reader.candidates[i_haddad].ibope_35a44,
        'Fernando Haddad-35 a 44-Facebook': models.data_reader.candidates[i_haddad].facebook_35a44,
        'Fernando Haddad-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Fernando Haddad-35 a 44-Distribuition Censo': models.data_distribuition.census_age_35a44             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-45 a 54-Datafolha': models.data_reader.candidates[i_haddad].dfolha_45a54, 'Fernando Haddad-45 a 54-IBOPE': models.data_reader.candidates[i_haddad].ibope_45a54,
        'Fernando Haddad-45 a 54-Facebook': models.data_reader.candidates[i_haddad].facebook_45a54,
        'Fernando Haddad-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Fernando Haddad-45 a 54-Distribuition Censo': models.data_distribuition.census_age_45a54             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_16a24)), 
        'Fernando Haddad-Acima de 55-Datafolha': models.data_reader.candidates[i_haddad].dfolha_55, 'Fernando Haddad-Acima de 55-IBOPE': models.data_reader.candidates[i_haddad].ibope_55,
        'Fernando Haddad-Acima de 55-Facebook': models.data_reader.candidates[i_haddad].facebook_55,
        'Fernando Haddad-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Fernando Haddad-Acima de 55-Distribuition Censo': models.data_distribuition.census_age_acima55          
    })]

    data_frame_lula = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-16 a 24-Datafolha': models.data_reader.candidates[i_lula].dfolha_16a24, 'Lula-16 a 24-IBOPE': models.data_reader.candidates[i_lula].ibope_16a24,
        'Lula-16 a 24-Facebook': models.data_reader.candidates[i_lula].facebook_16a24,
        'Lula-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Lula-16 a 24-Distribuition Censo': models.data_distribuition.census_age_16a24             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-25 a 34-Datafolha': models.data_reader.candidates[i_lula].dfolha_25a34, 'Lula-25 a 34-IBOPE': models.data_reader.candidates[i_lula].ibope_25a34,
        'Lula-25 a 34-Facebook': models.data_reader.candidates[i_lula].facebook_25a34,
        'Lula-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Lula-25 a 34-Distribuition Censo': models.data_distribuition.census_age_25a34            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-35 a 44-Datafolha': models.data_reader.candidates[i_lula].dfolha_35a44, 'Lula-35 a 44-IBOPE': models.data_reader.candidates[i_lula].ibope_35a44,
        'Lula-35 a 44-Facebook': models.data_reader.candidates[i_lula].facebook_35a44,
        'Lula-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Lula-35 a 44-Distribuition Censo': models.data_distribuition.census_age_35a44            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-45 a 54-Datafolha': models.data_reader.candidates[i_lula].dfolha_45a54, 'Lula-45 a 54-IBOPE': models.data_reader.candidates[i_lula].ibope_45a54,
        'Lula-45 a 54-Facebook': models.data_reader.candidates[i_lula].facebook_45a54,
        'Lula-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Lula-45 a 54-Distribuition Censo': models.data_distribuition.census_age_45a54           
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_16a24)), 
        'Lula-Acima de 55-Datafolha': models.data_reader.candidates[i_lula].dfolha_55, 'Lula-Acima de 55-IBOPE': models.data_reader.candidates[i_lula].ibope_55,
        'Lula-Acima de 55-Facebook': models.data_reader.candidates[i_lula].facebook_55,
        'Lula-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Lula-Acima de 55-Distribuition Censo': models.data_distribuition.census_age_acima55           
    })]

    data_frame_ciro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-16 a 24-Datafolha': models.data_reader.candidates[i_ciro].dfolha_16a24, 'Ciro Gomes-16 a 24-IBOPE': models.data_reader.candidates[i_ciro].ibope_16a24,
        'Ciro Gomes-16 a 24-Facebook': models.data_reader.candidates[i_ciro].facebook_16a24,
        'Ciro Gomes-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Ciro Gomes-16 a 24-Distribuition Censo': models.data_distribuition.census_age_16a24             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-25 a 34-Datafolha': models.data_reader.candidates[i_ciro].dfolha_25a34, 'Ciro Gomes-25 a 34-IBOPE': models.data_reader.candidates[i_ciro].ibope_25a34,
        'Ciro Gomes-25 a 34-Facebook': models.data_reader.candidates[i_ciro].facebook_25a34,
        'Ciro Gomes-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Ciro Gomes-25 a 34-Distribuition Censo': models.data_distribuition.census_age_25a34             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-35 a 44-Datafolha': models.data_reader.candidates[i_ciro].dfolha_35a44, 'Ciro Gomes-35 a 44-IBOPE': models.data_reader.candidates[i_ciro].ibope_35a44,
        'Ciro Gomes-35 a 44-Facebook': models.data_reader.candidates[i_ciro].facebook_35a44,
        'Ciro Gomes-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Ciro Gomes-35 a 44-Distribuition Censo': models.data_distribuition.census_age_35a44             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-45 a 54-Datafolha': models.data_reader.candidates[i_ciro].dfolha_45a54, 'Ciro Gomes-45 a 54-IBOPE': models.data_reader.candidates[i_ciro].ibope_45a54,
        'Ciro Gomes-45 a 54-Facebook': models.data_reader.candidates[i_ciro].facebook_45a54,
        'Ciro Gomes-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Ciro Gomes-45 a 54-Distribuition Censo': models.data_distribuition.census_age_45a54           
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_16a24)), 
        'Ciro Gomes-Acima de 55-Datafolha': models.data_reader.candidates[i_ciro].dfolha_55, 'Ciro Gomes-Acima de 55-IBOPE': models.data_reader.candidates[i_ciro].ibope_55,
        'Ciro Gomes-Acima de 55-Facebook': models.data_reader.candidates[i_ciro].facebook_55,
        'Ciro Gomes-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Ciro Gomes-Acima de 55-Distribuition Censo': models.data_distribuition.census_age_acima55          
    })]

    data_frame_marina = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-16 a 24-Datafolha': models.data_reader.candidates[i_marina].dfolha_16a24, 'Marina Silva-16 a 24-IBOPE': models.data_reader.candidates[i_marina].ibope_16a24,
        'Marina Silva-16 a 24-Facebook': models.data_reader.candidates[i_marina].facebook_16a24,
        'Marina Silva-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Marina Silva-16 a 24-Distribuition Censo': models.data_distribuition.census_age_16a24             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-25 a 34-Datafolha': models.data_reader.candidates[i_marina].dfolha_25a34, 'Marina Silva-25 a 34-IBOPE': models.data_reader.candidates[i_marina].ibope_25a34,
        'Marina Silva-25 a 34-Facebook': models.data_reader.candidates[i_marina].facebook_25a34,
        'Marina Silva-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Marina Silva-25 a 34-Distribuition Censo': models.data_distribuition.census_age_25a34            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-35 a 44-Datafolha': models.data_reader.candidates[i_marina].dfolha_35a44, 'Marina Silva-35 a 44-IBOPE': models.data_reader.candidates[i_marina].ibope_35a44,
        'Marina Silva-35 a 44-Facebook': models.data_reader.candidates[i_marina].facebook_35a44,
        'Marina Silva-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Marina Silva-35 a 44-Distribuition Censo': models.data_distribuition.census_age_35a44              
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-45 a 54-Datafolha': models.data_reader.candidates[i_marina].dfolha_45a54, 'Marina Silva-45 a 54-IBOPE': models.data_reader.candidates[i_marina].ibope_45a54,
        'Marina Silva-45 a 54-Facebook': models.data_reader.candidates[i_marina].facebook_45a54,
        'Marina Silva-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Marina Silva-45 a 54-Distribuition Censo': models.data_distribuition.census_age_45a54          
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_16a24)), 
        'Marina Silva-Acima de 55-Datafolha': models.data_reader.candidates[i_marina].dfolha_55, 'Marina Silva-Acima de 55-IBOPE': models.data_reader.candidates[i_marina].ibope_55,
        'Marina Silva-Acima de 55-Facebook': models.data_reader.candidates[i_marina].facebook_55,
        'Marina Silva-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Marina Silva-Acima de 55-Distribuition Censo': models.data_distribuition.census_age_acima55          
    })]

    data_frame_alckmin = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-16 a 24-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_16a24, 'Geraldo Alckmin-16 a 24-IBOPE': models.data_reader.candidates[i_alckmin].ibope_16a24,
        'Geraldo Alckmin-16 a 24-Facebook': models.data_reader.candidates[i_alckmin].facebook_16a24,
        'Geraldo Alckmin-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Geraldo Alckmin-16 a 24-Distribuition Censo': models.data_distribuition.census_age_16a24             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-25 a 34-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_25a34, 'Geraldo Alckmin-25 a 34-IBOPE': models.data_reader.candidates[i_alckmin].ibope_25a34,
        'Geraldo Alckmin-25 a 34-Facebook': models.data_reader.candidates[i_alckmin].facebook_25a34,
        'Geraldo Alckmin-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Geraldo Alckmin-25 a 34-Distribuition Censo': models.data_distribuition.census_age_25a34             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-35 a 44-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_35a44, 'Geraldo Alckmin-35 a 44-IBOPE': models.data_reader.candidates[i_alckmin].ibope_35a44,
        'Geraldo Alckmin-35 a 44-Facebook': models.data_reader.candidates[i_alckmin].facebook_35a44,
        'Geraldo Alckmin-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Geraldo Alckmin-35 a 44-Distribuition Censo': models.data_distribuition.census_age_35a44            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-45 a 54-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_45a54, 'Geraldo Alckmin-45 a 54-IBOPE': models.data_reader.candidates[i_alckmin].ibope_45a54,
        'Geraldo Alckmin-45 a 54-Facebook': models.data_reader.candidates[i_alckmin].facebook_45a54,
        'Geraldo Alckmin-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Geraldo Alckmin-45 a 54-Distribuition Censo': models.data_distribuition.census_age_45a54          
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_16a24)), 
        'Geraldo Alckmin-Acima de 55-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_55, 'Geraldo Alckmin-Acima de 55-IBOPE': models.data_reader.candidates[i_alckmin].ibope_55,
        'Geraldo Alckmin-Acima de 55-Facebook': models.data_reader.candidates[i_alckmin].facebook_55,
        'Geraldo Alckmin-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Geraldo Alckmin-Acima de 55-Distribuition Censo': models.data_distribuition.census_age_acima55          
    })]

    data_frame_alvaro = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-16 a 24-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_16a24, 'Alvaro Dias-16 a 24-IBOPE': models.data_reader.candidates[i_alvaro].ibope_16a24,
        'Alvaro Dias-16 a 24-Facebook': models.data_reader.candidates[i_alvaro].facebook_16a24,
        'Alvaro Dias-16 a 24-Distribuition Facebook': models.data_distribuition.facebook_age_16a24,
        'Alvaro Dias-16 a 24-Distribuition Censo': models.data_distribuition.census_age_16a24            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-25 a 34-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_25a34, 'Alvaro Dias-25 a 34-IBOPE': models.data_reader.candidates[i_alvaro].ibope_25a34,
        'Alvaro Dias-25 a 34-Facebook': models.data_reader.candidates[i_alvaro].facebook_25a34,
        'Alvaro Dias-25 a 34-Distribuition Facebook': models.data_distribuition.facebook_age_25a34,
        'Alvaro Dias-25 a 34-Distribuition Censo': models.data_distribuition.census_age_25a34             
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-35 a 44-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_35a44, 'Alvaro Dias-35 a 44-IBOPE': models.data_reader.candidates[i_alvaro].ibope_35a44,
        'Alvaro Dias-35 a 44-Facebook': models.data_reader.candidates[i_alvaro].facebook_35a44,
        'Alvaro Dias-35 a 44-Distribuition Facebook': models.data_distribuition.facebook_age_35a44,
        'Alvaro Dias-35 a 44-Distribuition Censo': models.data_distribuition.census_age_35a44            
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-45 a 54-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_45a54, 'Alvaro Dias-45 a 54-IBOPE': models.data_reader.candidates[i_alvaro].ibope_45a54,
        'Alvaro Dias-45 a 54-Facebook': models.data_reader.candidates[i_alvaro].facebook_45a54,
        'Alvaro Dias-45 a 54-Distribuition Facebook': models.data_distribuition.facebook_age_45a54,
        'Alvaro Dias-45 a 54-Distribuition Censo': models.data_distribuition.census_age_45a54          
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_16a24)), 
        'Alvaro Dias-Acima de 55-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_55, 'Alvaro Dias-Acima de 55-IBOPE': models.data_reader.candidates[i_alvaro].ibope_55,
        'Alvaro Dias-Acima de 55-Facebook': models.data_reader.candidates[i_alvaro].facebook_55,
        'Alvaro Dias-Acima de 55-Distribuition Facebook': models.data_distribuition.facebook_age_acima55,
        'Alvaro Dias-Acima de 55-Distribuition Censo': models.data_distribuition.census_age_acima55          
    })]


class Education:
    # EDUCATION
    data_frame = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        'Jair Bolsonaro-Ensino Fundamental-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_fundamental, 'Jair Bolsonaro-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_fundamental,
        'Jair Bolsonaro-Ensino Fundamental-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_fundamental
        # 'Jair Bolsonaro-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Jair Bolsonaro-Ensino Fundamental-Distribuition Censo': models.data_distribuition.census_education_fundamental        
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        'Jair Bolsonaro-Ensino Médio-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_medio, 'Jair Bolsonaro-Ensino Médio-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_medio,
        'Jair Bolsonaro-Ensino Médio-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_medio
        # 'Jair Bolsonaro-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Jair Bolsonaro-Ensino Médio-Distribuition Censo': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_male)), 
        'Jair Bolsonaro-Ensino Superior-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_superior, 'Jair Bolsonaro-Ensino Superior-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_superior,
        'Jair Bolsonaro-Ensino Superior-Facebook': models.data_reader.candidates[i_bolsonaro].facebook_superior
        # 'Jair Bolsonaro-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Jair Bolsonaro-Ensino Superior-Distribuition Censo': models.data_distribuition.census_education_superior
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Ensino Fundamental-Datafolha': models.data_reader.candidates[i_haddad].dfolha_fundamental, 'Fernando Haddad-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_haddad].ibope_fundamental,
        'Fernando Haddad-Ensino Fundamental-Facebook': models.data_reader.candidates[i_haddad].facebook_fundamental
        # 'Fernando Haddad-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Fernando Haddad-Ensino Fundamental-Distribuition Censo': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Ensino Médio-Datafolha': models.data_reader.candidates[i_haddad].dfolha_medio, 'Fernando Haddad-Ensino Médio-IBOPE': models.data_reader.candidates[i_haddad].ibope_medio,
        'Fernando Haddad-Ensino Médio-Facebook': models.data_reader.candidates[i_haddad].facebook_medio
        # 'Fernando Haddad-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Fernando Haddad-Ensino Médio-Distribuition Censo': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_male)), 
        'Fernando Haddad-Ensino Superior-Datafolha': models.data_reader.candidates[i_haddad].dfolha_superior, 'Fernando Haddad-Ensino Superior-IBOPE': models.data_reader.candidates[i_haddad].ibope_superior,
        'Fernando Haddad-Ensino Superior-Facebook': models.data_reader.candidates[i_haddad].facebook_superior
        # 'Fernando Haddad-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Fernando Haddad-Ensino Superior-Distribuition Censo': models.data_distribuition.census_education_superior
    }),
    # pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Ensino Fundamental-Datafolha': models.data_reader.candidates[i_lula].dfolha_fundamental, 'Lula-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_lula].ibope_fundamental,
    #     'Lula-Ensino Fundamental-Facebook': models.data_reader.candidates[i_lula].facebook_fundamental
    # }),
    # pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Ensino Médio-Datafolha': models.data_reader.candidates[i_lula].dfolha_medio, 'Lula-Ensino Médio-IBOPE': models.data_reader.candidates[i_lula].ibope_medio,
    #     'Lula-Ensino Médioo-Facebook': models.data_reader.candidates[i_lula].facebook_medio
    # }),
    # pd.DataFrame(
    # {
    #     'x': range(0, len(models.data_reader.candidates[i_lula].dfolha_male)), 
    #     'Lula-Ensino Superior-Datafolha': models.data_reader.candidates[i_lula].dfolha_superior, 'Lula-Ensino Superior-IBOPE': models.data_reader.candidates[i_lula].ibope_superior,
    #     'Lula-Ensino Superior-Facebook': models.data_reader.candidates[i_lula].facebook_superior
    # })
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Ensino Fundamental-Datafolha': models.data_reader.candidates[i_ciro].dfolha_fundamental, 'Ciro Gomes-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_ciro].ibope_fundamental,
        'Ciro Gomes-Ensino Fundamental-Facebook': models.data_reader.candidates[i_ciro].facebook_fundamental
        # 'Ciro Gomes-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Ciro Gomes-Ensino Fundamental-Distribuition Censo': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Ensino Médio-Datafolha': models.data_reader.candidates[i_ciro].dfolha_medio, 'Ciro Gomes-Ensino Médio-IBOPE': models.data_reader.candidates[i_ciro].ibope_medio,
        'Ciro Gomes-Ensino Médio-Facebook': models.data_reader.candidates[i_ciro].facebook_medio
        # 'Ciro Gomes-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Ciro Gomes-Ensino Médio-Distribuition Censo': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_male)), 
        'Ciro Gomes-Ensino Superior-Datafolha': models.data_reader.candidates[i_ciro].dfolha_superior, 'Ciro Gomes-Ensino Superior-IBOPE': models.data_reader.candidates[i_ciro].ibope_superior,
        'Ciro Gomes-Ensino Superior-Facebook': models.data_reader.candidates[i_ciro].facebook_superior
        # 'Ciro Gomes-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Ciro Gomes-Ensino Superior-Distribuition Censo': models.data_distribuition.census_education_superior
    })]

    data_frame2 = [pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Ensino Fundamental-Datafolha': models.data_reader.candidates[i_marina].dfolha_fundamental, 'Marina Silva-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_marina].ibope_fundamental,
        'Marina Silva-Ensino Fundamental-Facebook': models.data_reader.candidates[i_marina].facebook_fundamental
        # 'Marina Silva-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Marina Silva-Ensino Fundamental-Distribuition Censo': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Ensino Médio-Datafolha': models.data_reader.candidates[i_marina].dfolha_medio, 'Marina Silva-Ensino Médio-IBOPE': models.data_reader.candidates[i_marina].ibope_medio,
        'Marina Silva-Ensino Médio-Facebook': models.data_reader.candidates[i_marina].facebook_medio
        # 'Marina Silva-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Marina Silva-Ensino Médio-Distribuition Censo': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_male)), 
        'Marina Silva-Ensino Superior-Datafolha': models.data_reader.candidates[i_marina].dfolha_superior, 'Marina Silva-Ensino Superior-IBOPE': models.data_reader.candidates[i_marina].ibope_superior,
        'Marina Silva-Ensino Superior-Facebook': models.data_reader.candidates[i_marina].facebook_superior
        # 'Marina Silva-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Marina Silva-Ensino Superior-Distribuition Censo': models.data_distribuition.census_education_superior
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Ensino Fundamental-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_fundamental, 'Geraldo Alckmin-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_alckmin].ibope_fundamental,
        'Geraldo Alckmin-Ensino Fundamental-Facebook': models.data_reader.candidates[i_alckmin].facebook_fundamental
        # 'Geraldo Alckmin-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Geraldo Alckmin-Ensino Fundamental-Distribuition Censo': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Ensino Médio-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_medio, 'Geraldo Alckmin-Ensino Médio-IBOPE': models.data_reader.candidates[i_alckmin].ibope_medio,
        'Geraldo Alckmin-Ensino Médio-Facebook': models.data_reader.candidates[i_alckmin].facebook_medio
        # 'Geraldo Alckmin-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Geraldo Alckmin-Ensino Médio-Distribuition Censo': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_male)), 
        'Geraldo Alckmin-Ensino Superior-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_superior, 'Geraldo Alckmin-Ensino Superior-IBOPE': models.data_reader.candidates[i_alckmin].ibope_superior,
        'Geraldo Alckmin-Ensino Superior-Facebook': models.data_reader.candidates[i_alckmin].facebook_superior
        # 'Geraldo Alckmin-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Geraldo Alckmin-Ensino Superior-Distribuition Censo': models.data_distribuition.census_education_superior
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Ensino Fundamental-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_fundamental, 'Alvaro Dias-Ensino Fundamental-IBOPE': models.data_reader.candidates[i_alvaro].ibope_fundamental,
        'Alvaro Dias-Ensino Fundamental-Facebook': models.data_reader.candidates[i_alvaro].facebook_fundamental
        # 'Alvaro Dias-Ensino Fundamental-Distribuition Facebook': models.data_distribuition.facebook_education_fundamental,
        # 'Alvaro Dias-Ensino Fundamental-Distribuition Censo': models.data_distribuition.census_education_fundamental
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Ensino Médio-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_medio, 'Alvaro Dias-Ensino Médio-IBOPE': models.data_reader.candidates[i_alvaro].ibope_medio,
        'Alvaro Dias-Ensino Médio-Facebook': models.data_reader.candidates[i_alvaro].facebook_medio
        # 'Alvaro Dias-Ensino Médio-Distribuition Facebook': models.data_distribuition.facebook_education_medio,
        # 'Alvaro Dias-Ensino Médio-Distribuition Censo': models.data_distribuition.census_education_medio
    }),
    pd.DataFrame(
    {
        'x': range(0, len(models.data_reader.candidates[i_alvaro].dfolha_male)), 
        'Alvaro Dias-Ensino Superior-Datafolha': models.data_reader.candidates[i_alvaro].dfolha_superior, 'Alvaro Dias-Ensino Superior-IBOPE': models.data_reader.candidates[i_alvaro].ibope_superior,
        'Alvaro Dias-Ensino Superior-Facebook': models.data_reader.candidates[i_alvaro].facebook_superior
        # 'Alvaro Dias-Ensino Superior-Distribuition Facebook': models.data_distribuition.facebook_education_superior,
        # 'Alvaro Dias-Ensino Superior-Distribuition Censo': models.data_distribuition.census_education_superior
    })]

class ScoreVsLike:

    data_frame = [        
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_score)), 
            'Jair Bolsonaro-Jair Bolsonaro-Datafolha': [x/d_pesquisa for x in models.data_reader.candidates[i_bolsonaro].dfolha_score], 'Jair Bolsonaro-Jair Bolsonaro-IBOPE': [x/d_pesquisa for x in models.data_reader.candidates[i_bolsonaro].ibope_score],
            'Jair Bolsonaro-Jair Bolsonaro-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_bolsonaro].facebook_likes]
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_score)), 
            'Fernando Haddad-Fernando Haddad-Datafolha': [x/d_pesquisa for x in models.data_reader.candidates[i_haddad].dfolha_score], 'Fernando Haddad-Fernando Haddad-IBOPE':  [x/d_pesquisa for x in models.data_reader.candidates[i_haddad].ibope_score],
            'Fernando Haddad-Fernando Haddad-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_haddad].facebook_likes]
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_score)), 
            'Ciro Gomes-Ciro Gomes-Datafolha': [x/d_pesquisa for x in models.data_reader.candidates[i_ciro].dfolha_score], 'Ciro Gomes-Ciro Gomes-IBOPE': [x/d_pesquisa for x in models.data_reader.candidates[i_ciro].ibope_score],
            'Ciro Gomes-Ciro Gomes-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_ciro].facebook_likes]
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_score)), 
            'Marina Silva-Marina Silva-Datafolha': [x/d_pesquisa for x in models.data_reader.candidates[i_ciro].dfolha_score], 'Marina Silva-Marina Silva-IBOPE': [x/d_pesquisa for x in models.data_reader.candidates[i_marina].ibope_score],
            'Marina Silva-Marina Silva-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_marina].facebook_likes]
        }),       
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_score)), 
            'Geraldo Alckmin-Geraldo Alckmin-Datafolha': [x/d_pesquisa for x in models.data_reader.candidates[i_alckmin].dfolha_score], 'Geraldo Alckmin-Geraldo Alckmin-IBOPE': [x/d_pesquisa for x in models.data_reader.candidates[i_marina].ibope_score],
            'Geraldo Alckmin-Geraldo Alckmin-Facebook':  [x/d_facebook for x in models.data_reader.candidates[i_marina].facebook_likes]
        })]

class Score:

    data_frame = [        
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_bolsonaro].dfolha_score)), 
            'Jair Bolsonaro-Jair Bolsonaro-Datafolha': models.data_reader.candidates[i_bolsonaro].dfolha_score, 'Jair Bolsonaro-Jair Bolsonaro-IBOPE': models.data_reader.candidates[i_bolsonaro].ibope_score
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_haddad].dfolha_score)), 
            'Fernando Haddad-Fernando Haddad-Datafolha': models.data_reader.candidates[i_haddad].dfolha_score, 'Fernando Haddad-Fernando Haddad-IBOPE':  models.data_reader.candidates[i_haddad].ibope_score
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_ciro].dfolha_score)), 
            'Ciro Gomes-Ciro Gomes-Datafolha': models.data_reader.candidates[i_ciro].dfolha_score, 'Ciro Gomes-Ciro Gomes-IBOPE': models.data_reader.candidates[i_ciro].ibope_score
        }),
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_marina].dfolha_score)), 
            'Marina Silva-Marina Silva-Datafolha': models.data_reader.candidates[i_ciro].dfolha_score, 'Marina Silva-Marina Silva-IBOPE': models.data_reader.candidates[i_marina].ibope_score
        }),       
        pd.DataFrame(
        {
            'x': range(0, len(models.data_reader.candidates[i_alckmin].dfolha_score)), 
            'Geraldo Alckmin-Geraldo Alckmin-Datafolha': models.data_reader.candidates[i_alckmin].dfolha_score, 'Geraldo Alckmin-Geraldo Alckmin-IBOPE': models.data_reader.candidates[i_marina].ibope_score
        })]