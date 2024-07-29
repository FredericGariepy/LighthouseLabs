CVSS v3.1

### attacker side
- The Base Metric group: \
represents the intrinsic characteristics of a vulnerability that are constant over time and across user environments. 

### research , common knowledge  side
- The Temporal Metric group: \
reflects the characteristics of a vulnerability that may change over time but not across user environments. 

### asset side
- The Environmental Metric group; \
represents the characteristics of a vulnerability that are relevant and unique to a particular user’s environment.


Case: 

Web app auth bypass. Path Traversal. Payload. resource access to configurations.

Attack Complexity = conditions beyond the attacker's control that must exist in order to exploit the vulnerability

Click the two statements about the Base Metrics that are true. (check raw .md for answer)
- [ ] <!--TRUE-->Attack Vector reflects the context by which vulnerability exploitation is possible.
- [ ] Attack Complexity describes the level of privileges an attacker must possess before successfully exploiting the vulnerability.
- [ ] Privileges Required describes the conditions beyond the attacker's control that must exist in order to exploit the vulnerability.
- [ ] <!-- --> User Interaction captures the requirement for a user other than the attacker to participate in the successful compromise of the vulnerable component.
 
#### CVSS 3.1 Scope
"A vulnerable component is the thing that is vulnerable; also it’s the ___security scope___ that ___contains___ the vulnerability."

 "An impacted component is the thing that suffers the impact; also it’s the ___security scope___ that is ___affected___ by the vulnerability."

If Vulerable component == Impact component = Scope is Unchanged. \
If Vulnerable component != Impact component = Scope is ___Changed___.

<img src="https://cdn2.talentlms.com/sc/gAAAAABmpsQSaU9gcok83_m5kyMt-6q_RSey4wiY0snvu_aPMjiRFMRD4hoROkWiQDOsrSWNUNnDwD3-JdQcOgw70IeOQo8xxcg0-iDqpw8KFggUyYrPATz7LwHkhmCBP3x0GJjyhf8L-4vvkPNkyBqhUQCQT55Yuw==/firstdotorg/1695844820_course-v1-FIRST-CVSSv3.1-2020-SCORM-v1.2-20230927/assets/cvss_m003s049a.png" alt="CVSS Image">


Case: bank web app vulnerable to reflected cross-site scripting (XSS) \
Attacker tricks web app user to follow URL with custom parameters. \
parameters trigger XSS. \
Browser has Same Origin Policy (SOP), so XSS attack cannot access other domain.

Breakdown: 
XSS was blocked by web browser SOP control.  \
The vulnerable component was web app, impact component was web browser (and it blocked). \
web app and web browser are under different authority, therefore the __scope changed__

The vulnerable component is the web server vulnerable to cross-site scripting, and the impacted component is the victim's browser.
- The Scope is Changed.
 The vulnerable component and the impacted component are not the same thing, so the Scope cannot be Unchanged

Availability:
Attacks that consume network bandwith, processor cycles, diskspace. all effect the availablity 

The Confidentiality Impact and Integrity Impact metrics measure, respectively, \
the loss of confidentiality and integrity of ___data___ used by the impacted component. \
The Availability Impact metric measures the loss of availability of the impacted __component itself__.


|-|measures|
|-|-|
|C|component's data |
|I|component's data |
|A| Component _itself_|

Temporal Metric group: \
__Exploit Code Maturity measures the likelihood __of the vulnerable component being attacked. \

Enviromental Metric group: \

CIA modified base metrics are weight changes. Measured according to asset CIA. \
CIA `Not Defined` is the same as Medium by default.

Other base metric modifiers: \
Represent implmented protections (controls) measures, alterting configurations assumed when chosing base metrics (E.I hot fixes). \
`Not Defined` = associated base metrics (previously set).


#### Qualitative Scale is optional. 
<img src="https://cdn2.talentlms.com/sc/gAAAAABmpuB_e5duC4LruZ6RE8xX4Z_ZuvdauQSnHNFYTtVT-wklTw_R1DdjW4-SwEHbQxkDT5NKcVpYtDLf6f8OWh7Ct74xNPgy_vkbVnzr2XD48LSJqs2ptS8Ly91GgVjz-Lhe9SMkP9lv02X3Zh5lIuvCUxapGQ==/firstdotorg/1695844820_course-v1-FIRST-CVSSv3.1-2020-SCORM-v1.2-20230927/assets/Mod4_Slide106.jpeg" alt="Course Slide Image">


The CVSS v3.1 vector string is a text representation of a set of CVSS metrics. 

CVSS V3.1 Scoring scenarios.

#### Case 1:
An airplane in-flight entertainment system allows passengers to watch movies via mobile device over the plane's wi-fi network. \ 
The entertainment system creates a sandbox environment for each passenger. \
A flaw in the logic of the entertainment system allows an attacker to break out of the sandbox and access any data stored on the entertainment system. \
Only in-place wifi network. \
Answer: \
https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:L/RL:W/RC:R/CR:L/IR:H/AR:L
#### Case 2:

A machine-tooling organization’s website uses an embedded SQL database to store user data. \
The website is on the organization's internal network, not accessible from the Internet. \
The site creates SQL statements that include data supplied by users and passes these to the database. \
Insufficient validation of this data allows SQL-injection attacks. \
Answer \
Vulnerable component is the website. \
Impacted component databse in embeded in the software runnign the website, same securit scope. \
https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N/E:P/RL:T/RC:C/CR:L/IR:M/AR:L/MAV:A/MI:N

#### case 3:
A standalone document viewer displays documents that can contain embedded images. The viewer does not correctly check the length of these images before loading them into a memory buffer, allowing malformed images to overflow the buffer A carefully malformed image can contain malicious code that overwrites document-viewer code, gets run, and takes over the document-viewer program, inheriting all its rights and permissions. 


Vulnerable component: document viewer \













