def format_duration(seconds):
    years = seconds // (60 * 60 * 365 * 24)
    seconds %= 60 * 60 * 24 * 365

    days = seconds // (60 * 60 * 24)
    seconds %= 60 * 60 * 24

    hours = seconds // (60 * 60)
    seconds %= 60 * 60

    minutes = seconds // 60
    seconds %= 60

    seconds_text = (
        ("{} second".format(seconds) + ("s" if seconds > 1 else ""))
        if seconds > 0
        else ""
    )
    minutes_text = (
        ("{} minute".format(minutes) + ("s" if minutes > 1 else ""))
        if minutes > 0
        else ""
    )
    hours_text = (
        ("{} hour".format(hours) + ("s" if hours > 1 else "")) if hours > 0 else ""
    )
    days_text = ("{} day".format(days) + ("s" if days > 1 else "")) if days > 0 else ""
    years_text = (
        ("{} year".format(years) + ("s" if years > 1 else "")) if years > 0 else ""
    )

    texts = [years_text, days_text, hours_text, minutes_text, seconds_text]
    texts = list(filter(("").__ne__, texts))

    if len(texts) == 0:
        return "now"
    if len(texts) == 1:
        return texts[0]
    if len(texts) == 2:
        return "{0} and {1}".format(texts[0], texts[1])
    if len(texts) >= 3:
        return "".join(item + ", " for item in texts[:-2]) + "{0} and {1}".format(
            texts[-2], texts[-1]
        )
