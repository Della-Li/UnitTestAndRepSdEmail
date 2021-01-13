import time
import unittest
import yagmail
from HTMLTestRunner import HTMLTestRunner

#clone HTMLTestRunner from  https://github.com/defnngj/HTMLTestRunner and put HTMLTestRunner.py under python directory , such as 
#C:\Python37\Lib\


#email passord ：the first letter is upper case 
#access to the email server
def send_mail(report):
	yag = yagmail.SMTP(user='senderlyf@126.com', 
		password='XLWMZIOCIZGQGZPP',
		host='smtp.126.com')
	subject = 'autumation testing report'
	contents = 'For contents ,please check the attachment'
	yag.send(['receiverlyf@126.com','senderlyf@126.com'], subject, contents, report)
	print('email has sent out')

#email context
if __name__ == '__main__':
	test_dir = './test_case'
	suit = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

	now_time = time.strftime('%Y-%m-%d %H_%M_%S')
	print(now_time)
	html_report = './test_report/' + now_time + 'result.html'
	fp = open(html_report, 'wb')

	runner = HTMLTestRunner(stream=fp, title='Search testing report', description='testing environment： Windows 10, Browser Chrome')
	runner.run(suit)
	fp.close()

	send_mail(html_report)

