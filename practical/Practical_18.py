# Question:
# A program that creates a web application that allows users to upload and download files.

# Explanation:
# Uses Flask to handle file uploads and downloads.
# Files are saved to an 'uploads' folder.

# Code Breakdown:
# 1. Import os and Flask functions.
# 2. Create Flask app.
# 3. Define and create `uploads` directory if it doesn't exist.
# 4. Configure app `UPLOAD_FOLDER`.
# 5. Define HTML template showing upload form and list of files.
# 6. Define `/` route.
#    - If POST: Check file part, validate filename, save file using `file.save`.
#    - List files in `uploads` folder.
#    - Render HTML with file list.
# 7. Define `/download/<filename>` route.
#    - Use `send_from_directory` to serve the file.
# 8. Run app.

import os
from flask import Flask, request, send_from_directory, render_template_string

# 2. App Setup
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

# 3. Create Directory
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 5. HTML Template
html = """
<h1>File Manager</h1>
<h2>Upload File</h2>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
</form>
<h2>Download Files</h2>
<ul>
    {% for file in files %}
        <li><a href="/download/{{ file }}">{{ file }}</a></li>
    {% endfor %}
</ul>
"""

# 6. Index Route (Upload & List)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if file part is present
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # Check if file selected
        if file.filename == '':
            return 'No selected file'
        # Save file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
    # List files
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template_string(html, files=files)

# 7. Download Route
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# 8. Run App
if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)
