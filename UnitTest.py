
from selenium import webdriver
from time import sleep
import csv
import codecs
import unittest
from itertools import islice
from ddt import ddt, data, file_data, unpack
import yagmail



driver = webdriver.Chrome()
woolworths_url = 'http://www.woolworths.com.au/'

def setUpModule():
	print('test module start >>>>>>>>>>>>>>>>>>')

def tearDownModule():
	print('test module end >>>>>>>>>>>>>>>>>>')


@ddt
class TestWoolworths(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = driver
		cls.base_url = woolworths_url
	#  the following is for csv file
		cls.test_data = [ ]
		with codecs.open('./data_file/woolworths_data.csv','r','utf_8_sig') as f:
			data = csv.reader(f)
			for line in islice(data, 1, None):
				cls.test_data.append(line)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def woolworths_search(self, search_key):
		self.driver.get(self.base_url)
		self.driver.maximize_window() 
		self.driver.find_element_by_xpath("//input[@id='headerSearch']").click()
		self.driver.find_element_by_xpath("//input[@id='headerSearch']").send_keys(search_key)
		self.driver.find_element_by_xpath("//button[@value='Search']").click()

		sleep(4)

	


	def test_search_oil(self):
		self.woolworths_search(self.test_data[0][1])

	def test_search_chocolate(self):
		self.woolworths_search(self.test_data[1][1])

	def test_search_biscuit(self):
		self.woolworths_search(self.test_data[2][1])

	# the following is for json file
	@file_data('./data_file/ddt_data_file.json')
	def test_search_JsonFile(self, search_key):
		print('new search through json file：',search_key)	
		self.woolworths_search(search_key)
		#self.assertEqual(self.driver.title, search_key+'_WoolWorthsSearch')

	# the following is for yaml file
	@file_data('./data_file/ddt_data_file.yaml')
	def test_search_YamlFile(self, case):
		search_key = case[0]['search_key']
		print('new search through yaml file：',search_key)
		self.woolworths_search(search_key)
		#self.assertEqual(self.driver.title, search_key+'_WoolWorthsSearch')



if __name__ == '__main__':
	unittest.main(verbosity=2)

