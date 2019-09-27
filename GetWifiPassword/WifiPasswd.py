import os
import re

'''
最新：2018/11/13
修复无法打开一些wifi配置的问题
'''

class ToHtml(object):
	"""docstring for ToHtml"""
	def __init__(self, arg, filepoint):
		super(ToHtml, self).__init__()
		self.text_list = arg
		self.fp = filepoint

	def header(self):
		self.fp.write("<!DOCTYPE html>")
		self.fp.write('<html lang="zh-cn">')
		self.fp.write('<meta charset="gbk">')
		self.fp.write("<head></head>")
		self.fp.write("<body>")
		self.fp.write('<table border="1" cellpadding="10" cellspacing="0" style="margin:auto;width:500px">')
		self.fp.write("<tbody>")
	def body(self):

		self.fp.write("<tr><th>wifi名称</th><th>密码</th></tr>")
		for l in self.text_list:
			self.fp.write("<tr><td>{}</td><td>{}</td></tr>".format(l[0],l[1]))

	def footer(self):
		self.fp.write("</tbody>")
		self.fp.write("</table>")
		self.fp.write("</body>")
		self.fp.write("</html>")



def getWifiList():

	get_wifi = "netsh wlan show profiles "
	wifi_name_list = []
	
	with os.popen(get_wifi) as gw:

		for line in gw:
			
			line = line.strip('\n').rstrip(":")
			if ":" in line:
				wifi_name = line.split(":")[1].lstrip()
				if wifi_name:
					wifi_name_list.append(wifi_name)
	
	return wifi_name_list


def getUserPwd(detail):

	passwd = "no/other"
	user = ''

	for line in detail:
		try:
			if "名称" in line and "SSID" not in line:
				user = line.split(":")[1].lstrip()
			if "关键内容" in line:
				passwd = line.split(":")[1].strip()
		except:
			pass
			
	return (user, passwd)


def getNamePwd(wifi_name_list):
	user_passwd = []

	for wifi_name in wifi_name_list:
		print(wifi_name)
		get_wifi_detail_cmd = 'netsh wlan show profiles name="{}" key=clear'.format(wifi_name)

		# 获取wifi名称以及密码
		with os.popen(get_wifi_detail_cmd) as gwd:
			user_passwd.append(getUserPwd(gwd))

	return user_passwd


def main():
	wifi_name_list = getWifiList()

	name_pwd = getNamePwd(wifi_name_list)
	with open("WiFiPassword.html",'w') as f:
		th = ToHtml(name_pwd,f)
		th.header()
		th.body()
		th.footer()


if __name__ == '__main__':
	main()