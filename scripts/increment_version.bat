@echo off
set /p VERSION=<.env
for /f "tokens=1,2,3 delims=." %%a in ("%VERSION%") do (
    set "MAJOR=%%a"
    set "MINOR=%%b"
    set "PATCH=%%c"
)
set /a "PATCH+=1"
set "NEW_VERSION=%MAJOR%.%MINOR%.%PATCH%"
>.env echo %NEW_VERSION%
git add .env