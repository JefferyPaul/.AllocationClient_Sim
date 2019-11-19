import os
import shutil


def read_mapping():
    d_mapping = {}
    with open(PATH_MAPPING) as f:
        f.readline()
        for line in f.readlines():
            line = line.strip()
            if line == '':
                continue
            line_split = line.split(',')
            trader_name_sim = line_split[0]
            trader_name_pm = line_split[1]
            strategy_name = line_split[2]
            d_mapping[trader_name_sim] = {
                "trader_name_pm": trader_name_pm,
                "strategy_name": strategy_name
            }
    return d_mapping


def change_pnl_file(path_input, path_output):
    l_new_file = list()
    l_new_file.append('TraderId,Date,Pnl,Commission,Slippage\n')
    with open(path_input) as f_old:
        f_old.readline()
        for line in f_old.readlines():
            line = line.strip()
            if line == '':
                continue
            line_split = line.split(',')

            trader_id = os.path.basename(path_output).strip('.csv')
            s_date = line_split[0]
            s_pnl = line_split[2]
            s_commission = line_split[3]
            s_slippage = '0'

            l_new_file.append('%s,%s,%s,%s,%s\n' % (trader_id, s_date, s_pnl, s_commission, s_slippage))

    with open(path_output, 'w') as f_new:
        f_new.writelines(l_new_file)


def main():
    # 读取mapping
    d_mapping = read_mapping()

    # 遍历输入的数据
    for file_name in os.listdir(PATH_INPUT):
        path_file = os.path.join(PATH_INPUT, file_name)
        if not os.path.isfile(path_file):
            continue
        trader_name = file_name.strip('.csv')
        if trader_name not in d_mapping.keys():
            print('【Error】not find this trader in mapping, ', trader_name)
            continue
        trader_name_pm = d_mapping[trader_name]['trader_name_pm']
        strategy_name = d_mapping[trader_name]['strategy_name']

        # 找到对应的文件信息
        path_output_strategy = os.path.join(PATH_OUTPUT, strategy_name)
        if not os.path.exists(path_output_strategy):
            print('mkdir: ', strategy_name)
            os.mkdir(path_output_strategy)
        path_output_file = os.path.join(path_output_strategy, trader_name_pm + '.csv')
        # 重写文件 并输出
        change_pnl_file(path_input=path_file, path_output=path_output_file)


if __name__ == '__main__':
    PATH_ROOT = os.path.dirname(__file__)
    PATH_MAPPING = os.path.join(PATH_ROOT, '0.Configuration', 'Mapping.csv')
    PATH_INPUT = os.path.join(PATH_ROOT, '2.Output_SimulationPnlFiles')
    PATH_OUTPUT = os.path.join(PATH_ROOT, '3.Output')

    if os.path.isdir(PATH_OUTPUT):
        shutil.rmtree(PATH_OUTPUT)
    os.mkdir(PATH_OUTPUT)

    main()
    # os.system('pause')
