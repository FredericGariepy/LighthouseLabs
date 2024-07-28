CVSS v3.1


- The Base Metric group: \
represents the intrinsic characteristics of a vulnerability that are constant over time and across user environments. 

- The Temporal Metric group: \
reflects the characteristics of a vulnerability that may change over time but not across user environments. 

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
 

"A vulnerable component is the thing that is vulnerable; also it’s the ___security scope___ that ___contains___ the vulnerability."

 "An impacted component is the thing that suffers the impact; also it’s the ___security scope___ that is ___affected___ by the vulnerability."

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


