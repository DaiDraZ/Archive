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


:: Kiểm tra quyền admin
NET SESSION >nul 2>&1
if %errorlevel% NEQ 0 (
    :: Thực thi lại script với quyền admin
    color 04
    echo This script needed Administrator to running .PLease run as administrator...
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
    pip install colorama
    pip install pygame-ce

    echo INSTALL SUCCESSFUL !!!
    timeout /t 5 /nobreak > NUL    
    cd /
    
    title TREASURE HUNTER Z
    
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
    pip uninstall wheel setuptools termcolor keyboard colorama pygame-ce -y
    pip freeze > requirements.txt
    pip uninstall -r requirements.txt -y
    del requirements.txt
    echo Thank you for playing the game. See you soon!
    pause
)


