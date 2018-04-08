<?php    
    include_once '/opt/aliyun-php-sdk-core/Config.php';
    use Dm\Request\V20151123 as Dm;            
    //需要设置对应的region名称，如华东1（杭州）设为cn-hangzhou，新加坡Region设为ap-southeast-1，澳洲Region设为ap-southeast-2。
    $iClientProfile = DefaultProfile::getProfile("cn-hangzhou", "LTAIYHu9Sqt3hafdfdTK3", "KN30zUxIRtwz5g52Qxn8TuIx4adfdeleEydfc");        
    //新加坡或澳洲region需要设置服务器地址，华东1（杭州）不需要设置。
    //$iClientProfile::addEndpoint("ap-southeast-1","ap-southeast-1","Dm","dm.ap-southeast-1.aliyuncs.com");
    //$iClientProfile::addEndpoint("ap-southeast-2","ap-southeast-2","Dm","dm.ap-southeast-2.aliyuncs.com");
    $client = new DefaultAcsClient($iClientProfile);    
    $request = new Dm\SingleSendMailRequest();     
    //新加坡或澳洲region需要设置SDK的版本，华东1（杭州）不需要设置。
    //$request->setVersion("2017-06-22");
    $num=5;
    $dtime="2018-03-01";
#    <span style=''font-size:${tagSize}%;color:$tagColor''>$tag </span>
    $messages ="<span style=\"color:blue;font-size: 24px;\">尊敬的诺禾vip客户:</span><br/>
                    <br>&nbsp;&nbsp;&nbsp;&nbsp;您有'$num' 台云服务器将于$dtime' 00:00:00正式到期，<br/>
                    <br>&nbsp;&nbsp;&nbsp;&nbsp;截至目前仅剩7天。未续费的云服务器实例到期后将停止服务，<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;到期后数据为您保留7天，逾期未续费实例与磁会被释放，数据不可恢复。为了保证您的服务正常运行，请您及时与客服联系续费。";
    $request->setAccountName("cloud@novocloud.cn");
    $request->setFromAlias("novocloud");
    $request->setAddressType(1);
    $request->setTagName("novogene");
    $request->setReplyToAddress("true");
    $request->setToAddress("lilinji@novogene.com,qiangyubiao@novogene.com");        
    $request->setSubject("云主机到期提醒");
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
?>
