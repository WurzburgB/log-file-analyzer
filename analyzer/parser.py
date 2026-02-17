"""This module reads a log file and converts
each valid line into a structured dictionary containing
date, timestamp, level, and message.
"""
def parse_logs(file):
    cleaned_lines = []
    parsed_logs = []
    # Read file and remove empty lines
    with open(file, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                cleaned_lines.append(stripped)
    # Convert each valid line into a structured log entry
    for line in cleaned_lines:
        # Split line into components: date, time, level, message parts
        parts = line.split()
        if len(parts) >= 3:
            entry = {
                'date': parts[0],
                'timestamp': parts[1],
                'level': parts[2],
                'message': " ".join(parts[3:])
                    }
            parsed_logs.append(entry)
    return parsed_logs
