﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demographics.Facebook.Processing.Models
{
    public class PresidentialElection
    {
        public PresidentialElection()
        {
            elections_poll = new List<ElectionPoll>();
        }

        public List<ElectionPoll> elections_poll { get; set; }
    }
}
