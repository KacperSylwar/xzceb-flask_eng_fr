from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    result = english_to_french(textToTranslate)
    return str(result)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    result = french_to_english(textToTranslate)
    return str(result)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return flask.render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
