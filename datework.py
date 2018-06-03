from datetime import date, timedelta
import calendar
#import locale
#dt = date(2018, 1, 1)
today = date.today()
first = today.replace(day=1)
last_month = first - timedelta(days=1)
day = timedelta(days=1)
#month_ago = calendar.month_abbr[today.month - 1]
#delta_month = timedelta(month=1)

days_in_month = calendar.monthrange(last_month.year, last_month.month)[1]
day_month_ago = today - timedelta(days=days_in_month)  # 14.06 - 31 = 14.05
#try:
	#day_month_ago = dt.replace(dt.year, dt.month - 1, dt.day)
#except ValueError:
    #day_month_ago = dt.replace(dt.year - 1, dt.month, dt.day)
yesterday = today - day
#day_month_ago = today.replace(today.year, today.month - 1, today.day)
#date_month = date_today - delta_month
print(today)
print(yesterday)
print(day_month_ago)
#print(month)
#print(date_month)

