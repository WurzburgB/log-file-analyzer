from analyzer.analyzer import count_log
from analyzer.parser import parse_logs

logs = parse_logs("data/sample.log")
print(logs)
print(count_log(logs))