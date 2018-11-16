using Demographics.Facebook.Processing.Models;
using System;
using System.IO;
using System.Runtime.InteropServices;
using _Excel = Microsoft.Office.Interop.Excel;

namespace Demographics.Facebook.Processing.Tools
{
    public class Excel : IDisposable
    {
        _Excel.Application xlApp;

        public Excel()
        {
            //Create COM Objects. 
            xlApp = new _Excel.Application();
        }

        public ElectionPoll Read(string path)
        {
            _Excel.Workbook xlWorkbook = xlApp.Workbooks.Open(path);
            _Excel._Worksheet xlWorksheet = xlWorkbook.Sheets[1];
            _Excel.Range xlRange = xlWorksheet.UsedRange;

            try
            {
                int i = 3;
                ElectionPoll election = new ElectionPoll();

                while (xlRange[i, 1].Value2 != null)
                {
                    election.candidates.Add(new Candidate()
                    {
                        name = (string)xlRange[i, 1].Value2,
                        score = (double)xlRange[i, 2].Value2,
                        gender = new Gender()
                        {
                            male = xlRange[i, 3].Value2,
                            female = xlRange[i, 4].Value2
                        },
                        age_intervals = new Age()
                        {
                            age_16_24 = (double)xlRange[i, 5].Value2,
                            age_25_34 = (double)xlRange[i, 6].Value2,
                            age_35_44 = (double)xlRange[i, 7].Value2,
                            age_45_54 = (double)xlRange[i, 8].Value2,
                            above_55 = (double)xlRange[i, 9].Value2
                        },
                        education_status = new Education()
                        {
                            elementary_school = (double)xlRange[i, 10].Value2,
                            high_school = (double)xlRange[i, 11].Value2,
                            higher_education = (double)xlRange[i, 12].Value2,
                        },
                        regions = new Region()
                        {
                            southeast = (double)xlRange[i, 13].Value2,
                            south = (double)xlRange[i, 14].Value2,
                            northeast = (double)xlRange[i, 15].Value2,
                            north_midwest = (double)xlRange[i, 16].Value2,
                        }
                    });

                    i++;
                }

                election.institute = Path.GetFileName(path).Split('-')[0];
                election.date = DateTime.ParseExact(Path.GetFileName(path).Split('-')[1].Replace(".xlsx", ""), "yyyyMMdd", null);
                election.round = i <= 16 ? 2 : 1;

                return election;
            }
            finally
            {
                GC.Collect();
                GC.WaitForPendingFinalizers();

                //kill excel process
                Marshal.ReleaseComObject(xlRange);
                Marshal.ReleaseComObject(xlWorksheet);

                //close and release
                xlWorkbook.Close();
                Marshal.ReleaseComObject(xlWorkbook);
            }
        }

        public void Dispose()
        {
            xlApp.Quit();
            Marshal.ReleaseComObject(xlApp);
        }
    }
}
