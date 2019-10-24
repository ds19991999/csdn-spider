#!/usr/bin/env python
# coding: utf-8

import os, time, re
import requests
import threading
from bs4 import BeautifulSoup, Comment
from .tomd import Tomd


def result_file(folder_name, file_name, article_name):
	folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../"+article_name, folder_name)
	if not os.path.exists(folder):
		os.makedirs(folder)
		path = os.path.join(folder, file_name)
		file = open(path,"w")
		file.close()
	else:
		path = os.path.join(folder, file_name)
	return path


def delete_ele(soup:BeautifulSoup, tags:list):
	for ele in tags:
		for useless_tag in soup.select(ele):
			useless_tag.decompose()


def delete_ele_attr(soup:BeautifulSoup, attrs:list):
	for attr in attrs:
		for useless_attr in soup.find_all():
			del useless_attr[attr]


def delete_blank_ele(soup:BeautifulSoup, eles_except:list):
	for useless_attr in soup.find_all():
		try:
			if useless_attr.name not in eles_except and useless_attr.text == "":
				useless_attr.decompose()
		except Exception:
			pass


class TaskQueue(object):
	def __init__(self):
		self.VisitedList = []
		self.UnVisitedList = []
	
	def getVisitedList(self):
		return self.VisitedList

	def getUnVisitedList(self):
		return self.UnVisitedList
	
	def InsertVisitedList(self, url):
		if url not in self.VisitedList:
			self.VisitedList.append(url)
	
	def InsertUnVisitedList(self, url):
		if url not in self.UnVisitedList:
			self.UnVisitedList.append(url)
	
	def RemoveVisitedList(self, url):
		self.VisitedList.remove(url)

	def PopUnVisitedList(self,index=0):
		url = []
		if index and self.UnVisitedList:
			url = self.UnVisitedList[index]
			del self.UnVisitedList[:index]
		elif self.UnVisitedList:
			url = self.UnVisitedList.pop()
		return url
	
	def getUnVisitedListLength(self):
		return len(self.UnVisitedList)


class CSDN(object):
	def __init__(self, username, article__folder_name):
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
		}
		self.username = username
		self.TaskQueue = TaskQueue()
		self.article__folder_name = article__folder_name
		self.url_num = 1

	def start(self):
		"""获取文章标题和链接"""
		num = 0
		while True:
			num += 1
			url = u'https://blog.csdn.net/' + self.username + '/article/list/' + str(num)
			response = requests.get(url=url, headers=self.headers)
			html = response.text
			soup = BeautifulSoup(html, "html.parser")
			articles = soup.find_all('div', attrs={"class":"article-item-box csdn-tracking-statistics"})
			if len(articles) > 0:
				for article in articles:
					article_title = article.a.text.strip().replace('        ',': ')
					article_href = article.a['href']
					self.TaskQueue.InsertUnVisitedList([article_title, article_href])
			else:
				break
	
	def get_md(self, url):
		"""爬取文章"""
		response = requests.get(url=url, headers=self.headers)
		html = response.text
		soup = BeautifulSoup(html, 'lxml')
		content = soup.select_one("#content_views")
		# 删除注释
		for useless_tag in content(text=lambda text: isinstance(text, Comment)):
			useless_tag.extract()
		# 删除无用标签
		tags = ["svg", "ul", ".hljs-button.signin"]
		delete_ele(content, tags)
		# 删除标签属性
		attrs = ["class", "name", "id", "onclick", "style", "data-token", "rel"]
		delete_ele_attr(content,attrs)
		# 删除空白标签
		eles_except = ["img", "br", "hr"]
		delete_blank_ele(content, eles_except)
		# 转换为markdown
		md = Tomd(str(content)).markdown
		return md


	def write_readme(self):
		"""生成readme"""
		print("[++] 正在爬取 {} 的博文 ......".format(self.username))
		reademe_path = result_file(self.username,file_name="README.md",article_name=self.article__folder_name)
		with open(reademe_path,'w', encoding='utf-8') as reademe_file:
			readme_head = "# " + self.username + " 的博文\n"
			reademe_file.write(readme_head)
			for [article_title,article_href] in self.TaskQueue.UnVisitedList[::-1]:
					text = str(self.url_num) + '. [' + article_title + ']('+ article_href +')\n'
					reademe_file.write(text)
					self.url_num += 1
		self.url_num = 1
	
	def spider(self):
		"""爬取所有文章"""
		try:
			while True:
				[article_title,article_href] = self.TaskQueue.PopUnVisitedList()
				try:
					print("[++++] 正在处理URL：{}".format(article_href))
					file_name = re.sub(r'[\/:：*?"<>|]','-', article_title) + ".md"
					artical_path = result_file(folder_name=self.username, file_name=file_name, article_name=self.article__folder_name)
					md_head = "# " + article_title + "\n"
					md = md_head + self.get_md(article_href)
					with open(artical_path, "w", encoding="utf-8") as artical_file:
						artical_file.write(md)
				except Exception:
					print("[----] 处理URL异常：{}".format(article_href))
				self.url_num += 1
		except Exception:
			pass
	
	def muti_spider(self, thread_num):
		while True:
			if self.TaskQueue.getUnVisitedListLength() < 1:
				break
			thread_list = []
			for i in range(thread_num):
				th = threading.Thread(target=self.spider)
				thread_list.append(th)
			for th in thread_list:
				th.start()
			


def run(username: str = "ds19991999", thread_num: int = 10, article__folder_name: str = "articles"):
	if not os.path.exists(article__folder_name):
		os.makedirs(article__folder_name)
	csdn = CSDN(username,article__folder_name)
	csdn.start()
	csdn.write_readme()
	csdn.muti_spider(thread_num)


if __name__ == "__main__":
	run("ds19991999", 10, "articles")

