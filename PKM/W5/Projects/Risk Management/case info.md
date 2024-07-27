# info extracted
Established June 2019.

Business type: software development

Value: provides basic/fast Internet access, Web registration and hosting alternatives for SOHO.

Geolocation: Based in the Durham area. Main office in Oshawa, Ontario. Has everal branch offices.

## Security:  
```
CISO
├── Security Tech
├── Security Tech (Intern)
└── [ Vacant ]
```
- $ budget of approximately $500,000 for equipment, personnel, and training
- Needs: 
    - systems meet a minimum level of security and that its information is protected from attacks
    - collect and act on security events from across its digital estate
    - establish a network infrastructure to provide authentication, authorization, and accounting of its network assets
    - contingency system in place in a form of load-balancing and cluster management to provide redundancy and risk mitigation.

## Existing Environment: 

- Infratructure: DHAEI runs a mix of workloads on Rackspace and AWS.
- ONE(1) Active Directory domain named DHA.com.
- All the servers run Windows Server 2019.
- All of the clients run Windows 10.

__Main office__ has:
- USERS: 1,500 users. use desktop computers.
- TWO(2) domain controllers named DCI and DC2
- ONE(1) file server named FSI
- ONE(1) Windows Software Update Services (WSUS) server named WSUSI
- ONE(1) Infrastructure that provides DNS services to the network, server named DHADNS.
- ONE(1) Central technology Department: responsible for _all technical issues within the company_.

__ALL (each) branch offices__ has:
- USERS: aprox. 200 users. use desktop computers.
- ONE(1) server that is configured as a read-only domain controller (RODC).
- Branch office servers provide all _infrastructure services_ AND _branch office file_.
- ONE(1) Support Technician.

__REMOTE WORKERS / home offices__ has:
- USERS: 20 users. programmers. use company-issued laptops.
- __Connect to main office__ using __L2TP VPN__ connections

## Planned Changes:
- DHAEI plans a new branch office in Brampton, Mississauga.
- Data for users in the new office will be stored on FSI (file server named FSI) until the new branch office server is installed, then data will more to new branch server.

The changes will include the following technical, security, and user requirements:
#### Technical Requirements:
- Ensure that all company-issued computers receive all updates that have been approved for release by the technology department.
- Minimize Internet bandwidth by providing internal computers with Microsoft updates via internal servers.
- Minimize traffic across the VPN for remote users.
- Provide central monitoring of all servers.
- Generate an email whenever a hardware event occurs on any of the servers in the company.
- The support technicians located in the branch office must have the rights to perform all local maintenance on the branch office servers in their respective branches.
- The installation of the new RODC in the Brampton office must minimize active directory replication across the WAN link between Columbus and the main office storage space to store user data must be minimized.
- All company-issued computers must be configured with Office 365.

#### Security Requirements
- The branch office technicians should __not__ have any rights to servers not located in their respective branch offices.
- The installation of the new RODC in the Brampton office must not require any passwords or cached secrets to be stored outside of company servers.
- Files stored on the company file servers must be protected in the event that a file server or the drives from any file server are stolen.

#### User Requirements
- Users in the new branch office must access their data using mapped drives.
- User drives should not need to be remapped when the data is moved from the main office file server to the branch office server.
