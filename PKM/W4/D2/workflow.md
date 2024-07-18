Glossary 
|acro|def|
|-|--|
| SOC| Security Operations Center |
|CSIRT|computer security incident response team|
>  Remember, as a Junior Analyst, you may be in either or both of these positions from time to time.


##### [What is a Workflow?](https://www.process.st/what-is-a-workflow/)
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


```python
# this is the workflow.
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
# >>> [{'process2': 'process3'}, {'process2': 'process4'}]
print(workflow[workflow[workflow[p0]]][0][p2]) # The same process (p2) can lead to diffrent places depending on conditions we follow (chose 0,1) 
# >>> process3
print(workflow[workflow[workflow[workflow[p0]]][0][p2]]) 
# >>>> process 4
print(workflow[workflow[workflow[workflow[workflow[p0]]][0][p2]]])  # we got to the end by following the worflow.  (recursively) 
# >>>> end 
```

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
