# 📎
## reads/resources
- [ ] [OpenText Cybersecurity Cloud](https://www.opentext.com/products/security-cloud)
- [x] [The Mark Of The Web](https://www.youtube.com/watch?v=dZ21eDJl0co) Where was something Downloaded from?
- [x] [Digital Forensics with FTK Imager (TryHackMe Advent of Cyber Day 8) ](https://www.youtube.com/watch?v=7wB0HNf1qh4)
- [ ] [What The Tech? Using FTK Imager](https://www.youtube.com/watch?v=26QWF9Fm_Mk)
- [x] [Introduction to Wireshark 4.0 with Gerald Combs & Roland Knall](https://www.youtube.com/watch?v=3HdKhen0Gqw)
- [x] [The Ultimate PCAP](https://weberblog.net/the-ultimate-pcap/)
- [ ] [Volatility Foundation](https://volatilityfoundation.org/volatility-training/)
- [ ] [Volatility 3](https://volatility3.readthedocs.io/en/latest/)
- [x] [Starting a New Digital Forensic Investigation Case in Autopsy 4.19+](https://www.youtube.com/watch?v=fEqx0MeCCHg)
- [x] [Recovering Deleted Files using Autopsy || Practical Digital Forensics](https://youtu.be/sSLinAlFow0?t=125)
- [x] [Important Wireshark filters](https://www.securityinbits.com/tools/wireshark-filters/)
# EnCase Forensic
To get a copy of the data without altering the original, you can use EnCase Forensic. \
EnCase to gather evidence and mitigate the potential breach.

Physical drive is connected to a _write blocker_.

Forensically sound image of the server's hard drives, USB drives, or even data in the cloud.

# FTK Imager
FTK Imager allows investigators to extract specific files, folders, or partitions from forensic images or live systems.

# WireShark 4.0 new

`gre and ipsrc#2 = 172.23.11.56` second instance of ip source

`tcp.len % 512 == 0` modular arithmatic

`tcp.payload[0,2] == 00:00` first two bytes 

`tcp.payload[-2,2] == 00:00` last two bytes

`ip.len in {2,4,8,10}` 

# Volatility
Uncover the hidden malware in the RAM and investigate its activities.
- extract valuable information from the memory image, such as running processes, network connections, open files, and registry entries
- scan the memory image for known malware signatures or patterns and identify any malicious code or injected processes

# Autopsy
- Acquiring evidence such as disk images, memory dumps and files from affected systems
- Analyzing email files including attachments and examining email headers
- Detecting malware by scanning attachments or links to malicious websites
- Analyzing browser artifacts and understanding the attack vector
- Analyzing links, IP addresses and files among many others

Autopsy can help to recover deleted data, analyze web history, emails, and other artifacts from the affected systems. Its powerful keyword searching feature can help quickly locate the email artifacts related to the phishing incident. 

# OSForensics
OSForensics can acquire data from various sources, analyze file systems, perform memory analysis, crack passwords, and conduct keyword searches.
https://www.osforensics.com/faqs-and-tutorials/video_demonstrations.html

