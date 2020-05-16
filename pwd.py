password = 'a12345' #密码
time = 4 #密码的尝试次数

while time > 0:
	pwd = input('请输入密码： ')
	time = time - 1
	
	if pwd == password:
		print('密码正确，登陆成功！')
		break

	else:
		print('密码错误')
		
		if time > 0:
			print('请重新尝试，你还有', time, '次机会')

