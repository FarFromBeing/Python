import requests
import time
from bs4 import BeautifulSoup


#抓取原本网页
def get_html(url):
	try:

		r=requests.get(url,timeout=20)
		#对http请求码进行抛出，200响应就是none
		r.raise_for_status()
		r.encoding='utf-8'
		return r.text
	except:
		return "Error!!!!"

#分析网页，整理信息，保存在list中
def get_content(url):
	#初始化一个列表来存储一条一条爬取的信息
	comments=[]
	#需要的网页保存在本地
	html=get_html(url)
	#生成soup对象来操作
	soup=BeautifulSoup(html,'lxml')
	#找到所有<li class="j_ehread_list clearfix">的
	#通过循环找到每个帖子需要的信息
	liTags=soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
	for li in liTags:
	#用一个字典嘞存储文章信息。以名字开头，具体内容结尾
		comment={}
		try:
			comment['title']=li.find('a',attrs={'class':'j_th_tit'}).text.strip()
			print('-------------打印头部：'+comment['title'])
			comment['link']="http://tieba.baidu.com/"+li.find('a',attrs={'class':'j_th_tit'})['href']
			print('---------------link:'+comment['link'])
			comment['author_name']=li.find('span',attrs={'class':'frs-author-name-wrap'}).text.strip()
			print('*****************名字：'+comment['author_name'])
			comment['time']=li.find('span',attrs={'class':'pull-right is_show_create_time'}).text.strip()
			print('#################时间：'+comment['time'])
			comment['replynum']=li.find('span',attrs={'class':"threadlist_rep_num center_text"}).text.strip()
			print('^^^^^^^^^^^^^^^^^^回复：'+comment['replynum'])
			comments.append(comment)
		except:
			print("每条信息的各个元素有点问题！！！！！")
	return comments

#保存爬取的信息于本地文件
def Out2File(dict):
	with open('res.text','a+')as f:
		for comment in dict:
			f.write('标题：{} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量：{} \n'.format(comment['title'],comment['link'],comment['author_name'],comment['time'],comment['replynum']))
		print('当前网页成功保存于本地res.txt中！')


def main(base_url,deep):
	
	url_list=[]
	#根据贴吧翻页机制，设置增加的&pn= 即可实现每页的跳转爬取
	for i in range(0,deep):
		url_list.append(base_url+'&pn'+str(50*i))
	print('所有网页已经下载本地！开始分析.....')
	
	for url in url_list:
		content=get_content(url)
		Out2File(content)
	print('所有信息保存完毕！！1')
base_url= 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
deep=3

if __name__=='__main__':
	main(base_url,deep)
