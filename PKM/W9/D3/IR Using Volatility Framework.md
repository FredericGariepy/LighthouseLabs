## read/resources
- [x] Incident Response Using Volatility Framework by Bryan Macario at Tec-Refresh
- [ ] https://github.com/volatilityfoundation/volatility/wiki/Command-Reference
- [ ] https://www.youtube.com/watch?v=EqGoGwVCVwM
- [ ] [Volatility 2.4 cheatsheet](https://downloads.volatilityfoundation.org/releases/2.4/CheatSheet_v2.4.pdf)
- [ ] [Vol 2 to Vol 3 translation](https://blog.onfvp.com/post/volatility-cheatsheet/)
- [ ] 
- https://github.com/volatilityfoundation/volatility
- https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples

### What is Volatility?
Volatility framework is an open-source collection of tools implemented in Python to analyze and extract forensic artifacts from live memory (RAM)

### `pslist`
e.g. `python vol.py -f file.vmem pslist` \
show you an output of all the different processes running on the machine when the memory dump was captured
### `psscan`
`pslist` output, but the results to a visual graph using xdot
### `connscan`
With a suspicious process to further examine, `connscan` show any active TCP connections with a matching process ID
### `cmdline`
 use `cmdline` to show any cmdline executables running in the processes. \
 See proccess (child) running _inside_ a process (parent).
### `procdump`
To dump a process's executable, use the procdump command. \
`procdump` the process into an actual executable and run some tests. \
The full-fledged, live executable called “executable....exe”. \
I can now run this executable through VirusTotal and see what I get.

What is a hidden process?
Why do we want to be aware of them and be able to identify, see, and investigate them?
How does he use each thing he learns to progress his investigation
