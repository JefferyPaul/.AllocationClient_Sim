import os


PATH_ROOT = os.path.dirname(__file__)
PATH_FILE_IOList = os.path.join(PATH_ROOT, '1.CopyRunCopy', 'CopyRunCopyInput', 'IoList.csv')


with open(PATH_FILE_IOList, encoding='gb2312') as f:
    has_wrong = 0
    for line in f.readlines():
        line = line.strip()
        line = line.replace('\n', '')
        if line == '':
            continue

        line_split = line.split(',')
        if len(line_split) < 3:
            print('【Wrong】 IOList line:  ', line)
            has_wrong = 1
            continue
        
        path_input = line_split[0]
        path_output = os.path.dirname(line_split[2])
        # path_input_strategy_name = path_input.split('\\')[-1]
        # path_output_strategy_name = path_output.split('\\')[-1]
        
        # 检查
        if not os.path.exists(path_input):
            print('【Wrong】 此数据文件夹不存在: ', path_input)
            has_wrong = 1
        if not os.path.exists(path_output):
            print('【Wrong】 此输出目录不存在: ', path_output)
            has_wrong = 1
        # if path_input_strategy_name != path_output_strategy_name:
        #     print('【Wrong】 文件夹名字不一致,请检查是否正常。  input：%s, outpout: %s' % (path_input_strategy_name, path_output_strategy_name))
        #     has_wrong = 1

if has_wrong == 0:
    print('IOList 检查正常。')
else:
    while True:
        print('发现数据异常， 请手动强制关闭程序并检查')
        os.system('pause')
