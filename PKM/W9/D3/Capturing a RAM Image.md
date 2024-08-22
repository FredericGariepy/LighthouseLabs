- [x] [ DFS101: 10.2 Forensic Memory Acquisition in Windows - FTK Imager](https://www.youtube.com/watch?v=1XK86to03-Q)

GUI version : `VolatilityWorkbench.exe` \
CLI : `vol.exe.`

Open FTK make memory image

Windows > About > System 
- Version/Edition
- System type (x32,x64)
- RAM

Name of memory image: `Version-Type-Ram`

`certutil -hashfile path\to\yourfile.mem MD5` \
> MD5 hash of C:\Users\student\Desktop\ActivityW9D3\Windows11Home-x64-2GB.mem:
>
> ba9d6ff142774561f7a50994c10dfd7d
>
> CertUtil: -hashfile command completed successfully.

