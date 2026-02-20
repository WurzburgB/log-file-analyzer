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

print("Please enter the logs you would like to analyse:")
log = input()

try:
    logs = parse_logs(log)
except Exception as e:
    print(e)
    exit()

# Main program loop
while True:

    print("""
        Choose what you would like to do, input number

        1. Count all levels
        2. Count specific levels
        3. Filter logs
        4. Exit
    """)

    task = input()

    if task == '1':
        if count_logs_by_level(logs):
            print("Log Counts")
            print('-' * 14)
            for key, value in count_logs_by_level(logs).items():
                print(f"{key:<{9}} {value}")
        else:
            print("No results found.")


    elif task == '2':
        print("Please enter level to analyze:")
        level = input().upper()
        count = count_specific_level(logs, level)

        print(f"{level} Count")
        print('-' * 10)
        print(count)

    elif task == '3':
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

    elif task == '4':
        print("Program exited")
        break

    else:
        print("Invalid option selected.")
