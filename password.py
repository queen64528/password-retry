i = 1
while i < 4 :
	password = input('請輸入密碼：')
	if password == 'a123456':
		print ('登入成功')
		break
	else :
		print ('密碼錯誤！還有', 3-i , '次機會')
		i = i + 1

