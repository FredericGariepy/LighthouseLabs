# read
- [ ] [Computer Forensics: Memory Forensics](https://www.infosecinstitute.com/resources/digital-forensics/computer-forensics-memory-forensics/#:%7E:text=Memory%20forensics%20is%20a%20vital,known%20as%20a%20memory%20dump.)

Forensics is a crucial skill for first responders and investigators alike, as it allows for the quick and complete capturing of live system data for later scrutiny

Snapshot of RAM = "memory dump" \
Formats: 
- __RAW Format__ - extracted from a live environment
- __Crash Dump__ - information gathered by the operating system to aid in troubleshooting system or software issues
- __Hibernation File__ - a saved snapshot that your operating system can return to after hibernating (page, swap file)
- __Page File__ - a file that stores similar information that is stored in your system RAM
- __VMWare Snapshot__ - a snapshot of a virtual machine, which saves its state as it was at the exact moment that the snapshot was generated

## Memoryy Dump Tools

- __Volatility Suite__: an __open source suite of programs for analyzing RAM images__ from a wide variety of OSs.

- __Process Hacker__: an __open source process monitoring application__ that is very useful to run while the target machine is in use. \
  It will give the investigator a better understanding of what is currently affecting the system before the memory snapshot is taken, and can go a long way to help uncover any malicious processes, or even help to identify what processes have been terminated within a set period of time.

- __Rekall__: an end-to-end solution for incident responders and investigators, and features both acquisition and analysis tools. \
 More of a forensic framework suite than just a single application.
- __Helix ISO__: a bootable live CD as well as a standalone application that makes it very easy for you to capture a memory dump or memory image of a system. \
There are some risks associated with running this directly on a target system, namely an acquisition footprint, so make sure that it fits your requirements.
- __Belkasoft RAM Capturer__: another forensic tool that allows for the volatile section of system memory to be captured to a file. \
First responders will find that the functionality and wide range of tools available in this software package will allow for their investigations to start off as quickly as possible.


# What you can DO with memory analysis:
You can create a copy of the executable to run through a site like VirusTotal to learn more about it

- Discover and learn about processes that were running on the machine at the time:
    - what files or executables started them or are associated with them.
- Discover and examine timestamps on processes and files

- Examine what malware is present on the system and what all it is doing on the system:
    - Initiating and maintaining network connections and to whom
    - Adjusting the system registry
    - Making changes to scheduled tasks
    - id the hash or cypher being used to encrypt data on the system

- Identify and document network connections that have been initiated, IP addresses, ports used, frequency of communications and so on and
- See user and system account activities on the system

  



