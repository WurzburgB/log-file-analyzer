"""
Counts the number of log entries per level.
Args:
    logs (list[dict]): Parsed log entries.

Returns:
    dict: A dictionary where keys are log levels
          and values are occurrence counts.
"""

def count_logs_by_level(logs):
    counts = {}
    if not isinstance(logs, list):
        raise TypeError("logs must be a list of dictionaries")

    for log in logs:
        level = log["level"]
        if level not in counts:
            counts[level] = 1
        else:
            counts[level] += 1
    return counts

def filter_logs(logs, date=None, level=None, message_contains=None):
    filtered_list = []
    if not isinstance(logs, list):
        raise TypeError("logs must be a list of dictionaries")

    for log in logs:
        if date is not None and date != log["date"]:
            continue
        if level is not None and level.upper() != log["level"].upper():
            continue
        if message_contains is not None and message_contains.lower() not in log["message"].lower():
            continue
        filtered_list.append(log)
    return filtered_list


def count_specific_level(logs, level):
    counts = count_logs_by_level(logs)
    return counts.get(level, 0)
