echo off
rd /s /q 1.Input
Xcopy "..\..\3.GenNewData\Data\*.*" "1.Input\" /s /e /y /Q
