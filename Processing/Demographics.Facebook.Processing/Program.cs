using Demographics.Facebook.Processing.Models;
using Demographics.Facebook.Processing.Tools;
using Newtonsoft.Json;
using System;
using System.IO;

namespace Demographics.Facebook.Processing
{
    class Program
    {
        static string PathConfig;

        static void Main(string[] args)
        {
            PresidentialElection election = new PresidentialElection();
            Config();

            Console.WriteLine($"Os arquivos serão obtidos do caminho: {PathConfig}. Ok?");
            Console.ReadKey();

            using (Excel _excel = new Excel())
            {
                foreach (var item in Directory.GetFiles(PathConfig))
                    election.elections_poll.Add(_excel.Read(item));
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
        }

        static void Save(string text)
        {
            File.WriteAllText(Directory.GetCurrentDirectory() + "\\..\\..\\Json\\" + "PresidentialElection.json", text);
        }
    }
}
