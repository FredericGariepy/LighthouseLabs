### resource/reads
- [ ] Martin fowler
- [ ] bouncing server
- [ ] carbon black
- [ ] Zero trust Architecture
- [ ] https://www.youtube.com/@NetworkChuck
- [ ] https://1passwordstatic.com/files/security/1password-white-paper.pdf
- [ ] https://docs.aws.amazon.com/iam/
- [ ] https://cybersecurity.att.com/products/ossim
- [ ] https://www.youtube.com/watch?v=_WdRwDSYAyo

# Security First
Security is everyone's jobs. cyber Analyst will be specialists.
- advocate/proactive for potential vulnerabilities before they are exploitable by actors. 
- risk assessment
- threat modeling 
- security testing
- Control access
- Encryption
- Employee awareness and Training 
- human error, social engineering
- Secure Development practices:
code, env, code review, vuln test
- Zero trust Architecture,
user\device\network is untrusted (until proven trusted) \
segment resource, strict access controls
- EDR

### Difficulties in Secturity First approaches
- Tools can be failure points
(WAF down? your service is too)
- Poorly built security tools are hacking targets.
- personnel; hard to find/keep
- audits, assessment: 
time taken away from product
- training, awareness:
burden, poorly built training platform
##### __COST$__
Implementing security flows to development \
Compliance, cert: expensive $$$
- Incident response recovery:
expensive in tech, personnel, training, cost $$$
- Third party services:  
MSSP relationship complexity, relationship $$$

### Principles of Security Architecture
- __Combination of security layers controls against rage of threats__
- __Least Privilege__: \
Access request list. \
Users have minimum level of privilege. Access review. \
Identity management (IdM), also known as identity and access management (IAM or IdAM)

- __Separation of Dutie__s: \
Provision access (including admins) \
Divide permissions over roles/people \
Prevent single person with complete control 

- __Secure communication__: \
Encryption, comm protocol

- __Authentication and Authorization__: \
authentication (MFA) \
Combine with authorization in control access rights based on roles/responsibility

- __Fail-Safe Defaults__: \
Secure settings, secure configs. \
Review configurations, defaults, settings.

- __Auditable and Monitored__: \
high fidelity of audit logs, effective monitoring

- __Resilience and Redundancy__: \
System can withstand and recover incidents or failure \
Use redundancy and backup to ensure availability and system continuity.

- __Supply chain management__:
Verify security of 3rd party/vendors \
Update and patches. \
Ensure compliance of 3rd party with organization requirements. \

- __Separation of Concerns__: \
Architectural design allowing flexibility to change components to adopt new tech and adapt to new threats. 

#### Tools for Secuure architecture
- __Software__: \
Asset management software (maps access controls)
Access list (beware lazy admin access control profile copies! _lazy!_) \
Just-in-time (JIT) access controls. see cloud tech.
- __Documentation__: Security Plan. See NIST Core Function Framework (CSF); related to NIST CyberSecurity Framework (also, CSF)!
- __NIST Core Function Framework (CSF)__
- [ ] https://www.nist.gov/cyberframework/cybersecurity-framework-components
- [ ] __Current Profile VS Target Profile__

##### CSF
- __Identify__:
People, networks, software, hardware

Protect: (Select/implement NSIT RMF)

Detect:


Respond:

Recover:

### Other points.. to-be-continued... W10/D2
- [ ] Maturity models 
- [ ] Building a CSF
