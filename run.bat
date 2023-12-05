REM DISCLAIMER
REM The batch file provided herein is for informational and educational purposes only.
REM It is not intended for use in production environments or for critical operations.
REM The author(s) of this batch file make no representations or warranties of any kind,
REM express or implied, about the completeness, accuracy, reliability, suitability,
REM or availability with respect to the batch file or the information, products, services,
REM or related graphics contained on the batch file for any purpose. Any reliance you place
REM on such information is therefore strictly at your own risk. In no event will the
REM author(s) be liable for any loss or damage including without limitation, indirect
REM or consequential loss or damage, or any loss or damage whatsoever arising from
REM loss of data or profits arising out of, or in connection with, the use of this batch file.

REM This batch file is open source and can be used by anyone. You are free to modify
REM and distribute this batch file under the terms of the GNU General Public License
REM version 2.0 (GPLv2). Please see the LICENSE.txt file for more information.

@echo off
echo.

echo -------------------------------
set /p DirLoc="Enter file base location : "

echo -------------------------------
set /p Extension="Enter extension to search : "

echo -------------------------------
set /p FilePath="Generate output.txt as FileName with Path (Y/N) : "

python filenameExtension.py %DirLoc% %Extension% %FilePath%


if errorlevel 1 goto ende

:ENDE
pause
endlocal
