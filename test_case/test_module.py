
class Mail(object):

	def __int__(self,driver):
	  self.driver = driver


	def login(self,username,password):
	  login_frame = self.driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
	  self.driver.switch_to_frame(login_frame)
	  self.driver.find_element_by_name('email').clear()
	  self.driver.find_element_by_name('email').send_keys('username')
	  self.driver.find_element_by_name('password').clear
	  self.driver.find_element_by_name('password').send_keys('password')
	  sleep(3)
	  self.driver.find_element_by_id('dologin').click()

	def logout(self):
		#self.driver.find_element_by_link_text('exit').click()
	  self.driver.quit()

