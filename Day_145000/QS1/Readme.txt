Step1:
（从 原始PM数据文件夹 筛选所需的PM文件）
	0.Input_PMData: 存放从PM下载的解压后的数据文件夹
	运行1SelectPMData.py:
		将0.Input_PMData中的文件夹复制至1.Selector中相应文件夹中的“1.PmPnlCsvToStrategy\Configuration\Traders”中，
		并执行_PreprocessForPmPnl.bat，得到筛选过后的PM数据文件夹，
		并将结果输出至2.Ouput_SelectedPMData。

Step2：
（生成Allocation.csv）
	将2.Ouput_SelectedPMData中的数据文件夹，复制到指定的文件夹2.SelectedPMData_SS8，
	运行3.DataEditor.GenBaseAllocation_SS8\1.CopyRunCopy\_CopyRunCopy.bat
	运行3.DataEditor.GenBaseAllocation_SS8\2.GenBaseAllocation\_GenBaseAllocation.bat

Step3:
（改变BM的Subscribe.csv）
	将2.GenBaseAllocation\BaseAllocationOutput\Allocation.csv拷贝至4.UpdateSubscriber.csv\ss8
	运行changeSubscribe.py
		Mapping.csv：PMTrader和LivePublisherTrader的对应表（第一列填LivePublsiherTraderName，第二列填PMTraderName）；
		Subscribe.csvPath.txt：所需要更改的Subscribe.csv的目录（如：***/Config）。