|term|def.|
|-|-|
|ISAC|Information Sharing and Analysis Center
|"three-lettered agencies"|FBI, CIA, NSA, etc...|
| CJA|Crown Jewels Analysis|

[Even with AI, average time to detect is 200 days, and time to contain is 70.](https://www.statista.com/statistics/1417455/worldwide-data-breaches-identify-and-contain/)
<img src="https://github.com/user-attachments/assets/da3e3a77-d625-4d89-bd5f-150c7b6d2d01" width="500" alt="Bar chart image 2017 - 2023 Time to detect adn time to contain ">


Majority of incident response team is made up of augmentation workers who, as part of their regular roles, are generally have a variety of other responsibilities. \
It is possible that the team becomes permanent if the company continues to expand in size or if it experiences an increasing number of occurrences. 
## proactive

- Predicting adversary behavior
- Suggesting ways to find a threat
- Detecting anomalies, intrusions, baseline/threshold hits
- Studying event correlation
- Testing samples in sandboxes, honey pots, and emulated environments
- Documenting results
- Improving the protection of assets and infrastructure
- Performing mitigation
- Informing authorities (if applicable)

## Threat Hunting user stories

### Script/goal
- As [malicious script], I want to [send a request via TCP port 50050] so I can [establish connection].
- As an [infected zip], I want to [use WMI] so I can [maintain persistence].
- As a [Javascript code], I want to [exploit BITSAdmin] so I can [download modules].
### Actor & MITRE
APT37, uses Cobalt Strike in [T1218.011](https://attack.mitre.org/techniques/T1218/011/), planting rundll32 for proxy execution of malicious code.
### track motion, signatures, behaviours
Malware X:
- Executes a command via EXE file
- Imports and executes PowerShell cmdlets from an external source
- Runs a local .NET binary
- Uses setenv() function to add the variable to the environment
### Crown Jewels Analysis (CJA)
... continue








