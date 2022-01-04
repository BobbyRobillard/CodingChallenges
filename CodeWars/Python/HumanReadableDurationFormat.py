def format_duration(seconds):
    years = seconds // (60*60*365*24)
    seconds %= (60*60*24*365)

    days = seconds // (60*60*24)
    seconds %= (60*60*24)

    hours = seconds // (60*60)
    seconds %= (60*60)

    minutes = seconds // 60
    seconds %= 60

    seconds_text = ("{} second".format(seconds) + ("s" if seconds > 1 else "")) if seconds > 0 else ""

    minutes_text = ("{} minute".format(minutes) + ("s" if minutes > 1 else "")) if minutes > 0 else ""
    minutes_text += (" and " if seconds_text else "") if minutes_text else ""

    hours_text = ("{} hour".format(hours) + ("s" if hours > 1 else "")) if hours > 0 else ""
    hours_text += (", " if minutes_text else "") if hours_text else ""

    days_text = ("{} day".format(days) + ("s" if days > 1 else "")) if days > 0 else ""
    days_text += (", " if hours_text else "") if days_text else ""

    years_text = ("{} year".format(years) + ("s" if years > 1 else "")) if years > 0 else ""
    years_text += (", " if days_text else "") if years else ""

    return years_text + days_text + hours_text + minutes_text + seconds_text or "now"
