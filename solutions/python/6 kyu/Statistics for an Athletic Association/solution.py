from datetime import timedelta


def stat(strg):
    if not strg:
        return strg

    def f(td: timedelta):
        return "{:02d}|{:02d}|{:02d}".format(td.seconds // 3600, td.seconds // 60 % 60, td.seconds % 60)

    times = [*sorted(
        timedelta(**dict(zip(('hours', 'minutes', 'seconds'), (int(t) for t in res.strip().split('|')))))
        for res in strg.split(',')
    )]
    median = times[len(times) // 2] if len(times) % 2 else sum(times[len(times) // 2 - 1: len(times) // 2 + 1],
                                                               timedelta()) / 2
    return f'Range: {f(max(times) - min(times))} Average: {f(sum(times, timedelta()) / len(times))} ' + \
           f'Median: {f(median)}'