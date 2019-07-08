def format_duration(seconds):
    if not seconds:
        return "now"

    sec, seconds = seconds % 60, seconds // 60
    minutes, seconds = seconds % 60, seconds // 60
    hours, seconds = seconds % 24, seconds // 24
    days, seconds = seconds % 365, seconds // 365
    years = seconds

    values = [sec, minutes, hours, days, years]
    str_values = ["{} {}{}".format(value, title, "" if value == 1 else "s")
                  for value, title in reversed(zip(values, ["second", "minute", "hour", "day", "year"])) if value]

    return str_values[0] if len(str_values) == 1 else ", ".join(str_values[:-1]) + " and " + str_values[-1]