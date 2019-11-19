import os
import time


if __name__ == "__main__":
    allow_bigest_hour = 1           # 允许的最大小时数（可为小数）

    PATH_ROOT = os.path.dirname(__file__)
    PATH_FILE_IOList = os.path.join(PATH_ROOT, '1.CopyRunCopy', 'CopyRunCopyInput', 'IoList.csv')
    has_wrong = 0
    now_time = time.time()
    now_time_str = time.strftime('%Y%m%d_%H%M%S', time.localtime(now_time))
    print('当前日期时间:\t%s' % now_time_str)
    with open(PATH_FILE_IOList, encoding='gb2312') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace('\n', '')
            if line == '':
                continue
            line_split = line.split(',')
            if len(line_split) != 3:
                continue
            path_allocation = line_split[2]

            m_time = os.stat(path_allocation).st_mtime
            m_time_str = time.strftime('%Y%m%d_%H%M%S', time.localtime(m_time))
            d_time = now_time - m_time
            d_time_m, d_time_s = divmod(d_time, 60)
            d_time_s = int(d_time_s)
            d_time_h, d_time_m = divmod(d_time_m, 60)
            d_time_m = int(d_time_m)
            d_time_h = int(d_time_h)
            is_more_than_one_hour = d_time_h >= 1
            d_time_str = '%s:%s:%s' % (d_time_h, d_time_m, d_time_s)

            if d_time / 60 / 60 >= allow_bigest_hour:
                has_wrong = 1
                print('文件修改时间:\t%s\t修改时间超过1个小时: %s;\t\t %s' % (m_time_str, d_time_str, path_allocation))
            else:
                print('文件修改时间:\t%s;\t\tOK' % (m_time_str))

    if has_wrong == 0:
        print('Allocation+.csv修改日期 均在1小时内,正常。')
    else:
        while True:
            print('发现存在Allocation+.csv修改日期 在1个小时以前，请强行结束程序并检查')
            os.system('pause')
