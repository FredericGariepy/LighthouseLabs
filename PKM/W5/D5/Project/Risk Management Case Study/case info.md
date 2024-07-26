Company Background

DHAEI is a software development company based in the Durham area. The company has a main office in Oshawa, Ontario and several branch offices.

Established in June 2019, DHAEI provides basic Internet access, fast Internet access, and Web registration and hosting alternatives for small office/home office (SOHO) individuals and organizations. It is a privately-owned company managed by its founder and CEO, Alan Hake.

The CIO, Amanda Wilson, has 15 years of technical experience and 10 years of experience as a Senior IT Manager. Shortly after taking a position as CIO, Amanda hired Paul Alexander as Manager of Information Security. A reorganization in 2020 resulted in an enhanced recognition of the role of information security at DHAEI. It also resulted in Paul being named Chief Information Security. Along with this increased recognition came a group of dedicated personnel and a budget of approximately $500,000 for equipment, personnel, and training. As shown in the diagram, Paul currently has two full-time security technician positions (one of which is unfilled) and an intern.

DHAEI runs a mix of workloads on Rackspace and AWS. The company needs to ensure that all of its systems meet a minimum level of security and that its information is protected from attacks. The company also needs a way to collect and act on security events from across its digital estate.

DHAEI decided to establish a network infrastructure to provide authentication, authorization, and accounting of its network assets. It will also require a contingency system in place in a form of load-balancing and cluster management to provide redundancy and risk mitigation.
Existing Environment

DHAEI has a single Active Directory domain named DHA.com. All the servers run Windows Server 2019. All of the clients run Windows 10. The main office has two domain controllers named DCI and DC2; one file server named FSI, a Windows Software Update Services (WSUS) server named WSUSI, and an infrastructure server named DHADNS that provides DNS services to the network.

Each branch office has one server that is configured as a read-only domain controller (RODC). The branch office servers provide all infrastructure services as well as functioning as a branch office file.

There are 1,500 users in the main office. Each branch office has about 200 users. All of the users in the main office and the branch office use desktop computers.

About 20 programmers work from home offices using company-issued laptops. The remote workers connect to the main office using L2TP VPN connections.

The main office has a central technology department that is responsible for all technical issues within the company. There is one support technician located in each branch office.
Planned Changes

DHAEI plans a new branch office in Brampton, Mississauga. Data for users in the new office will be stored on FSI until the new branch office server is installed, at which time the data will be moved to the branch office server. The changes will include the following technical, security, and user requirements:
Technical Requirements

DHAEI must meet the following technical requirements:

    Ensure that all company-issued computers receive all updates that have been approved for release by the technology department.
    Minimize Internet bandwidth by providing internal computers with Microsoft updates via internal servers.
    Minimize traffic across the VPN for remote users.
    Provide central monitoring of all servers.
    Generate an email whenever a hardware event occurs on any of the servers in the company.
    The support technicians located in the branch office must have the rights to perform all local maintenance on the branch office servers in their respective branches.
    The installation of the new RODC in the Brampton office must minimize active directory replication across the WAN link between Columbus and the main office storage space to store user data must be minimized.
    All company-issued computers must be configured with Office 365.

Security Requirements

DHAEI must meet the following security requirements:

    The branch office technicians should not have any rights to servers not located in their respective branch offices.
    The installation of the new RODC in the Brampton office must not require any passwords or cached secrets to be stored outside of company servers.
    Files stored on the company file servers must be protected in the event that a file server or the drives from any file server are stolen.

User Requirements

DHAEI must meet the following user requirements:

    Users in the new branch office must access their data using mapped drives.
    User drives should not need to be remapped when the data is moved from the main office file server to the branch office server.
