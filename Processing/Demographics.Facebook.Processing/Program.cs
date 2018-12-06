using Demographics.Facebook.Processing.Models;
using Demographics.Facebook.Processing.Tools;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;

namespace Demographics.Facebook.Processing
{
    class Program
    {
        static string PathConfig;
        static bool comLula = true;
        static List<string> names = new List<string>() { "1-DataFolha-20171130.xlsx", "1-DataFolha-20180607.xlsx", "1-DataFolha-20180821.xlsx", "1-IBOPE-20171022.xlsx", "1-IBOPE-20180624.xlsx", "1-IBOPE-20180819.xlsx" };

        static void Main(string[] args)
        {
            PresidentialElection election = new PresidentialElection();
            Config();

            Console.WriteLine($"Os arquivos serão obtidos do caminho: {PathConfig}. Ok?");
            Console.ReadLine();

            Console.WriteLine($"Considerar pesquisas com Lula? 1 - Sim e 2 - Não");
            comLula = Convert.ToInt32(Console.ReadLine()) == 1 ? true : false;

            using (Excel _excel = new Excel())
            {
                foreach (var item in Directory.GetFiles(PathConfig))
                {
                    if (comLula && !item.Contains("Haddad"))
                        election.elections_poll.Add(_excel.Read(item));
                    else if (comLula == false)
                    {
                        var v = item.Split('\\');
                        string n = v[v.Length - 1];

                        if (!names.Exists(x => x == n))
                            election.elections_poll.Add(_excel.Read(item));
                    }
                }
            }

            string json = JsonConvert.SerializeObject(election);
            Save(json);

            Console.WriteLine(json);
            Console.ReadKey();
        }

        static void Config()
        {
            var lines = File.ReadAllLines(Directory.GetCurrentDirectory() + "\\..\\..\\" + "config.txt");

            PathConfig = lines[0].Split('=')[1].Replace("\"", "");

            if (string.IsNullOrEmpty(PathConfig))
                PathConfig = Directory.GetCurrentDirectory() + "\\..\\.." + lines[1].Split('=')[1].Replace("\"", "");
        }

        static void Save(string text)
        {
            string complemento = comLula == true ? "ComLula" : "SemLula";
            File.WriteAllText(Directory.GetCurrentDirectory() + "\\..\\..\\Json\\" + $"PresidentialElection-{complemento}.json", text);
        }
    }
}
