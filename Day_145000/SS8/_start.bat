echo off
chcp 65001
echo off

echo.
echo ====================================
echo 【Step1.1】
echo 运行\0.Input_PMData\genNewData.py
echo.
cd %~dp0
cd "0.Input_PMData"
genNewData.py


echo.
echo ========================================================================
echo 【Step1.2】
echo 运行\1.Selector\0.CopyInputData.bat 和 1.CopyFolderToNewFolder.bat
echo 将0.Input_PMData中的数据拷贝至1.Selector\1.Input中，并运行1.CopyFolderToNewFolder.bat
echo.
cd %~dp0
cd "1.Selector"
call 0.CopyInputData.bat
call 1.CopyFolderToNewFolder.bat

echo.
echo ========================================================================
echo 【Step1.3】
echo 运行\1.Selector\2.CopyDataAndRunSelector.py
echo 检查“1.Input”与“2.Selector”中的文件夹是否一一对应；将“1.Input”数据拷贝至selector中并运行，然后将生成的文件夹拷贝至\1.Selector\3.Output
echo.
cd %~dp0
cd "1.Selector"
2.CopyDataAndRunSelector.py

echo.
echo ========================================================================
echo 【Step2】
echo 运行\2.DataEditor.GenBaseAllocation\_start_DataEditor.bat
echo.
cd %~dp0
cd "2.DataEditor.GenBaseAllocation"
call _start_DataEditor.bat


echo.
echo ========================================================================
echo 【Step3.1】
echo 制文件至3.AllocationOutput
set Date=%DATE:~3,4%%DATE:~8,2%%DATE:~11,2%
if "%time:~0,1%" == " " (
	set Time=0%time:~1,1%%time:~3,2%%time:~6,2%
) else (
	set Time=%time:~0,1%%time:~1,1%%time:~3,2%%time:~6,2%
)
set FileName="Allocation_%Date%_%Time%.csv"

cd %~dp0
copy "2.DataEditor.GenBaseAllocation\2.GenBaseAllocation\BaseAllocationOutput\Allocation.csv" "3.AllocationOutput"
cd "3.AllocationOutput"
ren Allocation.csv %FileName%
cd %~dp0
copy "2.DataEditor.GenBaseAllocation\2.GenBaseAllocation\BaseAllocationOutput\Allocation.csv" "3.AllocationOutput"

echo.
echo ========================================================================
echo 【已完成 请检查】
echo Allocation.csv文件输出于： /3.AllocationOutput/Allocation.csv
cd %~dp0
cd "4.AllocationCsvDiffPlot"
AllocationCsvDiff.py
pause