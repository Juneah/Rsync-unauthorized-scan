import os
import time
import sys

def shell_exec(cmd):
    data=[]
    result = os.popen(cmd)
    res = result.read()
    for line in res.splitlines():
         data.append(str(line))
    return ''.join(data)
 
def rsync(ip,timeout=1.5,port=873):
	cm='timeout {} rsync rsync://{}:{}'.format(timeout,ip.strip(),port)
	os.system('clear')
	print(ip.strip())
	data=shell_exec(cm)
	if data!='':
		f=open('rsync_ok.txt','a+')
		port=str(port).strip()
		ok=f"{ip.strip()}:{port}\n"
		f.write(ok)
		f.close()
def Run():
	f=open('ip.txt')
	ip=True
	while ip:
		ip=f.readline()
		time.sleep(0.1)
		if ('&' in ip ) or ('|' in ip) or (';' in ip):
			continue
		if ':' in ip.strip():
			tip,tport=ip.split(':')
			rsync(ip=tip,port=tport)
		else:
			rsync(ip=ip)

if __name__=='__main__':
	if 'linux' not in sys.platform:
		exit('The operating system is not Linux!')
	Run()









