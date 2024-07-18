# Menu

1. [Glossary](#glossary)
2. [Common Symbols]
3. [What's a workflow in cybersecurity]()
4. [SOC Methodology]

### Glossary 
|acro|def|
|-|--|
| SOC| Security Operations Center |
|CSIRT|computer security incident response team|
|SME |Subject Matter Expert|


>  Remember, as a Junior Analyst, you may be in either or both of SOC  positions from time to time.

### Common Symbols
<img src="https://github.com/user-attachments/assets/f97bfd1e-0ac8-4fd0-900a-822dba982b7e" alt="6sigmatools-symbols" style="width: 60%;">


### [What is a Workflow?](https://www.process.st/what-is-a-workflow/)
> A workflow is not a process. We can proceed through a workflow by following it (see code analogy bellow).
To Build a workflow Ask:
- What exact jobs need to be done?
- Who is responsible for each job?
- How much time will each task take?

By measuring the work that needs to be done, you can manage how optimally it’s executed.
Otherwise, you have no idea what’s going on or where is the bottleneck in your team’s activies.
Stages of a workflow

#### Building a workflow comes down to 5 stages:

1. Identify the tasks that need to be done
2. Determine who’s accountable for those tasks
3. Organize the tasks into a sequence
4. Test the workflow
5. Review and repeat

#### The 3 basic components of a workflow

While the number of tasks in each workflow can vary from 1 to 99+, every workflow is made up of 3 basic components:

- **Trigger**: The event that begins the workflow. This can be an action, decision, specific time, or a response to something.

- **Series** of tasks/the work: This includes all of the tasks, people, and deliverables involved in the workflow.

- **Results**: What the workflow produces. A result or outcome can be something tangible like purchasing a service or more abstract like accessing certain information.


![small workflow](https://github.com/user-attachments/assets/00126562-2a88-45bc-8a1d-f9921577ab43)
```python
# this is the workflow, in the picture above
workflow = {p0:p1,p1:p2,p2:[{p2:p3},{p2:p4}],p3:p4,p4:p5}

# processes
p0='start'    #Trigger
p1='process1'   #Series
p2='process2'   #
p3='process3'   #
p4='process4'   #
p5='end'     #Result

#this is the beauty of a workflow. You can just keep asking it: `what happens next`

print(workflow[p0]) # look how we start at process 0. we just keep calling the workflow.
# >>> process1

print(workflow[workflow[p0]]) # and the workflow will lead us to the next process.
# >>> process2

print(workflow[workflow[workflow[p0]]])
# >>> [{'process2': 'process3'}, {'process2': 'process4'}]  # here we are given a choice by the workflow

print(workflow[workflow[workflow[p0]]][0][p2]) # let's chose p2 with option 0
# >>> process3

print(workflow[workflow[workflow[workflow[p0]]][0][p2]]) # keep following the workflow
# >>>> process 4

print(workflow[workflow[workflow[workflow[workflow[p0]]][0][p2]]])  # we got to the end by following the worflow.  (recursively) 
# >>>> end 
```

### [The SOC Methodology](https://secureglobal.de/the-soc-methodology)
The SOC handles the fast processing of events.
- If events are known/easy to solve – these are forwarded from the SOC to the relevant division (IT-Security, Networking, Servers etc.).
- If events are not easy to solve or completely unknown, they will be forwarded to the [**CSIRT**](#glossary).
- SOC **does not** make any changes to IT security assets or the IT infrastructure (responsibility of the relevant division).
- SOC takes care that tickets are worked on and closed in a timely manner. If not the SOC agents will escalate to their supervisor.


| Tier | Description |
| - | ---- |
| - | - |
| Tier 1 | The “new ones” who solve events by means of “learning by doing” and with the help of knowledgebase and their colleagues.|

| Tier 2 | Experienced employees who can handle most events from experience, know the workflows and other procedures well, and to an extent analyze events to a certain depth. |
| T2 & T1 | Tier 2 train the Tier 1 agents in daily business. |
| Tier 2**+** |This escalation level/complexity of an event requires Subject Matter Expert support. |


If the event can not be solved even in Tier 2+, it will be handed over to the CSIRT by Ticket.





| - | - |
| - | - |
| - | - |

reflect on each roll:
- Cyber Security Specialist
> the Watcher, monitoring, responding to tickets, Infra maintenance, Siem user, reporting, 'on ground'

- Threat Hunter
> vulnerabily collector, asset monitor, simulations, controlled testing,

- Vulnerability Analyst
> take the result from CSS and TH, understand exploits and create patch/solves. create actions plans for CSS (play books,...)

- Cryptanalyst
> capture the flag, decrypt, review/develop safe communications schemes, forensics, 
