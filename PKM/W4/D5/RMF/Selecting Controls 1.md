# RMF Stage 2 - Selecting Controls (Part One)

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


The tailoring process uses risk assessments to inform and guide its process. \
i.e. See where they're hitting from and controll that shit \
Tailoring includes:

- identifying and designating common controls in initial security control baselines,
- applying scoping considerations to the remaining baseline security controls,
- selecting compensating security controls (if needed),
- assigning specific values to organization-defined security control parameters via explicit assignment and selection statements,
- supplementing baselines with additional security controls and control enhancements, if needed, and
- providing additional specification information for control implementation, if needed.

At this point, start thinking about monitoring.. since controlls and monitoring are related. 

#### control Volatility. 

- __High Volatility Controls__:
These are controls that frequently change or are often subject to new threats. For example, a security control related to software patching may have high volatility because new vulnerabilities are constantly being discovered and need to be patched.

- __Low Volatility Controls__:
These are controls that do not change often and are generally stable. An example might be physical security controls like door locks or security guards, which do not need to be monitored or adjusted as frequently.
---

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

