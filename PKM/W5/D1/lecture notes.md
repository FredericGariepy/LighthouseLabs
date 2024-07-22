
#### NIST CSF
[The CSF 1.1 Five Functions](https://www.nist.gov/cyberframework/getting-started/online-learning/five-functions)

<img src="https://www.nist.gov/sites/default/files/styles/220_x_220_limit/public/images/2018/04/12/ipdrr_circle.png?itok=qV5agiH5" width="auto" />

#### NIST RMF, Implement step, Access Controls
NIST has good langage for mobilizing senior management

NIST RMF[Implement step Q&A](https://csrc.nist.gov/CSRC/media/Projects/risk-management/documents/04-Implement%20Step/NIST%20RMF%20Implement%20Step-FAQs.pdf) 

NIST [Cybersecurity and Privacy Reference Tool](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home), from there, chose from __Control Families__:

e.g.:
- [Access Control families](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=AC)
- [Risk Assesment](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=RA)

In practice, [IR](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home?element=IR) (incident response), is a neglected area. As it does not give immediate benefits.
- Unlike,  Immediate access controls benefits, such as:
MFA, ACCOUNT MANAGEMENT, SESSION TERMINATION, REMOTE ACCESS , LEAST PRIVILEGE, etc...

Other compliance mechanisms (besides NIST) [audit board](https://www.auditboard.com/) there are many products. Audit board is an example.

#### Intresting lecture chat coversations:
- "default router password :admin" - Rubel
- "Calvin is the default password on a lot of default Dell root admins, mostly iDrac interfaces" - Brian
- __Access controls without documentation do not exist__ - Eric (lecturer)
- Mulit cloud scenario (No locked in to one provider) - Eric (lecturer)
- Provided cloud responsibility model  [Azure shared responsibility](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) [AWS Shared Responsibility Mode](https://aws.amazon.com/compliance/shared-responsibility-model/) - Eric (lecturer)
- 'RBAC' Role based access control. needs to define roles clearly. - Pavan

- Question to Eric (lecturer) with # answers
```
Slight tangent. Since this might be a Security + question.
Control expiration:

So, even if a control is some specific set of instruction like : "at time X allow Y to do Z"

That control itself does not expire. 

# Yes, True

And even spawning a control from within a control, 

Like in programing, calling a class instance from within class.

That spawned control (called class/spawned control), does not expire, in the sense that it exists (script file/process) even if it is not used (called/executed).?

# Yes, True.
# Controlls can re retired, modified, made obselete through system redundancy, but have no expiration.
```

#### Additonal material (added to TODO)
- [Cloud control matrix (download)](https://cloudsecurityalliance.org/research/cloud-controls-matrix)

- ["NIST" for cloud](https://cloudsecurityalliance.org/education/ccsk)

#### Document from LHL Compass
https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Flearningimages.lighthouselabs.ca%2FCyber%2BBC%2FCyber%2BBC%2BC5%2FCyber%2BBC%2BC5.1%2FRisk%2BAssessment%2BTemplate%2BTemplate.xlsx&wdOrigin=BROWSELINK

#### Subjects in discord chat:
- Central bank digital currency (CBDC) is the digital form of a country's fiat currency, which is regulated by its central bank.

- [event: talk about the rapidly evolving AI ecosystem, Ethernet vs. InfiniBand, and creating sustainable AI data centers.](https://www.juniper.net/us/en/events/ai-native-now/seize-the-ai-moment.html?utm_medium=influencer&utm_source=networkchuck&utm_campaign=GLBL_DC_24Q3_VSM_AIDCVirtualLaunchEvent)
