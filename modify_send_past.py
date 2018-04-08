#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: count_time.py
# Author: lilinji
# mail: lilinji@novogene.com
# Created Time: Tue 27 Feb 2018 01:17:03 PM CST
#########################################################################
import xdrlib
import xlrd
import urllib2
import urllib
import datetime
import sys
import re
import os.path
from itertools import islice 
from collections import Counter
reload(sys)
sys.setdefaultencoding( "utf-8" )

###################Open Excel
def open_excel(file= 'sample.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
###################Read Excel
#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'sample.xlsx',colnameindex=1,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
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
####################Class
class CustomOpen(object):
    def __init__(self, filename):
      self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

####################

temp1 = '''<?php
    include_once '/opt/aliyun-php-sdk-core/Config.php';
    use Dm\Request\V20151123 as Dm;
    //需要设置对应的region名称，如华东1（杭州）设为cn-hangzhou，新加坡Region设为ap-southeast-1，澳洲Region设为ap-southeast-2。
    $iClientProfile = DefaultProfile::getProfile("cn-hangzhou", "LTAIYHu9Sqt3hTK3", "KN30zUxIRtwz5g52Qxn8TuIx4eleEy");
    //新加坡或澳洲region需要设置服务器地址，华东1（杭州）不需要设置。
    //$iClientProfile::addEndpoint("ap-southeast-1","ap-southeast-1","Dm","dm.ap-southeast-1.aliyuncs.com");
    //$iClientProfile::addEndpoint("ap-southeast-2","ap-southeast-2","Dm","dm.ap-southeast-2.aliyuncs.com");
    $client = new DefaultAcsClient($iClientProfile);
    $request = new Dm\SingleSendMailRequest();
    //新加坡或澳洲region需要设置SDK的版本，华东1（杭州）不需要设置。
    //$request->setVersion("2017-06-22");
'''
#    $num=5;
#    $dtime="2018-03-01";
#    $daty="6";
#    $ECS=6;
#    $ECS1="32C 128G; 10M 宽带; 40G 系统盘";
#    $NAS=1;
#    $NAS1="40T";
#    $OSS=1;
#    $OSS1="150T";
#    $PRO_NAME
#    $SUB_PRO_NAME
#    $NAME_NAME=


temp2 = '''    
    $messages ="尊敬的诺禾VIP客户:<br/>
    <br>&nbsp;&nbsp;&nbsp;&nbsp;您好～<br/>
    <br>&nbsp;&nbsp;&nbsp;&nbsp;您的项目<span style=\\\"color:blue;\\\">\\\"$PRO_NAME+$SUB_PRO_NAME+$NAME_NAME\\\"</span> 将于<span style=\\\"color:blue;\\\">”$dtime 24:00:00”</span> 正式到期，根据合作协议，贵公司应于 <span style=\\\"color:blue;\\\">\\\"$dtime 24:00:00\\\"</span> 前预付下月费用，还烦请贵公司近期内及时向我公司支付上述款项，感谢您的信赖与支持！<br/>
    <br>&nbsp;&nbsp;&nbsp;&nbsp;如果未及时付费，到期账号自动关闭，由此造成的损失由贵公司承担。账号关闭后，数据为您保留3天，逾期数据将不可恢复。到期后3天内续费，账号恢复正常，逾期数据存储产生的费用需由您承担。<br/>
    <br>&nbsp;&nbsp;&nbsp;&nbsp;截至目前仅剩<span style=\\\"color:blue;\\\">\\\"$daty\\\"</span>天。<br/>'''
temp5 ='''
    <br>&nbsp;&nbsp;&nbsp;&nbsp开通资源明细如下:<br/>'''
temp3 = '''
    </br>
    </br>
    <br>祝您工作顺利，生活愉快！</br>";
    $request->setAccountName("cloud@novocloud.cn");
    $request->setFromAlias("novocloud");
    $request->setAddressType(1);
    $request->setTagName("novogene");
    $request->setReplyToAddress("true");'''

#    $request->setToAddress("lilinji@novogene.com,qiangyubiao@novogene.com");
temp4 = '''
    $request->setSubject("温馨提示：您的云资源即将到期，请及时续费");
    $request->setHtmlBody("$messages");
    try {
        $response = $client->getAcsResponse($request);
        print_r($response);
    }
    catch (ClientException  $e) {
        print_r($e->getErrorCode());
        print_r($e->getErrorMessage());
    }
    catch (ServerException  $e) {
        print_r($e->getErrorCode());
        print_r($e->getErrorMessage());
    }
?>'''
dict1={}
List = []

def main():
   s_unicode = u'\u4f60\u597d'
   s_str = s_unicode.encode('utf-8')
#   s_str = s_unicode.encode('unicode-escape').decode('string_escape')
       #print type(row)
       #print list(row)
       #print row.items()
   tables = excel_table_byname()
   for row in tables:
       mail_person = row.get('mail_person')
       mail_group  = row.get('mail_group')
       ecs_num = row.get('ecs_num')
       ecs_des = row.get('ecs_des')
       nas_num = row.get('nas_num')
       nas_des = row.get('nas_des')
       oss_num = row.get('oss_num')
       oss_des = row.get('oss_des')
       project = row.get('project')
       pro_name = row.get('pro_name')
       sub_name = row.get('sub_name')
       ##倒期时间
       end_time = row.get('end_time1')
       #line5 = re.split('T', line4[3])
       line5 = re.split('T', end_time)
       time5 = line5[0]
       d1 = datetime.datetime.strptime(time3+' 23:41:20', '%Y-%m-%d %H:%M:%S')
       d2 = datetime.datetime.strptime(time5+' 23:41:20', '%Y-%m-%d %H:%M:%S')
       delta = d2 - d1
       if (delta.days <= 7 and delta.days >=0):
           #line8=time5+'\t'+bytes(delta.days)+'\t'+bytes(ecs_num)+'\t'+(ecs_des)+'\t'+bytes(nas_num)+'\t'+(nas_des)+'\t'
           line8=time5+'\t'+bytes(delta.days)+'\t'+bytes(ecs_num)+'\t'+(ecs_des)+'\t'+bytes(nas_num)+'\t'+(nas_des)+'\t'+bytes(oss_num)+'\t'+(oss_des)+'\t'+mail_person+'\t'+mail_group+'\t'+pro_name+'\t'+sub_name+'\t'+project
           #print line8
           List.append(line8)
###########################################
#print str(time1)[:-7],
nowtime=datetime.datetime.now()
time4="2018-02-28"
time3=str(nowtime)[:10]
#print time3
#print delta.days
##########################################

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


def save_file(this_download_url,path):
    print"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "


#ReadToFile()
main()
d = Counter(List)
count=0
#print List
def WriteToFile_Change_exechost():
    saveout = sys.stdout
    for k in d:
            num = bytes(d[k])
#            print k            
#            print (d[k])
            novo=num +'\t'+str(k)
            line5 = re.split('\s+', novo)
            sendname = line5[11]
            ecs_num = (line5[3])
            nas_num = (line5[5])
            oss_num = (line5[7])

            date_ago = int(line5[2]) -7
#    $num=5;
#    $dtime="2018-03-01";
#    $daty="6";
#    $ECS=6;
#    $ECS1="32C 128G; 10M 宽带; 40G 系统盘";
#    $NAS=1;
#    $NAS1="40T";
#    $OSS=1;
#    $OSS1="150T";
        #print date_ago
            if (date_ago == 0 or date_ago == -4 ):
             #   print line5
                fd = open(sendname+'send_maill.php', 'w')
                sys.stdout = fd
                print temp1+"    $num="+line5[0]+";"+'\n'+"    $dtime=\""+line5[1]+"\""+";"+'\n'+"    $daty=\""+line5[2]+"\""+";"
                print "    $ECS=\""+line5[3]+"\""+";"
                if (line5[3]!= '0'):
                    des = re.split('-', line5[4])
                    print "    $ECS1=\""+des[0]+des[1]+'-'+des[2]+"带宽"+'-'+des[3]+"硬盘""\""+";"
                else:
                    print ""
                print "    $NAS=\""+line5[5]+"\""+";"
                print "    $NAS1=\""+line5[6]+"\""+";"
                print "    $OSS=\""+line5[7]+"\""+";"
                print "    $OSS1=\""+line5[8]+"\""+";"
                print "    $PRO_NAME=\""+line5[13]+"\""+";"
                print "    $SUB_PRO_NAME=\""+line5[11]+"\""+";"
                print "    $NAME_NAME=\""+line5[12]+"\""+";"
                print temp2
                print temp5
                if (ecs_num != '0.0'):
                    print "    <span style=\\\"color:blue;\\\"><br>&nbsp;&nbsp;&nbsp;&nbsp;产品个数: \\\"$ECS\\\"，产品类型: \\\"ECS\\\"，产品标准: \\\"$ECS1\\\"</span>"
                else:
                    print ""
                if (nas_num != '0.0'):
                    print "    <span style=\\\"color:blue;\\\"><br>&nbsp;&nbsp;&nbsp;&nbsp;产品个数: \\\"$NAS\\\"，产品类型: \\\"NAS\\\"，产品标准: \\\"$NAS1\\\"</span>"
                else:
                    print ""
                if (oss_num != '0.0'):
                    print "    <span style=\\\"color:blue;\\\"><br>&nbsp;&nbsp;&nbsp;&nbsp;产品个数: \\\"$OSS\\\"，产品类型: \\\"OSS\\\"，产品标准: \\\"$OSS1\\\"</span>"
                else:
                    print ""
                print temp3
                print "    $request->setToAddress(\""+line5[9]+','+line5[10]+"\");"
                print temp4

        #elif (date_ago == -6):
        #   print line5[0]
            else:
                print "hellowrd"
           # k是lst中的每个元素
        # d[k]是k在lst中出现的次数
#print (Counter(List)).most_common()
WriteToFile_Change_exechost()
