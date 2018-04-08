#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: count_time.py
# Author: lilinji
# mail: lilinji@novogene.com
# Created Time: Tue 27 Feb 2018 01:17:03 PM CST
#########################################################################

import urllib2
import urllib
import datetime
import sys
import re
import os.path
from itertools import islice
from collections import Counter
import xlrd
import re
import sqlite3

def read_xlsx():
    workbook = xlrd.open_workbook('sample.xlsx')
    booksheet = workbook.sheet_by_name('Sheet1')
    p = list()
    for row in range(booksheet.nrows):
            row_data = []
            for col in range(booksheet.ncols):
                    cel = booksheet.cell(row, col)
                    val = cel.value
                    try:
                            val = cel.value
                            val = re.sub(r'\s+', '', val)
                    except:
                            pass

                    if type(val) == float:
                        val = int(val)
                    else:
                        val = str(val)
                    row_data.append(val)
            p.append(row_data)

    return  p

def operat_sqlite(*data):
    # print(type(data))
    # print(data)
    print(data[0])
    try:
        conn = sqlite3.connect('E:\list.db')
    except:
        print('open sqlite3 failed.')
        return
    else:  #操作数据库
         c = conn.cursor()
         for item in data:
             for i in range(len(item)):
                 DLDMv = item[i][1]
                 LDDMv = item[i][3]
                 LDMCv = item[i][2]
                 FHSSLXv = item[i][5]
                 XZQHv = item[i][6]
                 try:
                    #creat sql
                     c.execute("insert into roadkey (DLDM, LDDM, LDMC, FHSSLX, XZQH) values (?, ?, ?, ?, ?)", (DLDMv, LDDMv, LDMCv, FHSSLXv, XZQHv))
                     conn.commit()
                 except:
                     print('insert roadky failed ')
                     pass
                 print(i)
                 print(item[i])
         conn.close()

    return

if __name__ == '__main__':
   data_list =  list()
   data_list = read_xlsx()
 #  operat_sqlite(data_list)
