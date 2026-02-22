"""
CLI entry point for the Log Analyzer application.

Workflow:
1. Prompt the user for a log file path.
2. Parse the log file into structured data.
3. Let the user choose an action:
   - Count all log levels
   - Count a specific log level
   - Filter logs by date, level, and/or message content
4. Display the results.

Any parsing or runtime errors are handled gracefully.
"""

from analyzer.analyzer import count_logs_by_level, count_specific_level, filter_logs
from analyzer.parser import parse_logs

logs = None

# Main program loop
while True:

    print("""
        Choose what you would like to do, input number
        
        1. Load log file
        2. Count all levels
        3. Count specific levels
        4. Filter logs
        5. Exit
    """)

    task = input()

    if task == '5':
        print("Program exited")
        break

    elif task == '1':
        print('Enter valid file path')
        path = input()

        try:
            logs = parse_logs(path)
            if not logs:
                print("No valid logs found.")
                logs = None
            else:
                print('Logs loaded successfully')
        except Exception as e:
            print('Error loading file:', e)
            logs = None

    elif task in ['2', '3', '4'] and not logs:
        print("No logs loaded")
        continue

    elif task == '2':
        counts = count_logs_by_level(logs)
        if counts:
            print("Log Counts")
            print('-' * 14)
            for key, value in counts.items():
                print(f"{key:<{9}} {value}")
        else:
            print("No results found.")


    elif task == '3':
        print("Please enter level to analyze:")
        level = input().upper()
        count = count_specific_level(logs, level)
        if count > 0:
            print(f"{level} Count")
            print('-' * 10)
            print(count)
        else:
            print("No results found.")

    elif task == '4':
        print("Leave blank if you dont want to filter by that field.")

        print("Enter date to filter by (YYYY-MM-DD):")
        date = input().strip()
        if date == '':
            date = None

        print("Enter level to filter by:")
        level = input().strip().upper()
        if level == '':
            level = None

        print("Enter text the message should contain:")
        message = input().strip()
        if message == '':
            message = None

        results = filter_logs(logs, level=level, date=date, message_contains=message)

        if results:
            # Header
            print('Results'.center(60))
            print('-' * 60)
            print(f"{'Date':<{12}} {'Time':<{14}} {'Level':<{10}} {'Message'}")
            print('-' * 60)
            # Results
            for line in results:
                print(f"{line['date']:<{12}} {line['timestamp']:<{14}} {line['level']:<{10}} {line['message']}")
        else:
            print('No results')

    else:
        print("Invalid option selected.")
