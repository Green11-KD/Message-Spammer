@echo off
setlocal

rem Check if Python is installed
python --version 2>nul

if errorlevel 1 (
  echo Python is not installed.
  echo Python is required to be installed to run Message Spammer.
  echo Please install the lastest Python from here:
  echo https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=en-us^&gl=US
  pause
  endlocal
) else (
  python message_spammer.py
)

echo.

endlocal

