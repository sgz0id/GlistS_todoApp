from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home_page():
    return "Hello Home!"

if "__main__" == __name__:
    app.run(debug=True)
    
