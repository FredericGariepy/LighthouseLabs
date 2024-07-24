# Case Study: Class Network Vulnerabilities
W05D3 - Assignment
Wed Jul 24


### VM Context:
__Network__: VMS are on NAT Network. They have internet access.They have internal-VM access as well.

__CS value for system__: { Confidentiality: Moderate, Integrity: Moderate,  Availability: Moderate } \
In real word, each asset would have its own CS value.  \
We put every CIA: moderate (make life easy).

Some __asset versions were artificially lowered__. \
This was done in order to allow for greater vulnerabilities to be researched.

### Workflow -  How this was done:
1. Gather Information: Categorise: Find VM OS versions, software versions
2. Research: Vulnerability assessment: Find asset related CVE
    2.1  Find asset related CVE, and CVE details. \
           - Use: https://www.cvedetails.com/vulnerability-list/ VND search \
           - Use: VND search \
           - Use: Your research skills. \
    2.2  Read the CVE and look for: \
           - Read CVE for description, listed mitigations, listed CV score, links to CWE. \
           - Use CWE  https://cwe.mitre.org/ for vulnerability category and mitigations. \
           - If you found a documented vector, plug it into NVD CVSS v3.x Calculator. \
           - Else, Use CVSS NVD CVSS v3.x Calculator to calculate CVS. 

3. Document findings: With information in Step 2, fill in the table in Step 3.

### Step 1: Gather Information
Windows OS:  Microsoft Windows 11 Home 10.0.22631 22631. Windows version 23H2, Sun Valley 3

Internet Information Services (IIS) webserver (S): IIS Version 10.0

PRTG Network Monitor (SM): PRTG Probe 24.2.96.1315, PRTG Server 24.2.96.1315

Linux OS: Ubuntu (debian) 22.04.4 LTS (Jammy Jellyfish)

Services with LISTENING PORTS (Ubuntu, Jammy Jellyfish) : \
| Service | Port |
|-|-|
|systemd-r | 53 |
|cupsd |  631|
|apache 2 | *:80|
|mysqld | 33060 , 3306 |

Add more as needed...

### Step 2: Research
Look up vulnerabilities in the NVD, CVE and any other tools you need. \
Calculate a customised CVSS score for each vulnerability \
Prioritise the vulnerabilities, giving rationales as to why you have chosen this order \
List relevant mitigations \
Run through chosen vectors used to generate the score \
Provide rationales for order of priority, then select vectors \

Resource links:

Search for asset related CVE
VND search
https://www.cvedetails.com/vulnerability-list/ VND search

Get CVE details
CVE home page

List of mitigations and vulnerability category
https://cwe.mitre.org/
software CWE

Chose a CVSS calculator
NVD CVSS v2.0 Calculator

NVD CVSS v3.x Calculator  ← We used this one 

NVD CVSS v4.0 Calculator


Proceed to the next page for Step 3.

Step 3: Document your Findings
Create a brief report that covers the following information:
The vulnerabilities you identified, and their relevant CVSS score
The variables you used to generate the score
The rationales for your order of priority
Recommendations for mitigation



Asset
Vulnerability
(CVE #ID)
CVSS score


CVSS Vector
Mitigations
PRTG Probe 24.2.96.1315
CVE 2023-32781

A command injection vulnerability was identified in PRTG v.23.2.84.1566 and earlier versions in the HL7 sensor. 

Where an authenticated user with write permissions could abuse the debug option to write new files that could potentially get executed by the EXE/Script sensor.


https://nvd.nist.gov/vuln/detail/CVE-2023-32781#vulnCurrentDescriptionTitle 
Base Score: 7.2

Impact Score: 5.9

Exploitability Score: 1.2
https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H&version=3.1 
https://cwe.mitre.org/data/definitions/77.html 

Assign permissions that prevent the user from accessing/opening privileged files.
Asset
Vulnerability
(CVE #ID)
CVSS score


CVSS Vector
Mitigations
apache 2.4.59
CVE  2024-36387

https://www.cve.org/CVERecord?id=CVE-2024-36387

Serving WebSocket protocol upgrades over a HTTP/2 connection could result in a Null Pointer dereference, leading to a crash of the server process, degrading performance.

https://nvd.nist.gov/vuln/detail/CVE-2024-36387


Overall CVSS Score:
4.3
—
CVSS Base Score:
4.5
Impact Subscore:
3.6
Exploitability Subscore:
0.9
CVSS Temporal Score:
4.3
CVSS Environmental Score:
4.3
Modified Impact Subscore:
3.6
Overall CVSS Score:
4.3




https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:H/UI:R/S:U/C:N/I:N/A:H/E:H/RL:O/RC:C/CR:M/IR:M/AR:M/MAV:N/MAC:L/MPR:H/MUI:R/MS:U/MC:N/MI:N/MA:H&version=3.1 
https://httpd.apache.org/security/vulnerabilities_24.html

Users are recommended to upgrade to version 2.4.60, which fixes this issue.
apache 2.4.59

*we just pretended that its 2.4.59
CVE 2024-38476

https://www.cve.org/CVERecord?id=CVE-2024-38476

information disclosure, SSRF or local script execution via backend applications whose response headers are malicious or exploitable

https://nvd.nist.gov/vuln/detail/CVE-2024-38476


Overall CVSS Score:
8.4
—
CVSS Base Score:
10.0
Impact Subscore:
5.8
Exploitability Subscore:
3.9
CVSS Temporal Score:
9.5
CVSS Environmental Score:
8.4
Modified Impact Subscore:
5.9
Overall CVSS Score:
8.4


https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N/E:H/RL:O/RC:C/CR:M/IR:M/AR:M/MAV:N/MAC:L/MPR:L/MUI:N/MS:U/MC:H/MI:H/MA:H&version=3.1 
https://httpd.apache.org/security/vulnerabilities_24.html

Users are recommended to upgrade to version 2.4.60, which fixes this issue.




