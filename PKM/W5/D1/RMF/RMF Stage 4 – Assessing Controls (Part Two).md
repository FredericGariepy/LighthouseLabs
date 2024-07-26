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
# steps for documenting the Assessing Control Compliance
1. __Document the assessment results__:
> the assessment results should be documented in a format that allows for easy review and analysis. This documentation should include the control objectives, the assessment methodology, and the results of the assessment.
2. __Identify any control deficiencies__:
> if any control deficiencies are identified during the assessment, they should be documented in detail. This documentation should include the specific control that is deficient, the severity of the deficiency, and any recommended remediation actions.
3. __Review and approve the assessment results__:
>  the assessment results should be reviewed and approved by the appropriate stakeholders, including the system owner, the authorizing official, and any other relevant parties.
4. __Update the SSP__:
>  any changes to the security controls resulting from the assessment should be documented in the SSP. The updated SSP should reflect the new security posture of the system.
5. __Update the Plan of Action and Milestones (POA&M)__:
>  if any control deficiencies are identified, a POA&M should be developed to address them. The POA&M should include specific remediation actions, timelines, and responsible parties.
6. __Document any residual risk__:
>  the residual risk associated with the assessed controls should be documented. This documentation should include the level of residual risk, the rationale for accepting this risk, and any risk mitigation strategies that will be implemented.
7. __Prepare the final assessment report__:
>  the final assessment report should document the assessment results, control deficiencies, and any remediation actions or risk mitigation strategies. The report should be reviewed and approved by the appropriate stakeholders before being submitted for authorization.

























