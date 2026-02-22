"""
Counts the number of log entries per level.
Args:
    logs (list[dict]): Parsed log entries.

Returns:
    dict: A dictionary where keys are log levels
          and values are occurrence counts.
"""
def count_logs_by_level(logs):
    if not isinstance(logs, list):
        raise TypeError("logs must be a list of dictionaries")

    counts = {}

    for log in logs:
        if not isinstance(log, dict):
            continue

        level = log.get("level")
        if not level:
            continue

        counts[level] = counts.get(level, 0) + 1

    return counts


def filter_logs(logs, date=None, level=None, message_contains=None):
    if not isinstance(logs, list):
        raise TypeError("logs must be a list of dictionaries")

    filtered_list = []

    for log in logs:
        if not isinstance(log, dict):
            continue

        log_date = log.get("date")
        log_level = log.get("level")
        log_message = log.get("message")

        # Filter by date
        if date is not None and log_date != date:
            continue

        # Filter by level (case insensitive)
        if level is not None:
            if not log_level or log_level.upper() != level.upper():
                continue

        # Filter by message content (case insensitive)
        if message_contains is not None:
            if not log_message or message_contains.lower() not in log_message.lower():
                continue

        filtered_list.append(log)

    return filtered_list


def count_specific_level(logs, level):
    counts = count_logs_by_level(logs)
    return counts.get(level, 0)