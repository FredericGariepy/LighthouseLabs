
#### reads
- [x] https://web.mit.edu/smadnick/www/wp/2020-16.pdf

|parts|reading|
|-|-|
|text/Summary|1. Introduction  <br>2. Related Articles <br>Methodological <br>3. Considerations <br>__...__|
|case start <br> __image bellow__ |6.2 Technical Assessment of the Capital One Incident|
> image of the case [img]
```mermaid
graph TD
    A[criminal] <-->|1. Hide access| B["TOR Network VPN Service"]
    B -->|2. SSRF Query| C["EC2 with full access IAM Role"]
    C -->|3. Trick WAF to relay commands to Metadata service| C
    C <-->|4. http://169.254.169.254/iam/security-credentials| D["EC2 Metadata service\n169.254.169.254"]
    C <-->|"5. ls command to list existing buckets"| E["AWS S3 Buckets"]
    E -->|"6. sync command to copy confidential data from buckets"| A
    
    subgraph "Private infrastructure"
        D
        E
    end

    style A fill:#000000,color:#FFFFFF
    style B fill:#FFD700
    style C fill:#FFFFFF,stroke:#000000,stroke-width:2px
    style D fill:#D3D3D3
    style E fill:#D3D3D3
    
    classDef misconfigured fill:#FFD700,stroke:#FF0000,stroke-width:2px,stroke-dasharray: 5, 5
    class C misconfigured

```
___...___
|parts|reading|
|-|-|
|Explanation brief of steps <br> 1,2,3,4,5,6 |6.2 after [img]|
| mapping of steps to -> MITRE ATT&CK <br>Table of ATT&CK tactics/techniques used |6.2 end|
> Table of ATT&CK tactics/techniques used

| MITRE Tactic "Stage" | Step of the attack | ATT&CK # |
| -| -|-|
|C2|__1__|T1188|
|Innitial access|__2__|T1190|
|Innitial access|__3__|N/A|
|Innitial access|__4.__|T1078|
|Execution|__4.__|T1059|
|Discovery|__5__|T1007|
|Exfiltration|__6__|T1048|

___...___
|parts|reading|
|-|-|
|Mapping CSF NIST controlls <br>(Failed Controls v. incident) -> NIST CSF |6.4 Assessment of Technical Controls <br>Versus<br>Normative Standards Applied to the Capital One Incident

- [ ] [NIST RMF CONTROLS](https://csf.tools/reference/nist-sp-800-53/r5/) 
- [ ] [NIST __CSF__ CONTROLS](https://csf.tools/reference/nist-cybersecurity-framework/v2-0/) <-
> Table of FAILED Controls CSF NIST:

| MITRE Tactic "Stage" | Step of the attack| _Mitigation_ "Technical Controls"| CSF NIST Controls (that failed)|
|-|-|-|-|
|C2|__1__<br>T1188|Firewall, host access rules:<br>deny(TOR node, flagged proxy)<br>--------<br>IDS/IPS alert on success from flagged IP|[ID.AM-4](https://csf.tools/reference/nist-cybersecurity-framework/v2-0/id/id-am/id-am-04/)<br>PR.DS-5<br>DE.AE-1<br>DE.CM-1,DE.CM-6,DE.CM-7,<br>DE.DP-2
|Innitial access|__2__<br>T1190|use WAF, Vulnerability scanner|PR.IP-12<br>PR.PT-1,PR.PT-3<br>DE-AE-3<br>DE.CM-1,DE.CM-6,DE.CM-7,DE.CM-8<br>DE.DP-2|
|Innitial access|__3__<br>N/A|Early detection by Vulnerability scanner |PR.IP-12<br>PR.PT-1,PR.PT-3<br>DE-AE-3<br>DE.CM-7,DE.CM-8<br>DE.DP-2|
|Innitial access|__4.__<br>T1078|Monitor , Auddit:<br>Admin acc.|PR-AC-1,PR-AC-4,PR-AC-6,PR-AC-67<br>PR.IP-1<br>PR-PT-1,PR-PT-3<br>DE.CM-6,DE.CM-7<br>DE.DP-2|
|Execution|__4.__<br>T1059|Track commands on AWS acc. |...|
|Discovery|__5__<br>T1007|Track commands on AWS acc.|same as ^above _+plus_ PR.DS-5|
|Exfiltration|__6__<br>T1048|Outbound traffic monitor|...|

___...___
|parts|reading|
|-|-|
|explain attack step<br>list controlls<br>talk about control mitigation power|6.5 Details of __Two__ of the Failed Controls<br>6.5.1 Case Study: "Obtain access credentials (AccessKeyld and SecretAccessKey)"<br>6.5.2 Case Study: "Data Exfiltration"|
| Discussion & Recommendation<br>TONE CHANGE, _persuasive writting_ | 7. Discussion and Recommendations|
|'GRC' only works when applied correctly<br> _don't fuck up GRC_<br>Trust us|7. Discussion and Recommendations|
| Where is the  g a p |7.2 The cyber security GAP between Governance, Management and IT|
|Fundamental RECOMMENDATIONS |7.3. (1,2,3,4,5)|
|Summary, global view, call to action (sell) |8. Final considerations |
|Future work, Gloal focus|9. Future work|
|Acknowledgments,|References|10. Acknowledgments, 11. References|
