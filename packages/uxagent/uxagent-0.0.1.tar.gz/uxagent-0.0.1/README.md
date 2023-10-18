RANDOM USER AGENTS
==================

Random User Agents is a python library that provides list of user agents,
from a collection of more than 326,000+ user agents, based on filters.

Installation
------------

You can install random useragent by running the following command:

```bash
  pip install uagent
```

Some of the filter names which can be passed to `UserAgent()` are listed below:

    popularity : [ POPULAR, COMMON, AVERAGE ]

    software_engines : [ BLINK, GECKO, WEBKIT ]

    hardware_types : [ MOBILE, COMPUTER, SERVER ]

    operating_systems : [ UNIX, LINUX, WINDOWS, MAC ]

    software_names : [ EDGE, CHROME, CHROMIUM, FIREFOX, OPERA ]

    software_types : [ WEB_BROWSER, BOT__CRAWLER, BOT__ANALYSER ]


*All filters are available in UAGENT.params*

Usage
-----

To get 100 user agents of browser `chrome` based on operating systems `windows` or `linux`

```python

from UAGENT.user_agent import UserAgent
from UAGENT.params import SoftwareName, OperatingSystem


# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter
    
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
useragent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

# Get list of user agents.
user_agents = useragent_rotator.get_user_agents()

# Get Random User Agent String.
user_agent = useragent_rotator.get_random_user_agent()

```

License
-------
The MIT License (MIT). Please see [License File](https://github.com/Luqman-Ud-Din/random_user_agent/blob/master/LICENSE) for more information.


User Agents Source
-------
special thanks to [whatismybrowser](https://developers.whatismybrowser.com/) for providing real user agents.
