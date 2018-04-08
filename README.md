#用于邮件提醒在SDK 阿里云邮件服务
# AdminSet
<img src="https://travis-ci.org/guohongze/adminset.svg?branch=master"></img> 
<img src="https://img.shields.io/hexpm/l/plug.svg"></img>
[![release](https://img.shields.io/github/release/guohongze/adminset.svg)]https://github.com/lilinji/Aliyun_Maill_SDK)
<br>
Aliyun_Maill_SDK基于DevOps理念开发，以整合全部运维场景为己任。Aliyun_Maill_SDK是一个真正的基于运维思维而开发的全自动化安装集群Pipline。<br>

## v1.0.1 新功能
自动调用阿里云 aliyun-php-sdk-core
自动针对企业邮件群发
自动通过excel OSS抓取自动实时提醒

## 开发环境
centos 6.8()  vim （兼容 Notes） python 2.7 兼容（3.4）<br>

## 服务端安装
生产服务器建议 4核CPU，8G内存以上.<br>
学习测试建议 2核CPU，2G内存以上.<br>
服务器操作系统版本要求 centos7.2及以上<br>
安装过程不需要任何操作<br>
```
git clone https://github.com/lilinji/Aliyun_Maill_SDK
```

## 客户端安装
客户端脚本目前rhel/centos6、7,ubuntu14.04经过测试<br>
客户端python版本支持2.6.6及以上<br>
说明：为保证注册IP是管理IP（后续会被epel等调用），客户端的保证与主机在同一网络。保证当前节点能上网 
#### step1:
拷贝源码到管理主机上并执行:
git clone https://github.com/lilinji/Aliyun_Maill_SDK



```
crontab -e 
02 09 * * *  ./send_mail.sh
## 访问
https://github.com/lilinji/Aliyun_Maill_SDK


## 说明

FAQ请转到，<a href="https://www.baidu.com">常见问题</a>

# 安全
要将程序启动在有公网可以直接访问的设备上<br>
建议生产环境中使用https配置服务器<br>
由于开发方便，在ptython的settings中开启了DEBUG，在生产中需要关闭并指定自己的域名。

# 开发者交流
请加入开发者群，注明来自github
<img src="https://github.com/lilinji/WUKONG-SGE/blob/master/Aliyun-Novogene-SGE/1.png"></img>
