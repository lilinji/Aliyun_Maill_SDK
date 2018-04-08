#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import re
from itertools import islice
reload(sys)
sys.setdefaultencoding( "utf-8" )
def open_excel(file= 'a.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= 'a.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'a.xls',colnameindex=1,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    #print table
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(2,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

#def main():
   #s_unicode = u'\u4f60\u597d' 
   #s_str = s_unicode.encode('utf-8')
#   s_str = s_unicode.encode('unicode-escape').decode('string_escape')  
   #tables = excel_table_byindex()
   #for row in tables:
       #print type(row)
       #print list(row)
       #print row.keys()
       #print row       
   #tables = excel_table_byname()
   #for row in tables:
       #print row
dict1={}
List = []
def main():
   s_unicode = u'\u4f60\u597d'
   s_str = s_unicode.encode('utf-8')
#   s_str = s_unicode.encode('unicode-escape').decode('string_escape')
       #print type(row)
       #print list(row)
       #print row.items()
       #print row.get('nihao')
   tables = excel_table_byname()
   for row in tables:
       print row
       #print row.get('nihao')
       mail_person = row.get('mail_person')
       mail_group  = row.get('mail_group')
       ecs_num = row.get('ecs_num')
       #print ecs_num
       ecs_des = row.get('ecs_des')
       nas_num = row.get('nas_num')
       nas_des = row.get('nas_des')
       #print nas_des
       oss_num = row.get('oss_num')
       oss_des = row.get('oss_des')
       project = row.get('project')
       pro_name = row.get('pro_name')
       sub_name = row.get('sub_name')
       ##倒期时间
       end_time = row.get('end_time')
       #line5 = re.split('T', line4[3])
       #line5 = re.split('T', end_time)
       #time5 = line5[0]
       #d1 = datetime.datetime.strptime(time3+' 23:41:20', '%Y-%m-%d %H:%M:%S')
       #d2 = datetime.datetime.strptime(time5+' 23:41:20', '%Y-%m-%d %H:%M:%S')
       #delta = d2 - d1
       #if (delta.days <= 7 and delta.days >=0):
       #line8=bytes(ecs_num)+'\t'+(ecs_des)+'\t'+bytes(nas_num)+'\t'+(nas_des)+'\t'+pro_name+'\t'+sub_name
       line8=bytes(ecs_num)+'\t'+(ecs_des)+'\t'+bytes(nas_num)+'\t'+(nas_des)+'\t'+bytes(oss_num)+'\t'+(oss_des)+'\t'+mail_person+'\t'+mail_group+'\t'+pro_name+'\t'+sub_name+'\t'+project
       print line8
  #     List.append(line8)


if __name__=="__main__":
    main()
