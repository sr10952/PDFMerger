# PDF Merger Web Application

This is a simple Flask web application that allows users to upload multiple PDF files and merge them into a single PDF file.

## Features

- Web-based interface for uploading multiple PDF files.
- Merges uploaded PDF files into a single PDF file.
- Downloads the merged PDF file automatically after processing.

## Installation

To run this application, you need Python installed on your machine. You can then install the required dependencies:

```bash
pip install flask pypdf2
```

## Usage

To start the web application, run the Python script:

```bash
python app.py
```


Navigate to [http://localhost:5000/](http://localhost:5000/) in your web browser to access the application.


# How It Works
1. The user is presented with a simple HTML form to upload multiple PDF files.
2. After selecting the PDF files, the user submits the form to upload and merge the files.
3. The server merges the PDFs and sends the resulting file back to the user as a download.


## Contributing
Feel free to fork this project and submit pull requests. You can also open issues if you find any bugs or have suggestions for improvements.

## License
This project assumes MIT License.
