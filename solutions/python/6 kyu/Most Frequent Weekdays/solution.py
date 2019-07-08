from collections import Counter
from datetime import date, timedelta

WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def most_frequent_days(year):
    res = Counter(
        (date(year, 1, 1) + timedelta(d)).weekday()
        for d in range((date(year + 1, 1, 1) - date(year, 1, 1)).days)
    )
    m = max(res.values(), default=0)

    return [WEEK_DAYS[i] for i in res if res[i] == m]