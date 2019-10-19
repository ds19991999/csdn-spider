#!/usr/bin/env python
# coding: utf-8

import os, time, re
import requests
import threading
import logging
from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from tomd import Tomd


def result_file(folder_name, file_name):
	folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "articles", folder_name)
	if not os.path.exists(folder):
		os.makedirs(folder)
		path = os.path.join(folder, file_name)
		file = open(path,"w")
		file.close()
	else:
		path = os.path.join(folder, file_name)
	return path


def get_headers(cookie_path:str):
	cookies = {}
	with open(cookie_path, "r", encoding="utf-8") as f:
		cookie_list = f.readlines()
	for line in cookie_list:
		cookie = line.split(":")
		cookies[cookie[0]] = str(cookie[1]).strip()
	return cookies


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
		url = ""
		if index and self.UnVisitedList:
			url = self.UnVisitedList[index]
			del self.UnVisitedList[:index]
		elif self.UnVisitedList:
			url = self.UnVisitedList.pop()
		return url
	
	def getUnVisitedListLength(self):
		return len(self.UnVisitedList)


class Article(object):
	def __init__(self):
		self.options = webdriver.ChromeOptions()
		self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
		self.options.add_argument('headless')
		self.browser = webdriver.Chrome(options=self.options)
		# 设置全局智能等待时间
		self.browser.implicitly_wait(30)
	
	def get_content(self, url):
		self.browser.get(url)
		try:
			self.browser.find_element_by_xpath('//a[@class="btn-readmore"]').click()
		except Exception:
			pass
		content = self.browser.find_element_by_xpath('//div[@id="content_views"]').get_attribute("innerHTML")
		return content
	
	def get_md(self, url):
		"""
		转换为markdown格式
		"""
		content = self.get_content(url)
		soup = BeautifulSoup(content, 'lxml')
		# 删除注释
		for useless_tag in soup(text=lambda text: isinstance(text, Comment)):
			useless_tag.extract()
		# 删除无用标签
		tags = ["svg", "ul", ".hljs-button.signin"]
		delete_ele(soup, tags)
		# 删除标签属性
		attrs = ["class", "name", "id", "onclick", "style", "data-token", "rel"]
		delete_ele_attr(soup,attrs)
		# 删除空白标签
		eles_except = ["img", "br", "hr"]
		delete_blank_ele(soup, eles_except)
		# 转换为markdown
		md = Tomd(str(soup)).markdown
		return md


class CSDN(object):
	def __init__(self, cookie_path):
		self.headers = get_headers(cookie_path)
		self.TaskQueue = TaskQueue()

	def get_articles(self, username:str):
		"""获取文章标题和链接"""
		num = 0
		while True:
			num += 1
			url = u'https://blog.csdn.net/' + username + '/article/list/' + str(num)
			response = requests.get(url=url, headers=self.headers)
			html = response.text
			soup = BeautifulSoup(html, "html.parser")
			articles = soup.find_all('div', attrs={"class":"article-item-box csdn-tracking-statistics"})
			if len(articles) > 0:
				for article in articles:
					article_title = article.a.text.strip().replace('        ','：')
					article_href = article.a['href']
					yield article_title,article_href
			else:
				break
	
	def write_articals(self, username:str):
		"""将博文写入本地"""
		print("[++] 正在爬取 {} 的博文......".format(username))
		artical = Article()
		reademe_path = result_file(username,file_name="README.md")
		with open(reademe_path,'w', encoding='utf-8') as reademe_file:
			i = 1
			readme_head = "# " + username + " 的博文\n"
			reademe_file.write(readme_head)
			for article_title,article_href in self.get_articles(username):
				print("[++++] {}. 正在处理URL：{}".format(str(i), article_href))
				text = str(i) + '. [' + article_title + ']('+ article_href +')\n'
				reademe_file.write(text)
				file_name = str(i) + "." + re.sub(r'[\/:：*?"<>|]','-', article_title) + ".md"
				artical_path = result_file(folder_name=username, file_name=file_name)
				md_content = artical.get_md(article_href)
				md_head = "# " + str(i) + "." + article_title + "\n"
				md = md_head + md_content
				with open(artical_path, "w", encoding="utf-8") as artical_file:
					artical_file.write(md)
				i += 1
				time.sleep(2)

	def spider(self):
		"""将爬取到的文章保存到本地"""
		while True:
			if self.TaskQueue.getUnVisitedListLength():
				username = self.TaskQueue.PopUnVisitedList()
				self.write_articals(username)
	
	def check_user(self, user_path:str):
		with open(user_path, 'r', encoding='utf-8') as f:
			users = f.readlines()
		for user in users:
			self.TaskQueue.InsertUnVisitedList(user.strip())

	def run(self, user_path):
		UserThread = threading.Thread(target=self.check_user, args=(user_path,))
		SpiderThread = threading.Thread(target=self.spider, args=())
		UserThread.start()
		SpiderThread.start()
		UserThread.join()
		SpiderThread.join()


def main():
	user_path = 'username.txt'
	csdn = CSDN('cookie.txt')
	csdn.run(user_path)


if __name__ == "__main__":
	main()

