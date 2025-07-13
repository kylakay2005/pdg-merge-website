from flask import Flask, request, send_file, render_template_string
from PyPDF2 import PdfMerger

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Merge PDFs</title></head>
<body>
    <h1>Upload PDF Files to Merge</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="pdfs" multiple required>
        <button type="submit">Merge</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def merge_pdfs():
    if request.method == 'POST':
        files = request.files.getlist('pdfs')
        merger = PdfMerger()

        for file in files:
            merger.append(file)

        output_filename = "merged_output.pdf"
        merger.write(output_filename)
        merger.close()

        return send_file(output_filename, as_attachment=True)

    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True)