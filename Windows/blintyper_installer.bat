@echo off
echo Installing Blin Typer[0/3]
echo Installing Python...
set install_path=C:\Python312

:: Download Python installer
curl -o python_installer.exe https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe

:: Install Python
python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Python installation complete.


echo Installing Blin Typer [1/3]
echo Installing pip-modules
pip install Pillow keyboard pystray pyperclip

echo Installing Blin Typer [2/3]
set "source_folder=."
set "destination_folder=C:\Program Files\blintyper-main"
if not exist "%destination_folder%" ( mkdir "%destination_folder%" echo Folder created. )
echo Copy in Program Files [0/2]
copy /y "%source_folder%\quotim_win.pyw" "%destination_folder%"
copy /y "%source_folder%\blin.png" "%destination_folder%"
echo Copy in Program Files [1/2]
copy /y "%source_folder%\milashka.txt" "%destination_folder%"
copy /y "%source_folder%\texts.txt" "%destination_folder%"
echo Copy in Program Files [2/2]

echo Installing Blin Typer [3/3]
copy /y "%source_folder%\quotim.lnk" " C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup%"
echo Add to Autostart

echo You can close me^_^
pause
