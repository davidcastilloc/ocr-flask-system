from flask import Flask, request, render_template

from .controllers.ocr import RecipeProcessor

app = Flask(__name__)

@app.route('/', methods = ['GET'] )
def index():
        return render_template('upload_recipe.html.jinja', titulo="OCR Flask")

@app.route('/upload', methods=['GET', 'POST'])
def upload_form():
    """
    Display the upload form and handle file upload.
    """
    ocrInst = RecipeProcessor()
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(f'app/static/uploads/{uploaded_file.filename}')
            return render_template('recipe.html.jinja',
                            titulo="OCR Flask",
                            lists = ocrInst.process_recipe(uploaded_file.filename) ,
                            img_filename = uploaded_file.filename)
        else:
            return "No file selected"
    return render_template('upload_form.html')