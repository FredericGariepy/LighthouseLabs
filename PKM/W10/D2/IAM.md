## reads
- [x] https://www.onelogin.com/learn/iam#:%7E:text=Identity%20and%20access%20management%20(IAM)%20ensures%20that%20the%20right%20people,each%20app%20as%20an%20administrator.
- [x] https://www.anomali.com/resources/what-are-stix-taxii
- [ ] https://www.strongdm.com/rbac
- [x] https://www.strongdm.com/blog/iam-best-practices#:%7E:text=One%20of%20the%20most%20common,interfering%20with%20users%27%20daily%20workflows
- [ ] https://blog.gitguardian.com/aws-iam-security-best-practices/

## IAM, & friends
Identity and Access Management (IAM) \
Role-Based Access Control (RBAC) \
Attribute-based access control (ABAC) \
access control lists (ACL) \
Policy-Based Access Control (PBAC) \
bring your own device (BYOD) \

#### Zero Trust architecture (ZTA)
- __Principles__
    - Never trust, always verify
    - Assume breach
    - least-privileged access
    - Terminate Every Connection:
    - Protect Data Using Context-Based Policies
    - Prevent Risk by Reducing the Attack Surface
    - POLP, Defence depth, KISS, Seperation of Duties
 - __Pillars__:
    - Identiy Securtiy (RBAC)
    - Endpoint Security (ESM)
    - Application security (SDLC DevOps app. Sec.)
    - Data security (encryption)
    - Visibility and analytics (Dashboard, Clearbox)
    - Automation
    - Infrastructure security
    - Network security (E2EE, micro-segmenting, control network flow)
- __Tech__:
    - Identity Management and Privileged Access Management (PAM)
    - Security Analytics
    - Endpoint Protection
    - Encryption
    - MFA
    - Software-Defined Perimeter/Policy-Based Access Control
    - Network and Microsegmentation
    - Continuous Monitoring
    - Endpoint Security
 
__Extra__ \
Zero Trust Network Access (ZTNA) \
Zero Trust Application Access (ZTAA)

## IAM best practices
1. __Adopt a Zero Trust Approach to Security__ (see above)
2.  Identify and Protect High-Value Data |  high-value assets (HVAs)
3.  Enforce a Strong Password Policy
4.  MFA
5.  Automate Workflows
6.  Least priviledge
7.  Enforce Just-in-Time Access Where Appropriate
8.  Leverage Both RBAC & ABAC Policies
9.  Regularly Audit Access to Resources (reduce attack surface, review POLP)
10. Centralize Log Collection
11. Adopt IAM Solutions That Work With Existing Tools
12. Culture | IAM Best Practices Standard in Your Organization

## extra
### Security Access Markup Language (SAML)
SAML is an open standard used to exchange :
- authentication and authorization information.
Used between an _identity provider system_ such as an IAM \
and a service or application. \
This is the most commonly used method for an IAM to provide a user with the ability to log in to an application that has been integrated with the IAM platform

SAML based on XML format, \
web applications use SAML to transfer authentication data between two parties:
- the identity provider (IdP) and
- the service provider (SP)
OAuth and SAML

 single sign-on (SSO)__ 
