## awk
`awk '/regex_pattern/ { action }' file`

- /regex_pattern/: This is where you specify your regex pattern enclosed in slashes (/). awk will match lines where this pattern is found.
- { action }: Action to perform when the pattern matches. It could be printing the line (print), extracting specific fields ($1, $2, etc.), or any other operation.



## Pre-defined Variables
The Bash shell includes the following predefined variables:

- `$?` which stores the exit status of the last executed program;
- `$#` which stores the number of command line parameters;
- `$$` which stores the PID (Process Identifier) ​​value of the shell script being executed;
- `$@` which stores the value of all passed parameters, similar to the argv variable present in the C and C++ programming languages;
- `$!` which stores the PID of the last background process, which helps track the process as work is carried out;
- `$0`, ..., `$9` which stores the values ​​of all command line parameters separately
  
## Global Variables
The LANG environment variable comes pre-defined in several Linux distributions!
> $ `export LANG=en_US.UTF-8`

- `PATH`: defines search directories for programs executed in the shell;
- `USER`: informs the name of the shell user;
- `HOME`: informs the path of the user's home directory;
- `LANG`: Language/Language, specified as locale;
- `PWD`: current directory;
- `TERM`: Current terminal type in use.
- `UID`: UID of the current user.
- `RANDOM`: Generates a random number

  
