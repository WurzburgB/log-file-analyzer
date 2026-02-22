"""
Reads a log file and converts each valid line into a dictionary.

Each log entry contains:
    - date
    - timestamp
    - level
    - message

Supports multiple separators:
    |  ,  ;  or spaces
"""

def detect_separator(line):
    """Detect the separator used in a log line."""
    if "|" in line:
        return "|"
    elif "," in line:
        return ","
    elif ";" in line:
        return ";"
    else:
        return None  # Assume space separated


def parse_logs(file):
    parsed_logs = []

    # Read uploaded file
    for raw_line in file:
        line = raw_line.decode("utf-8").strip()

        if not line:
            continue

        separator = detect_separator(line)

        # Split based on detected separator
        if separator:
            parts = [p.strip() for p in line.split(separator)]
        else:
            parts = line.split()

        # Must have at least date, time, level
        if len(parts) >= 3:
            entry = {
                "date": parts[0],
                "timestamp": parts[1],
                "level": parts[2],
                "message": " ".join(parts[3:])
            }

            parsed_logs.append(entry)

    return parsed_logs