# ( ͡° ͜ʖ ͡°)
# RMF Stage 2 - Selecting Controls (Part One)
## Stage 2, breakdown:
- selecting controls
- tailoring controls
- documenting controls

As specified by NIST, outcomes of this stage are:

Control baselines selected and tailored \
Controls designated as system-specific, hybrid, or common \
Controls allocated to specific system components \
System-level continuous monitoring strategy developed \
Security and privacy plans that reflect the control selection, designation, and allocation are reviewed and approved \

# tasks of the Select stage (1,2,3,4):
### Task 1 - Common Control Identification:
identify the security controls that are provided by the organization as common controls for organizational information systems and document the controls in a security plan (or equivalent document).

### Task 2 - Security Control Selection/System-Specific Control Selection:
select the security controls for the information system and document the controls in the security plan.


### Task 3 - Monitoring Strategy:
develop a strategy for the continuous monitoring of security control effectiveness and any proposed or actual changes to the information system and its environment of operation.

### Task 4 - Security Plan Approval:
review and approve the security plan.
---
#### Common Controls vs. System-Specific Controls

Common controls are controls that support multiple systems efficiently and effectively as a common capability. 
 - Common controls = __inherited controls__

System-specific controls provide a capability for a particular system only and are the primary responsibility of system owners and their respective authorizing officials. 
- An example: IA-6 AUTHENTICATION FEEDBACK, designed to obscure the feedback of authentication information during the authentication process.
---

# Task 1 of Select: Identify Common Controls
- __Identify__ common controls in organization.
- __document__ the controls in a security plan (or equivalent document).

### Security Control Family (NIST) SP 800-53
Hierarchy in control family; begin with a base control family (broadest set). Then, branches to one or more sub-control families (sub-sets).

### NIST SP 800-53 [Control Families](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home)
### NIST  SP 800-53 [Access Controll Familly](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=AC)

```WASSSSUPPPPPP !!
+----------------------+
|   Control Families   |
|                      |
|  +----------------+  |
|  |Access Controll |  |
|  +----------------+  |
|  |Incident reponce|  |  
|  +----------------+  |
|  |       ...      |  | 
|  +----------------+  |
+----------------------+
```

### 3 control implementation approaches
- __Common controls__: controls that provide a capability for multiple systems  __COMMON__ __INHerited___
- __System-specific controls__: controls that provide a capability for a particular system only __SPECIFIC__
- __Hybrid controls__: controls that have both system-specific and common characteristics __HYBRID__

# Task 2 of Select: Select System-Specific Controls
- __select__ the security __controls for the information system__ 
-__tailoring__
- __document__ the controls in the security plan.


The tailoring process includes:

- identifying and designating common controls in initial security control baselines,
- applying scoping considerations to the remaining baseline security controls,
- selecting compensating security controls (if needed),
- assigning specific values to organization-defined security control parameters via explicit assignment and selection statements,
- supplementing baselines with additional security controls and control enhancements, if needed, and
- providing additional specification information for control implementation, if needed.




##### Access control family  
| No. |  Access control family                                   |
|-----|----------------------------------------------------------|
| 1   | POLICY AND PROCEDURES                                    |
| 2   | ACCOUNT MANAGEMENT                                       |
| 3   | ACCESS ENFORCEMENT                                       |
| 4   | INFORMATION FLOW ENFORCEMENT                             |
| 5   | SEPARATION OF DUTIES                                     |
| 6   | LEAST PRIVILEGE                                          |
| 7   | UNSUCCESSFUL LOGON ATTEMPTS                              |
| 8   | SYSTEM USE NOTIFICATION                                  |
| 9   | PREVIOUS LOGON NOTIFICATION                              |
| 10  | CONCURRENT SESSION CONTROL                               |
| 11  | DEVICE LOCK                                              |
| 12  | SESSION TERMINATION                                      |
| 13  | SUPERVISION AND REVIEW — ACCESS CONTROL                   |
| 14  | PERMITTED ACTIONS WITHOUT IDENTIFICATION OR AUTHENTICATION |
| 15  | AUTOMATED MARKING                                        |
| 16  | SECURITY AND PRIVACY ATTRIBUTES                           |
| 17  | REMOTE ACCESS                                            |
| 18  | WIRELESS ACCESS                                          |
| 19  | ACCESS CONTROL FOR MOBILE DEVICES                        |
| 20  | USE OF EXTERNAL SYSTEMS                                  |
| 21  | INFORMATION SHARING                                      |
| 22  | PUBLICLY ACCESSIBLE CONTENT                              |
| 23  | DATA MINING PROTECTION                                   |
| 24  | ACCESS CONTROL DECISIONS                                 |
| 25  | REFERENCE MONITOR                                        |

