def parse_logs(file):
    parsed_logs = []

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            # Detect separator automatically
            if "|" in line:
                parts = line.split("|")
            elif "," in line:
                parts = line.split(",")
            else:
                parts = line.split()

            if len(parts) >= 4:
                entry = {
                    'date': parts[0],
                    'timestamp': parts[1],
                    'level': parts[2],
                    'message': parts[3]
                }

                parsed_logs.append(entry)

    return parsed_logs