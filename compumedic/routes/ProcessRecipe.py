import os.path

from flask import Blueprint, request, render_template

from compumedic.services.RecipeProcessorService import RecipeProcessor
# Logger
from compumedic.utils.Logger import Logger

upload = Blueprint('process_recipe_blueprint', __name__, static_folder='../static')


@upload.post('/')
def process():
    """
    Display the upload form and handle file upload.
    """
    ocr_inst = RecipeProcessor()
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(upload.static_folder, "uploads/") + uploaded_file.filename)
        return render_template('recipe.jinja2',
                               titulo="OCR Flask",
                               lists=ocr_inst.process_recipe(uploaded_file.filename),
                               img_filename=uploaded_file.filename)
    else:
        return render_template('upload_recipe.jinja2')
