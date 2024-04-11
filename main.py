# ValueError: unconverted data remains in Python

from datetime import datetime


dt = '2024-09-24 08:30:00'

date_1 = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
print(date_1)  # 👉️ 2024-09-24 08:30:00
