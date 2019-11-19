echo off
chcp 65001
echo off

echo.
echo 运行 /1.0.CheckDataEditorIOList.py
echo 检查IOList中的输入输出地址是否存在并且一一对应
cd %~dp0
1.0.CheckDataEditorIOList.py

echo.
echo 运行 /1.CopyRunCopy/_CopyRunCopy.bat
echo 调用39中的Filter，生成Allocation+.csv
cd %~dp0
cd 1.CopyRunCopy
call _CopyRunCopy.bat

echo.
echo 运行 /2.0.Check_Allocation.csv_mtime.py
echo 检查所有在IOList.csv中的目标Allocation+.csv文件的修改时间
cd %~dp0
2.0.Check_Allocation.csv_mtime.py

echo.
echo 运行 /2.GenBaseAllocation/_GenBaseAllocation.bat
echo 生产最终的Allocation.csv
cd %~dp0
cd 2.GenBaseAllocation
call _GenBaseAllocation.bat
