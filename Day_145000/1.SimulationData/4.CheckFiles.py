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
            trader_name_pm = line_split[1]
            strategy_name = line_split[2]
            if strategy_name not in d_mapping.keys():
                d_mapping[strategy_name] = []
            d_mapping[strategy_name].append(trader_name_pm)
    return d_mapping


def main():
    # 读取mapping
    d_mapping = read_mapping()

    for strategy_name in os.listdir(PATH_TARGET_FOLDER):
        if strategy_name not in d_mapping.keys():
            print('strategy folder name error, ', strategy_name)
            continue
        path_strategy = os.path.join(PATH_TARGET_FOLDER, strategy_name)
        l_traders_file = [i.strip('.csv') for i in os.listdir(path_strategy)]
        l_traders_target = d_mapping[strategy_name]

        l_not_find = set(l_traders_file).difference(set(l_traders_target))
        l_not_exists = set(l_traders_target).difference(set(l_traders_file))

        if l_not_find or l_not_exists:
            if l_not_find:
                print('%s 缺少这些trader: \n\t%s' % (strategy_name, ',\n\t'.join(l_not_find)))
            if l_not_exists:
                print('%s 多了这些trader: \n\t%s' % (strategy_name, ',\n\t'.join(l_not_exists)))
        else:
            print('%s 正常,trader完全一致' % strategy_name)


if __name__ == '__main__':
    PATH_ROOT = os.path.dirname(__file__)
    PATH_MAPPING = os.path.join(PATH_ROOT, '0.Configuration', 'Mapping.csv')
    PATH_TARGET_FOLDER = os.path.join(PATH_ROOT, '3.Output')

    main()
    # os.system('pause')
