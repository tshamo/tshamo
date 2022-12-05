import datetime
import pytz
from pytz import timezone

utc=pytz.UTC
eastern = timezone('US/Eastern')

tday = datetime.date.today()
est_now = datetime.datetime.now(tz=eastern)
utc_now = datetime.datetime.now(tz=utc)

print(tday)
print(f'EST {est_now}')
print(f'UTC {utc_now}')
