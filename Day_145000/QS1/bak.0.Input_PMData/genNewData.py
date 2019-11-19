import os
import shutil
import time


# 将 SimData 的 最后一条插入到 PM中
def main():
    for strategy_name in os.listdir(PATH_INPUT_PM):
        path_strategy_pm = os.path.join(PATH_INPUT_PM, strategy_name)
        path_strategy_sim = os.path.join(PATH_INPUT_SIM, strategy_name)
        path_strategy_output = os.path.join(PATH_OUTPUT, strategy_name)
        if not os.path.isdir(path_strategy_sim):
            continue
        os.mkdir(path_strategy_output)
        print('mkdir ', strategy_name)

        for file_name in os.listdir(path_strategy_pm):
            path_file_pm = os.path.join(path_strategy_pm, file_name)
            path_file_sim = os.path.join(path_strategy_sim, file_name)
            path_file_output = os.path.join(path_strategy_output, file_name)
            if not os.path.isfile(path_file_sim):
                continue

            # 读取文件
            with open(path_file_pm) as f:
                l_lines_pm = f.readlines()
            n = 0
            while True:
                n += -1
                line_pm = l_lines_pm[n].strip()
                if line_pm == '':
                    continue
                else:
                    s_least_dt_pm = line_pm.split(',')[1]
                    break

            with open(path_file_sim) as f:
                l_lines_sim = f.readlines()
                n = 0
                while True:
                    n += -1
                    line_sim = l_lines_sim[n].strip()
                    if line_sim == '':
                        continue
                    else:
                        if line_sim.split(',')[0] == 'TraderId':
                            line_new_from_sim = ''
                            break
                        line_new_from_sim = line_sim
                        break

            l_lines_new = l_lines_pm + [line_new_from_sim]
            with open(path_file_output, 'w') as f:
                f.writelines(l_lines_new)


if __name__ == '__main__':
    PATH_ROOT = os.path.dirname(__file__)
    PATH_OUTPUT = os.path.join(PATH_ROOT, 'Data')
    PATH_INPUT_SIM = os.path.join(os.path.dirname(os.path.dirname(PATH_ROOT)), '1.SimulationData', '3.Output')
    PATH_INPUT_PM = os.path.join(os.path.dirname(os.path.dirname(PATH_ROOT)), '2.PMData', 'Data')

    if os.path.exists(PATH_OUTPUT):
        shutil.rmtree(PATH_OUTPUT)
        time.sleep(0.0001)
    os.mkdir(PATH_OUTPUT)

    main()

    # os.system('pause')
