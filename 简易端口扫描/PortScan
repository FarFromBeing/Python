import socket
import time

def scan_connect(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s=socket.socket()
		i=s.connect((ip,port))
		return True
	except Exception as e:
		#print("port %s is closed"%port)
		return
def scan_port():
	domain=input("URL||IP:")
	ip=socket.gethostbyname(domain)
	print('URL: %s <=> IP:'%domain,ip)
	iplists={22:'SSH',
	80:'HTTP',
	8080:'HTTP',
	443:'HTTPS',
	3389:'WindowsRemoteDesktop',
	1158:'Oracle_em',
	1521:'Oracle',
	1433:'SQLserver',
	3306:'Mysql',
	7001:'Weblogic',
	2100:'Oracle_XDB_FTP'}
	print("---------------------------------------------")
	print('Port             Status               Service')
	starttime=time.time()
	#print('start_time:',starttime)
	
	for key,value in iplists.items():
		#print('port:',key)
		#print('service:',value)
		res=scan_connect(ip,key)
		#print('res:',res)
		if res:
			print('{:<4d}{:>18s}{:>21s}'.format(key,'open',value))
	endtime=time.time()
	operationtime=endtime-starttime
	print("---------------------------------------------")
	print("Scanning takes  %.1f s"%operationtime)
if __name__ == '__main__':
	scan_port()
