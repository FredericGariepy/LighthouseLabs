# Cyber Security Risk Assessment and Management
# Menu
- [Multi-Tiered Risk Management Strategy](#multi-tiered-risk-management) handles: operational risks & strategic risks.
  > More like a business-related 'big picture'
  > 
  > __mostly business perspective/talk__.
- [ORM (operational risk management)](#operational-risk-management-orm) handles operational risks.
  > Management level process, used **ACROSS INDUSTRY**
  > 
  > ORM has three levels, four principles, and five steps.
- [NIST RMF](#nist-risk-management-framework) ALSO handles operational risks.

## Multi-Tiered Risk Management
#### need to know: Operational risks -v. strategic/tactical risks
two categories: 
- strategic (organization's ability to achieve its goals) AND tactical (impact day-to-day operations)
- operational

Examples of strategic risks are:
- Management team makes poor decisions, launching ineffective new products, etc.
- Company using technology that hinders their operations, for example, using on-premises IT instead of cloud-based services
- Consumer preferences changing, threatening your product offerings and value proposition

Examples of tactical risks are:
- Inadequate or failed internal processes
- System failures and downtime
- Poorly trained staff
- Cyber Security incidents, such as data breaches
- Fraud
- External events, such as natural disasters or pandemics

[Clarifications from mentor Q&A](https://github.com/FredericGariepy/LighthouseLabs/blob/main/PKM/W5/D1/mentorQ&A.md)
- Information systems represent the potential to introduce tactical risk to an operation.
- Policies represent a potential strategic risk as policy documents are considered strategic.
- Policies and information systems are tactical or operational tools in the company.
#### Multi-Tiered Risk Management Strategy (below):
```
    Strategic risk          risks: Policy, fines, reputation, market relevance, compliance # Risk to both enterprise and business
          /\
         /  \               
        /     \             width of triangle likely the volume of risks
      Enterprise            
     / (Policy)  \          The term `mitigation` changes at each level 
    /             \         between the strategy - tactical poles.
   / Business Areas \       e.g.
  /    (Processes)   \      mitigation = {Enterprise:Policy, Business:Process, Info Systems:Tools}
 /                    \     dictionary = {Policy: Binding agreements & laws, Process: Ways of doing business $,
/__Information Systems_\                 Tools: Technology that fits both Policy, Processes, Organization goals}  

      Tactical Risk        risks: compromise (CI), availability(A)   # risk to both info and buisiness
```
#### level breakdown
1. Enterprise Tier (Tier 1): Governance
    - Executive Leaders: set priorities, create policies to achieve strategic objectives.
    - $ Investment strategy to achieve mission and risk prioritie
    - Frame organization’s risk and informs all other activities.
    - Enterprise Tier is expressed as policies; scope for Enterprise Tier is the entire organization
    - Tier 1 sets the direction for Tier 2 managers.

2. Business-Area Tier (Tier 2):
    - Tier 2 focuses on developing risk-informed mission processes that meet Enterprise goals.
    - Administration of an enterprise architecture
    - $ Budget: Establishment of a consistent information system architecture
    - Business-Area Tier is expressed as processes. Its scope is a business, with parts having some autonomy.
    - Tier 2 builds infrastructure for execution of activities at Tier 3.

3. Information System (Tier 3):
    - Conduct the day-to-day activities
    - Risk from an information system perspective
    - Ensure systems are secure, reliable, and available
    - Information System Tier is expressed as guides, plans, procedures, ... Scope is a system defined by security.

Multi-Tiered Risk Management Strategy __example__:
> A company may have identified that one of their biggest risks is
> the possibility of an employee stealing trade secrets or other confidential information (this corresponds to Tier 1 stage).
>
> To reduce this risk, they might implement policies
> that allow employees with access to such information to only use it for work purposes (this corresponds to Tier 2 stage).
>
> They may also make sure all employees have training on
> how to implement identity and access management (this corresponds to Tier 3 stage)

## Operational Risk Management (ORM)
ORM has three levels, four principles, and five steps

#### Three Levels of ORM
1. __Time-Critical__ ORM
    - On-the-run mental or oral review
    - Employed by experienced personnel in time-critical situations
    - Used when unusual situations occur in an otherwise routine operation
2. __Deliberate__ ORM
    - Applies entire process
    - Most effective in group setting
    - Used when applying general principles to specific situations
3. __In-Depth__ ORM
    - Develop general principles
    - Set policies
    - Applied to complex systems or operations

#### Four Principles of ORM:
ORM is guided by four principles:

1. Accept risk when benefits outweigh costs
2. Do NOT accept unnecessary risk
3. Anticipate and manage risk by planning
4. Make risk decisions at the right level

#### Five Steps of ORM: (proactive risk management, for bottom line $)
> this is like 6 steps of incident response (IR)
```
...-> Identify risk -> Assess risk -> Mitigation/Decision -> Implement controls -> Take corrective action/Monitor -> ...
```

### ORM -v. Cyber Security Controls
> ORM is not industry specific

Cyber Security Controls:
-deals with securing, assessing, and testing an organization’s IT environment against malware and cyber attackers.

IT Risk Management (IT ORM):
- hardware and software defects, IT-related compliance and regulatory risks, human error, and natural disasters, among others

|Category|IT Risk Management (IT ORM) |Cyber Security Controls|
| - | -- | --|
| 1: Serrious, Immediate |Mission Failure, Loss of life, Unacceptable|Total loss, Compromise, Violation|
||||
| 2: Significant, Potential |Security Failure, Severe injury, Significan Damage|Partial loss, Some compromise,Degredation|


## NIST Risk Management Framework
<img src="https://csrc.nist.gov/CSRC/media/Projects/risk-management/images-media/RMF%20Logos/PNG%20Format/NIST%20RMF%20Graphc.png" alt="NIST RMF Logo" width="original width" height="220">

[NIST RMF](https://csrc.nist.gov/projects/risk-management/about-rmf) is an IT-specific implementation of ORM. (NIST SP 800-37)
- Security as part of SDLC (system development life cycle)

0. __Prepare__
    - Essential activities to prepare the organization to manage security and privacy risks 

__RMF 6 stages__:
1. __Categorize__ the system:
    - Categorize the system and information processed, stored, and transmitted based on an impact analysis.
    - Assess risks.

2. __Select__ appropriate controls:
    - Select the controls to protect the system based on Risk Assessment(s), tailored to the system and environment.

3. __Implement__ the controls:
    - Implement the controls and document how controls are deployed (system architecture, configuration, and procedures).

4. __Assess__ control application:
    - Assess to determine if the controls are in place, operating as intended, and producing the desired results (scope and depth of compliance, mitigations).

5. __Authorize__ system operation:
    - Senior official makes a risk-based decision to authorize the system (to operate) and accept residual risk.

6. Monitor system and environment:
    - Maintain acceptable security posture.
    - Continuously monitor control implementation and risks to the system.
  






