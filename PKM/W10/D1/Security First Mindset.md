Defense in Depth, Least Priviledge, Seperation of Duties, Secure by Design

### Secuity First Thinking
__continuous Learning and Improvement__: non-stop.

__CIA objectives__

__proactive__ risk(vuln scan & test), controls, monitor, update measures & policies.

__risk aware__ threatlandscape, risk assesmnet(CVSS), resource allotmnet

__integrate :__ \
_see images bellow_

<img src="https://www.ciat.edu/wp-content/uploads/2022/07/devops-netops-secops.png" width=400px alt="Software development lifecycle Schema" />
<img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*UN3_vDPpkqhznJfXO4VmvA.png" width=400px alt="Software development lifecycle TOOlS/SOFTWARE"/>

### Security Principles
#### 0. Key it Simple and Secure, Keep it stupid simple, Keep it simple, stupid.
also knownn as KISS \
Path of least resistance \
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Path_of_least_resistance.jpg/1024px-Path_of_least_resistance.jpg" width=400px alt="Path of least resistance"/>
#### - [Kerckhoffs's principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle)
- _Glass_ box Security :window:

##### Defense in Depth
NO single point of Failure.

Security layers: \
auth _enticate_, auth _orize_,just-in-time auth, Deny rules (implicit, explicit), Zero trust  

Combination of: \
preventive, detective, and responsive measures at
Layers:
- network
- host
- application
- data

##### Least Priviledge:
Temporary access to necessary and required parties to complete operations.
1. Access rights: (role,JIT)
2. Hardening: remove vulneralble serices (cut/slim down attack surface)
3. priviledge creep: Monitor access rights, Modify access rights, asses acces rights
4. Just in Case: Review access rights, do not overextend attribution.

##### Seperation of Duties
_anti-dictatorship_ \
No single individual has complete control or authority over critical process or resource.
- concept of _forced collusion_

##### Secure by Design
```
Production ---- Requirements
    /      \   /    \
Test ------ SEC ----- Design
    \    /      \    /
    Install ---- Code
```
Developement, Operations, Maintenance __left shift__ \
Developement, Operations, __left shift__, Maintenance \
Developement, ___left shift___, Operations, Maintenance \
 ___Left Shift___, Developement, Operations, Maintenance 

__Objective__: \
Secure by Design \
Start to Finish \
Secure out-of-the-box (OOTB)

 # designs to avoid
- Complexity ___for the user___
- Obscurity
    - e.g. Black Box Security :black_large_square:







