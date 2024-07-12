#### the basics are this ones:
1. the idea is to monitor the web server access.log for potential IoC
2. for that it is required to read and move the log (typically using a bash script)  to a centralized log repository
3. and there parse/analyze the logs (commonly using python)
4. an extra would be trying to do the same for windows server
5. or try to match some extra patterns against a regex
> the project involves some other aspects as well
6. like understanding why you are looking for those indicators, expected outputs, a monitoring workflow...
7. and future improvements to the logs.

- Oscar Rios
