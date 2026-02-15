"""This module reads a log file and converts
each valid line into a structured dictionary containing
date, timestamp, level, and message.
"""

def parse_logs(file):
    cleaned_lines = []
    parsed_logs = []
    # Phase 1: Read and clean raw log lines
    with open(file, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                cleaned_lines.append(stripped)
    # Phase 2: Parse cleaned lines into structured log dictionaries
    for line in cleaned_lines:
        # Split line into components: date, time, level, message parts
        parts = line.split(" ")
        if len(parts) >= 3:
            entry = {
                'Date': parts[0],
                'Timestamp': parts[1],
                'Level': parts[2],
                'Message': " ".join(parts[3:])
                    }
            parsed_logs.append(entry)
    return parsed_logs
