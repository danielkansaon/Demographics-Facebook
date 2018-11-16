using Demographics.Facebook.Processing.Json;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;

namespace Demographics.Facebook.Processing.Models
{
    public class ElectionPoll
    {
        public ElectionPoll()
        {
            candidates = new List<Candidate>();
        }

        public string institute { get; set; }

        public int round { get; set; }

        [JsonConverter(typeof(DateFormatConverter), "yyyy-MM-dd")]
        public DateTime date { get; set; }

        public List<Candidate> candidates { get; set; }
    }
}
