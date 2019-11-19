# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:32:24 2018

@author: Administrator
"""

import os
import sys
import pandas as pd
from glob import glob
from pyecharts.charts import Bar, Page
from pyecharts import options as opts
from datetime import datetime


def ValidateFolder(folder_path):
    if os.path.isdir(folder_path):
        print('Valid folder path. [%s]'%(folder_path))
        return True
    else:
        print('Invalid folder path. Please check')
        return False


def ValidateAllocationCsvFileNumber(folder_path):
    allocation_files = glob(AllocationCsvFolder+'\\*.csv')
    if len(allocation_files) < 2:
        print('No two allocation files to compare.')
        return False
    else:
        print('Valid file number')
        return True

def ValidateAllocationCsvFile(new_allocation_file, old_allocation_file):
    new_substrategies = pd.read_csv(new_allocation_file,header=None)
    new_substrategies.columns = ['Substrategy', 'Allocation']
    old_substrategies = pd.read_csv(old_allocation_file,header=None)
    old_substrategies.columns = ['Substrategy', 'Allocation']
    if new_substrategies.Substrategy.tolist().sort(reverse=True) == new_substrategies.Substrategy.tolist().sort(reverse=True):
        print('Same substrategies.')
        return True
    else:
        print('Different substrategies. Please ckeck the Allocation.csv files!')
        return False

def GenStrategy(substrategy):
    strategy = ('|').join(substrategy.split(' ')[-1].split('\\')[:-1])
    return strategy

def GenPort(substrategy):
    port = substrategy.split(' ')[-1].split('\\')[-1].strip('.csv')
    return port

if __name__ == '__main__':
    
    #global height
    global width
    global bar_width 
    bar_width = 15
    #height = 1200
    width = 2300
    
    # ======================== Allocation.csv Folder Path ========================================================
    PATH_FILE = os.path.dirname(__file__)
    PATH_ROOT = os.path.dirname(PATH_FILE)
    AllocationCsvFolderLocal = '3.AllocationOutput'
    AllocationCsvFolder = os.path.join(PATH_ROOT, AllocationCsvFolderLocal)
    HtmlOutputLocal = r'4.AllocationCsvDiffPlot/AllocationCompare'
    HtmlOutput = os.path.join(PATH_ROOT, HtmlOutputLocal)
    # ============================================================================================================
    
    
    folder_validation = ValidateFolder(AllocationCsvFolder)
    if folder_validation == False: sys.exit(0)
    
    number_validattion = ValidateAllocationCsvFileNumber(AllocationCsvFolder)
    if number_validattion == False: sys.exit(0)
    
    allocation_files = glob(AllocationCsvFolder+'\\*.csv')
    allocation_files.sort(reverse=True)
    
    new_allocation_file = allocation_files[0]
    print('New: %s'%(new_allocation_file))
    old_allocation_file = allocation_files[1]
    print('Old: %s'%(old_allocation_file))
    
    file_validation = ValidateAllocationCsvFile(new_allocation_file, old_allocation_file)
    if file_validation == False: sys.exit(0)
    
    new_substrategies = pd.read_csv(new_allocation_file,header=None)
    new_substrategies.columns = ['Substrategy', 'Allocation']
    new_substrategies['Strategy'] = new_substrategies.Substrategy.apply(lambda x: GenStrategy(x))
    new_substrategies['Port'] = new_substrategies.Substrategy.apply(lambda x: GenPort(x))
    old_substrategies = pd.read_csv(old_allocation_file,header=None)
    old_substrategies.columns = ['Substrategy', 'Allocation']
    old_substrategies['Strategy'] = old_substrategies.Substrategy.apply(lambda x: GenStrategy(x))
    old_substrategies['Port'] = old_substrategies.Substrategy.apply(lambda x: GenPort(x))
    
    
    page = Page()
    def barplot(substrategies,new_allocations,old_allocations,strategy) -> Bar:
        height = len(substrategies)*(bar_width + 40) + 120
        c = (
            Bar(init_opts=opts.InitOpts(width='%dpx'%(width),height="%dpx"%(height)))
            .add_xaxis(substrategies)
            .add_yaxis("New %s"%(new_allocation_file.split('.')[0].split('\\')[-1]), new_allocations)
            .add_yaxis("Old %s"%(old_allocation_file.split('.')[0].split('\\')[-1]), old_allocations)
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"),barWidth=15)
            .set_global_opts(
                title_opts=opts.TitleOpts(title=strategy, subtitle=datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
            )
        )
        return c
    
    strategies = new_substrategies.Strategy.drop_duplicates().tolist()
    for strategy in strategies[::-1]:
        df_new = new_substrategies[new_substrategies.Strategy == strategy]
        ports = df_new.Port.tolist()[::-1]
        new_allocations = df_new.Allocation.tolist()
        df_old = old_substrategies[old_substrategies.Strategy == strategy]
        old_allocations = df_old.Allocation.tolist()
        page.add(barplot(ports,new_allocations,old_allocations,strategy))
        
    page.render('%s.html'%(new_allocation_file.replace(AllocationCsvFolderLocal,HtmlOutputLocal)))
    os.system('%s.html'%(new_allocation_file.replace(AllocationCsvFolderLocal,HtmlOutputLocal)))

