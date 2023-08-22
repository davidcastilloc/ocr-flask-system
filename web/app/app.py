from flask import Flask
from flask import render_template

from .controllers.ocr import get_recipe_list_items

app = Flask(__name__)

img_recipe = "./app/static/img/text2.jpg"

@app.route('/')
def index():
    return render_template('index.html.jinja',
                           titulo="OCR Flask",
                           recipe=get_recipe_list_items(img_recipe),
                           img_example = img_recipe.split("app/")[-1])
