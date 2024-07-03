<!-- Hey fancy seeing you here -->
###### Heya LHL cohort👋 right here is the response:
➡️ [Click here: Jump to task response](#response) ⬅️
🐜
# Security Categorization Case Study (Task 1 - 5)
## task - storyline

Your client, CyberOpps, is a small development company in Canada.

CyberOpps is developing several unique and high value programs (and program structures)

that their C Suite Executives are seeking to protect with copyright or patent.

The C Suite Executives expressed that if given a choice,

they would rather destroy their unique product
than let it be stolen.

CyberOpps also values an SQL Database of private employee and client information.

Kevin covets (covet = desires, yearns to possess or have). the company’s
high value programs and employee and client information.

Kevin knows that CyberOpps relies on
an unpatched 2019 Windows server
that can be exploited through TitanFTP.

___
# > Share with Discord!
## response
-> Please check the note bellow before proceeding 😸
### Note:
> This text covers tasks 1 - 5
> 
> Given the information in the storyline, it is known that the high value asset (HVA) is high value programs.
> 
> However, the type of data and its relative value contained in the SQL Database is *unknown**.
> 
> The company *may* be developing its HVA in relation to medical, financial or personal data.
>
> In other words, data type contained in the SQL databse can be assumed to be personal and financial.
> However, it is possible that client information is medical, if the company's HVA is related to medical programs.
> 
> The organization mission and goals are not revealed and the nature of the data type stored is unknown.
> The following tasks were performed with this lack of information in mind.

### Task 1:
-> Classify CyberOpps’ each **information asset** as one of the following:

(P) privacy - (M) medical - (IP) proprietary - (F) financial - (SM) security management - (S) systems

- IP : programs, program structures, development environment (potentially proprietary)
- Privacy: potential SQL Database of private employee and client information
- Financial : potential Database of private employee and client information
- medical : potential SQL Database of private employee and client information
- System : server (vulnerable), developer computers, network
- Security management : logs, network monitoring tools, firewalls

### Task 2
-> Rank CyberOpps' information assets' importance as follows (from most important to least important, as listed below):

(IP) Proprietary : programs, program structures
(P)  Privacy : employee and or client PII 
(M)  Medical : employee and or client medical information
(F)  Financial : employee and or client financial information
(SM) Security management : logs, network monitoring tools, firewalls
(S)  System : server (vulnerable), virtual environment (development computers), network environment

### Task 3
-> Use the SC equation (given below) to categorize the impact to CyberOpps if each asset were to be compromised:
> SC information type = {(confidentiality, impact), (integrity, impact), (availability, impact)}

- SC IP = {(confidentiality, high), (integrity, low), (availability, low)}

*Confidentiality* : If compromised, data owner "would rather destroy their unique product, than let it be stolen." As noted above IP is HVA. Data owner chooses destruction over loss of confidentiality. 

*Integrity* : integrity of the project as whole* is important, but high value programs developed in a company would typically be encircled with security controls (e.g. GIT, data backups, data segregation) that would mitigate and remediate loss of integrity. 

*Availability* : availability of the project is important, but high value programs developed in a company would typically be encircled with security controls (e.g. GIT, data backups, data segregation) that would mitigrate and remdiate loss of availability.

- SC for Data type: Privacy, Medical, Financial  = {(confidentiality, moderate), (integrity, low), (availability, low)}
> Given the information so far, we do not know the organization mission or goals. Organization choses self-erasure over theft of HVA.
> 
> Data held in SQL database holds importance, but it's relation or complimentation to HVA is unknwon.
>
> Data could be used to **reverse engineer HVA**, depending on its structure, labels, comments, and other information.

*Confidentiality* : If compromised, personal, financial or medical data may lead to leak of PII, secrets, or critical information. Data may be used to reverse engineer HVA, depending on its form or nature. Though of high importance, loss of confidentiality is moderate due to measures in place for a typical development organizaiton.

*Integrity* : Data held by in a developemnt company would typically be encircled with security controls (e.g. data backups, data segregation) that would mitigate and remediate loss of integrity. Though of great importance, loss of integrity is low due to measures in place for a typical development organizaiton to recover integrity.

*Availability* : Data held by in a developemnt company would typically be encircled with security controls (e.g. data backups) that would mitigate and remediate loss of integrity. Though of great importance, loss of availability is low due to measures in place for a typical development organizaiton to recover availability.

- SC for Security management = {(confidentiality, high), (integrity, low), (availability, low)}

*Confidentiality* : If confidentiality was compromised to attackers: network's structure, security measures, and vulnerabilities could be exposed providing valuable information that would lead to loss of confidentiality for organizaiton's HVA. Therefore, a loss of confidentiality is high.

*Integrity* : while integrity of logs and network monitoring data is important, their primary value lies in protecting confidentiality and availability of HVA on the network. Atackers manipulating logs to hide tracks is important, but the direct impact on the company's operations is relatively low compared to loss of confidentiality.

*Availability* : Availability of security management assets is important for monitoring and incident response. The organization being a development business is assumed to posses backup systems or manual monitoring procedures in place that should remdiate for a temporaty loss of availability.

- SC for Systems: {(confidentiality, low), (integrity, moderate), (availability, moderate)}
(S)  System : server (vulnerable), virtual environment (development computers), network environment

*Confidentiality* : System information is important and may contain sensitive information *about* : network environment, system configurations, developer computers. Loss of confidentality on systems information does not impact the organization to the same high degree as loss on IP HVA, PII or medical or financial data. Operations can carry on.

*Integrity* : Loss of integrity on system configurations, software, or data, has potential to disrupt development and production environments. Assuming measures in place, such as back-ups, enviroment set-up documentation, available hardware, Loss of integrity could be remidiated, but disruptions may last and negatively effect organization operations.

*Availability* : Availability of system assets is needed for operations. Downtime on servers, developer computers, network, environment would disrupt business activities, development processes. Assuming measures in place, such as back-ups, enviroment set-up documentation, available hardware, Loss of Availability could be remidiated, but disruptions may last and negatively effect organization operations.

### task 4
-> Create the SILs based on the SC equation results.

Hey but wait, How to calculate SILs from SC?
> 1. Identify the SC equation for each type of information asset.
>    
> 2. Evaluate the highest impact category (confidentiality, integrity, or availability) from the SC equation.
>    
> 3. Assign the SIL based on the highest impact identified:
>    
> e.g.
> 
> High (H) if any impact category is high. Moderate (M) if all impacts are moderate and no high impacts. Low (L) if all impacts are low.
> 
> SIL reflects the most significant potential impact of a compromise on C,I,A for each type of information asset.


#### Intellectual Property SIL = High
IP is HVA. Therefore, confidentiality of IP is high.
> SC IP = {(confidentiality, high), (integrity, low), (availability, low)}

#### Privacy, Medical, Financial Data SIL = Moderate
Exact Data type contained about clients and employees in unconfirmed, liekly PII and financial informaiton, possibly client medical data type. Confidentiality is moderate as it is unknown, and could potentially be secured with hashing, data segregation, or other security controls.
> SC for Data type: Privacy, Medical, Financial  = {(confidentiality, moderate), (integrity, low), (availability, low)}#

#### Security management Data SIL - High
Security management confidentiality is high as it can be leveraged to impact HVA's confidentiality.
> SC for Security management = {(confidentiality, high), (integrity, low), (availability, low)}

#### System Data SIL - moderate
System Integrity and Availability are moderate, as they both impact organization operations and can reasonably be assumed to have remediation strageies.
> SC for Systems: {(confidentiality, low), (integrity, moderate), (availability, moderate)}

## Task 5
-> Use the National Vulnerability Database (NVD) to look up and assess the threat that the unpatched 2019 Windows Server
(and the fact that Kevin has his Valentines Day exploit for the TitanFTP vulnerability found on these servers) are to CyberOpps and its assets.

Steps taken to complete this task:
> Go to `https://nvd.nist.gov/vuln/search`
> 
> Searching for `Windows Server 2019` is *too broad*!
> Instead, narrowing down in our basic search with `TitanFTP 2019` will yeild narrower results
>
> This leads us to two Vulnerabilities CVE-2022-34006 and CVE-2022-34005. Both Vuln IDs relate to Microsoft SQL Express.
>
> Then, asses the impact of the vulnerabilities onto the data owner's asssets.

#### Threat assesment 
- [CVE-2022-34005](https://nvd.nist.gov/vuln/detail/CVE-2022-34005)

  Base Score: 9.8 CRITICAL

  Vector:  CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

  Exploit: Remote Code Execution, enables attackers to take control of a system or application completely while acting **remotely**.

  *Assesment* : All of the assets are compromised including their respective CIA. Attacker can execute code **remotely** and take control of systems and or applications.
  HVA, Data, Security Measures, Systems are all affected. 

  *Recommendation* : Vendor, South River Technologies, recommends Upgrading a Legacy Installation. Alternatively, use diffrent FTP services.

- [CVE-2022-34006](https://nvd.nist.gov/vuln/detail/CVE-2022-34006)

  Base Score: 7.8 HIGH

  Vector:  CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H

  Exploit: Unprivileged Windows users to execute commands **locally** as NT AUTHORITY\SYSTEM, which is a built-in Windows account with the highest privileges on the operating system.

  *Assesment* : Attacker must gain access to the local network. Some security controls may block this level of access. If attack is successfull, all of the assets are compromised including their respective CIA.  HVA, Data, Security Measures, Systems are all affected. 

  *Recommendation* : Vendor, South River Technologies, recommends Upgrading a Legacy Installation. Alternatively, use diffrent FTP services.
