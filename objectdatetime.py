from datetime import datetime

try:
	user_answer = input('Введи нужную дату ')
	user_date_time = datetime.strptime(user_answer, '%d %m %Y')
		#user_answer = '01/01/17 12:10:03.234567'
		#user_date_time = datetime.strptime(user_answer, '%d/%m/%y %H:%M:%S.%f')
	print(user_date_time)
except ValueError:
	print('Как-то непонятно написал.')
	while True:
		try:
			user_answer = input('Введи, пожалуйста, дату в формате "хх хх хххх" ')
			user_date_time = datetime.strptime(user_answer, '%d %m %Y')
			print('Вот теперь понятно=)')
			print(user_date_time)
			break
		except ValueError:
			print('Совсем запутался.')
		

