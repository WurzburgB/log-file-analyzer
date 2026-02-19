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
    print("""
          Choose what you would like to do, input number\n
          1. Count all levels\n
          2. Count specific levels\n
          3. Filter logs
    """)
    task = input()
    if task == '1':
        print(count_logs_by_level(logs))
    elif task == '2':
        print("Please enter level to analyse:")
        level = input().upper()
        print(count_specific_level(logs, level))
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
        print(results)
    else:
        print("Invalid option selected.")

except Exception as e:
    print(e)


