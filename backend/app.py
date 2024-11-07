from flask import Flask, request, jsonify, send_file
import os
from services.artifacts import parse_eml_file

app = Flask(__name__)

# Define a directory to save uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Endpoint to upload an .eml file and parse it.
    Returns parsed artifacts as a downloadable file.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.eml'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Parse the .eml file
        artifacts = parse_eml_file(file_path)

        # Create a downloadable response with artifacts
        result_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'parsed_artifacts.json')
        with open(result_file_path, 'w') as result_file:
            json.dump(artifacts, result_file)

        return send_file(result_file_path, as_attachment=True, attachment_filename='parsed_artifacts.json')

    return jsonify({'error': 'Invalid file format. Only .eml files are allowed.'}), 400

if __name__ == '__main__':
    app.run(debug=True)