# RMF Stage 4 – Assessing Controls (Part One)
- [ ] finish later.


##### Diffrent types of controls
Base Control
> Base control example: A standard access control mechanism requiring strong passwords.

Control Enhancement
> Enhancement example: Implementing multi-factor authentication (MFA) in addition to the strong passwords.

Internal Dependencies: Controls that are interconnected within the system are assessed in a logical order, where the output or effectiveness of one control can affect or be affected by others.
> Control Dependency Example: If Control A is responsible for logging access attempts and Control B is responsible for reviewing logs, you need to assess Control A before assessing Control B. Control B relies on the data produced by Control A.
Assesment sequencing is important because of Internal Dependency.

External Dependencies: Any dependencies on external controls are identified and assessed to ensure that they do not undermine the effectiveness of the system’s controls.
> External Dependency Example: If your system depends on a third-party service for authentication, your assessment of the system’s authentication controls (e.g., Control C) would need to consider the security controls implemented by the third-party service (Control D).

Related Controls: The interactions between related controls are understood, so that the overall security posture is evaluated comprehensively, considering how different controls support or impact one another.
> Related Controls Example: In a system where encryption (Control E) is used to protect data at rest, and access controls (Control F) are used to manage who can access that data, both controls are related. The effectiveness of Control E (encryption) may be undermined if Control F (access controls) is weak or misconfigured.


# Glossary 
| Acronym | Expansion |
| --- | --- |
| RMF | Risk Management Framework |
| NIST | National Institute of Standards and Technology |
| AC | Access Control |
| MP | Media Protection |
| CM | Configuration Management |
| PL | Planning |
| RA | Risk Assessment |
| NAC | Network Access Control |
| PCI-DSS | Payment Card Industry Data Security Standard |
| HIPAA | Health Insurance Portability and Accountability Act |

 Purpose of the Assess Step?
> the purpose of the Assess step is to determine that selected security and privacy controls are implemented correctly, operate as intended, produce the desired outcome, and meet organizational or system security and privacy requirement


-    How to develop a security assessment plan
-    to assess controls as per the security assessment plan


## Assess stage, you complete four tasks

1. Develop security assessment plan
2. Assess control compliance
3. Prepare security assessment report
4. Conduct remediation


# first task in the Assess stage is to develop, review, and approve a plan
Basically, Security assessment plans describe what controls will be assessed.

What Information do Assessment Plans Provide?
- identify system, component, and organization-related roles and responsibilities
- assessment procedures for each security and privacy control
- identify the type of assessment to be conducted, such as development testing, initial authorization, re-authorization, or continuous monitoring. (part of authorize)

The purpose of the security assessment plan __approval__ is two-fold:
1. To establish the appropriate expectations for the security control assessment.
2. To bound the level of effort for the security control assessment. An approved security assessment plan helps to ensure that an appropriate level of resources is applied toward determining security control effectiveness.

#### Control Coverage and Control Depth
Control __coverage__ can be: comprehensive(high), focused(mid), or basic(low) 

Control __Depth__ how rigorously selected controls will be assessed

#### Assessment Optimization / determine required level of independence.
1. Step 1: assessment sequencing has internal dependencies in case of control and control enhancements and external dependencies in case of related controls.

2. Step 2: assessment consolidation: * Merges related assessment requirements. * Performs after assessment sequencing. * Eliminates duplicative testing.

___Wtf__ is ^ this saying?_ \
Assessment Sequencing sets the order for how assessments are performed, considering dependencies and relationships between controls. \
Assessment Consolidation follows this sequencing to merge related assessments, eliminate redundancy.


# Task 2: Conducting Security Controls Assessment (according to security assessment plan)
In the second task of the Assess stage, you assess the security controls in accordance with the assessment procedures defined in the security assessment plan.

Assessment Procedures
```python
def Assesment proceedures(assessment objectives)
    assessment objectives = (determination statements, methods, objects)
    return assessment finding
```

security or privacy control 
assessment procedure to a security or privacy control produces assessment finding














