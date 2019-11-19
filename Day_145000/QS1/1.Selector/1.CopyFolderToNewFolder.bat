echo off
xcopy "1.Input\Cn.All.60B.PairX(MFA)@Cn.Id807035.ComM3\*.*" "1.Input\Cn.All.60B.PairX(MFA)@Cn.Id807035.ComM3_AuAg\" /Q
xcopy "1.Input\Cn.All.60B.PairX(MFA)@Cn.Id807035.ComM3N\*.*" "1.Input\Cn.All.60B.PairX(MFA)@Cn.Id807035.ComM3N_AuAg\" /Q
xcopy "1.Input\Cn.All.60.PairX(CalArb)@CnCom.Id807035.CalArb3R\*.*" "1.Input\Cn.All.60.PairX(CalArb)@CnCom.Id807035.CalArb3\" /Q
cd 1.Input
rd /s /q Cn.All.60.PairX(CalArb)@CnCom.Id807035.CalArb3R /Q