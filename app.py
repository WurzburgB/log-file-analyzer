from flask import Flask, render_template, request, session, Response, redirect
import os
from parser import parse_logs

app = Flask(__name__)
app.secret_key = "log-analyzer-secret"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    PAGE_SIZE = 20
    page = int(request.args.get("page", 1))
    sort_by = request.args.get("sort", "date")
    sort_order = request.args.get("order", "asc")

    logs = []
    filtered_logs = []
    filenames = []

    # Filters from session
    level_filter = session.get("level_filter", "ALL")
    message_filter = session.get("message_filter", "")
    date_filter = session.get("date_filter", "")

    # Upload multiple files
    if request.method == "POST" and "upload" in request.form:
        files = request.files.getlist("logfiles")
        filepaths = session.get("filepaths", [])

        for file in files:
            if file and file.filename:
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(filepath)
                filepaths.append(filepath)

        session["filepaths"] = filepaths
        return redirect("/")

    # Clear all files
    if request.method == "POST" and "clear_files" in request.form:
        session.clear()
        return redirect("/")

    # Apply filters
    if request.method == "POST" and "apply_filters" in request.form:
        session["level_filter"] = request.form.get("level", "ALL")
        session["message_filter"] = request.form.get("message", "")
        session["date_filter"] = request.form.get("date", "")
        return redirect("/")

    # Clear filters
    if request.method == "POST" and "clear_filters" in request.form:
        session["level_filter"] = "ALL"
        session["message_filter"] = ""
        session["date_filter"] = ""
        return redirect("/")

    # Load logs
    if "filepaths" in session:
        filepaths = session["filepaths"]
        filenames = [os.path.basename(p) for p in filepaths]

        for path in filepaths:
            logs.extend(parse_logs(path))

        filtered_logs = logs

        # Apply filters
        if level_filter != "ALL":
            filtered_logs = [log for log in filtered_logs if log["level"].upper() == level_filter.upper()]
        if message_filter:
            filtered_logs = [log for log in filtered_logs if message_filter.lower() in log["message"].lower()]
        if date_filter:
            filtered_logs = [log for log in filtered_logs if log["date"] == date_filter]

        # Sorting
        reverse = sort_order == "desc"
        if sort_by == "date":
            filtered_logs = sorted(filtered_logs, key=lambda x: (x["date"], x["timestamp"]), reverse=reverse)
        elif sort_by == "level":
            filtered_logs = sorted(filtered_logs, key=lambda x: x["level"], reverse=reverse)
        elif sort_by == "message":
            filtered_logs = sorted(filtered_logs, key=lambda x: x["message"], reverse=reverse)

        # Save filtered logs for export
        session["filtered_logs"] = filtered_logs

        # Detect levels
        detected_levels = sorted(set(log["level"].upper() for log in logs))

        # Stats
        stats = {"total": len(filtered_logs)}
        for level in detected_levels:
            stats[level] = sum(1 for log in filtered_logs if log["level"].upper() == level)

        # Pagination
        total_pages = max(1, (len(filtered_logs) + PAGE_SIZE - 1) // PAGE_SIZE)
        if page > total_pages:
            page = total_pages
        start = (page - 1) * PAGE_SIZE
        end = start + PAGE_SIZE
        paginated_logs = filtered_logs[start:end]

    else:
        detected_levels = []
        stats = {"total": 0}
        total_pages = 1
        paginated_logs = []

    return render_template(
        "index.html",
        logs=paginated_logs,
        stats=stats,
        filenames=filenames,
        level_filter=level_filter,
        message_filter=message_filter,
        date_filter=date_filter,
        detected_levels=detected_levels,
        current_page=page,
        total_pages=total_pages,
        sort_by=sort_by,
        sort_order=sort_order
    )


@app.route("/export")
def export_csv():
    if "filtered_logs" not in session or not session["filtered_logs"]:
        return "No data to export"

    logs = session["filtered_logs"]

    def generate():
        yield "date,time,level,message\n"
        for log in logs:
            yield f"{log['date']},{log['timestamp']},{log['level']},{log['message']}\n"

    return Response(
        generate(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=logs.csv"}
    )


if __name__ == "__main__":
    app.run(debug=True)