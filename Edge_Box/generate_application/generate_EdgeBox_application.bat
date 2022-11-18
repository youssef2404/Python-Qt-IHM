python -m PyInstaller --onefile --name EdgeBoxApplication --distpath ..\Edge_Box_exe --windowed --icon=..\icons\addixo_X_icon.ico ..\main_user_interface.py

xcopy /e /k /h /i /y ..\icons ..\Edge_Box_exe\icons
xcopy /e /k /h /i /y build ..\Edge_Box_exe
xcopy /e /k /h /i /y EdgeBoxApplication.spec ..\Edge_Box_exe
del /f EdgeBoxApplication.spec
rmdir /s /q build
