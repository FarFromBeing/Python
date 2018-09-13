
import socket

#------send--------
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
#------receive------
buffer=[]
while True:
	r=s.recv(1024)
	if r:
		buffer.append(r)
	else:
		break
	#each 1024 bytes join ''
data=b''.join(buffer)
s.close()
#-------split--------
#这里是分割1次，有换行（\n、\r）都会转换为\n
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#-------save--------
with open('sina.html','wb') as f:
	f.write(html)
'''
Q:
HTTP/1.1 302 Moved Temporarily

Server: nginx

Date: Thu, 13 Sep 2018 15:27:39 GMT

Content-Type: text/html

Content-Length: 154

Connection: close

Location: https://www.sina.com.cn/

X-Via-CDN: f=edge,s=ctc.chengdu.ha2ts4.27.nb.sinaedge.com,c=110.184.161.129;

X-Via-Edge: 153685245918681a1b86e3850d3de083ea7d3
'''