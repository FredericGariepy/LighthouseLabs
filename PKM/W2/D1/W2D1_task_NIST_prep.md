<!-- Hey fancy seeing you here -->
###### Heya LHL cohort👋 right here is the response:
➡️ [Click here: Jump to task response](#response) ⬅️
🐜
# task
## NIST RMF Quick Start Guide ( W2 | D1 )
Access and review the resources and information available at [NIST’s Prepare Step page](https://csrc.nist.gov/Projects/risk-management/about-rmf/prepare-step) along with it's associated FAQ (with a focus on section 2 & 3).

FAQ section 2 & 3:

2. What is the Prepare step?
> The purpose of the Prepare step is to carry out essential risk management tasks at the organization, mission and business process, and
> system levels to establish context and help prepare the organization to manage its security and privacy risks using the Risk
> Management Framework (RMF).
>
> Prepare step tasks are completed before the Categorize step and support all subsequent Risk Management
> Framework steps and tasks.
>
> Ultimately, the intention of the Prepare step is to provide the information and resources necessary to
> successfully manage information security and privacy risk to the organization and its missions from the operation and use of systems.
3. What are some of the objectives and benefits of the Prepare step?
> The objectives and benefits of the Prepare step include:
> - Facilitating better **communication** between senior leaders and executives at the organization and mission and business process levels and system owners
> - Facilitating organization-wide **identification of common controls** and the **development of organizationally tailored control**
>   **baselines, reducing the workload on individual system owners and the cost of system development and asset protection
> - **Reducing the complexity** of the information technology and operations technology infrastructure using enterprise architecture concepts and models to consolidate, optimize, and standardize organizational systems, applications, and services
> - Identifying, **prioritizing**, and focusing resources on the organization’s high-value assets and high impact systems that require increased levels of protection and taking steps commensurate with the risk to such assets. 

## Task Instructions
Then use what you learn to assist you in the following scenario:

You are the head of cyber security for a start up company.
This company's main product is an online payment processor that must securely handle customer credit card information.
The company currently has only two developers, no formal security policies or procedures and the application is hosted in AWS and is accessed publicly over the internet via two dedicated web servers.
The information for your current user base of 200 people is stored on a server that is directly connected to the web servers for easy retrieval.

After reviewing the NIST quick start guide FAQ related to the prepare step,
perform the key preparation activties for the given scenario and identify the following:

1. The top 3 biggest risks to company security with explanations for your determination
2. Security controls that could compensate for the company's major risks
3. A strategy for implementing continous monitoring of company source code
4. Identify the company's high value assets

Now, review the Categorize Step page along with it's associated FAQ (with a focus on section 2 & 3).
Then using what you learned make a categorization determination around the company's database server and the potential impact on the organization if it is compromised in anyway,
be sure to address all elements of the CIA triad.
___
# -> Share your responses with your peers on discord!
## response

### top 3 biggest risk:
1. Data Breach:
   
   A Data breach would expose the company's data: PII and Financial data
   and without security policy in place the breach may be very deep,
   especially since the data is stored on the webservers.
   With no security policy, there may be poor debriefing about a data breach
   to customers. This would also lead to a loss of trust in the company.
   Both of these negative effects would break the company's operations.

2. [Insider threat](https://www.fortinet.com/resources/cyberglossary/types-of-cyber-attacks)

   Company has only 2 developers, and no security policy or procedures.
   Insider threats can occur both intentionally and *un-intentionally**.
   A majority of cybersecurity vulnerabilities are caused by humans.
   Without security policy in place, backups may not be avaible to revert
   the organization to a working stage or recover. 

3. Lack of security measures

   Without security measures in place, a plethora of possible
   vulnerabilities from unencrypted data to protect PII and Financial data,
   AWS cloud network misconfigurations, secrets mismanagement (like crypto keys),
   open up the organization to threats.
   Without security measures, recovery of the organization's operations is unlikely.
   
### Security controls that could compensate for the company's major risks

- Data controls:
  Encrypt data (using hashes), segreagate data (keep secrets isolated), use encryption key management systems (in AWS),
  perform data backups.

- Operational controls:
  System auto updates, use secure encrypted ports for ssh login, enable multi-factor authentification (MFA), use network
  segmentation, implement firewalls, employ network monitoring tools.

- Administrative controls:
  Data breach pollicies, to prevent, mitigate, recover from and disclose data breaches.

### A strategy for implementing continous monitoring of company source code

Using GIT for version control. Establish a secure CI/CD pipeline and using third party security code scanners. Set-up tests to ensure security and functionality. Use a development enviroment and run tests before deployment.

### Identify the company's high value assets

Database server containing PII and Financial data.
AWS infratructure containing web servers and database.

### Categorize Step : database server

| Task | Title             | Description                                        |
|-------|-------------------|----------------------------------------------------|
| P-12  | Information Types | Identify types of information processed, stored, and transmitted by the system. |
| P-13  | Information Life Cycle | Identify and understand all stages of the information life cycle for each information type processed, stored, or transmitted by the system |

##### P-12:
- information processed: financial, PII, user inputs
- information stored: financial (maybe), PII, account information
- information transmitted by the system: financial (transactions, 3rd party), PII (services, 3rd party), account (operations)

##### P-13:
In the database:
- user information is stored and used for service operations (login, auth, emails)
- PII information is likely stored, used for 3rd party services (shipping, marketing)
- financial information may be stored, used for 3rd party services (transactions)

Because this task involves an organization NOT at the federal level, trying to use Use NIS 800-60v2r1:
> `https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-60v2r1.pdf`
does not lend to any truly relatable information type.

Based outputs of P12, P-13, information type in this scenario will be:

   *Security Category* = {(confidentiality, Moderate), (integrity, Low), (availability, Low)}

Confidentiality

The confidentiality impact level is the effect of unauthorized disclosure of personally identifying information and financial data that an adversary could use to perform financial crimes and or crimes related to the use of gained personal identites. Loss of condidentiality will results in loss of public trust. Situation is exacerbated by the lack of security policies and measures. However, PII information stored is not likely to contain secrets such as SIN, SNN, Passport number, biometric data, and other highly sensitive PII, therefore confidentiality is important at a Moderate level.

Integrity

When inforamtion is modified, destructed, a loss of integrity can be remediated by Data backups, security controlls, administrative resets. Though there is currently a lack of security policies and measures that would act to remediate a loss of integrity. Integrity is important but at a lower level.

Availability

Availability of the system and its data is crucial though at a lower impact level. The organization has 2 web servers to offer some reundancy to its 200 users. 
