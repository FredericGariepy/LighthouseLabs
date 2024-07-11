## Before you begin wizzarding into the windows shell 🪄 
## `dos2unix` `unix2dos`
> dos2unix is a tool to convert text files from DOS line endings (carriage return + line feed) to Unix line endings (line feed)
> unix2dos is a tool to convert line breaks in a text file from Unix format to DOS format and vice versa.

| Command   | Description                                | Example                  |
| -         | -                                          | -                        |
| dos2unix  | Convert DOS/Windows (CRLF) to Unix (LF)    | `dos2unix myscript.bat`  |
| unix2dos  | Convert Unix (LF) to DOS/Windows (CRLF)    | `unix2dos myscript.sh`   |

- LF (Line Feed): Represented as \n, it is the Unix and Unix-like systems' line ending character.
- CRLF (Carriage Return + Line Feed): Represented as \r\n, it is the DOS/Windows line ending character.


[Windows command line](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
Related links
- [Command-Line Syntax Key](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/command-line-syntax-key)

| Notation |	Description |
| - | - |
| Text without brackets or braces |	Items you must type as shown. |
| \<Text inside angle brackets\> |	Placeholder for which you must supply a value. |
| [Text inside square brackets] |	Optional items. |
| {Text inside braces} |	Set of required items. You must choose one. |
| Vertical bar (|) |	Separator for mutually exclusive items. You must choose one. |
| Ellipsis (…) |	Items that can be repeated and used multiple times. |


| Command  | Description                                  | Example                                      |
| -        | -                                            | -                                            |
| `@echo`  | Turns command echoing on/off                 | `@echo off`                                  |
| `cls`    | Clears the screen                            | `cls`                                        |
| `del`    | Deletes a file                               | `del filename.txt`                           |
| `echo`   | Displays messages                            | `echo Hello, World!`                         |
| `set`    | Defines a variable                           | `set /p name=Enter your name:`               |
| `if`     | Conditional execution                        | `if %age% GEQ 18 (echo Adult)`               |
| `for`    | Loop through a set of values                 | `for /L %%i in (1,1,5) do echo %%i`          |
| `goto`   | Jump to a labeled line                       | `goto :myLabel`                              |
| `call`   | Calls another batch file or function         | `call :myFunction`                           |
| `pause`  | Pauses execution and waits for a key press   | `pause`                                      |
| `rem`    | Adds a comment                               | `rem This is a comment`                      |
| `move`   | Moves a file to a new location               | `move filename.txt C:\newfolder`             |
| `start`  | Starts a separate window to run a program    | `start notepad.exe`                          |


## set options (set switch)
> switch is just another word for option

| SET | description | example| 
| - | - | - |
| `set`    | Defines a variable                           | `set /p name=Enter your name:`               |
| option | Description                  | Example                        |
|--------|------------------------------|--------------------------------|
| `/a`   | Arithmetic Mode              | `set /a Sum=5+3`               |
| `/p`   | Prompt for Input             | `set /p Name=Enter your name:` |
| `/?`   | Help                         | `set /?`                       |


`echo %%`
> %

Usually, variables are %betweeen% percentage signs to be interpreted as a variable




- [select partition command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/select-partition)


