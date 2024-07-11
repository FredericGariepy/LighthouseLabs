@echo off
echo Type your e-mail address :
Set /p "Email="
Call :CheckValidMail %Email%
cls
IF "%errorlevel%" EQU "0" ( 
    Color 0A
    echo %Email% is valid 
) else (
    Color 0C
    echo %Email% is not valid
)
pause 
Color 07
exit
rem pause & Exit

::*********************************************************************************

:CheckValidMail &lt;Email>
(
echo If IsValidEmail("%~1"^) = True Then
echo    Wscript.Quit(0^)
echo Else
echo    Wscript.Quit(1^)
echo End If
echo Function IsValidEmail(strEAddress^)
echo    Dim objRegExpr
echo    Set objRegExpr = New RegExp
echo    objRegExpr.Pattern = "^[a-zA-Z0-9][\w\.-]*[a-zA-Z0-9]@[\w-\.]*[a-zA-Z0-9]\.[a-zA-Z]{2,7}$"
echo    objRegExpr.Global = True
echo    objRegExpr.IgnoreCase = False
echo    IsValidEmail = objRegExpr.Test(strEAddress^)
echo    Set objRegExpr = Nothing
echo End Function
)>"%tmp%\%~n0.vbs"
Cscript /nologo "%tmp%\%~n0.vbs"
Exit /b
::*********************************************************************************
