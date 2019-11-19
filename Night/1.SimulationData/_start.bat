echo off
cd %~dp0

echo.
cd %~dp0
call 1.downloadZipFile.bat

echo.
cd %~dp0
2.uncompressFile.py

echo.
cd %~dp0
3.structureFiles.py

echo.
cd %~dp0
4.CheckFiles.py

echo.
echo ========== FINISHED ALL ========== 
pause