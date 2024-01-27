from datetime import datetime
import pytz

# 创建表示所需日期和时间的 datetime 对象
pub_date_datetime = datetime.strptime("2024-01-19", "%Y-%m-%d")
print(pub_date_datetime)
# 将 datetime 对象转换为毫秒级时间戳
timestamp_milliseconds = 1598431770000

print(timestamp_milliseconds)

# 将时间戳转换回 datetime 对象（使用指定时区）
tz = pytz.timezone('Asia/Shanghai')  # 请根据实际情况替换时区
pub_date_datetime_converted = datetime.fromtimestamp(timestamp_milliseconds / 1000.0, tz=tz)

# 将转换后的 datetime 对象格式化为字符串
formatted_date = pub_date_datetime_converted.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_date)
