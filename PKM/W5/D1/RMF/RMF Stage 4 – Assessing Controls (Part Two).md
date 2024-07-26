Assess RMF stage Task:
1. ~~Developing Security Assessment Plan~~
2. ~~Assessing Control Compliance~~
3. Preparing Security Assessment Report
4. Conducting Remediation.

Readings:
- [ ] page 32 and 33, [NIST:  Guide for Applying the Risk Management Framework to Federal Information Systems](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-37r1.pdf)

## dictionary
| Acronym | Expansion |
| - | - |
| RMF | Risk Management Framework |
| SOC | Security Operations Center |
| NIST | National Institute of Standards and Technology |
| SCA | Security Control Assessor |
| SCAR | Security Control Assessment Representative |
| CIO | Chief Information Officer |
| SSP | System Security Plan |
| POA&M | Plan of Action and Milestones |

- Who is primarily responsible for developing the security assessment report in an SOC
- What important information is covered in the security assessment report
- How the report provides visibility into specific weaknesses and deficiencies in the security controls employed
- How remediation actions are decided based on the findings and recommendations in the security assessment report

### SCA vs. SCAR | Security Control Assessor -v Security Control Assessment Representative

- The Security Control Assessor (SCA) is appointed by Chief Information Officer  CIO.
- SCA is the individual authorized to sign the final Security Assessment Report.
- SCAR (Security Control Assessment Representative) assist SCA.
    - Assesses control compliance
    - Assesses mitigations
    - Prepares draft Security Assessment Report


## Diagram Documenting the Assessing Control Compliance Step
```
┌────────────────────────────────┐
│ Control Compliance details.txt │
│ Unsatisfied controls.txt       │
│ Inherited controls.txt         │
| Supporting artifacts.txt       |
├────────────────────────────────┘
├───System Security plan.sql                   ┌────System Risk Assesment.txt
|                                              |
└───Plan of Action and Milestones.sql          │    Authorization Recomendation.txt
           └───────Security assessment report──┴───────┘
```



























