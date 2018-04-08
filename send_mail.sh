#!/bin/bash
#########################################################################
# File Name: send_mail.sh
# Author: lilinji
# mail: lilinji@novogene.com
# Created Time: Thu 15 Mar 2018 03:36:04 PM CST
#########################################################################

/usr/bin/rm -f /root/messages/*.php 

sleep 2
#/usr/bin/rm -f /root/messages/sample.txt
/usr/bin/rm -f /root/messages/sample.xlsx
ossutil  cp  oss://novo-transdata-bj/运营相关文件/运营项目自动提醒.xlsx /root/messages/sample.xlsx
#/usr/bin/ossutil oss://novo-transdata-bj/sample.txt /root/messages/sample.txt
#cat /root/messages/sample.txt |tr '\r' '\n' >/root/messages/pro_list.txt
cd /root/messages

/usr/bin/python /root/messages/modify_send_past.py >>/dev/null 


if ls /root/messages/*.php >/dev/null 2>&1;
then 
    chmod 755 /root/messages/*.php
    ls /root/messages/ |grep 'php' |while read l; do echo "/usr/bin/php  /root/messages/"$l; done |sh >/dev/null 2>&1
    echo "hellow"
else
    echo -e  "hellow"
fi


