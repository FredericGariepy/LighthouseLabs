- [x] https://www.digitalguardian.com/blog/what-data-classification-matrix

### Data Classificaiton, Why, How, What
WHY Classify data:
- Makes information easy to spot
- Cost-effective (controlls applied to relevant classificaiton)
- enables Data Loss Prevention (DLP) consumers

HOW to classify data (labeling):
1. Regular expressions (RegEx), identify: PII, PCI, PHIPA or trade secrets
2. Training (humans, AI)

ASK:
- Who should have access to that data
- Where that data should be stored
- Who has responsibility for maintaining that data
- The audit requirements for that data

### Data Classification Matrix (Tool)
> Public, Internal, Confidential, Restricted__
| | __Public__| __Internal__ | __Confidential__|__Restricted__|
|-|-|-|-|-|
|Risk level| No risk| Low |Medium |High|
| **Details**            | Data disclosed to the public, such as general company details. No risk and openly revealed.       | Known to most or all company employees. Revealing it may have low or no impact.           | Created for internal use, not meant for public. Moderate impact if revealed.              | Most confidential data. Revealing it can cause huge financial or reputational losses.         |
| **Access Rights**      | Open to the public.                                                                              | Low limitations.                                                                           | Available to company employees, generally on a need-to-know basis.                         | Very sensitive information, available only to some top-level employees.                      |
| **Impact**             | No harmful impact.                                                                              | Some inconvenience if published.                                                           | Losses but not business-critical if exposed.                                                | Devastating impact if revealed, affecting both the company and possibly its customers.      |
| **Examples**           | Data on the company website, public press releases, public seminars.                              | Employee data, employee roles and responsibilities, company event data.                    | Business sensitive data, intellectual property, data protected by regulations.             | Company supplier data, user credit card data, client HIPAA information.                      |
| **Storage Options**    | Can be posted on a website, blog, or publicly accessible portal.                                  | A computer or server available to all or most employees.                                   | A server or virtual server accessible only to certain teams.                                | Highly secure server or virtual server accessed by only a few top-level employees.           |
| **Other Security Considerations** | No major considerations.                                                                 | Must be protected by a username/password mechanism.                                         | Should be accessible only by organization insiders or authorized recipients.                | Must be stored in encrypted form, travel over the network in encrypted format, accessible to few teams. |
| **Audit Controls**     | No audit controls required.                                                                       | Some level of monitoring or reviewing might be required.                                    | Data stewards are responsible for monitoring and reviewing for potential misuse.            | Data stewards must monitor for misuse or unauthorized access. Backup plans are required.      |

#### Best practices for Data Classificiation Matrix (Tool use)
- Use correct framework for your data types
-  data type should be mapped to the correct class
-  defining the scope of the matrix, you can classify only the data you want to regulate.
-  Assigning ownership to data makes it easier to classify
-  Assign safety grades. best not to make the data classification matrix too complicated.
-  Assign safety measures
-  Maintenance of the matrix. Data lifecycle may change its risk level

### CIS Security Controls
CIS (Center for Internet Security)
