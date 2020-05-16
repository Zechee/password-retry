password = 'a12345' #密码
time = 4 #密码的尝试次数

while True:
	pwd = input('请输入密码： ')
	if pwd == password:
		print('密码正确，登陆成功！')
		break

	else:
		time = time - 1
		if time < 1:
			print('你已经没有尝试机会了！')
			break

		else:
			print('请重新尝试，你还有', time, '次机会')
