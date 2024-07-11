@echo off
rem Turn off command echoing

echo Enter two numbers to add:
rem Prompt the user

set /p "num1="
rem Get the first number from user input

set /p "num2="
rem Get the second number from user input

call :add_numbers %num1% %num2%
rem Call the add_numbers function with the two numbers

echo The sum is: %result%
rem Display the result

pause
rem Wait for user to press a key before exiting

exit /b
rem Exit the main script

:add_numbers
rem Define the add_numbers function

set /a "result=%1 + %2"
rem Add the two numbers and store in 'result'
rem %1 is the first parameter, %2 is the second

exit /b
rem Return from the function
