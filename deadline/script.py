from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests ,json, uuid, arrow
from deadline.models import *

path = '../../chromedriver'
driver = webdriver.Chrome(path)
url = 'https://yocket.in/university-application-deadlines?page='
a = []
for page in range(61,555):
	try:
		driver.get(url+str(page))
		time.sleep(10)
		soup = BeautifulSoup(driver.page_source)
		for tag in soup.find_all('tr'):
			x = str(tag.text).splitlines()
			try:
				a.append({'college':x[1],'subject':x[2],'type':x[3],'deadline':x[4]})
				c = None 
				try:
					c = College.objects.get(college_name = x[1])
				except Exception, e:
					c = College(college_name = x[1],deadline = x[4],refid = uuid.uuid1().hex,created = str(arrow.now().timestamp),updated = str(arrow.now().timestamp))
					c.save()
				try:
					Subjects.objects.get(college = c,subject_name = x[2],deadline_type = x[3])
				except Exception, e:
					s = Subjects(refid = uuid.uuid1().hex,deadline_type = x[3],college = c,subject_name = x[2],subject_deadline = x[4],created = str(arrow.now().timestamp),updated = str(arrow.now().timestamp))
					s.save()
			except Exception as e:
				print e.message
		if page%8 == 0:
			driver.quit()
			time.sleep(5)
			driver = webdriver.Chrome(path)
			time.sleep(5)
	except Exception as e:
		print e.message
		pass
	print a
