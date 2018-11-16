using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demographics.Facebook.Processing.Models
{
    public class Candidate
    {
        public string name { get; set; }
        public double score { get; set; }
        public Gender gender { get; set; }
        public Age age_intervals { get; set; }
        public Education education_status { get; set; }
        public Region regions { get; set; }
    }
}
