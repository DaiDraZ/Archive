@echo OFF

:: FULL SCREEN WITHOUT CLICKED
:: Created by: MMKF

:VBSDynamicBuild
SET TempVBSFile=%temp%\~tmpSendKeysTemp.vbs

:: Delete the VBS file if it exists
IF EXIST "%TempVBSFile%" DEL /F /Q "%TempVBSFile%"

:: Create the VBS file to send F11 key
ECHO Set WshShell = WScript.CreateObject("WScript.Shell") >>"%TempVBSFile%"
ECHO Wscript.Sleep 900                                    >>"%TempVBSFile%"
ECHO WshShell.SendKeys "{F11}"                             >>"%TempVBSFile%"
ECHO Wscript.Sleep 900                                    >>"%TempVBSFile%"

:: Run the VBS file using CSCRIPT
CSCRIPT //nologo "%TempVBSFile%"

:: Optional: Delete the temporary VBS file after execution
DEL /F /Q "%TempVBSFile%"

:: End of script



color 2
title = CHECK SYSTEM ...

:: Check file is edited by user and block user

setlocal

rem Kiểm tra nếu file là read-only
if not exist "run.bat" (
    echo File not exist.
    exit /b
)

rem Đặt biến để kiểm tra chế độ read-only
set "readonly=0"
for %%A in ("run.bat") do (
    if "%%~aA" neq "r" (
        set "readonly=1"
    )
)

rem Nếu file không phải là read-only, cảnh báo người dùng
if "%readonly%"=="1" (
    echo Set objShell = CreateObject("WScript.Shell") > temp.vbs
    echo objShell.Popup "Danger : You shouldn't be edited this file !", 0, "Danger !!!", 48 >> temp.vbs
    start /wait wscript temp.vbs
    del temp.vbs
    pause
) else (
    echo Check success.Please waiting ...
    cls
)

endlocal





:: Kiểm tra quyền admin
NET SESSION >nul 2>&1
if %errorlevel% NEQ 0 (
    :: Thực thi lại script với quyền admin
    color 04
    echo This script needed Administrator to running ...
    pause
    exit
)



echo Install requirement library
set /p option=Install [1] / Uninstall [0] : 

:: Check if the option is 1
if %option%==1 (
    :: Get system info
    systeminfo
    
    :: Get window size
    for /f "delims=" %%# in  ('"wmic path Win32_VideoController  get CurrentHorizontalResolution,CurrentVerticalResolution /format:value"') do (
  	set "%%#">nul=
	)

    echo Size window : %CurrentVerticalResolution% x %CurrentHorizontalResolution%

    :: Check for Python installation
    python --version > temp.txt 2>&1
    set /p version=<temp.txt
    del temp.txt

    if errorlevel 1 goto errorNoPython

    echo Python version: %version%

    :: Upgrade pip and install required packages
    python.exe -m pip install --upgrade pip
    pip install wheel setuptools
    pip install termcolor
    pip install keyboard
    pip install playsound
    pip install colorama

    echo INSTALL SUCCESSFUL !!!
    timeout /t 5 /nobreak > NUL
    title TREASURE HUNTER Z
    python.exe main.py

    echo If you want back screen window, press F11. Thank you !!!

    pause
    goto :eof

    :errorNoPython
    echo.
    echo Error: Python not installed. Please install Python by visiting [www.python.org].
    goto :eof
) else (
    :: Option is not 1, so uninstall packages
    color a
    echo Thank you for playing game >.<.See You Soon !!!
    pip uninstall wheel setuptools termcolor keyboard playsound colorama -y
    
)

pause
