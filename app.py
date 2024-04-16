from flask import Flask, request, send_file
from PyPDF2 import PdfMerger

## pip install flask pypdf2


app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html><body>
    <h1>Upload PDFs to Merge</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="pdf_files" multiple>
        <input type="submit" value="Upload and Merge">
    </form>
    </body></html>
    '''

@app.route('/upload', methods=['POST'])
def upload_files():
    pdf_files = request.files.getlist('pdf_files')
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    output_path = "merged.pdf"
    merger.write(output_path)
    merger.close()
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
