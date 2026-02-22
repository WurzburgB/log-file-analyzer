from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['logfile']

    if not file:
        return 'No file uploaded'

    contents = file.read().decode('utf-8')
    lines = contents.split()

    parsed_logs = []
    for line in lines:
        parts = line.split()
        if len(parts) > 4:
            log_entry = {
                "date": parts[0].strip(),
                "time": parts[1].strip(),
                "level": parts[2].strip(),
                "message": parts[3].strip(),
            }
            parsed_logs.append(log_entry)
    return render_template('results.html', logs=parsed_logs)

if __name__ == '__main__':
    app.run(debug=True)
