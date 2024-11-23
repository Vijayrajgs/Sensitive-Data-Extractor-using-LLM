from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

from app.models.database import save_scan, get_all_scans, delete_scan, get_scan_by_filename
from app.detection.llm_detector import detect_sensitive_data

app = Flask(__name__)

# Set upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt'}

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Extract content from the file
            with open(file_path, 'r') as f:
                content = f.read()
            extracted_data = detect_sensitive_data(content)

            # Save scan results to database
            save_scan(filename, extracted_data)
            
            # Redirect to the view page
            return render_template('view_scan.html', filename=filename, extracted_data=extracted_data)

    return render_template('upload.html')

# Route to view extracted data after upload
@app.route('/view_scan/<filename>', methods=['GET'])
def view_scan(filename):
    scan = get_scan_by_filename(filename)
    if scan:
        return render_template('view_scan.html', filename=filename, extracted_data=scan['data'])
    return redirect(url_for('home'))

# Route for the history page to view all uploaded scans
@app.route('/History', methods=['GET'])
def history():
    scans = get_all_scans()
    return render_template('history.html', scans=scans)

# Route for deleting an entry
@app.route('/Delete_entry/<scan_id>', methods=['POST'])
def delete_entry(scan_id):
    delete_scan(scan_id)
    return redirect(url_for('history'))

if __name__ == '__main__':
    app.run(debug=True)
