echo off
chcp 65001
echo off


echo.
echo ============  ============
cd %~dp0
cd "1.SimulationData"
call _start.bat

echo.
echo ============  ============
cd %~dp0
cd "2.PMData"
getPMData.py

echo.
echo ============  ============
cd %~dp0
cd "3.GenNewData"
genNewData.py

pause