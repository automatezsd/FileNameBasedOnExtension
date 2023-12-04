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
