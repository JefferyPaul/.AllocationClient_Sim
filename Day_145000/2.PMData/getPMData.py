import os
import json
import pyodbc
import shutil
import time


# {trader_id: [[date, pnl], [], [], ], }
def get_pm_strategy_trader_pnl(conn_info, strategy_name):
	# 连接db
	conn = pyodbc.connect(conn_info)
	cursor = conn.cursor()

	# 获取pm_strategy_info  （主要用于获取 Init Capital信息）
	l_traders = []
	sql = '''SELECT [Id]
		  FROM [Platinum.PM].[dbo].[TraderDbo]
		  where strategyid = '%s'
	''' % strategy_name
	for row in cursor.execute(sql).fetchall():
		l_traders.append(row[0])

	# 获取pm_trader_data
	d_traders_pnl = {trader_id: [] for trader_id in l_traders}
	sql = '''SELECT [Date]
	,[TraderId]
	,[Pnl]
	FROM [Platinum.PM].[dbo].[TraderLogDbo]
	where date >= '%s' and traderId in ('%s') 
	''' % (start_date, "' ,'".join(l_traders))
	for row in cursor.execute(sql).fetchall():
		date = row[0]
		trader_id = row[1]
		pnl = row[2]
		d_traders_pnl[trader_id].append([date, pnl])

	# 退出db连接
	conn.close()
	return d_traders_pnl


# 读取配置文件
PATH_FILE = os.path.dirname(__file__)
PATH_CONFIG_FOLDER = os.path.join(PATH_FILE, 'Config')
PATH_DB_INFO = os.path.join(PATH_CONFIG_FOLDER, 'db_info.json')
PATH_Strategies = os.path.join(PATH_CONFIG_FOLDER, 'targetStrategies.txt')
PATH_OUTPUT = os.path.join(PATH_FILE, 'Data')

with open(PATH_DB_INFO, encoding='utf-8') as f:
	db_info = json.loads(f.read())
conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s' % (
	db_info.get('db'),
	db_info.get('host'),
	db_info.get('user'),
	db_info.get('pwd')
)
start_date = str(int(db_info.get('start_date')))
with open(PATH_Strategies) as f:
	l_target_strategies = f.readlines()

# 获取db数据
# d_d_traders_pnl = {strategy_name: {trader_name: [[date,pnl], [], ], }, }
d_d_traders_pnl = {}
for target_strategy in l_target_strategies:
	target_strategy = target_strategy.strip()
	target_strategy = target_strategy.replace('\n', '')
	if target_strategy == '':
		continue
	print('geting pm data of :  ', target_strategy)
	d_traders_pnl = get_pm_strategy_trader_pnl(conn_info, target_strategy)
	d_d_traders_pnl[target_strategy] = d_traders_pnl

# 删除旧output
# 输出新data至新output
if os.path.exists(PATH_OUTPUT):
	print('删除旧Output')
	shutil.rmtree(PATH_OUTPUT)
	time.sleep(0.5)
os.mkdir(PATH_OUTPUT)


for strategy_name, d_traders_pnl in d_d_traders_pnl.items():
	path_output_strategy = os.path.join(PATH_OUTPUT, strategy_name)
	os.mkdir(path_output_strategy)

	for trader_name, l_pnl in d_traders_pnl.items():
		# 数据按日期排序
		d_pnl = {}
		for line in l_pnl:
			date = line[0]
			pnl = line[1]
			d_pnl[date] = pnl

		path_output_trader = os.path.join(path_output_strategy, '%s.csv' % trader_name)
		l_write_line = ["TraderId,Date,Pnl,Commission,Slippage\n"] + \
					   ["%s,%s,%s,0,0\n" % (trader_name, date, d_pnl[date]) for date in sorted(d_pnl)]
		with open(path_output_trader, 'w') as f:
			f.writelines(l_write_line)

