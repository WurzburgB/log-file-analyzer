"""
Counts the number of log entries per level.
Args:
    logs (list[dict]): Parsed log entries.

Returns:
    dict: A dictionary where keys are log levels
          and values are occurrence counts.
"""

def count_log(logs):
    counts = {}
    if logs is None:
        raise TypeError("logs must be a list of dictionaries")

    for log in logs:
        level = log["level"]
        if level not in counts:
            counts[level] = 1
        else:
            counts[level] += 1
    return counts
