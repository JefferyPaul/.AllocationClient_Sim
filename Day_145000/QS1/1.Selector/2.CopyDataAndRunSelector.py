import os
import shutil
import time


PATH_BASE = os.path.dirname(__file__)
PATH_PROCESS = os.path.join(PATH_BASE, '2.Selector')
PATH_OUTPUT = os.path.join(PATH_BASE, '3.Output')
PATH_INPUT = os.path.join(PATH_BASE, '1.Input')

# 检查数据文件夹和Selector文件夹是否对应
# l_floder_input = [i for i in os.listdir(PATH_INPUT) if os.path.isdir(os.path.join(PATH_INPUT, i))]
# l_floder_process = [i for i in os.listdir(PATH_PROCESS) if os.path.isdir(os.path.join(PATH_PROCESS, i))]
# l_floder_input_not_in_process = [i for i in l_floder_input if i not in l_floder_process]
# l_floder_process_not_in_input = [i for i in l_floder_process if i not in l_floder_input]
# if len(l_floder_input_not_in_process) > 0 or len(l_floder_process_not_in_input) > 0:
#     if len(l_floder_input_not_in_process) > 0:
#         print("【Wrong】这些 1.Input 中的数据文件夹，在 2.Selector 中没有对应的 Selector文件夹")
#         for i in l_floder_input_not_in_process:
#             print('     ', i)
#             # os.system('pause')
#     if len(l_floder_process_not_in_input) > 0:
#         print("【Wrong】这些 2.Selector 中的文件夹，在 1.Input 中没有对应的 数据文件夹")
#         for i in l_floder_process_not_in_input:
#             print('     ', i)
#             # os.system('pause')
#     while True:
#         print('发现数据异常， 请手动强制关闭程序并检查')
#         os.system('pause')
# else:
#     print("1.Input中的数据文件夹 与 2.Selector中的文件夹 完全一致一一对应  ")
# print("\n")

# 复制数据文件至 相应的2.Selector中
# 并运行Selector中的_PreprocessForPmPnl.bat
# 然后将生成的 DataFolder 拷贝至3.Output
if os.path.exists(PATH_OUTPUT):
    shutil.rmtree(PATH_OUTPUT)
    time.sleep(0.1)
os.mkdir(PATH_OUTPUT)
for strategy_folder_name in os.listdir(PATH_INPUT):
    path_input_folder = os.path.join(PATH_INPUT, strategy_folder_name)
    path_process_folder = os.path.join(PATH_PROCESS, strategy_folder_name)
    if not os.path.isdir(path_input_folder):
        continue
    if not os.path.isdir(path_process_folder):
        print('【Wrong】Have data folder, but not exist process: ', strategy_folder_name)
        continue

    print("执行selector:  ", strategy_folder_name)
    path_process_input = os.path.join(path_process_folder, '1.PmPnlCsvToStrategy', 'Configuration', 'Traders')
    # 新建目标文件夹
    if os.path.exists(path_process_input):
        shutil.rmtree(path_process_input)
        time.sleep(0.1)
    os.mkdir(path_process_input)

    # 复制文件
    path_process_input_strategy = os.path.join(path_process_input, strategy_folder_name)
    shutil.copytree(path_input_folder, path_process_input_strategy)

    # 运行bat 执行selector
    path_bat = path_process_folder + '/_PreprocessForPmPnl.bat'
    # print(path_bat)
    # os.popen(path_bat)
    # cmd = """cd %s call _PreprocessForPmPnl.bat""" % path_process_folder
    # os.system(path_bat)
    # print("运行_PreprocessForPmPnl.bat")
    os.chdir(path_process_folder)
    os.system(r"_PreprocessForPmPnl.bat")
    # os.popen(str(path_bat))

    # 将结果拷贝至 3.Output
    # print("将文件夹拷贝至3.Output\n")
    print("-----------------------------------\n")
    path_selector_output = os.path.join(path_process_folder, '2.MappingCopyPmPnl', 'MappingCopyPnlOutput')
    path_selector_output_in_output = os.path.join(PATH_OUTPUT, strategy_folder_name)
    shutil.copytree(path_selector_output, path_selector_output_in_output)

print("已全部运行 1.Selector/2.Selector/xxx/_PreprocessForPmPnl.bat")
print("根据MappingPath筛选PMData，并复制至3.Output")