using Demographics.Facebook.Processing.Models;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demographics.Facebook.Processing
{
    class Program
    {
        static void Main(string[] args)
        {
            var eleicao = new BrazilElection();
            var listapesquisas = new List<ElectionPoll>();
            var pesquisa = new ElectionPoll();
            var candidatos = new List<Candidate>() { new Candidate()
            {
                name = "Bolsonaro",
                score = 27.88,
                age_intervals = new Age()
                {
                    age_16_24 = 18.07747489,
                    age_25_34 = 26.39885222,
                    age_35_44 = 22.59684362,
                    age_45_54 = 14.84935438,
                    above_55 = 18.07747489
                },
                education_status = new Education()
                {
                    elementary_school = 25.83241859,
                    high_school = 46.50567142,
                    higher_education = 27.66190999
                },
                gender = new Gender()
                {
                    female = 38.51744186,
                    male = 61.48255814
                },
                regions = new Region()
                {
                    southeast = 55.67765568,
                    south = 14.48551449,
                    northeast = 13.85281385,
                    north_midwest = 15.98401598
                }
            } };

            pesquisa.candidates = candidatos;
            pesquisa.date = new DateTime(2018, 9, 18);
            pesquisa.institute = "IBOPE";
            pesquisa.round = 1;
            listapesquisas.Add(pesquisa);
            eleicao.elections_poll = listapesquisas;

            string json = JsonConvert.SerializeObject(eleicao);
            Console.WriteLine(json);
            Console.ReadKey();
        }
    }
}
