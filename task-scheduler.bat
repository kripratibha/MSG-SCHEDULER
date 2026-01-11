@echo off

REM ---- CONFIGURATION ----
set TASK_NAME=DailyTelegramMessage
set PYTHON_PATH=C:\Users\Asus\AppData\Local\Programs\Python\Python311\python.exe
set SCRIPT_PATH=C:\Users\Asus\Downloads\task_schedular\telegram_auto_send.py

REM ---- CREATE SCHEDULED TASK ----
schtasks /create ^
 /tn "%TASK_NAME%" ^
 /tr "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" ^
 /sc daily ^
 /st 09:00 ^
 /f

echo Task "%TASK_NAME%" created successfully!
pause
