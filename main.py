import requests
import time
import datetime
import json
from requests.adapters import HTTPAdapter
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models
 
domain_id = '填写网址id'
SecretId='填写id'
SecretKey='填写密钥'
ip_old=""
 
def updateDNS( value ):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "dnspod.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = dnspod_client.DnspodClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ModifyRecordRequest()
        params1 = {
            "Domain": "adamaik.top",
            "SubDomain": "@",
            "RecordType": "A",
            "RecordLine": "默认",
            "Value": value,
            "RecordId": 1565168996
        }
        params2 = {
            "Domain": "adamaik.top",
            "SubDomain": "www",
            "RecordType": "A",
            "RecordLine": "默认",
            "Value": value,
            "RecordId": 1565168997
        }
        req.from_json_string(json.dumps(params1))
        # 返回的resp是一个ModifyRecordResponse的实例，与请求对象对应
        client.ModifyRecord(req)
        # 输出json格式的字符串回包
        print("更新@DNS成功")
        req.from_json_string(json.dumps(params2))
        client.ModifyRecord(req)
        print("更新wwwDNS成功")
        print('域名解析已更改为' + ip)
    except TencentCloudSDKException as err:
        print(err)
        print("操作失败")
 
 
def getIP():
    print("获取iping")
    url = "http://www.3322.org/dyndns/getip"
    IPInfo = requests.get(url)
    IPInfo.encoding = 'UTF-8'
    ip = IPInfo.text
    print("获取ip完毕")
    return ip
 




while True:
    ip = getIP().strip()
    if(ip_old!=ip):
        ip_old=ip
        print(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')+"  更改解析ing，可能会卡住")
        updateDNS(ip)
    else:
        print(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')+"  ip一致，无需更改")
    time.sleep(3600)
 
 
