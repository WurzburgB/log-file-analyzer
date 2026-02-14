#This will be used to read files
#This is not responsible for slicing the lines

def parse_logs(file):
    cleaned_lines = []

    with open(file, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                cleaned_lines.append(stripped)
    return cleaned_lines
