# RMF Stage 5 - Authorizing Information Systems
# Authorize stage tasks
- Finalize POA&M
  - Compile and review deficiencies
- Assemble authorization package
  - Gather essential security documents
- Perform risk determination
  - Assess and finalize risks
- Make a risk acceptance decision
  - Decide on system authorization

# glossary
| Acronym | Expansion |
| - | - |
| RMF | Risk Management Framework |
| NIST | National Institute of Standards and Technology |
| POA&M | Plan of Action and Milestones |
| ISO | Information System Owner |
| ISSO | Information System Security Officer |
| SCA | Security Control Assessor |
| AO | Authorizing Official |
| SAR | Security Assessment Report |
| ATO | Authority To Operate |
| IATT | Interim Authority To Test |
| DATO | Denial of Authority To Operate |
| ATC | Authority to Connect |
| CIO | Chief Information Officer |
| SSP | System Security Plan |

Enclaves:
Shared Security Controls:  Common Controls in the enclave
Quick Adaptation: updating the controls in the enclave will automatically propagate compliant security measures to all systems within that enclave.

Traffic Light Metaphor in RMF Stage 5:
| **Traffic Light** | **Meaning** | **In RMF Terms** | **Actions** |
|-------------------|-------------|------------------|-------------|
| **Green Light (Authority to Operate - ATO)** | The system meets security requirements and is authorized to operate. | The system has been assessed, risks have been addressed to an acceptable level, and the authorizing official (AO) has granted an ATO. The system can proceed to production and operate within its intended environment. | Continue normal operations while maintaining monitoring and regular assessments. |
| **Yellow Light (Interim Authority to Test - IATT)** | The system is not fully compliant but can operate in a limited capacity for testing purposes. | The system is in a state where it's not entirely meeting security standards but is being tested to identify and mitigate risks. The AO grants an IATT for a specific period to conduct these tests. | Conduct the necessary tests, address identified vulnerabilities, and work towards meeting full compliance to obtain an ATO. |
| **Red Light (Denial of Authority To Operate - DATO)** | The system does not meet security requirements and is not authorized to operate. | The AO has determined that the risks are too high, the system has significant security defects, and it cannot operate in its current state. | Stop operations immediately, address the deficiencies and risks, make necessary improvements, and then re-assess the system for potential re-authorization. |
