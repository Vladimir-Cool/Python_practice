from datetime import date, timedelta

year, month, day = map(int, input().split())
delta_days = int(input())
now_date = date(year, month, day)
then_date = now_date + timedelta(days=delta_days)

print(then_date.year, then_date.month, then_date.day)


