@echo off
chcp 65001 > nul
cd /d %~dp0
setlocal enabledelayedexpansion

call:rmdir "%~dp0.venv"
call:del "%~dp0.venv\pyenv.cfg"

powershell -NoProfile -ExecutionPolicy Unrestricted %~dp0bin\setup.ps1
call "%~dp0\bin\python\tools\python.exe" -B -m venv .venv
call %~dp0.venv\Scripts\activate.bat
python -m pip install -r "%~dp0bin\requirements.txt"


:rmdir
if exist %1 rmdir /s /q %1
exit /b

:del
if exist %1 del %1