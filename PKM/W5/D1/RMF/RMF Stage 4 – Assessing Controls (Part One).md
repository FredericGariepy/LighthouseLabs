# RMF Stage 4 – Assessing Controls (Part One)

WOW before you do any of this shit look at [Sample Assesment OBJECT](#sample-assessment-object)

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

## Assessment Procedures
We're In the business of validating selected controls. \
"Assessment __objectives__ are created for each control being validated."

```python
def Assesment proceedures(assessment objectives)
    assessment_objectives = (determination_statements, methods, objects)
    return assessment_finding
```
assessment procedure(security_control) => assessment finding
assessment procedure(privacy control) => assessment finding

These findings reflect, or are subsequently used, to help determine the overall effectiveness of the security or privacy control. \
i.e. function(assessment finding) =>  overall effectiveness # I don't know the function name

"Assessment objectives define assessment object, assessment method, assessment coverage, assessment depth, and assessment findings"
```python
class AssessmentObjectives:
    def __init__(self, assessment_object, assessment_method, assessment_coverage, assessment_depth, assessment_findings):
    self. ... = ...
```

assessment_object\
AssessmentObjectives.objects \
Assessment __objects__ = specific items being assessed \
Assessment __objects__ = determination statements, specifications, mechanisms, activities, and individuals, as explained below:
| Word          | Explanation                                                                                  |
|---------------|----------------------------------------------------------------------------------------------|
| Determination Statements | Qualities to be assessed in a particular context.                                        |
| Specifications  | Documentary artifacts related to the control, including plans, policies, procedures, and regulations. |
| Mechanisms     | System functionality or features that support or enforce the control.                       |
| Activities     | Actions to be taken in system configuration, operation, or sustainment.                      |
| Individuals    | Parties responsible for performing activities related to the control.                       |

AssessmentObjectives.Methods \
Assessment methods =  list(examine, interview, test)  # nature of the assessor actions 

examine \
> this activity involves reviewing documentation, policies, procedures, and other artifacts to determine if they are consistent with the security controls and requirements. This activity is primarily focused on assessing the control design.

_The examine method_ is the process of : reviewing, inspecting, observing, studying, analyzing >>  __i.e. 'check on'__ \
examine_method = check_on(specifications, mechanisms, activities) \
examine_method = check_on(AssessmentObjectives.objects.specifications, AssessmentObjectives.objects.mechanisms, AssessmentObjectives.objects.activities) \
"The purpose of the examine method is to facilitate assessor understanding, achieve clarification, or obtain evidence" \
```python
#examine method
def examine(assesmentObject<specs, mech, activity>) => [evidence, understanding, clarificaiton]
```

interview \
>  this activity involves conducting interviews with system administrators, security personnel, and other relevant stakeholders to verify that the controls are implemented and operating as intended. This activity is primarily focused on assessing the control implementation.

"_The interview method_ is the process of: __holding discussions__ to do: facilitate assessor understanding, achieve clarification, or obtain evidence." \
def interview_method: call (examine method(), people) \
```python
#interview_method
def interview_method(examine(), people) => discussions
```

test \
>  this activity involves testing the security controls to determine if they are effective in mitigating risks and protecting the system. This activity is primarily focused on assessing the control effectiveness.

"The test method is the process of exercising one or more assessment objects (i.e., activities or mechanisms) under specified conditions to compare actual with expected behavior." \
def test(AssessmentObjective.object.mechanisms, AssessmentObjective.object.activities) \
```python
# test method
def test(mechanisms or activities, expected) => accuracy
```

Result of all three assessment methods, are used in making specific determinations <sub>(defined in determination statements)</sub> to succeed in objectives for the assessment procedure.

> Note: example of assessment procedures (object, objectives, and methods) in assessment tailoring later in the reading.



## Testing Coverage and Depth

Subject: parent class of `Methods` used by AssessmentObjectives.Methods.<examine,intervie,test> \
Methods base class takes (depth, coverage) # help define the level of effort for the assessment. 
class Methods(depth, coverage) # help define the level of effort for the assessment. 

depth \
depth # the rigor of and level of detail in Methods(i.e. examination, interview, and testing). \
__Possible Values depth__ = (basic, focused, comprehensive)

coverage \
coverage # scope or breadth of in Methods(i.e. examination, interview, and testing) \
scope: count, type in:  [specifications, mechanisms, and activities, individuals] \
__Possible Values of scope__ = (basic, focused, comprehensive)


organization assurance requirements defines : appropriate depth and coverage for Method.<examine,intervie,test> \
"As assurance requirements increase with regard to the development, implementation, and operation of security and privacy controls within or inherited by the information system" \
Δ Assurance requirements = Δ security and privacy controls # in or inherited 
Δ Assurance requirements = Method.<examine,intervie,test>(Δ depth, Δcoverage, ...)

### Table Assessment methods
|           | examine | interview | test |
|-----------|---------|-----------|------|
| specification |plans, policies, procedures,requirements,designs|           |      |
| mechanism     |Hard/Software, configs|           |Hard/Software, configs|
| activities    |Sys op. Admin. maintenance|Sys op. Admin. maintenance|Sys op. Admin. maintenance|
| individuals   |         |Operators, Admins, maintainers|

### Table Assessing Control Compliance (three testing technique)
|             | basic       | focused    | comprehensive |
|-------------|-------------|------------|---------------|
|   BOX     |  black :black_circle:  | grey :grey_heart:  | white :white_circle:  |
|   Confidence | some | increased | High |
| Based on: | high-level process, functional | Architecture, integrations, op env | full knowledge |


### Table Assessment Activities (Activity and objective of Methods)
|             | examine                             | interview                  | test                                        |
|-------------|-------------------------------------|----------------------------|---------------------------------------------|
| activity    | check, Inspect, Review, Observe, study, analyze | conduct discussions        | assess objects under specified conditions |
| Objective   | understand, clarify, obtain evidence | understand, clarify, obtain evidence | Compare actual and expected results to determine control functionality, correctness, completeness |


### Table (activies/objective) : methods <examine, interview, test>
| Activities/Objectives | examine | interview | test |
|-----------------------|---------|-----------|------|
| Identify              |    x    |    x       |  x    |
| Develop               |    x     |      x     |    x  |
| Review                |     x    |    x       |      |
| Verify                |         |      x     |   x   |
| Validate              |         |     x      |  x    |
| Evaluate              |   x      |           |  x    |

## Assessment Tailoring
> Assessment tailoring is an essential part of the RMF process 

Assessment tailoring is the process of adjusting the level of rigor of the assessment.

To tailor the assessment, the organization needs to populate the parameters and adapt the generic objectives defined in the assessment procedures. 

__Populating parameters__: assessment boundary, the system environment, and the assessment objectives.

__Adapting generic objectives__:  For example, if the system under assessment stores sensitive information, the confidentiality objective would need to be adapted to ensure that the system adequately protects that information

__Adjusting assessment methods__:  For example, if the system under assessment is a legacy system, the assessment team may need to use manual testing methods instead of automated tools.
----

# sample assessment object
With corresponding assessment methods and objectives.

- Assessment __Object__: Network Access Control (NAC)

- __Description__: NAC controls ensure that only authorized devices and users can access the network.

Assessment __Methods__:
1. Penetration testing: the assessment team will attempt to bypass the NAC controls to gain unauthorized access to the network.
2. Configuration review: the assessment team will review the NAC configuration to ensure it aligns with the organization's security policies and industry best practices.
3. Compliance assessment: the assessment team will check the NAC controls against relevant regulations and standards, such as PCI-DSS or HIPAA.

Assessment __Objectives__:
1. Verify that the NAC controls are effective in preventing unauthorized access to the network.
2. Ensure that the NAC configuration aligns with the organization's security policies and industry best practices.
3. Confirm that the NAC controls meet relevant regulations and standards.












