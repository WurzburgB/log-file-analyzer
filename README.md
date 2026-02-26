# Log File Analyzer

A web-based log file analyzer built with Python and Flask. This application allows users to upload log files, filter and sort entries, and export results to CSV. The project demonstrates backend processing, file handling, filtering logic, and a clean web interface.

This project was built as a portfolio project to demonstrate practical Python development skills and basic web application design.

---

## Features

- Upload multiple log files
- Parse log files automatically
- Filter logs by:
  - Log level
  - Date
  - Message content
- Sort logs by:
  - Date
  - Level
  - Message
- Pagination for large log files
- Highlighted search matches
- Export filtered logs to CSV
- Dark mode toggle
- Clean and professional interface

---

## Supported Log Format

The parser supports common log formats such as:

2026-02-20 10:32:15 INFO Server started
2026-02-20 10:33:01 ERROR Connection failed
2026-02-20 10:33:45 WARNING High memory usage


It also attempts to automatically detect separators like:
- Spaces
- Commas
- Pipes
- Tabs

---

## Project Structure

log-file-analyzer/\n
│
├── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ └── script.js
│
├── templates/
│ └── index.html
│
├── uploads/
│
├── data/
│ └── sample.log
│
├── parser.py
├── app.py
├── README.md


---

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/log-file-analyzer.git

cd log-file-analyzer


2. Create a virtual environment:

python -m venv .venv


3. Activate the environment:

Windows:

.venv\Scripts\activate

Mac/Linux:

source .venv/bin/activate


4. Install Flask:

pip install flask

---

## Running the Application

Run the server:

python app.py

Then open your browser and go to:

http://127.0.0.1:5000


---

## Example Usage

1. Upload one or more log files
2. Apply filters if needed
3. Sort columns by clicking headers
4. Export filtered results if desired

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

---

## Future Improvements

Possible improvements include:

- Log charts and visualizations
- Live log monitoring
- User accounts
- Advanced filtering
- Drag and drop uploads
- Log format templates

---

## Author

Created as a portfolio project to demonstrate:

- Python development
- File parsing
- Web development
- Backend logic
- UI design
- Data processing
