from datetime import datetime, timedelta

today = datetime.today()

yesterday = today - timedelta(1)

tomorrow = today + timedelta(1)

print("Today ", today.strftime("%Y-%m-%d"))
print("Tomorrow ", tomorrow.strftime("%Y-%m-%d"))
print("Yesterday ", yesterday.strftime("%Y-%m-%d"))
