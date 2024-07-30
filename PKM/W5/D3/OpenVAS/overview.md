OpenVAS (OpenVAS or "GVM") is an open-source Linux-based vulnerability scanner supported by a community spearheaded by the German organization [Greenbone Networks](https://www.greenbone.net/en/)

- [Greenbone OpenVAS](https://www.openvas.org/) scannner
<img src="https://forum.greenbone.net/uploads/default/optimized/1X/901766e0fa6b6cb6aee9f4702f46fb8a703a332b_2_690x323.png" width="300" alt="Image">


The major tool modules are all open source, \
but there is a turnkey appliance and \
a cloud service available for enterprise clients that wish to use a solution that is simpler to implement and use.

 System Architecture of the OpenVAS system:
- The scanner applications that __run the vulnerability tests__.
- The Greenbone Vulnerability Manager (GVM) __database__
- The Greenbone Security Assistant (GSA) = __API interface__. 

##### When looking for supporting documentation, try searching under both names (OpenVAS and GVM)
This is because The Greenbone Vulnerability Manager daemon (GVMD) is the heart.
__GVMD brings functionality like__: :anatomical_heart:
- control scanner applications, directly and remotely
- a database that stores configuration information and all scan results
- user management and permissions control with groups and roles
- Scheduleer, for tasks and other events.


##### Greenbone Security Assistant (GSA) :eyes:
GSA web interface <--> GVMD

##### OpenVAS & Notus :
The OpenVAS Scanner and the Notus Scanner are the scanning applications used by this system,  compares data from target to known.













