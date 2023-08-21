# Copyright 2018 Cisco Systems, Inc.
# All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from flask import Flask
from flask import render_template

from .controllers.ocr import extract_text_from_recipe

app = Flask(__name__)

@app.route('/')
def index():
    list_detected_words = extract_text_from_recipe(route_img_recipe="./app/static/img/text.png")
    return render_template('index.html.jinja', titulo="OCR Flask", recipe=list_detected_words)
