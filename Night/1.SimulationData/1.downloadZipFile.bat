echo off

cd %~dp0
rd /s /q "1.Output_ZipFile"
md "1.Output_ZipFile"

cd %~dp0
cd "0.TradingPlatform.MessageClient"
TradingPlatform.MessageClient.exe 220.231.191.82 11005 getfile "Jeffery_SimPnl_Night_29402.zip" "../1.Output_ZipFile/Jeffery_SimPnl_Night_29402.zip"