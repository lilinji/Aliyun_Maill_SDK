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

def ReadToFile():
    with open('/root/messages/pro_list.txt', 'r') as f1:
            list3 = f1.readlines()
            for line in islice(list3, 1, None):
                    line = line.strip('\n')
                    #print line
                    line4 = re.split('\s+', line)# split 空格 输出数组行
                    #print line4
                    mail_person = line4[9]
                    mail_group  = line4[10]
                    ecs_num = line4[11]
                    ecs_des = line4[13]
                    #print line4[14]
                    nas_num = line4[14]
                    nas_des = line4[16]
                    oss_num = line4[17]
                    oss_des = line4[19]
                    project = line4[5]
                    pro_name = line4[6]
                    sub_name = line4[7]
                    ##倒期时间
                    line5 = re.split('T', line4[3])
                    time5 = line5[0]
                    #print time5
                    d1 = datetime.datetime.strptime(time3+' 23:41:20', '%Y-%m-%d %H:%M:%S')
                    d2 = datetime.datetime.strptime(time5+' 23:41:20', '%Y-%m-%d %H:%M:%S')
                    delta = d2 - d1
                    #print delta.days
                    if (delta.days <= 7 and delta.days >=0):
                        line8=time5+'\t'+bytes(delta.days)+'\t'+bytes(ecs_num)+'\t'+(ecs_des)+'\t'+bytes(nas_num)+'\t'+(nas_des)+'\t'+bytes(oss_num)+'\t'+(oss_des)+'\t'+mail_person+'\t'+mail_group+'\t'+pro_name+'\t'+sub_name+'\t'+project
                        print line8
                        List.append(line8)
                        # dic(line4[0]) = line4[1]
                    dict1[line4[0]] = line4[1]

            f1.close()
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


ReadToFile()
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
            ecs_num = line5[3]
            nas_num = line5[5]
            oss_num = line5[7]

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
                if (ecs_num != '0'):
                    print "    <span style=\\\"color:blue;\\\"><br>&nbsp;&nbsp;&nbsp;&nbsp;产品个数: \\\"$ECS\\\"，产品类型: \\\"ECS\\\"，产品标准: \\\"$ECS1\\\"</span>"
                else:
                    print ""
                if (nas_num != '0'):
                    print "    <span style=\\\"color:blue;\\\"><br>&nbsp;&nbsp;&nbsp;&nbsp;产品个数: \\\"$NAS\\\"，产品类型: \\\"NAS\\\"，产品标准: \\\"$NAS1\\\"</span>"
                else:
                    print ""
                if (oss_num != '0'):
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
