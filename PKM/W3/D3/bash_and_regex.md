[ Bash scripting cheatsheet ](https://devhints.io/bash)

[Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/bash-functions.php)

## regular expression match with `=~`

```bash
numeric_pattern='^[0-9]+$'
# Check if variable is numeric
if [[ "$variable" =~ $numeric_pattern ]]; then
    echo "Variable is numeric"
else
    echo "Variable is not numeric"
fi
```

# egrep
```bash
egrep -i 'dude' Dude_wheres_my_car_script.txt | wc -l
```
- `'dude'` dude. if dude was (dude), it would be a capture group. Id be captured dude.

- `-i`: case insenstive

- `wc -l` word count (wc) `-l` line number

Meaning, how many Lines have the word 'dude', in the movie 'Dude where's my car'

`egrep -i -c 'dude' Dude_wheres_my_cat_script.txt`

- `c` counts number of lines that match insenstive matches-i

```bash
egrep -i '(dude).*\1' Dude_wheres_my_car_script.txt | wc -l
```
- `.*` including anything up until  `\1` capture group 1, which is dude

Meaning, how many times they say 'dude' at **least 2 times** in the same line, in the movie 'Dude where's my car'

```bash
dude=$(egrep -i c 'dude' Dude_wheres_my_car_script.txt ) # -c is count
movie_lines=$(wc -l < Dude_wheres_my_car_script.txt ) # < is important to redirect
echo "scale=2; ($dude / $movie_lines) * 100" | bc # bc is basic calculator and scale is for decimal
>> 3.00
```

## sed 
Replace "apple" with "orange" in file.txt
`sed 's/apple/orange/g' file.txt`

➡️ why s and g ?
> s = substitute
>
> g = global. meaning, all the file

## awk
`awk '/regex_pattern/ { action }' file`

- /regex_pattern/: This is where you specify your regex pattern enclosed in slashes (/). awk will match lines where this pattern is found.
- { action }: Action to perform when the pattern matches. It could be printing the line (print), extracting specific fields ($1, $2, etc.), or any other operation.

E.g. : `awk '/./ {print $0}' noauth.log`


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

  
