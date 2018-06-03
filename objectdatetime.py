from datetime import datetime

user_answer = '01/01/17 12:10:03.234567'
user_date_time = datetime.strptime(user_answer, '%d/%m/%y %H:%M:%S.%f')
print(user_date_time)