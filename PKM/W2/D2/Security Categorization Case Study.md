
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


Task 1:

Classify CyberOpps’ each information asset as one of the following: - (P) privacy - (M) medical - (IP) proprietary - (F) financial - (SM) security management - (S) systems

System : server (vulnerable), developer computers, network
IP : programs, program structures, development environment
Privacy: potential SQL Database of private employee and client information
Financial : potential Database of private employee and client information
medical : potential SQL Database of private employee and client information

VULN : unpatched 2019 Windows server
EXEC: TitanFTP

Task 2 Rank CyberOpps' information assets' importance as follows (from most important to least important, as listed below):

(IP) Proprietary : programs, program structures
(P)  Privacy : employee and or client PII 
(M)  Medical : employee and or client medical information
(F)  Financial : employee and or client financial information
(SM) Security management : logs, network monitoring tools, firewalls
(S)  System : server (vulnerable), virtual environment (development computers), network environment


Task 3: Use the SC equation (given below) to categorize the impact to CyberOpps if each asset were to be compromised:
SC information type = {(confidentiality, impact), (integrity, impact), (availability, impact)}

SC IP = {(confidentiality, high), (integrity, low), (availability, low)}

Confidentiality: If compromised, data owner "would rather destroy their unique product, than let it be stolen."

Integrity : integrity of the project as whole* is important, but high value programs developed in a company would typically be encircled with security controls (e.g. GIT, data backups, data segregation) that would remediate loss of integrity. 

Availability : availability of the project is important, but high value programs developed in a company would typically be encircled with security controls (e.g. GIT, data backups, data segregation) that would remdiate loss of availability.


SC for P,M,F = {(confidentiality, high), (integrity, low), (availability, low)}
Given the information so far, we do not know the organization mission or goals. Organization choses self-erasure over theft.
Data owner 
Given the unknown of importance of 







SC information type = {(confidentiality, impact), (integrity, impact), (availability, impact)}

