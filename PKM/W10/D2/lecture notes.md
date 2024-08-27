- Identity Access Management (IAM): \
rules and policies for managing and controlling access

- Role-Based Access Control (RBAC): \
One way to implement IAM: \
Providing permissions based on their role in the company

- Principle of Least Privilege (PoLP) \
When you grant only the minimum level of access or permissions necessary to perform the user  or a specific task

- Separation of Duties (SoD) \
Users should not have control over a single process. \
Separate duties over a process

- Defense in Depth: \
No single point of failure. \
Layers of security. e.g. MFA.

- [ ] YubiKeys
- [ ] https://www.yubico.com/?gad_source=1&gclid=CjwKCAjw8rW2BhAgEiwAoRO5rJKGrow5sNStegcL2awPNoZAtTcbPbpRVP34G3ZhuejCePKHs5I8vhoCpzwQAvD_BwE
- [ ] Hardware token project :brain:

### 3 Pillars of Authentication:
Know
- password
- passphrase
- pin

Have
- smart card
- TOTP generator
- Hardware token

ARE
- fingerprint
- voice auth
- retina

Zero-Trust Security Model
- [ ] https://www.cyber.gc.ca/en/guidance/zero-trust-security-model-itsap10008

- Continuous Validation
- Access Conditions 
- History of account : \
Geolocation, device, user, service, behavior (time of day, etc)

Single process access. Just-in-Time access.

Tailgating Attack.

Single sing-on SSO (can be pricy for orgs. $)


### Deny Rules:

- Explicit Deny \
common in Access Control Lists (ACLs), firewalls, ..

- Implicit Deny \
default deny, (think java switch case default)

DFIR (Digital Forensics and Incident Response)

### Backups (Full, differential, incremental)

Backup frequency. \
Backup is network resource intensive be considerate. \
Test backups for completeness.

- Recovery point objective (RPO): (backup frequency requirements) \
is the maximum length of time permitted that data can be restored from, which may or may not mean data loss.

- The recovery time objective (RTO): (time to recovery requirement) \
is the targeted duration of time between the event of failure and the point where operations resume.


Secure Design: Logging

Monitoring, Detection, Incident Response. 

Windows Event Viewer: Windows Event ID.

Linux: Syslogs

ELK Stack: Elasticsearch, Logstash, and Kibana

##### Does linux hash sudo passwords ?
Linux user passwords are stored in `/etc/shadow file`
- [x] https://www.cyberciti.biz/faq/understanding-etcshadow-file/
###### What about in Windows ? 
`ntds.dit` \

NTDS (Windows NT Directory Services) is the directory services used by Microsoft Windows NT to: \
locate, manage, and organize network resources.

The NTDS.dit file is a database that stores the Active Directory data \
(including users, groups, security descriptors and password hashes).

This file is stored on the domain controllers.

Once the secrets are extracted, they can be used for various attacks: \
credential spraying, stuffing, shuffling, cracking, pass-the-hash, overpass-the-hash or silver or golden tickets.
- [ ] https://www.thehacker.recipes/ad/movement/credentials/dumping/ntds
- [ ] https://attack.mitre.org/techniques/T1003/003/
_[thanks Ernie!](https://github.com/ej8899/)_
