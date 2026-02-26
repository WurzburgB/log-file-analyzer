def detect_separator(line):

    separators =  ['|', ',', ';', '\t']
    for sep in separators:
        if sep in line:
            return sep
    return None


def parse_logs(filepath):
    parsed_logs = []

    with open(filepath, 'r', encoding="utf-8") as f:

        for raw_line in f:
            line = raw_line.strip()

            if not line:
                continue

            # Auto-detect separators
            if "|" in line:
                parts = line.split("|")
            elif "," in line and line.count(",") >= 3:
                parts = line.split(",")
            else:
                parts = line.split()

            # Clean whitespace
            parts = [p.strip() for p in parts]

            if len(parts) < 3:
                continue

            # Handle timestamp with milliseconds
            if len(parts) >= 4:
                date = parts[0]
                timestamp = parts[1]
                level = parts[2]
                message = " ".join(parts[3:])
            else:
                continue

            entry = {
                "date": date,
                "timestamp": timestamp,
                "level": level,
                "message": message
            }

            parsed_logs.append(entry)

    return parsed_logs